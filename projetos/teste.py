import math
import os
import sys
import time
from dataclasses import dataclass

# =========================
# Terminal utils (cross OS)
# =========================
IS_WIN = os.name == "nt"

if IS_WIN:
    import msvcrt

    def key_pressed():
        return msvcrt.kbhit()

    def read_key():
        ch = msvcrt.getch()
        # arrow keys come as b'\xe0' + code; ignore extras
        if ch in (b"\x00", b"\xe0"):
            _ = msvcrt.getch()
            return None
        try:
            return ch.decode("utf-8").lower()
        except:
            return None
else:
    import termios
    import tty
    import select

    class RawTerminal:
        def __enter__(self):
            self.fd = sys.stdin.fileno()
            self.old = termios.tcgetattr(self.fd)
            tty.setcbreak(self.fd)
            return self

        def __exit__(self, exc_type, exc, tb):
            termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old)

    def key_pressed():
        r, _, _ = select.select([sys.stdin], [], [], 0)
        return bool(r)

    def read_key():
        try:
            ch = sys.stdin.read(1)
            return ch.lower()
        except:
            return None

def clear():
    sys.stdout.write("\x1b[H\x1b[2J")
    sys.stdout.flush()

def hide_cursor():
    sys.stdout.write("\x1b[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\x1b[?25h")
    sys.stdout.flush()

# =========================
# Rendering config
# =========================
W = 110
H = 34
FPS = 20
PALETTE = " .,:;irsXA253hMHGS#9B&@"  # dense ASCII ramp

def clamp(a, lo, hi):
    return lo if a < lo else hi if a > hi else a

def to_char(v01):
    """v01 in [0,1] -> palette char"""
    i = int(clamp(v01, 0.0, 1.0) * (len(PALETTE) - 1))
    return PALETTE[i]

# =========================
# Mode management
# =========================
class Mode:
    JULIA = 1
    MANDELBROT = 2
    LORENZ = 3
    SCHRODINGER = 4
    VECTOR_CALC = 5

@dataclass
class State:
    mode: int = Mode.JULIA
    t: float = 0.0

# =========================
# 1) Julia set (animated c)
# =========================
def render_julia(t):
    # Animated parameter c(t)
    cx = 0.285 + 0.10 * math.cos(t * 0.7)
    cy = 0.01  + 0.10 * math.sin(t * 0.9)
    max_iter = 60

    # view window
    x0, x1 = -1.8, 1.8
    y0, y1 = -1.2, 1.2

    lines = []
    for j in range(H):
        y = y0 + (y1 - y0) * j / (H - 1)
        row = []
        for i in range(W):
            x = x0 + (x1 - x0) * i / (W - 1)
            zx, zy = x, y
            k = 0
            # z = z^2 + c
            while k < max_iter and (zx*zx + zy*zy) < 4.0:
                zx, zy = (zx*zx - zy*zy + cx), (2*zx*zy + cy)
                k += 1
            v = k / max_iter
            # smooth-ish contrast
            v = v ** 0.55
            row.append(to_char(v))
        lines.append("".join(row))

    hud = [
        "MODE 1: Julia (fractal animado)",
        f"c(t) = {cx:+.3f} {cy:+.3f}i   iter={max_iter}",
        "Teclas: 1 Julia | 2 Mandelbrot | 3 Lorenz | 4 Schrödinger | 5 Vetorial | q sair"
    ]
    return overlay_hud(lines, hud)

# =========================
# 2) Mandelbrot (animated zoom/center)
# =========================
def render_mandelbrot(t):
    max_iter = 70

    # Animated zoom and center (gentle)
    zoom = 1.0 + 0.6 * (0.5 + 0.5 * math.sin(t * 0.35))  # ~[1.0,1.6]
    center_x = -0.5 + 0.15 * math.cos(t * 0.2)
    center_y =  0.0 + 0.10 * math.sin(t * 0.17)

    # base window size
    span_x = 3.2 / zoom
    span_y = 2.0 / zoom

    x0, x1 = center_x - span_x/2, center_x + span_x/2
    y0, y1 = center_y - span_y/2, center_y + span_y/2

    lines = []
    for j in range(H):
        y = y0 + (y1 - y0) * j / (H - 1)
        row = []
        for i in range(W):
            x = x0 + (x1 - x0) * i / (W - 1)
            zx, zy = 0.0, 0.0
            k = 0
            while k < max_iter and (zx*zx + zy*zy) < 4.0:
                zx, zy = (zx*zx - zy*zy + x), (2*zx*zy + y)
                k += 1
            v = k / max_iter
            v = v ** 0.6
            row.append(to_char(v))
        lines.append("".join(row))

    hud = [
        "MODE 2: Mandelbrot (zoom animado)",
        f"center=({center_x:+.3f},{center_y:+.3f})  zoom={zoom:.2f}  iter={max_iter}",
        "Teclas: 1 Julia | 2 Mandelbrot | 3 Lorenz | 4 Schrödinger | 5 Vetorial | q sair"
    ]
    return overlay_hud(lines, hud)

# =========================
# 3) Lorenz attractor (ODE simulation)
# =========================
def render_lorenz(t, sim):
    # Integrate a few steps per frame for stability
    steps = 200
    dt = 0.005

    sigma = 10.0
    rho = 28.0
    beta = 8.0 / 3.0

    # advance
    for _ in range(steps):
        x, y, z = sim["x"], sim["y"], sim["z"]
        # dx/dt = sigma(y-x), dy/dt = x(rho-z)-y, dz/dt = xy - beta z
        dx = sigma * (y - x)
        dy = x * (rho - z) - y
        dz = x * y - beta * z
        sim["x"] = x + dx * dt
        sim["y"] = y + dy * dt
        sim["z"] = z + dz * dt

        # keep trail
        sim["trail"].append((sim["x"], sim["y"], sim["z"]))
        if len(sim["trail"]) > 2500:
            sim["trail"].pop(0)

    # project 3D to 2D (simple)
    # rotate slowly with time for cooler look
    ang = t * 0.25
    ca, sa = math.cos(ang), math.sin(ang)

    # screen buffer
    buf = [[" " for _ in range(W)] for _ in range(H)]
    zbuf = [[-1e9 for _ in range(W)] for _ in range(H)]

    # map points
    for (x, y, z) in sim["trail"]:
        # rotate around z and x-ish
        xr = x * ca - y * sa
        yr = x * sa + y * ca
        zr = z

        # perspective-ish
        px = int(W/2 + xr * 1.3)
        py = int(H/2 - (yr * 0.6 - zr * 0.05))

        if 0 <= px < W and 0 <= py < H:
            # depth by z
            if zr > zbuf[py][px]:
                zbuf[py][px] = zr
                # intensity by local z (normalize roughly)
                v = (zr - 0) / 50.0
                v = clamp(v, 0.0, 1.0)
                buf[py][px] = to_char(v)

    lines = ["".join(r) for r in buf]
    hud = [
        "MODE 3: EDO – Atrator de Lorenz (simulação)",
        "dx=σ(y-x), dy=x(ρ-z)-y, dz=xy-βz   (σ=10, ρ=28, β=8/3)",
        "Teclas: 1 Julia | 2 Mandelbrot | 3 Lorenz | 4 Schrödinger | 5 Vetorial | q sair"
    ]
    return overlay_hud(lines, hud)

# =========================
# 4) Schrödinger 1D (wavepacket)
# i dψ/dt = -1/2 d²ψ/dx² + Vψ  (ħ=m=1)
# split-step-ish / finite difference explicit (small dt)
# =========================
def render_schrodinger(sim):
    N = sim["N"]
    dx = sim["dx"]
    dt = sim["dt"]

    re = sim["re"]
    im = sim["im"]
    V  = sim["V"]

    # Laplacian (2nd derivative) via finite difference
    # Using explicit Euler on complex equation (small dt to keep it ok for visual)
    new_re = [0.0] * N
    new_im = [0.0] * N

    for i in range(1, N-1):
        lap_re = (re[i-1] - 2*re[i] + re[i+1]) / (dx*dx)
        lap_im = (im[i-1] - 2*im[i] + im[i+1]) / (dx*dx)

        # i dψ/dt = -1/2 lap(ψ) + Vψ
        # Let ψ = re + i im
        # dψ/dt = -i(-1/2 lap + Vψ) = i/2 lap - i Vψ
        # So:
        # dre/dt = -(1/2) lap_im + V * im
        # dim/dt = +(1/2) lap_re - V * re
        dre = -(0.5)*lap_im + V[i]*im[i]
        dimm = +(0.5)*lap_re - V[i]*re[i]

        new_re[i] = re[i] + dt * dre
        new_im[i] = im[i] + dt * dimm

    # boundary (absorbing-ish)
    new_re[0] = new_re[1]*0.98
    new_im[0] = new_im[1]*0.98
    new_re[N-1] = new_re[N-2]*0.98
    new_im[N-1] = new_im[N-2]*0.98

    sim["re"], sim["im"] = new_re, new_im
    sim["time"] += dt

    # render probability density |ψ|^2 across width
    # map N to W
    lines = [[" " for _ in range(W)] for _ in range(H)]
    # compute |psi|^2
    prob = [new_re[i]*new_re[i] + new_im[i]*new_im[i] for i in range(N)]
    # normalize
    m = max(prob) if max(prob) > 1e-12 else 1.0

    for x in range(W):
        i = int(x * (N-1) / (W-1))
        p = prob[i] / m
        # height
        h = int(p * (H-6))
        for yy in range(H-2, H-2 - h, -1):
            if 0 <= yy < H:
                lines[yy][x] = to_char(p)

    # draw potential barrier line (scaled)
    for x in range(W):
        i = int(x * (N-1) / (W-1))
        vv = V[i]
        # vv in [0, ~1] -> draw a small baseline
        yv = int((H-6) - vv * (H-10))
        yv = clamp(yv, 4, H-6)
        lines[yv][x] = "-"

    lines = ["".join(r) for r in lines]
    hud = [
        "MODE 4: Onda tipo mecânica quântica (Schrödinger 1D) – |ψ|²",
        "i dψ/dt = -1/2 d²ψ/dx² + Vψ   (discretizado)",
        "Teclas: 1 Julia | 2 Mandelbrot | 3 Lorenz | 4 Schrödinger | 5 Vetorial | q sair"
    ]
    return overlay_hud(lines, hud)

# =========================
# 5) Vector calculus: grad/div/curl visualization
# Use scalar field φ(x,y) and vector field F(x,y)
# φ(x,y) = sin(ax)cos(by) ; grad φ
# F = (P,Q) ; div F = dP/dx + dQ/dy ; curl F (2D) = dQ/dx - dP/dy
# =========================
def render_vector_calc(t):
    # world bounds
    x0, x1 = -2.8, 2.8
    y0, y1 = -1.8, 1.8

    a = 1.2
    b = 1.0

    lines = []
    for j in range(H):
        y = y0 + (y1 - y0) * j / (H - 1)
        row = []
        for i in range(W):
            x = x0 + (x1 - x0) * i / (W - 1)

            # scalar potential
            phi = math.sin(a*x + 0.6*math.sin(t*0.7)) * math.cos(b*y + 0.6*math.cos(t*0.5))

            # gradient (approx analytic)
            dphidx = a * math.cos(a*x + 0.6*math.sin(t*0.7)) * math.cos(b*y + 0.6*math.cos(t*0.5))
            dphidy = -b * math.sin(a*x + 0.6*math.sin(t*0.7)) * math.sin(b*y + 0.6*math.cos(t*0.5))

            # define vector field F = (P,Q)
            P = math.sin(y + t) + 0.35*dphidx
            Q = math.cos(x - t) + 0.35*dphidy

            # divergence (analytic partials approx)
            # d/dx sin(y+t)=0 ; d/dx cos(x-t)=-sin(x-t)
            dPdx = 0.0 + 0.35 * (-(a*a) * math.sin(a*x + 0.6*math.sin(t*0.7)) * math.cos(b*y + 0.6*math.cos(t*0.5)))
            dQdy = 0.0 + 0.35 * (-(b*b) * math.sin(a*x + 0.6*math.sin(t*0.7)) * math.cos(b*y + 0.6*math.cos(t*0.5)))
            divF = dPdx + dQdy

            # curl (2D scalar): dQ/dx - dP/dy
            dQdx = -math.sin(x - t) + 0.35 * (-a*b * math.cos(a*x + 0.6*math.sin(t*0.7)) * math.sin(b*y + 0.6*math.cos(t*0.5)))
            dPdy =  math.cos(y + t) + 0.35 * (-a*b * math.cos(a*x + 0.6*math.sin(t*0.7)) * math.sin(b*y + 0.6*math.cos(t*0.5)))
            curlF = dQdx - dPdy

            # combine: show structure via div and curl and phi
            val = 0.55*phi + 0.25*math.tanh(divF) + 0.20*math.tanh(curlF)
            v01 = (val + 1.2) / 2.4
            row.append(to_char(v01))
        lines.append("".join(row))

    hud = [
        "MODE 5: Cálculo Vetorial – grad/div/rot (curl) (visualização)",
        "φ=sin(ax)cos(by) ; F=(sin(y+t)+0.35∂φ/∂x , cos(x-t)+0.35∂φ/∂y)",
        "Teclas: 1 Julia | 2 Mandelbrot | 3 Lorenz | 4 Schrödinger | 5 Vetorial | q sair"
    ]
    return overlay_hud(lines, hud)

# =========================
# HUD overlay helper
# =========================
def overlay_hud(lines, hud_lines):
    # lines: list[str] length H
    out = [list(line) for line in lines]
    for r, text in enumerate(hud_lines):
        if r >= H:
            break
        for c, ch in enumerate(text[:W]):
            out[r][c] = ch
    return "\n".join("".join(row) for row in out)

# =========================
# Sim init
# =========================
def init_lorenz():
    return {"x": 0.1, "y": 0.0, "z": 0.0, "trail": []}

def init_schrodinger():
    # grid 1D
    N = 420
    x0, x1 = -30.0, 30.0
    dx = (x1 - x0) / (N - 1)

    # Gaussian wave packet with momentum k0
    re = [0.0] * N
    im = [0.0] * N

    x_center = -12.0
    sigma = 2.5
    k0 = 1.2

    # potential barrier
    V = [0.0] * N
    for i in range(N):
        x = x0 + i * dx
        # barrier near x=2..6
        if 2.0 < x < 6.0:
            V[i] = 0.8
        else:
            V[i] = 0.0

        gauss = math.exp(-((x - x_center) ** 2) / (2 * sigma * sigma))
        phase = k0 * x
        re[i] = gauss * math.cos(phase)
        im[i] = gauss * math.sin(phase)

    # small dt to keep stable visually
    dt = 0.02
    return {"N": N, "dx": dx, "dt": dt, "re": re, "im": im, "V": V, "time": 0.0}

# =========================
# Main loop
# =========================
def main():
    st = State()
    lorenz = init_lorenz()
    sch = init_schrodinger()

    clear()
    hide_cursor()

    # On Unix, use raw terminal context for immediate key reads
    ctx = RawTerminal() if not IS_WIN else None
    try:
        if ctx:
            ctx.__enter__()

        last = time.time()
        while True:
            now = time.time()
            dt = now - last
            last = now
            st.t += dt

            # key handling
            if key_pressed():
                k = read_key()
                if k in ("q", "\x1b"):
                    break
                if k == "1":
                    st.mode = Mode.JULIA
                elif k == "2":
                    st.mode = Mode.MANDELBROT
                elif k == "3":
                    st.mode = Mode.LORENZ
                elif k == "4":
                    st.mode = Mode.SCHRODINGER
                elif k == "5":
                    st.mode = Mode.VECTOR_CALC

            # render frame
            if st.mode == Mode.JULIA:
                frame = render_julia(st.t)
            elif st.mode == Mode.MANDELBROT:
                frame = render_mandelbrot(st.t)
            elif st.mode == Mode.LORENZ:
                frame = render_lorenz(st.t, lorenz)
            elif st.mode == Mode.SCHRODINGER:
                frame = render_schrodinger(sch)
            else:
                frame = render_vector_calc(st.t)

            sys.stdout.write("\x1b[H")  # go home
            sys.stdout.write(frame)
            sys.stdout.flush()

            # FPS cap
            sleep_time = max(0.0, (1.0 / FPS) - (time.time() - now))
            time.sleep(sleep_time)

    finally:
        if ctx:
            ctx.__exit__(None, None, None)
        show_cursor()
        clear()

if __name__ == "__main__":
    main()

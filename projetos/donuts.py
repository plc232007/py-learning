import math
import time
import os
import sys

WIDTH = 90
HEIGHT = 28
FPS = 30

CHARS = " .:-=+*#%@"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def render(t):
    buffer = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for y in range(HEIGHT):
        for x in range(WIDTH):
            # Normaliza coordenadas
            nx = (x - WIDTH / 2) / (WIDTH / 8)
            ny = (y - HEIGHT / 2) / (HEIGHT / 4)

            # ===== CAMPO VETORIAL =====
            vx = math.sin(ny + t)
            vy = math.cos(nx - t)

            # Divergência simbólica (visual)
            div = math.sin(nx * ny + t)

            # ===== ONDA =====
            wave = math.sin(nx * 2 + t) + math.sin(ny * 2 - t)

            # Intensidade combinada
            intensity = vx * vy + wave * 0.6 + div * 0.4

            # Normaliza intensidade
            idx = int((intensity + 2) / 4 * (len(CHARS) - 1))
            idx = max(0, min(len(CHARS) - 1, idx))

            buffer[y][x] = CHARS[idx]

    # ===== PARTÍCULAS ORBITAIS =====
    for i in range(20):
        angle = t + i * 0.3
        r = 8 + 2 * math.sin(t + i)
        px = int(WIDTH / 2 + math.cos(angle) * r)
        py = int(HEIGHT / 2 + math.sin(angle) * r)

        if 0 <= px < WIDTH and 0 <= py < HEIGHT:
            buffer[py][px] = "@"

    # ===== HUD MATEMÁTICO =====
    info = [
        "Math Visual Engine",
        "Campo Vetorial: F(x,y) = (sin(y+t), cos(x-t))",
        "Onda: ψ = sin(x+t) + sin(2y-t)",
        "Álgebra + Cálculo + Trigonometria",
        "CTRL+C para sair"
    ]

    for i, line in enumerate(info):
        for j, c in enumerate(line):
            if j < WIDTH:
                buffer[i][j] = c

    return "\n".join("".join(row) for row in buffer)

def main():
    t = 0.0
    clear()
    sys.stdout.write("\033[?25l")  # esconde cursor

    try:
        while True:
            clear()
            print(render(t))
            t += 0.07
            time.sleep(1 / FPS)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\033[?25h")  # mostra cursor
        clear()

if __name__ == "__main__":
    main()

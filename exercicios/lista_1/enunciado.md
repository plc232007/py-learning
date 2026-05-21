# 🧩 Lista de Exercícios — IF, Comparações e Lógica em Python

> Objetivo: treinar **operadores relacionais**, **if/elif/else**, **and/or/not**, **in/not in** e **f-strings**.

---

## 🔹 BLOCO 1 — Operadores relacionais

- [ ] **1) Maior, menor ou igual**  
  Peça dois números e mostre:
  - `10 é maior que 5`
  - ou `5 é igual a 5`

- [ ] **2) Maior de idade**  
  Peça a idade e mostre:
  - `Você é maior de idade.`
  - ou `Você é menor de idade.`

- [ ] **3) Nota do aluno**  
  Peça uma nota (0 a 10) e diga:
  - aprovado (≥ 7)
  - recuperação (≥ 5 e < 7)
  - reprovado (< 5)  
  Use `if / elif / else`.

---

## 🔹 BLOCO 2 — Operador lógico `and`

- [ ] **4) Acesso permitido**  
  Peça:
  - idade
  - se tem autorização (`sim` ou `não`)  
  Acesso permitido **somente se**:
  - idade ≥ 18 **e**
  - autorização == `sim`

- [ ] **5) Intervalo numérico**  
  Peça um número e diga se ele está **entre 10 e 20** (inclusive).  
  📌 Use `and`.

---

## 🔹 BLOCO 3 — Operador lógico `or`

- [ ] **6) Promoção**  
  Peça:
  - se o usuário é estudante
  - se é idoso  
  Ele ganha desconto se for **estudante ou idoso**.

- [ ] **7) Fim de semana**  
  Peça o dia da semana e diga se é:
  - dia útil
  - fim de semana  
  📌 Use `or` para sábado ou domingo.

---

## 🔹 BLOCO 4 — Operador lógico `not`

- [ ] **8) Negação simples**  
  Peça um número e diga se ele **não é positivo**.

- [ ] **9) Senha inválida**  
  Peça uma senha e diga `Senha inválida` se **não** for igual a `"1234"`.  
  📌 Use `not`.

---

## 🔹 BLOCO 5 — Operadores `in` e `not in`

- [ ] **10) Letra no nome**  
  Peça o nome e diga se a letra `"a"` está presente.

- [ ] **11) Vogal ou consoante**  
  Peça uma letra e diga se é:
  - vogal
  - consoante  
  📌 Use:
  ```python
  letra in "aeiou"

## 🔹 BLOCO 6 — Misturando tudo 🔥 (nível real)

### 1️⃣3️⃣ Login simples
Peça:
- usuário
- senha

Login válido se:
- usuário == `"admin"`
- senha == `"123"`

Use `and`.

---

### 1️⃣4️⃣ Classificação etária
Peça idade e diga:
- criança (< 12)
- adolescente (12–17)
- adulto (≥ 18)

---

### 1️⃣5️⃣ Desafio final 💥
Peça:
- nome
- idade
- cidade

Mostre:
- `Acesso permitido`

Se:
- idade ≥ 18
- e cidade **não** for `"Brasília"`

📌 Use:
- `and`
- `not in`
- `f-string`

---

## 🧠 Regra de ouro (pra tudo isso)

```python
if condicao1 and condicao2:
    ...
elif condicao3 or condicao4:
    ...
else:
    ...


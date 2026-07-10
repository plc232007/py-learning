"""
========================================================================
 REVISÃO DIAGNÓSTICA DE PYTHON — FUNDAMENTOS
========================================================================

COMO USAR
---------
1. Implemente cada função abaixo (troque o `raise NotImplementedError`
   pela sua solução).
2. Rode no terminal:  python revisao.py
3. Leia o relatório no fim. Ele diz, por tópico:
      ✓ ok           -> você domina, pode PULAR.
      ✗ revisar      -> sua resposta saiu errada, FOQUE aqui.
      ✗ erro         -> seu código quebrou, FOQUE aqui.
      ○ não feito     -> ainda não implementou.

COMO INTERPRETAR (a régua)
--------------------------
- Se você resolveu de primeira, sem consultar nada e sem hesitar: PULE.
- Se travou, precisou pesquisar sintaxe básica, ou errou: é ali que sua
  base está frágil. Esse é o sinal que você pediu.
- Algumas questões têm uma "pegadinha" de propósito. Elas revelam
  entendimento raso mesmo em quem "já programa". Não subestime.

Não vale colar resposta pronta: o objetivo é medir, não completar.
========================================================================
"""


# ----------------------------------------------------------------------
# ÁREA A — TIPOS E MUTABILIDADE
# ----------------------------------------------------------------------

def divisao_inteira_e_resto(a, b):
    """Retorne uma tupla (quociente_inteiro, resto) da divisão de a por b.
    Ex.: divisao_inteira_e_resto(17, 5) -> (3, 2)
    Pista: os operadores // e % existem por um motivo."""
    c = a // b
    resto = a % b

    return c, resto


def dobra_valores(numeros):
    """
    Retorne uma NOVA lista com cada valor dobrado.
    A lista original NÃO pode ser modificada.
    Ex.: dobra_valores([1, 2, 3]) -> [2, 4, 6]
    (Pegadinha de mutabilidade: se você alterar a lista recebida, falha.)
    
    """
    return [n * 2 for n in numeros]


# ----------------------------------------------------------------------
# ÁREA B — STRINGS
# ----------------------------------------------------------------------

def formata_nome(nome, sobrenome):
    """Retorne "Sobrenome, Nome" com a primeira letra de cada em maiúscula.
    Ex.: formata_nome("ana", "souza") -> "Souza, Ana"
    Pista: f-strings + um método de string para capitalizar."""

    texto = f'{sobrenome.capitalize()}, {nome.capitalize()}'

    return texto


def conta_vogais(texto):
    """Conte quantas vogais (a, e, i, o, u) há no texto, ignorando
    maiúsculas/minúsculas.
    Ex.: conta_vogais("banana") -> 3 ; conta_vogais("PYTHON") -> 1"""

    vogais = "aeiou"
    total = 0
    for i in texto.lower():
        if i in vogais:
            total += 1

    return total


# ----------------------------------------------------------------------
# ÁREA C — LISTAS E SLICING
# ----------------------------------------------------------------------

def segundo_maior(numeros):
    """Retorne o segundo maior valor DISTINTO da lista.
    Ex.: segundo_maior([3, 1, 4, 1, 5, 9, 2, 6]) -> 6
    (Cuidado: valores repetidos não contam duas vezes.)"""
    raise NotImplementedError


def primeiros_e_ultimos(lst, n):
    """Retorne uma nova lista com os primeiros n e os últimos n elementos.
    Ex.: primeiros_e_ultimos([1, 2, 3, 4, 5, 6], 2) -> [1, 2, 5, 6]
    Pista: slicing com índices negativos."""
    raise NotImplementedError


# ----------------------------------------------------------------------
# ÁREA D — DICIONÁRIOS E SETS
# ----------------------------------------------------------------------

def frequencia(palavras):
    """Retorne um dicionário {palavra: quantas_vezes_apareceu}.
    Ex.: frequencia(["a", "b", "a", "c", "a"]) -> {"a": 3, "b": 1, "c": 1}
    (Padrão clássico de contagem. Se você não sabe fazer sem pensar,
    é um buraco importante na base.)"""
    raise NotImplementedError


def inverte_dicionario(d):
    """Retorne um novo dicionário com chaves e valores trocados.
    Ex.: inverte_dicionario({"a": 1, "b": 2}) -> {1: "a", 2: "b"}
    (Assuma que os valores são únicos.)"""
    raise NotImplementedError


# ----------------------------------------------------------------------
# ÁREA E — CONDICIONAIS E LOOPS
# ----------------------------------------------------------------------

def fizzbuzz(n):
    """Retorne uma lista de strings de 1 até n onde:
      - múltiplos de 3 viram "Fizz"
      - múltiplos de 5 viram "Buzz"
      - múltiplos de 3 e 5 viram "FizzBuzz"
      - os demais viram o próprio número como string.
    Ex.: fizzbuzz(5) -> ["1", "2", "Fizz", "4", "Buzz"]
    (Teste clássico. A ordem das condições importa — pense nisso.)"""
    raise NotImplementedError


def primos_ate(n):
    """Retorne a lista dos números primos de 2 até n (inclusive).
    Ex.: primos_ate(10) -> [2, 3, 5, 7]"""
    raise NotImplementedError


# ----------------------------------------------------------------------
# ÁREA F — FUNÇÕES E ESCOPO
# ----------------------------------------------------------------------

def media(*numeros):
    """Retorne a média aritmética dos números passados.
    Se nenhum número for passado, retorne 0.
    Ex.: media(2, 4, 6) -> 4.0 ; media() -> 0
    Pista: isto usa *args (número variável de argumentos)."""
    raise NotImplementedError


def adiciona_item(item, lista=None):
    """Adicione `item` a `lista` e retorne a lista.
    Se `lista` não for informada, crie uma lista NOVA e vazia a cada
    chamada.
    Ex.: adiciona_item(1) -> [1] ; adiciona_item(2) -> [2]
    (A PEGADINHA MAIS FAMOSA DE PYTHON: usar `lista=[]` como padrão
    parece funcionar, mas é uma armadilha. Se você não sabe por quê,
    marque isto como prioridade de estudo.)"""
    raise NotImplementedError


# ======================================================================
# RUNNER — não precisa mexer daqui para baixo
# ======================================================================

def _testes():
    return [
        ("A", "Tipos e mutabilidade",
         lambda: divisao_inteira_e_resto(17, 5) == (3, 2)
                 and divisao_inteira_e_resto(10, 3) == (3, 1)),
        ("A", "Tipos e mutabilidade",
         lambda: (lambda orig: dobra_valores(orig) == [2, 4, 6] and orig == [1, 2, 3])([1, 2, 3])),
        ("B", "Strings",
         lambda: formata_nome("ana", "souza") == "Souza, Ana"),
        ("B", "Strings",
         lambda: conta_vogais("banana") == 3 and conta_vogais("PYTHON") == 1),
        ("C", "Listas e slicing",
         lambda: segundo_maior([3, 1, 4, 1, 5, 9, 2, 6]) == 6),
        ("C", "Listas e slicing",
         lambda: primeiros_e_ultimos([1, 2, 3, 4, 5, 6], 2) == [1, 2, 5, 6]),
        ("D", "Dicionarios e sets",
         lambda: frequencia(["a", "b", "a", "c", "a"]) == {"a": 3, "b": 1, "c": 1}),
        ("D", "Dicionarios e sets",
         lambda: inverte_dicionario({"a": 1, "b": 2}) == {1: "a", 2: "b"}),
        ("E", "Condicionais e loops",
         lambda: fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"] and fizzbuzz(15)[-1] == "FizzBuzz"),
        ("E", "Condicionais e loops",
         lambda: primos_ate(10) == [2, 3, 5, 7]),
        ("F", "Funcoes e escopo",
         lambda: media(2, 4, 6) == 4.0 and media() == 0),
        ("F", "Funcoes e escopo",
         lambda: adiciona_item(1) == [1] and adiciona_item(2) == [2]),
    ]


def _run():
    from collections import defaultdict
    resultados = _testes()
    por_area = defaultdict(list)
    simbolo = {"ok": "\u2713 ok", "revisar": "\u2717 revisar", "erro": "\u2717 erro", "nao": "\u25cb nao feito"}

    print("\n" + "=" * 60)
    print(" RELATORIO DA REVISAO")
    print("=" * 60)

    for i, (area, topico, teste) in enumerate(resultados, 1):
        try:
            status = "ok" if teste() else "revisar"
        except NotImplementedError:
            status = "nao"
        except AssertionError:
            status = "revisar"
        except Exception as e:
            status = "erro"
            print(f"  [ex {i:2}] {topico}: {simbolo[status]}  ({type(e).__name__}: {e})")
            por_area[topico].append(status)
            continue
        print(f"  [ex {i:2}] {topico}: {simbolo[status]}")
        por_area[topico].append(status)

    print("-" * 60)
    print(" ONDE FOCAR (por topico)")
    print("-" * 60)
    for topico, status_list in por_area.items():
        if all(s == "ok" for s in status_list):
            print(f"  {topico}: dominado -> PODE PULAR")
        elif any(s == "nao" for s in status_list) and not any(s in ("revisar", "erro") for s in status_list):
            print(f"  {topico}: ainda nao feito")
        else:
            print(f"  {topico}: FOQUE AQUI")

    total_ok = sum(1 for lst in por_area.values() for s in lst if s == "ok")
    print("-" * 60)
    print(f"  Total: {total_ok}/{len(resultados)} exercicios corretos")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    _run()
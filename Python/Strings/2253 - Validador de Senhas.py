"""
Autor: Pierre Vieira
Data da submissão: 26/01/2020 21:06:03
"""


class Senha:
    def __init__(self, texto_senha):
        self.texto_senha = texto_senha

    def tem_numero(self):
        for caractere in self.texto_senha:
            if caractere.isnumeric():
                return True
        return False

    def tem_maiuscula(self):
        for caractere in self.texto_senha:
            if caractere.isupper():
                return True
        return False

    def tem_minuscula(self):
        for caractere in self.texto_senha:
            if caractere.islower():
                return True
        return False

    def tem_caractere_especial(self):
        for caractere in self.texto_senha:
            if not caractere.islower() and not caractere.isupper() and not caractere.isnumeric():
                return True
        return False

    def tamanho_ok(self):
        if 6 <= len(self.texto_senha) <= 32:
            return True
        return False

    def tem_espaco(self):
        if ' ' in self.texto_senha:
            return True
        return False


def validador_de_senha(texto_senha):
    senha = Senha(texto_senha)
    if senha.tem_numero() and senha.tem_minuscula() and senha.tem_maiuscula() and not senha.tem_caractere_especial() and senha.tamanho_ok() and not senha.tem_espaco():
        return 'Senha valida.'
    return 'Senha invalida.'


def main():
    while True:
        try:
            texto_senha = input()
            print(validador_de_senha(texto_senha), end='')
        except EOFError:
            break
        else:
            print()


main()

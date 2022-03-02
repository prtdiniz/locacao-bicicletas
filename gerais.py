#
# Métodos de uso geral no Sistema
#

import ast


class ValorNaoEncontado(Exception):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return "===> Código %i não encontrado." % self.valor


class Sistema:
    estoque_geral = 0  # Implementa Estoque Geral da Empresa (Todas as Lojas)

    @staticmethod
    def carrega_lojas():
        with open('lojas.txt', 'r') as f:
            lojas = {}
            for registro in f:
                valores = registro.split(",")
                linha = eval("{"+valores[0]+"{"+valores[1]+","+valores[2]+"}}")
                lojas.update(linha)
            f.close()
            return lojas

    @staticmethod
    def simnao(resposta):
        sailoop = 0
        while sailoop == 0:
            resposta = resposta.upper()
            if resposta != "N" and resposta != "S":
                print(f"===> Entrada Inválida, tente novamente")
                resposta = input("===> Por favor, digite apenas 'S' ou 'N' :")
            if resposta == 'S' or resposta == 'N':
                sailoop = 1
        return resposta

    @staticmethod
    def leh_clientes():
        with open('clientes.txt', 'r') as file:
            clientes = file.read()
            clientes = ast.literal_eval(clientes)
        return clientes

    @staticmethod
    def leh_emprestimos():  # carrega dicionário de emprestimos da loja
        with open('emprestimos.txt', 'r') as file:
            emprestimos = file.read()
            emprestimos = ast.literal_eval(emprestimos)
        return emprestimos

    @staticmethod
    def leh_lojas():
        with open('lojas.txt', 'r') as file:
            lojas = file.read()
            lojas = ast.literal_eval(lojas)
        return lojas

    @staticmethod
    def atualiza_clientes(dicionario):  # atualiza dicionário de clientes da loja
        with open('clientes.txt', 'w+') as file:
            clientes = str(dicionario)
            file.write(clientes)
        return clientes

    @staticmethod
    def atualiza_emprestimos(dicionario):  # atualiza dicionário de emprestimos da loja
        with open('emprestimos.txt', 'w+') as file:
            emprestimos = str(dicionario)
            file.write(emprestimos)
        return emprestimos

    @staticmethod
    def atualiza_lojas(dicionario):  # atualiza dicionário de lojas
        with open('lojas.txt', 'w+') as file:
            lojas = str(dicionario)
            file.write(lojas)
        return lojas

    @staticmethod
    def aguarda_tecla():
        print("\n===> Aperte <ENTER>> para continuar...", end="")
        try:
            input()
        except:
            pass
        finally:
            return

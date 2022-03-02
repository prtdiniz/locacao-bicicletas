import ast
from datetime import datetime
from gerais import Sistema

class Emprestimo(Sistema):

    def __init__(self, cod_cli, cod_loja, qtde, ano, mes, dia, hora, minutos, valor_hora=5, valor_dia=25, valor_semana=100):
        self.cod_cli = cod_cli
        self.cod_loja = cod_loja
        self.qtde = qtde
        self.ano = ano
        self.mes = mes
        self.dia = dia
        self.hora = hora
        self.minutos = minutos
        self.valor_hora = valor_hora
        self.valor_dia = valor_dia
        self.valor_semana = valor_semana

    # Getters / Setters
    @property
    def cod_cli(self):
        return self.__cod_cli

    @cod_cli.setter
    def cod_cli(self, cod_cli):
        self.__cod_cli = cod_cli

    @property
    def cod_loja(self):
        return self.__cod_loja

    @cod_loja.setter
    def cod_loja(self, cod_loja):
        self.__cod_loja = cod_loja

    @property
    def qtde(self):
        return self.__qtde

    @qtde.setter
    def qtde(self, qtde):
        if qtde < 0:
            raise ValueError('Você não pode informar quantidade negativa!')
        self.__qtde = qtde

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        self.__mes = mes

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        self.__dia = dia

    @property
    def hora(self):
        return self.__hora

    @hora.setter
    def hora(self, hora):
        self.__hora = hora

    @property
    def minutos(self):
        return self.__minutos

    @minutos.setter
    def minutos(self, minutos):
        self.__minutos = minutos

    @property
    def valor_hora(self):
        return self.__valor_hora

    @valor_hora.setter
    def valor_hora(self, valor_hora):
        self.__valor_hora = valor_hora

    @property
    def valor_dia(self):
        return self.__valor_dia

    @valor_dia.setter
    def valor_dia(self, valor_dia):
        self.__valor_dia = valor_dia

    @property
    def valor_semana(self):
        return self.__valor_semana

    @valor_semana.setter
    def valor_semana(self, valor_semana):
        self.__valor_semana = valor_semana

    # Métodos Gerais
    def fecha_emprestimo(self, cod_cli, loja_dev=0):  # parametro loja_dev considera que a Bike pode ser devolvida em outra loja
        emprestimos = Sistema.leh_emprestimos()
        try:
            dados_emprestimo = emprestimos[cod_cli]
        except KeyError:
            print("Emprestimo não encontrado")
        else:
            valor_final = self.calcula_valor(dados_emprestimo["ano"],
                                             dados_emprestimo["mes"],
                                             dados_emprestimo["dia"],
                                             dados_emprestimo["hora"],
                                             dados_emprestimo["min"])
            valor_final *= dados_emprestimo["qtde"]
            if dados_emprestimo['qtde'] > 1:
                plural = "s"
            else:
                plural = ""
            print(f"{dados_emprestimo['qtde']} Bicicleta{plural} Emprestada{plural}. \tValor Total R$ {valor_final:>8.2f}")
            if dados_emprestimo["qtde"] >= 3:
                print(f"===> Desconto Família:(30%)\t\t\t R$ {valor_final*0.3:>11.2f}")
                valor_final *= 0.7
            print("                                     --------------")
            print(f"Valor final a pagar: \t\t\t\t R$ {valor_final:>11.2f}\n")
            if loja_dev == 999:
                sai_loop = 'nao_entra'  # apenas consultar para clientes
            else:
                sai_loop = 'loop'
            while sai_loop == 'loop':
                del_emprestimo = self.simnao(input("Confirma devolução e pagamento? (S/N) "))  # Validar Entrada (S ou N)
                print()
                if del_emprestimo == "S":
                    print(f"===> Iniciando a baixa do Empréstimo ")
                    # Valida Loja de Devolução = Loja Empréstimo (Atualização do estoque)
                    if emprestimos[cod_cli]['loja'] != loja_dev:
                        print(f"\n===>       A T E N Ç Ã O  ")
                        print(f"Loja de Devolução {loja_dev} diferente da Loja de Empréstimo {emprestimos[cod_cli]['loja']}")
                        print(f"\n       Confirma devolução na loja {loja_dev} ? ")
                        questiona = Sistema.simnao(input("S - Loja Atual | N - Loja do Empréstimo - S/N "))
                        if questiona == "S":  # Altera loja de devolução para atual
                            emprestimos[cod_cli]['loja'] = loja_dev
                    # Atualiza Estoque da Loja
                    lojas = Sistema.leh_lojas()
                    loja_atual = lojas[emprestimos[cod_cli]['loja']]
                    loja_atual['estoque'] += dados_emprestimo['qtde']
                    # Grava novo estoque da Loja
                    with open('lojas.txt', 'w+') as file:
                        lojas = str(lojas)
                        file.write(lojas)
                    # Fim atualização lojas
                    print (f"===> Atualizando Estoque\n"
                           f"\t Loja {emprestimos[cod_cli]['loja']} - {loja_atual['loja']} \t\tEstoque Atual: {loja_atual['estoque']}")
                    # Dá Baixa no Empréstimo
                    del emprestimos[cod_cli]
                    with open('emprestimos.txt', 'w+') as file:
                        emprestimos = str(emprestimos)
                        file.write(emprestimos)
                    print(f"\n===> Bicicleta{plural} devolvida{plural} com Sucesso!")
                    sai_loop = "sair"
                else:
                    print(">>>>>> Devolução Cancelada !!!")
                    return False
                    sai_loop = "sair"
        return True

    def calcula_valor(self, ano, mes, dia, hora, min):
        valor_acobrar = 0
        agora = datetime.now()
        data_emprestimo = datetime(ano, mes, dia, hora, min, 0)
        tempo = (agora - data_emprestimo)
        horas = int(tempo.total_seconds() / 60 // 60)
        minutos = (tempo.total_seconds() / 60) % 60
        if minutos >= 45:  # Testar quartos de hora
            horas += 0.75
        elif minutos >= 30:
            horas += 0.5
        elif minutos >= 15:
            horas += 0.25

        dias = tempo.days
        if horas % 24 >= 0:
            dias += 1
        resto_semana = dias % 7
        semana = dias//7
        if resto_semana != 0:  # Acrescentar nova semana quando não exato.
            semana += 1
        vlr_final_horas = horas * self.valor_hora
        vlr_final_dias = dias * self.valor_dia
        vlr_final_sem = semana * self.valor_semana
        if 0 < vlr_final_sem <= vlr_final_dias:
            if vlr_final_sem <= vlr_final_horas:
                valor_acobrar = vlr_final_sem
        elif 0 < vlr_final_dias <= vlr_final_horas:
            valor_acobrar = vlr_final_dias
        else:
            valor_acobrar = vlr_final_horas
        msg_dias = str(tempo)
        msg_dias = msg_dias[:-10]  # retirar segundos
        msg_dias = msg_dias.replace(':', "h")
        msg_tolerancia = ""
        if minutos < 15:
            msg_tolerancia = msg_dias.replace('day','dia')     #"< 15 min = tolerância"
        else:
            msg_tolerancia = msg_dias.replace('day','dia')

        print(f"==== F E C H A M E N T O   D O   A L U G U E L ====\n")
        print(f"Inicío da Locação: \t\t\t\t\t{dia}/{mes}/{ano} {hora}:{min}")
        print(f"Tempo de Locação: \t\t{msg_tolerancia:>27}\n")
        print(f"========= Valores do Empréstimo/Bicicleta =========")
        print(f"Horas Locadas: \t{horas:>7}  \tValor Total R$ {vlr_final_horas:>8.2f}")
        print(f"Dias Locados: \t{dias:>7}  \tValor Total R$ {vlr_final_dias:>8.2f}")
        print(f"Semanas Locadas: {semana:>6}  \tValor Total R$ {vlr_final_sem:>8.2f}")
        print(f"===================================================")
        print(f"Melhor Valor a Cobrar/Bicicleta: \t\tR$ {valor_acobrar:>8.2f}")
        print(f"===================================================\n")
        return valor_acobrar

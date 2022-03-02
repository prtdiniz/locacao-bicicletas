from gerais import Sistema, ValorNaoEncontado
from emprestimo import Emprestimo
from datetime import datetime


class Loja(Sistema):

    def __init__(self, id_loja, nom_loja, estoque_local):
        self.id_loja = id_loja
        self.nom_loja = nom_loja
        self.__estoque_local = estoque_local

    # Getters / Setters
    @property
    def id_loja(self):
        return self.__id_loja

    @id_loja.setter
    def id_loja(self, id_loja):
        self.__id_loja = id_loja

    @property
    def nom_loja(self):
        return self.__nom_loja

    @nom_loja.setter
    def nom_loja(self, nom_loja):
        self.__nom_loja = nom_loja

    @property
    def estoque_local(self):
        return self.__estoque_local

    @estoque_local.setter
    def estoque_local(self, estoque_local):
        if estoque_local >= 0:
            self.__estoque_local = estoque_local
        else:
            raise ValueError("Estoque não pode ficar negativo !")

    # Métodos da Classe
    def locar_bikes(self, cod_loja, cod_cli):
        lojas_geral = Sistema.leh_lojas()
        loja_atual = Loja(cod_loja, lojas_geral[cod_loja]["loja"], lojas_geral[cod_loja]["estoque"])
        print(f"\n==> Validando se cliente tem empréstimos pendentes... \n"
              f"Loja: {loja_atual.id_loja}-{loja_atual.nom_loja} \t\tEstoque: {loja_atual.estoque_local}")
        emprestimos = Sistema.leh_emprestimos()
        # Validar se Cliente já está com empréstimo ativo.
        # Regra Considerada: Somente um empréstimo ativo por cliente
        if cod_cli in emprestimos:
            print(f"\n==> Só é possível realizar um empréstimo por vez.\n\n\tCliente -{cod_cli}- tem empréstimo ativo\n")
            devolve_sn = self.simnao(input("Quer consultar para devolução? (S/N) "))
            if devolve_sn == "N":
                print("Cancelando o procedimento de Empréstimo")
                print("Só é possível realizar um empréstimo por vez.")
                return
            else:
                agora = datetime.now()
                print("===> Iniciando a consulta para devolução.\n")
                emprestimo_atual = Emprestimo(cod_cli,
                                              loja_atual.id_loja,
                                              emprestimos[cod_cli]["qtde"],
                                              emprestimos[cod_cli]["ano"],
                                              emprestimos[cod_cli]["mes"],
                                              emprestimos[cod_cli]["dia"],
                                              emprestimos[cod_cli]["hora"],
                                              emprestimos[cod_cli]["min"])
                # Efetua a devolução
                devolveu = emprestimo_atual.fecha_emprestimo(emprestimo_atual.cod_cli,emprestimo_atual.cod_loja)
                if devolveu == False:
                    print ("Ok. Cancelando o procedimento de Empréstimo")
                    return
        else:
            print("\n Cliente sem empréstimos ativos. Liberado para novo empréstimo...")
        print("\n===> Iniciando Processo de Empréstimo.")
        agora = datetime.now()
        emprestimo_atual = Emprestimo(cod_cli,
                                      loja_atual.id_loja,
                                      0,
                                      agora.year,
                                      agora.month,
                                      agora.day,
                                      agora.hour,
                                      agora.minute)
        sai_loop = 0
        while sai_loop == 0:
            try:
                emprestimo_atual.qtde = int(input("Informe a quantidade de Bicicletas (999 p/ Sair): "))
            except ValueError:
                print(f"===> Informe um valor válido. O valor informado não pode ser Quantidade ")
            else:
                if emprestimo_atual.qtde == 999:  # Sair do processo de empréstimo
                    return
                novo_estoque = loja_atual.estoque_local - emprestimo_atual.qtde
                try:
                    loja_atual.estoque_local = novo_estoque
                except ValueError:
                    print("\n====== A T E N Ç Ã O ======")
                    print("Estoque Atual na Loja: \t", loja_atual.estoque_local)
                    print("Qtde Solicitada: \t\t", emprestimo_atual.qtde)
                    print()
                    print(f"===> Estoque não pode ser negativo. ")
                    print(f"===> Biclicletas Disponíveis: {loja_atual.estoque_local}")
                    print(f"===> Informe 999 para cancelar o processo.\n")
                else:
                    print(f"Novo Estoque da Loja: {loja_atual.estoque_local}")
                    confirma = Sistema.simnao(input("\nConfirma o empréstimo ? S/N "))
                    if confirma == "S":
                        print (f"\n===> Gravando dados do empréstimo ... ")
                        grava_emprestimo = {}
                        grava_emprestimo = {'loja':emprestimo_atual.cod_loja,
                                           'qtde': emprestimo_atual.qtde,'ano': emprestimo_atual.ano,
                                            'mes':emprestimo_atual.mes,'dia': emprestimo_atual.dia,
                                            'hora':emprestimo_atual.hora, 'min': emprestimo_atual.minutos}

                        emprestimos[emprestimo_atual.cod_cli] = grava_emprestimo
                        lojas_geral[loja_atual.id_loja]['estoque'] = loja_atual.estoque_local
                        # Atualiza o arquivo de empréstimos
                        Sistema.atualiza_lojas(lojas_geral)
                        Sistema.atualiza_emprestimos(emprestimos)
                        print (f"\n===> Empréstimo finalizado... <enter> para continuar. ")
                        input()
                        sai_loop = 1

    def lista_estoquegeral(self):
        lojas_geral = Sistema.leh_lojas()
        emprestadas = 0
        estoque_geral = 0
        total_empresa = 0
        print()
        print(f"|      G E R A L   D E    B I C I C L E T A S     |")
        for i in lojas_geral:
            self.lista_estoquelocal(i)
            emprestadas += self.qtde_emprestada(i)
            estoque_geral += lojas_geral[i]["estoque"]
            total_empresa = emprestadas + estoque_geral
        print(f"#"*51)
        print(f"             T o t a i s   G e r a i s    ")
        print(f"="*51)
        print(f"Em estoque: {estoque_geral:>4} Bicicletas   \t\tEmprestadas:{emprestadas:>3}")
        print(f"      Total de Bicicletas da Empresa:{total_empresa:>5}")
        print(f"#"*51,"\n")

    def lista_estoquelocal(self, loja):
        lojas_geral = Sistema.leh_lojas()
        loja_atual = Loja(loja, lojas_geral[loja]['loja'], lojas_geral[loja]['estoque'])
        head_loja = "Estoque da Loja " + str(loja) + "-" + loja_atual.nom_loja
        emprestadas = self.qtde_emprestada(loja)
        plural = ""
        if loja_atual.estoque_local > 1:
            plural = "s"
        print(f"="*51)
        print(f"{head_loja:^51} ")
        print(f"Em estoque: {loja_atual.estoque_local:>2} Bicicleta{plural}   \t\tEmprestadas:{emprestadas:>3}")

    def qtde_emprestada(self, loja):
        emprestimos = Sistema.leh_emprestimos()
        tot_emprestimos = 0
        for i in emprestimos:
            if emprestimos[i]['loja'] == loja:
                tot_emprestimos += emprestimos[i]['qtde']
        return tot_emprestimos

    @staticmethod
    def escolhe_loja():
        lojas = Sistema.leh_lojas()
        for i in lojas:
            print(f"{i} - {lojas[i]['loja']}")
        sel_loja = 0
        while sel_loja == 0:
            try:
                id_loja = int(input("Informe o código da loja: "))
                if id_loja not in lojas:
                    print("===> Loja informada não existe...")
                else:
                    loja_atual = [id_loja,lojas[id_loja]['loja'],lojas[id_loja]['estoque']]
                    return loja_atual
            except ValueError:
                print("Informe um código Válido, por favor")

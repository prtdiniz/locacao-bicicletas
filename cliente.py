from gerais import Sistema, ValorNaoEncontado


class Cliente:

    def __init__(self, nome_cli, cpf_cli, cod_cli):
        self.cod_cli = cod_cli
        self.nome_cli = nome_cli
        self.cpf_cli = cpf_cli

    @property
    def cod_cli(self):
        return self.__cod_cli

    @cod_cli.setter
    def cod_cli(self, cod_cli):
        if cod_cli == 0:
            print("Cadastrando novo Cliente ")
            self.__cod_cli = Cliente.gera_codigo()
            print("Novo Código do Cliente: ", self.__cod_cli)
        else:
            self.__cod_cli = cod_cli

    @property
    def nome_cli(self):
        return self.__nome_cli

    @nome_cli.setter
    def nome_cli(self, nome_cli):
        self.__nome_cli = nome_cli

    @property
    def cpf_cli(self):
        return self.__cpf_cli

    @cpf_cli.setter
    def cpf_cli(self, cpf_cli):
        self.__cpf_cli = cpf_cli

    def consulta_cli_cod(cod_cli):
        clientes = Sistema.leh_clientes()
        print(f"\nValidando Código Cliente ...")
        if cod_cli in clientes.keys():
            cliente_atual = Cliente(clientes[cod_cli]['nome'], clientes[cod_cli]['cpf'], cod_cli)
            print("="*60)
            print(f"Código do Cliente: {cliente_atual.cod_cli}")
            print(f"Cliente: {cliente_atual.nome_cli:<34}CPF : {cliente_atual.cpf_cli}")
            print("="*60)
            return cliente_atual
        else:
            raise ValorNaoEncontado(cod_cli)
            return

    @staticmethod
    def listar_clientes():
        clientes = Sistema.leh_clientes()
        emprestimos = Sistema.leh_emprestimos()
        print()
        print("="*70)
        print("=========================  C L I E N T E S  ==========================")
        print("Cod   Nome                                      CPF         Bicicletas")
        print("-"*70)
        for index in clientes:
            if index in emprestimos.keys():
                qtde = emprestimos[index]['qtde']
            else:
                qtde = 0
            print(f"{index:>3} - {clientes[index]['nome']:<41} {clientes[index]['cpf']:<11} {qtde:>10}")
            print("-"*70)
        print("="*70)

    def cadastrar_cliente():
        print("\n=== Cadastrar novo Cliente ===")
        final = False
        while final == False:
            nome_new = input("Nome do Cliente: ")
            status = False
            cliente_novo = None
            while status == False:
                cpf_new = str(input("CPF do Cliente: "))
                status = Cliente.valida_cpf(cpf_new)
                if status == False:
                    print("\n==================================================")
                    print("===> CPF informado é inválido, informe novamente")
                    print("==================================================\n")
                else:
                    eh_cliente = Cliente.existe_cliente(cpf_new)
                    if eh_cliente == None:
                        cliente_novo = Cliente(nome_new, cpf_new, 0)  # "0" indica que deve ser gerado um novo código.
                        cliente_novo.gravar_novo_cliente(cliente_novo.cod_cli, cliente_novo.nome_cli, cliente_novo.cpf_cli)

                        return cliente_novo
                    else:
                        print("\n==================================================")
                        print(f"=> Cliente já Cadastrado.")
                        print(f"=> Código do Cliente: {eh_cliente.cod_cli}-{eh_cliente.nome_cli} ")
                        print("==================================================\n")
                        try:
                            resp_local = input("Deseja usar esse Cliente? (S/N)) : ")
                        except ValueError:
                            print("Valor inválido")
                        else:
                            if resp_local.upper() == 'S':
                                return eh_cliente
                            else:
                                status = True  # Retorna ao loop solicitando Nome.
            # Fim do while | Validacao Cliente
            # Cadastrar Novo Cliente

    @staticmethod
    def gravar_novo_cliente(cod_cli, nome_cli, cpf_cli):
        print(f"==> Gravando Novo Cliente...")
        clientes = Sistema.leh_clientes()  # Carrega Dicionario de Clientes
        grava_cliente = {}
        grava_cliente = {'nome':nome_cli, 'cpf': cpf_cli}
        clientes[cod_cli] = grava_cliente
        # Atualiza o arquivo de clientes
        Sistema.atualiza_clientes(clientes)
        print(f"==> Cliente atualizado: {cod_cli}-{nome_cli} {cpf_cli}")
        return

    def existe_cliente(cpf_new):  # Validar se existe o cliente na Base de Clientes
        clientes = Sistema.leh_clientes()
        print(f"\nValindando Cliente ...")
        for i in clientes:
            if cpf_new in clientes[i]['cpf']:
                cliente_atual = Cliente(clientes[i]['nome'], clientes[i]['cpf'], i)
                return cliente_atual
        return None

    @staticmethod
    def gera_codigo():
        print ("Gerando novo código de Cliente")
        clientes = Sistema.leh_clientes()
        cod_cli = 0
        for i in clientes:
            if i > cod_cli:
                cod_cli = i
        cod_cli += 1
        return cod_cli

    @staticmethod
    def valida_cpf(cpf):
        total =0
        for i in range(len(cpf)-2):
            total += int(cpf[i])*(10-i)
        dig1 = total % 11
        if dig1 < 2:
            dig1 = 0
        else:
            dig1 = 11 - dig1
        total = dig1 * 2
        for i in range(len(cpf)-2):
            total += int(cpf[i])*(11-i)
        dig2 = total % 11

        if dig2 < 2:
            dig2 = 0
        else:
            dig2 = 11 - dig2
        status = str(cpf[-2:]) == str(dig1) + str(dig2)
        return status

"""
Programa principal
- Identifica o tipo de Usuário
- Gerar funções/menu por usuário.
    - Atividades com Clientes
        - Cadastrar Cliente
        - Alugar Bicicleta
        - Verificar em qual loja tem estoque
    - Atividades nas Lojas
        - Mostrar Estoque Próprio de Bicicletas
        - Mostrar Estoque Geral de Bicicletas
        - Devolver Empréstimo
"""
###################################
# Administração geral
###################################
# Importações Classes
###################################
from gerais import Sistema, ValorNaoEncontado
from cliente import Cliente
from loja import Loja
from emprestimo import Emprestimo

sistema = Sistema()

# Inicialização de variaveis de trabalho
valida_usuarios = {"C": "Cliente", "L": "Loja"}
tipo_usuario = ""

####################################
#  Identifica o tipo de usuário   #
####################################

while tipo_usuario == "":
    try:
        print("Você é Cliente ou Loja?")
        tipo_usuario = input("Informe 'C' ou 'L' ")
    except ValueError:
        print("Opção inválida, informe novamente")
        tipo_usuario = ""
    else:  # Validar entrada Cliente ou Loja
        tipo_usuario = tipo_usuario.upper()
        if tipo_usuario not in valida_usuarios:
            print("Opção inválida, informe novamente")
            tipo_usuario = ""
        else:
            sai_loop = 0
            print(f"Olá {valida_usuarios[tipo_usuario]} !")
            while sai_loop == 0:  # Receber/Validar Código do Cliente ou Loja | Possibilitar cadastramento.
                try:
                    print(f"Informe o seu código de {valida_usuarios[tipo_usuario]}")
                    if tipo_usuario == "C":
                        cod_usuario = int(input("ou '999' p/ Novo Cadastro | '000'p/ Encerrar: "))
                    else:
                        cod_usuario = int(input("ou '000'p/ Encerrar: "))
                except ValueError:
                    print("==========")
                    print("=> O Código é um número Inteiro. Por favor, tente novamente.")
                    print("==========")
                else:
                    if cod_usuario == 000:
                        exit()
                    if tipo_usuario == "C":
                        if cod_usuario == 999:  # Cadastrar novo Cliente
                            cliente_atual = Cliente.cadastrar_cliente()
                            print(f"O Cliente atual é: {cliente_atual.cod_cli} - {cliente_atual.nome_cli}")
                            sai_loop = 1  # <==== SAIDA DO LOOP
                        else:  # Código Informado, validar se Cliente existe.
                            try:
                                cliente_atual = Cliente.consulta_cli_cod(cod_usuario)
                                sai_loop = 1  # <==== SAIDA DO LOOP
                            except ValorNaoEncontado as err:
                                print(err, "\n")
                    else:
                        lojas = Sistema.leh_lojas()
                        if cod_usuario not in lojas:
                            print("===> Loja informada não existe...")
                        else:
                            print(f"="*60)
                            print(f"Loja Atual: {cod_usuario} - {lojas[cod_usuario]['loja']:<21} Estoque: {lojas[cod_usuario]['estoque']:<3} Biciletas")
                            loja_atual = Loja(cod_usuario, lojas[cod_usuario]['loja'], lojas[cod_usuario]['estoque'])
                            sai_loop = 1
# ==================
# Menu do Programa
# ==================
opcao = 9
while opcao != 0:
    if tipo_usuario == "C":  # Menu de Cliente
        print(f' =======================  M E N U  =========================\n',
              '1 - Ver bicicletas disponíveis.\n',
              '2 - Alugar bicicleta\n',
              '3 - Calcular valor atual de emprestimo\n',
              '0 - Encerrar programa\n',
              '='*60)
    else:  # Menu de Loja
         print(f' =======================  M E N U  =========================\n',
               '1 - Mostrar estoque de bicicletas nas Lojas.\n',
               '2 - Alugar bicicleta\n',
               '3 - Receber devolução de emprestimo\n',
               '4 - Cadastrar Clientes\n',
               '5 - Listar Clientes\n',
               '0 - Encerrar programa\n',
               '='*60)
    try:
        id_loja = 0
        try:
            opcao = int(input("\n=> Informe a opção desejada: \n"))
        except ValueError:
            print("Opção Inválida, tente novamente")
        else:
            if opcao == 1:
                if tipo_usuario == "C":
                    loja_selecionada = Loja.escolhe_loja()     # Selecionar a Loja
                    print("="*60)
                    print(f"Loja: {loja_selecionada[0]} - {loja_selecionada[1]:<28} \tEstoque Atual: {loja_selecionada[2]}")
                    print("="*60)
                    simnao = Sistema.simnao(input("Deseja utilizar esta Loja para efeuar um empréstimo? S/N "))
                    if simnao == "S":
                        id_loja = loja_selecionada[0]
                        opcao = 2
                    else:
                        id_loja = 0
                    sel_loja = 1
                else:
                    loja_atual.lista_estoquegeral()
                    sistema.aguarda_tecla()
            if opcao == 2:
                if tipo_usuario == "C":  # Criar objeto loja_atual
                    if id_loja == 0:  # Cliente direto do menu, carregar dicionário de lojas
                        loja_selecionada = Loja.escolhe_loja()     # Selecionar a Loja
                        print("="*60)
                        print(f"Loja: {loja_selecionada[0]} - {loja_selecionada[1]:<28} \tEstoque Atual: {loja_selecionada[2]}")
                        print("="*60)
                    loja_atual = Loja(loja_selecionada[0], loja_selecionada[1], loja_selecionada[2])
                    loja_atual.locar_bikes(loja_atual.id_loja, cod_usuario)
                else:

                    print(f"Informe o Código do Cliente, 0 para Consultar.")
                    while True:
                        try:
                            cod_cliente = int(input())
                        except ValueError:
                            print("Informe um valor numérico Inteiro")
                        else:
                            if cod_cliente != 0:
                                clientes = sistema.leh_clientes()

                                if cod_cliente in clientes.keys():
                                    loja_atual.locar_bikes(loja_atual.id_loja, cod_cliente)
                                    break
                                else:
                                    print("\n===> Cliente não encontrado\n")
                            else:
                                Cliente.listar_clientes()
            elif opcao == 3:
                if tipo_usuario == "C":  # Apenas consultar empréstimo.
                    e = Emprestimo(cod_usuario, 1, 0, 0, 0, 0, 0, 0)
                    e.fecha_emprestimo(cod_usuario, 999)
                    sistema.aguarda_tecla()
                else:
                    print(f"Informe o Código do Cliente, 0 para Consultar.")
                    while True:
                        try:
                            cod_cliente = int(input())
                        except ValueError:
                            print("Informe um valor numérico Inteiro")
                        else:
                            if cod_cliente != 0:
                                clientes = sistema.leh_clientes()
                                if cod_cliente in clientes.keys():
                                    e = Emprestimo(cod_cliente, 1, 0, 0, 0, 0, 0, 0)
                                    e.fecha_emprestimo(cod_cliente, loja_atual.id_loja)
                                    print()
                                    break
                                else:
                                    print("\n===> Cliente não encontrado\n")
                            else:
                                Cliente.listar_clientes()
                    pass
            elif opcao == 4 or opcao == 5:
                if tipo_usuario == "C":
                    print("Opção disponível apenas para a Loja")
                    raise ValorNaoEncontado(opcao)
                else:
                    if opcao == 4:
                        cliente_atual = Cliente.cadastrar_cliente()
                    else:
                        Cliente.listar_clientes()
                        sistema.aguarda_tecla()

            elif opcao >= 6:
                raise ValorNaoEncontado(opcao)
    except ValorNaoEncontado as err:
        print(err, "\n")

print(f"\n===> Saida Normal do Sistema...")

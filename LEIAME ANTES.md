

# Projeto empréstimos de Bicicleta
### Paulo Ricardo Diniz

## Arquivos de dados para testes. Os arquivos são lidos de acordo com a opção desejada.
# Arquivos de Dados
* clientes.txt
* lojas.txt
* empréstimos.txt

## Programa principal:
main

## Classes

# gerais - Sistema, ValorNaoEncontrado
— Classes Genéricas e métodos gerais, utilizados pelas outras classes.

# cliente
- Classe de Cliente

# loja
- Classe de Loja

# empréstimos
- Classe Geral de Empréstimos

## Regras de Negócio que forma consideradas:
1) Cada Cliente somente pode ter um empréstimo ativo
2) O estoque da Loja não pode ser negativo
3) O Cliente pode fazer cadastro, caso não tenha código ainda, mas, depois de “logado” não pode cadastrar novo Cliente.
4) O Usuario deve se identificar como Cliente ou Loja
5) O Cliente pode:
	1 - Ver bicicletas disponíveis.
 	2 - Alugar bicicleta
 	3 - Calcular valor atual de emprestimo
 	0 - Encerrar programa
6) A Loja pode:
	1 - Mostrar estoque de bicicletas nas Lojas.
 	2 - Alugar bicicleta
 	3 - Receber devolução de emprestimo
 	4 - Cadastrar Clientes
 	5 - Listar Clientes
 	0 - Encerrar programa
	
Para fazer reaproveitamento, tentei deixar o programa com bastante diálogo.

============================================================
# Dados para instanciar:

### Clientes:

Cod   Nome                 		CPF         
----------------------------------------------------------------------
 15 - Marcos Vinicius               	72365275052        
----------------------------------------------------------------------
 49 - Paulo Ricardo                  	96256623088          
----------------------------------------------------------------------
  3 - Maria Quitéria             	 64938859068          
----------------------------------------------------------------------
 51 - Antonio Carlos             	 41262992036          
----------------------------------------------------------------------
 52 - José Pedro de Alcantara 		78349584025          
----------------------------------------------------------------------
 53 - José Bonifácio            	 95086491002         
----------------------------------------------------------------------
 54 - Silvio Santos                     	65700212064          


### Lojas/Estoque:
1 - Londrina		56 Bicicletas 	4 Locadas
2 - Rio de Janeiro	30 Bicicletas 	22 Locadass
3 - Maringá		23 Bicicletas 	0 Locadas
4 - Santos			05 Bicicletas 	0 Locadas
5 - Piracicaba		63 Bicicletas 	0 Locadas


### Empréstimos Ativos
Cliente 3	Loja 1	Qtde 4
Ciente 51	Loja 2	Qtde 1
Cliente 15	Loja 2	Qtde 21

======================================

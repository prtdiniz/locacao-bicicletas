# locacao-bicicletas
##Projeto do do Programa Desenvolve 40+ Magalu

Sistema de Empréstimo de Bicicletas
Vocês farão um sistema de empréstimo de bibliotecas, que envolverá duas 
classes principais (Cliente, Loja). O projeto deve ser entregue até 18/02/2022.
Cliente pode:
• Ver as bicicletas disponíveis na Loja;
• Alugar bicicletas por hora (R$5/hora);
• Alugar bicicletas por dia (R$25/dia);
• Alugar bicicletas por semana (R$100/semana)
• Aluguel para família, uma promoção que 3 ou mais empréstimos (de qualquer 
tipo) com 30% de desconto no valor total.
Loja pode:
• Calcular a conta quando o cliente decidir devolver a bicicleta;
• Mostrar o estoque de bicicletas;
• Receber pedidos de aluguéis por hora, diários ou semanais validando a 
possibilidade com o estoque e modo de aluguel existente.
Por questão de simplicidade vamos assumir que:
• Cada empréstimo segue apenas um modelo de cobrança (hora, dia ou semana);
• O cliente pode decidir livremente quantas bicicletas quer alugar;
• Os pedidos de aluguéis só podem ser efetuados se houver bicicletas suficientes 
disponíveis.
• Não se preocupem quanto a dinheiro em caixa das Lojas nem dos Clientes.
Ao projetar seus objetos você deve se atentar ao que cada classe será 
responsável por fazer, entenda o que cada elemento pode fazer, e em seguida abstraia 
o problema para desenhar as classes e seus métodos. Note que nem tudo que um 
objeto pode fazer é necessariamente um método desse objeto.
Utilize a biblioteca datetime para trabalhar com tempo no seu programa.
Você provavelmente vai querer testar o funcionamento e relação dessas classes, 
para isso use um terceiro arquivo que usa pelo menos três instâncias de Cliente e duas 
de Loja e testa a integração e funcionamento das duas classes. Para facilitar o fluxo 
das chamadas use prints em cada método que funcionem como logs, um bom log 
consiste em informar de onde ele vem (classe que printou o log), o que ele está 
fazendo (qual método), com quais informações (os parâmetros recebidos) e o momento 
que ocorreu.
Faça validações, e gere erros caso alguma validação falhe (raise), note que é 
comum logarmos (neste caso, com o print) quando algum erro ocorreu em nosso 
sistema.

**********
Texto de Resposta

*** Projeto empréstimos de Bicicleta Paulo Ricardo Diniz

Arquivos de dados para testes. Os arquivos são lidos de acordo com a opção desejada. === Arquivos de Dados clientes.txt lojas.txt empréstimos.txt

=== Programa principal: main

=== Classes

gerais - Sistema, ValorNaoEncontrado — Classes Genéricas e métodos gerais, utilizados pelas outras classes.

cliente

Classe de Cliente
loja

Classe de Loja
empréstimos

Classe Geral de Empréstimos

Regras de Negócio que forma consideradas: 1) Cada Cliente somente pode ter um empréstimo ativo 2) O estoque da Loja não pode ser negativo 3) O Cliente pode fazer cadastro, caso não tenha código ainda, mas, depois de “logado” não pode cadastrar novo Cliente. 4) O Usuario deve se identificar como Cliente ou Loja 5) O Cliente pode: 1 - Ver bicicletas disponíveis. 2 - Alugar bicicleta 3 - Calcular valor atual de emprestimo 0 - Encerrar programa 6) A Loja pode: 1 - Mostrar estoque de bicicletas nas Lojas. 2 - Alugar bicicleta 3 - Receber devolução de emprestimo 4 - Cadastrar Clientes 5 - Listar Clientes 0 - Encerrar programa

Para fazer reaproveitamento, tentei deixar o programa com bastante diálogo.

============================================================ Dados para instanciar:

Clientes:

Cod Nome CPF
15 - Marcos Vinicius 72365275052
49 - Paulo Ricardo 96256623088
3 - Maria Quitéria 64938859068
51 - Antonio Carlos 41262992036
52 - José Pedro de Alcantara 78349584025
53 - José Bonifácio 95086491002
54 - Silvio Santos 65700212064

Lojas/Estoque: 1 - Londrina 56 Bicicletas 4 Locadas 2 - Rio de Janeiro 30 Bicicletas 22 Locadass 3 - Maringá 23 Bicicletas 0 Locadas 4 - Santos 05 Bicicletas 0 Locadas 5 - Piracicaba 63 Bicicletas 0 Locadas

Empréstimos Ativos Cliente 3 Loja 1 Qtde 4 Ciente 51 Loja 2 Qtde 1 Cliente 15 Loja 2 Qtde 21

======================================


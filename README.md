# Python Snack Bar 🐍🍔

Repositório público contendo código-fonte do projeto de um sistema gerenciamento de lanchonete em Python.

## Descrição/Requisitos 📄📃

A lanchonete Tocatta and Fügue está em processo de crescimento em seu delivery e atendimento, deste modo, os seus proprietários pretendem automatizar seu funcionamento por meio de softwares
e sistemas de gerenciamento e interação poderosos. Todavia, os proprietários, ambos com formações educacionais distintas da área de Tecnologia de Informação e Comunicação, utilizam planilhas
de Excel, calculadoras, papel e caneta, porém, munidos da ciência de que você presta serviços com desenvolvimento de software, contratam-o para realizar tal tarefa. Durante o levantamento
de requisitos, alguns detalhes foram sendo percebidos durante o procedimento:

1 - A lanchonete possui três itens de pratos disponíveis à venda: lanches, pizzas e salgadinhos. 

2 - Todos os itens disponíveis à venda devem conter id, nome, quantidade disponível em estoque e preço unitário. Vale ressaltar que o id é uma chave primária que identifica unicamente um 
item e não deve se repetir; a quantidade disponível em estoque deve ser visualizada e atualizada de modo incremental pelos proprietários e de modo decremental pelos usuários, tudo de modo
síncrono e paralelo.

3 - O cliente deve fornecer dados pessoais como nome e CPF, ademais o seu endereço deve ser composto de nome da rua, número do domicílio e nome do bairro. A solicitação do CPF é devido à
à pertinência das leis brasileiras para combater sonegação fiscal e irregularidades mercadológicas. 

4 - O sistema deverá permitir a geração da nota fiscal "SiTef" contendo uma seção "Dados do cliente" com nome do cliente, nome de sua rua, além de um id próprio gerado pelo UUID 
(Identificador Único Global), outra seção contendo "Dados da compra" com informações sobre os itens consumidos e uma seção "Dados de finanças" reunindo informações sobre preço total e 
tipo de pagamento realizado pelo cliente (Dinheiro, cartão ou pix). O CPF do cliente não deve ser exposto na nota fiscal.

5 - O sistema deve ter um sistema de cálculo de troco em caso de pagamento realizado por dinheiro em cédula e retornar o valor ao usuário.

Para o cliente, é imprescendível que o sistema tenha funcionalidades de apresentação de cardápio virtual, informações adicionais sobre os pratos, a título de exemplo, pizzas possuem 
sabor e ingredientes de borda, recheio e molho, lanches têm sobre molhos, recheio e o tipo de pão, salgadinhos têm sobre recheio e massa. Além disso, é importante que haja bons tratamentos de exceções, verificações em testes de usabilidade e persistência e segurança do software em acessos simultâneos mesmo com uso de tecnologias de orquestração de contêineres como
Docker e Kubernetes ou a garantia de propriedades de sistemas de gerenciamento de bancos de dados, sejam eles relacionais sejam não-relacionais.





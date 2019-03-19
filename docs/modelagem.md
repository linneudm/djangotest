

# Modelagem

## Diagrama de Casos de Uso
![DIagrama de Casos de Uso](http://i731.photobucket.com/albums/ww311/LinneuDM/casosdeuso-djangotest1_1.jpeg)
### Atores

     1. Usuário Autenticado: Usuário cujas credenciais foram cadastradas previamente;
     2. Usuário Não Autenticado: Usuário que acessa a aplicação sem nenhuma credencial;

### Ações

    1. Criar Novo Produto: cadastra um novo produto
    2. Modificar Produto: atualiza os dados de um produto existente
    3. Remover Produto: remove um produto previamente cadastrado
    4. Consultar Produto: consulta um ou mais produtos existentes
    5. Criar Nova Operação: cadastra uma nova operação relacionada a algum produto, modificando seu estoque
    6. Remover Operação: remove uma operação previamente cadastrada, retornando os produtos pro estoque
    7. Consultar Operação: consulta uma ou mais operações existentes

## Diagrama de Entidade Relacionamento (DER)
![Diagrama de Entidade Relacionamento](https://i731.photobucket.com/albums/ww311/LinneuDM/der-djangotest1.jpeg)
### Entidades

 **1. Produto**
 Atributos: nome, preço e estoque
 **2. Operação**
 Atributos: autor, data, tipo e quantidade

## Diagrama de Classes (UML)
![Diagrama de Classes](https://i731.photobucket.com/albums/ww311/LinneuDM/classes-djangotest.jpeg)
**1. Product**
Classe que mantém as informações acerca de um produto.
Atributos:

 1. *name*: do tipo *String*. Guarda o nome que descreve o produto
 2. *price*: do tipo *Float*. Guarda o preço unitário do produto.
 3. *stock*: do tipo *Integer*. Mantém a informação da quantidade de produtos existente em estoque.
 
 **2. Operation**
Classe que mantém as informações acerca das operações relacionadas a um determinado produto.
Atributos:
1. *author*: do tipo *User*. É a chave estrangeira para o autor da operação.
2. *product*: do tipo *Product*. É a chave estrangeira para o produto a qual a operação está sendo feita.
3. *date*: do tipo *Date*. Armazena a data em que foi realizada a operação.
4. *typeOperation*: do tipo *String*. Guarda a natureza da operação. Possíveis valores: Entrada - quando a operação visa renovar o estoque de um produto. Saída - quando a operação visa cadastrar a retirada de um produto do estoque.
5. *quantity*: do tipo *Integer*. Este campo armazena a quantidade de produtos que está sendo colocada ou retirada do estoque.
Métodos:
- *totalPrice()*: este método calcula o custo total da operação - *quantidade de produtos x valor do produto*.
Este projeto foi um estudo utilizando Flask, Bootstrap, Cru.js e um banco de dados fictício para explorar e aprender novos conceitos de desenvolvimento web.

# Aplicação CRUD com Flask

Este projeto demonstra uma aplicação simples CRUD (Create, Read, Update, Delete) usando Flask, onde você pode gerenciar dados de clientes.

## Rotas

### Rota Principal

* /: Renderiza a página inicial.

### Rotas de Cliente (/cliente)

* /: Lista todos os clientes.
* /new: Mostra um formulário para adicionar um novo cliente.
* /<int:cliente_id>: Mostra detalhes de um cliente específico.
* /<int:cliente_id>/edit: Mostra um formulário para editar um cliente específico.
* /<int:cliente_id>/update: Atualiza os detalhes de um cliente específico.
* /<int:cliente_id>/delete: Deleta um cliente específico

## Banco de Dados
Este projeto utiliza um banco de dados fictício em memória armazenado em `database/cliente.py` para fins de demonstração. Ele armazena dados de cliente usando uma lista em Python.

## Tecnologias Utilizadas
* Flask: Framework web em Python para construir aplicações web.
* Bootstrap: Framework front-end para design responsivo e mobile-first de websites.
* cru.js: (Assumido como uma biblioteca para requisições AJAX ou operações do lado cliente, baseado na sua descrição)

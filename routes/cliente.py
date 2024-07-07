from flask import Blueprint,render_template,request
from database.cliente import CLIENTES
import requests

cliente_route = Blueprint('cliente',__name__)

# listar cliente
@cliente_route.route('/')
def lista_cliente():
    return render_template('lista_cliente.html', clientes= CLIENTES)

# Inserir cliente
@cliente_route.route('/', methods = ['POST'])
def inserir_cliente():
    data = request.json
    
    novo_usuario = {
        "id": len(CLIENTES) + 1,
        "nome": data['nome'],
        "email": data['email']
    }
    CLIENTES.append(novo_usuario)
    
    return render_template('item_cliente.html', cliente=novo_usuario)

# Formulario cliente
@cliente_route.route('/new')
def form_cliente():
    return render_template('form_cliente.html')

# Mostrar detalhe do cliente
@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    
    cliente = list(filter(lambda c: c['id'] == cliente_id, CLIENTES))[0]
    return render_template('detalhe_cliente.html', cliente=cliente)

# Formulario de alterar dados Cliente
@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    
    cliente = None
    for c in CLIENTES:
        if c['id'] == cliente_id:
            cliente = c
    
    return render_template('form_cliente.html', cliente = cliente)

# Atualizar dados de Cliente
@cliente_route.route('/<int:cliente_id>/update', methods = ['PUT'])
def update_cliente(cliente_id):
    cliente = None
    
    data = request.json
    
    for c in CLIENTES:
        if c['id'] == cliente_id:
            c['nome'] = data['nome']
            c['email'] = data['email']
            
            cliente_editado = c
        
    return render_template('item_cliente.html', cliente= cliente_editado)

# Deletar Cliente
@cliente_route.route('/<int:cliente_id>/delete', methods = ['DELETE'])
def delete_cliente(cliente_id):
    global CLIENTES
    CLIENTES = [ c for c in CLIENTES if c['id'] != cliente_id ]
    return {'delete': 'ok'}
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from models import Crud

# Inicializando a aplicação
app = Flask(__name__)
# Permite que o front end faça requisições, mesmo em dominios diferentes
CORS(app)

# Instanciando o Crud
crud = Crud()

# Criando rota principal 
@app.route('/')
def index():
    return render_template("form.html")

# Criando rota de envio de dados
@app.route("/relatos/post", methods = ['POST'])
def post_relatos():
    data = request.json
    nome = data["nome"]
    email = data["email"]
    praia = data["praia"]
    descricao = data["descricao"]
    response = crud.post(nome, email, praia, descricao)
    if response["status"] == "succes":
        return jsonify({"message":"Dados inseridos no banco de dados com sucesso!"})
    else:
        return jsonify({"message": "404"})

# Criando rota de atualização de dados
@app.route("/relatos/put", methods=['PUT'])
def put_relatos(id:int, nome:str, email:str, praia:str, descricao:str):
    response = crud.put(id, nome, email, praia, descricao)
    if response["status"] == "success":
        return jsonify({"message": "Dados atualizado com sucesso"})
    else:
        return jsonify({"message": "404"})

# Criando rota de atualização de um unico dado
@app.route("/relatos/patch")
def patch_relatos(id:int, dado:str, novo_dado:str):    
    response = crud.patch(id, dado, novo_dado)
    if response["status"] == "succes":
        return jsonify({"message": "Dado atualizados com sucesso"})
    else:
        return jsonify({"message": "404"})

# Criando rota de removação de dado
@app.route("/relatos/delete")
def delete_relatos(id:int):
    deleted = crud.delete(id)
    if deleted["status"] == "success":
        return jsonify({"message":"Registro deletado com sucesso!"})
    else:
        return jsonify({"message": "404"})
    
# Criando rota de pegar dados
@app.route("/relatos/get", methods=['GET'])
def get_relatos():
    response = crud.get()
    if response["status"] == "success":
        return jsonify({"message": response["message"]})
    else:
        return jsonify({"message": "404"})

# Criando rota de pegar dado com id
@app.route("/relatos/get-with-id")
def get_relatos_with_id(id:int):
    response = crud.get_with_id(id)
    if response["status"] == "succes":
        return jsonify({"message": response["message"]})
    else:
        return jsonify({"message": "404"})

if __name__ == "__main__":
    # Executa a aplicação
    app.run(debug=True)
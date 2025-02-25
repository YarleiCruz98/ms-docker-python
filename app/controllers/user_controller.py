from flask import make_response, jsonify, request
from app.models.user_model import User

def get_users():
    """ Retorna todos os usuários """
    return make_response(jsonify({
        "mensagem": "Listagem de usuários",
        "usuarios": User.get_users()
    }), 200)

def get_user_by_id(user_id):
    """ Retorna um usuário específico """
    user = User.get_user_by_id(user_id)
    
    if not user:
        return make_response(jsonify({"mensagem": "Usuário não encontrado"}), 404)

    return make_response(jsonify({
        "mensagem": "Usuário encontrado",
        "usuario": user
    }), 200)

def store():
    """ Cria um novo usuário """
    data = request.get_json()

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()

    if not name or not email:
        return make_response(jsonify({
            "mensagem": "Erro",
            "erro": "Os campos 'name' e 'email' são obrigatórios e não podem estar vazios."
        }), 400)  

    new_user = User.store(data)

    return make_response(jsonify({
        "mensagem": "Usuário salvo com sucesso",
        "usuario": new_user
    }), 201)

def update(user_id):
    """ Atualiza um usuário pelo ID """
    data = request.get_json()
    user = User.update(user_id, data)

    if not user:
        return make_response(jsonify({"mensagem": "Usuário não encontrado"}), 404)

    return make_response(jsonify({
        "mensagem": "Usuário atualizado com sucesso",
        "usuario": user
    }), 200)

def delete(user_id):
    """ Deleta um usuário pelo ID """
    if User.delete(user_id):
        return make_response(jsonify({"mensagem": "Usuário deletado com sucesso"}), 200)
    
    return make_response(jsonify({"mensagem": "Usuário não encontrado"}), 404)
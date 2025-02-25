import uuid

class User:
    users = [
        {"id": str(uuid.uuid4()), "name": "Alice", "email": "alice@example.com"},
        {"id": str(uuid.uuid4()), "name": "Bob", "email": "bob@example.com"}
    ]

    @classmethod
    def get_users(cls):
        """ Retorna todos os usuários """
        return cls.users

    @classmethod
    def get_user_by_id(cls, user_id):
        """ Retorna um usuário pelo ID """
        for user in cls.users:
            if user["id"] == user_id:
                return user
        return None
    
    @classmethod
    def store(cls, data):
        """ Cria um novo usuário """
        new_user = {
            "id": str(uuid.uuid4()),
            "name": data["name"],
            "email": data["email"]
        }
        cls.users.append(new_user)
        return new_user

    @classmethod
    def update(cls, user_id, data):
        """ Atualiza um usuário pelo ID """
        for user in cls.users:
            if user["id"] == user_id:
                user["name"] = data.get("name", user["name"])
                user["email"] = data.get("email", user["email"])
                return user
        return None

    @classmethod
    def delete(cls, user_id):
        """ Deleta um usuário pelo ID """
        for user in cls.users:
            if user["id"] == user_id:
                cls.users.remove(user)
                return True
        return False
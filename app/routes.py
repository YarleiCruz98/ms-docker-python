from app.controllers.user_controller import get_users, get_user_by_id, store, update, delete

def init_routes(app):
    @app.route('/users', methods=['GET'])
    def users():
        return get_users()

    @app.route('/users/<user_id>', methods=['GET'])
    def user_detail(user_id):
        return get_user_by_id(user_id)

    @app.route('/users', methods=['POST'])
    def store_user():
        return store()

    @app.route('/users/<user_id>', methods=['PUT'])
    def update_user(user_id):
        return update(user_id)

    @app.route('/users/<user_id>', methods=['DELETE'])
    def delete_user(user_id):
        return delete(user_id)
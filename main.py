from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from db import create_db
import db_actions
app = Flask(__name__)
api = Api(app)


def row_to_json(tables: list):
    data = []
    for table in tables:
        data.append({
            "id": table.id,
            "author": table.author,
            "text": table.text
        })

    data_response = jsonify(data)
    data_response.status_code = 200
    return data_response

class PostAPI(Resource):
    def get(self, id=0):
        if id:
            table = db_actions.get_table(id)
            if table:
                return row_to_json([table])

            answer = jsonify("Такого столу немає")
            answer.status_code = 400
            return answer

        tables = db_actions.get_tables()
        return row_to_json(tables)
    
    def table(self):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("text")
        params = parser.parse_args()
        id = db_actions.add_post(params.get("author"), params.get("text"))
        answer = jsonify(f"Новий стіл успішно додано id {id}")
        answer.status_code = 200
        return answer
    def put(self,id):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("text")
        params = parser.parse_args()
        answer = db_actions.update_table(id, params.get("author"))
        answer = jsonify(answer)
        answer.status_code = 200
        return answer
    def delete(self,id):
        answer = db_actions.delete_post(id)
        answer = jsonify(answer)
        answer.status_code = 200
        return answer

api.add_resource(PostAPI, "/api/tables/", "/api/tables/<int:id>/")


if __name__ == "__main__":
    create_db()
    app.run(debug=True, port=3000)

        




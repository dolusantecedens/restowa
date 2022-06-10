from flask import Flask,  abort, jsonify, request, make_response
from models import library

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/api/v1/todos/", methods=["GET"])
def todos_list_api_v1():
    return jsonify(library.all())
@app.route("/api/v1/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = library.get(todo_id)
    if not todo:
        abort(404)
    return jsonify({"todo": todo})

@app.route("/api/v1/todos/", methods=["POST"])
def create_todo():
    if not request.json or not 'title' in request.json:
        abort(400)
    book = {
        'id': library.all()[-1]['id'] + 1,
        'title' : request.json ['title'],
        'author': request.json['author'],
        'year': request.json['title'],
        'genre' : request.json['genre'],
        'description' : request.json['description']
            }
    library.create(book)
    return jsonify({'book': book}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)
@app.route("/api/v1/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    result=library.delete(todo_id)
    if not result:
        abort(404)
    return jsonify({'result':result})
@app.route("/api/v1/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    x=library.get(todo_id)
    if not x:
        abort(404)
    if not request.json:
        abort(400)
    data=request.json
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'description' in data and not isinstance(data.get('description'), str),
        'done' in data and not isinstance(data.get('done'), bool)
    ]):
        abort(400)
    todo = {
        'title': data.get('title', x['title']),
        'genre': data.get('genre',x['genre']),
        'description': data.get('description', x['description']),
        'year': data.get('done', x['done']),
        'author': data.get('author', x['author'])
    }
    library.update(todo_id, todo)
    return jsonify({'todo':todo})





if __name__ == "__main__":
    app.run(debug=True)
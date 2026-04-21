from flask import Flask, request, jsonify
from database.database import db
from services.repo_service import SnippetRepository
from models.snippet import SnippetDomain

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
repo = SnippetRepository()

@app.route('/api/snippets', methods=['GET'])
def get_snippets():
    snippets = repo.get_all()
    return jsonify([{"id": s.id, "content": s.content} for s in snippets])

@app.route('/api/snippets', methods=['POST'])
def create_snippet():
    data = request.get_json()
    new_snippet = SnippetDomain(id=None, content=data.get('content'))
    repo.add(new_snippet)
    return jsonify({"message": "Snippet created"}), 201

@app.route('/api/snippets/<int:id>', methods=['PUT', 'PATCH'])
def update_snippet(id):
    data = request.get_json()
    if repo.update(id, data.get('content')):
        return jsonify({"message": "Snippet updated"}), 200
    return jsonify({"error": "Snippet not found"}), 404

@app.route('/api/snippets/<int:id>', methods=['DELETE'])
def delete_snippet(id):
    if repo.delete(id):
        return jsonify({"message": "Snippet deleted"}), 200
    return jsonify({"error": "Snippet not found"}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
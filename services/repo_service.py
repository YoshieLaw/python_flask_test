from database.database import db
from models.snippet import SnippetDomain

# Define the Persistence Model here for simplicity
class SnippetModel(db.Model):
    __tablename__ = 'snippets'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

class SnippetRepository:
    def get_all(self):
        return [SnippetDomain(s.id, s.content) for s in SnippetModel.query.all()]

    def add(self, domain_obj):
        new_item = SnippetModel(content=domain_obj.content)
        db.session.add(new_item)
        db.session.commit()
        return new_item.id

    def update(self, id, content):
        item = SnippetModel.query.get(id)
        if item:
            item.content = content
            db.session.commit()
            return True
        return False

    def delete(self, id):
        item = SnippetModel.query.get(id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return True
        return False
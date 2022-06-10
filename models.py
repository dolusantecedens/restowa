from importlib.abc import TraversableResources
import json


class Library:
    def __init__(self):
        try:
            with open("biblioteka.json","r") as f:
                self.library = json.load(f)
        except FileNotFoundError:
            self.library = []
    def all(self):
        return self.library
    def get(self, id):
        todo = [todo for todo in self.all() if todo['id'] == id]
        if todo:
            return todo[0]
        return []
    def save_all(self):
        with open('library.json','w') as f:
            json.dump(self.library, f)
    def create(self,book):
        self.library.append(book)
        self.save_all()
    def delete(self,id):
        book=self.get(id)
        if book:
            self.library.remove(book)
            self.save_all()
            return True
        return False
    def update(self,id,data):
        book=self.get(id)
        if book:
            index=self.library.index(book)
            self.library[index]=data
            self.save_all()
            return True
        return False


library=Library()
from random import randint
class Family:
    def __init__(self, last_name): #init es mi constructor
        self._last_name = last_name
        self._name=""
        self._age= 0
        self._members = [{"_id": "1", "_name": "esteban", "_lastname": "bravo", "_age": 29}] #vamos a ir guardando cada uno de los elementos de la familia que vaayamos creando
   
    def _generateId(self): # devuelve un numero aleatorio entre 0 y el numero que se ve
        return randint(0, 99999999)

    def add_member(self, member):
        member = {
            "id": self._generateId(),
            "name": member._name,
            "lastname": member._last_name,
            "age": member._age
        }
        self._members.append(member)
        return member

        
    def delete_member(self, id):
        member = self.get_member(id):
        member.remove()
        

        
    def update_member(self, id, member):
        obj = self.get_member(id)
        obj.update(member)
        return obj

    def get_member(self, id):
        member = list(filter(lambda item: item["id"] == id, self._members))
        return member[0]

    def get_all_members(self):
        return self._members
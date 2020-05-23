import os
from flask import Flask, render_template, jsonify, request
from flask_script import Manager
from  flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from models import db
from family import Family

BASE_DIR = os.path.abspath(os.path.dirname( __file__))  #guarda la ruta del directorio de mi aplicacion// donde estoy ubicado

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'dev.db') #cual va ser la base de datos que voi a utilizar
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # EVITA QUE MI BASE DE DATOS GUARDE CAMBIOS INNECESARIOS CADA VEZ QUE HAGO UNA MODIFICACION A NIVEL DE TABLAS

db.init_app(app)
migrate = Migrate(app, db)#genera los comandos para crear la migracion.

manager = Manager(app)
manager.add_command('db', MigrateCommand)#ejecuta mis migraciones por consola
CORS(app) #evite que tenga problemas con el navegador,para que pueda utilizarse en manera de desarollo


fam = Family("bravo")

@app.route('/') #se crea una ruta principal
def home():
    return render_template('index.htm', name = "home")

@app.route("/family", methods=["GET","POST"])
def members():
    if request.method=="GET":
        members = fam.get_all_members()
        return jsonify(members),200

    if request.method == "POST":# nueva informacion, crea informacion
        if not request.json.get("name"):
            return jsonify({"name": "is required"}), 422
        if not request.json.get("age"):
            return jsonify({"age": "is required"}),422
        if not.request.json.get("lastname")
            return jsonify({"lastname": "is required"}),422    

        fam._name = request.json.get("name")
        fam._age = request.json.get("age")
        fam._last_name = request.json.get("lastname")

        member= fam.add_member(fam)
        return jsonify(member), 200 

    
    if request.method == "PUT":# para actualizar
        if not request.json.get("name"):
            return jsonify({"name": "is required"}), 422
        if not request.json.get("age"):
            return jsonify({"age": "is required"}),422

        update = {
            "name": request.json.get("name")
            "age": request.json.get("age")
        }
        
        member = fam.update_member(id,update)
            return jsonify(member), 200


    if request.method == "DELETE":
        
            member = fam.delete_member(id,members)
            return jsonify("msge": "member eliminado")

            
        
        
    
    if __name__ == "__main__":
    manager.run() # inicializa mi aplicacion

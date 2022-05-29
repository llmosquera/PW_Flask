#importar la libreria flask
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
 
#Aqui almacenara la lista de tareas que seran registradas 
tareas = []
 # Controlador de las rutas de las páginas 
@app.route("/")
def home():
	return render_template("Index.html", tareas=tareas)


# Se redirigue al controlador de la pagina agregar 
@app.route("/agregar", methods=["GET", "POST"])
def agregar():
	if request.method == "GET":
		return render_template("agregar.html")
	else:
		tarea = request.form.get("tarea")
		tareas.append(tarea)
		return redirect("/")

#Para reproducir automaticamente 
if __name__ == "__main__":
	app.run(debug=True)
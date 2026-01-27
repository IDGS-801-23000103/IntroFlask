from flask import Flask, render_template, request



app=Flask(__name__)

@app.route("/")
def index():
    titulo="Flask IDGS801"
    lista="Melannie", "Alejandro", "Elena"
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")


@app.route("/operasBas",methods=['GET', 'POST'])
def operas1():
    n1=0
    n2=0
    res=0
    if request.method=='POST':
        n1=request.form.get('n1')
        n2=request.form.get('n2')
        tem=float(n1)+float(n2)
    return render_template("operasBas.html",n1=n1,n2=n2,res=res)

@app.route("/resultado",methods=['GET', 'POST'])
def resultado():
    if request.method == "POST":
        n1=request.form.get('n1')
        n2=request.form.get('n2')
        tem=float(n1)+float(n2)
    return f"La suma es: {tem}"


@app.route("/hola")
def hola():
    return "Hola mundo"

@app.route("/user/<string:user>")
def user(user):
    return f"Hello, {user}"

@app.route("/default/")
@app.route("/default/<string:parm>")
def func(param="melannie"):
    return f"<h1>¡Hola, {param}!</h1>"

@app.route("/operas")
def operas():
    return '''
        <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        </br>
        <label for="name">apaterno:</label>
        <input type="text" id="name" name="name" required>
        </form>
        
        '''

if __name__=='__main__':
    app.run(debug=True)
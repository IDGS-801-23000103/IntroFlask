from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hello Word"

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
from flask import Flask, request

port = 5000
app = Flask(__name__)
contador = 0


@app.route("/")
def hello_world():
    global contador
    contador += 1
    print(f"LOG: visita numero:{contador}")
    response = "<h1>Hola Usuario</h1>"
    response += f"<h3>Numero de visitas {contador}</h3>"

    return response


@app.route("/casa")
def casa():
    return f"Mi casa es el num {contador}"


@app.route("/camion")
def camion():
    cilindros = request.args.get('ruedas')
    k = request.args.get('k')

    k = "perro"

    print(type(cilindros))
    a = int(cilindros)
    print(type(a))
    response = f"He visto pasar {contador * 7} camiones"
    response += f'<h1> Tenemos  : {round(a / 10)} ruedas en el camion</h1>'

    return response



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)

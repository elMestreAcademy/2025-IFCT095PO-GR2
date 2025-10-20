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


def sanitize_int(dato):
    sanitized = None
    try:
        int(dato)
        sanitized = int(dato)
    except TypeError:
        sanitized = "NONE"
    except ValueError:
        sanitized = "INVALID"

    return sanitized


@app.route("/camion")
def camion():
    ruedas = sanitize_int(request.args.get('ruedas'))

    response = f"He visto pasar {contador * 7} camiones"
    response += f'<h1> Tenemos  : {ruedas} ruedas en el camion</h1>'

    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)

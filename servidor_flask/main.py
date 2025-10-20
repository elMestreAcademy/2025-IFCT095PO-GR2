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
        # sanitized = "NONE"
        print("[WARN: missing parameter]")
    except ValueError:
        # sanitized = "INVALID"
        print("[WARN: missing parameter]")

    return sanitized


@app.route("/camion")
def camion():

    response = f"He visto pasar {contador * 7} camiones"

    for arg in ["ruedas", "color", "peso"]:
        dato = sanitize_int(request.args.get(arg))
        if dato is not None:
            response += f'<h1> Tenemos  : {dato} {arg} en el camion</h1>'

    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)

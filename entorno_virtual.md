# Entorno virual

[VENV](https://docs.python.org/3/library/venv.html)
[FLASK](https://flask.palletsprojects.com/en/stable/installation/)

- Ir al directorio de trabajo

```bash
cd \directorio_de_trabajo
```
- Creamos un directorio para el proyecto (y entramos)

```bash
mkdir mi_proyecto
cd mi_proyecto
```

- crear entorno virtual

```bash
python -m venv .venv
```

- activamos entorno virtual

```bash
.venv\Scripts\activate
```

- Instalamos dependencias (Flask es solo un ejemplo)

```bash
pip install Flask
```

o

```bash
pip install -r requirements.txt
```

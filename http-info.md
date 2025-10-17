# HTTP

## request methods

- **GET**: El método GET solicita una representación de un recurso específico. Las peticiones que usan el método GET sólo deben recuperar datos.
- **HEAD**: El método HEAD pide una respuesta idéntica a la de una petición GET, pero sin el cuerpo de la respuesta.
- **POST**: El método POST se utiliza para enviar una entidad a un recurso en específico, causando a menudo un cambio en el estado o efectos secundarios en el servidor.
- **PUT**: El modo PUT reemplaza todas las representaciones actuales del recurso de destino con la carga útil de la petición.
- **DELETE**: El método DELETE borra un recurso en específico.
- **CONNECT**: El método CONNECT establece un túnel hacia el servidor identificado por el recurso.
- **OPTIONS**: El método OPTIONS es utilizado para describir las opciones de comunicación para el recurso de destino.
- **TRACE**: El método TRACE realiza una prueba de bucle de retorno de mensaje a lo largo de la ruta al recurso de destino.
- **PATCH**: El método PATCH es utilizado para aplicar modificaciones parciales a un recurso

## Códigos de estado de respuesta HTTP

- Respuestas informativas (100–199),
- Respuestas satisfactorias (200–299),
- Redirecciones (300–399),
- Errores de los clientes (400–499),
- y errores de los servidores (500–599).

## Ejemplo de peticion (RAW)

Requests HEADER

```
GET /casa HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: es-ES,es;q=0.9,ca;q=0.8,en;q=0.7
Cache-Control: no-cache
Connection: keep-alive
DNT: 1
Host: 10.196.3.160:5000
Pragma: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36
```


Response HEADER

```
HTTP/1.1 200 OK
Server: Werkzeug/3.1.3 Python/3.13.7
Date: Fri, 17 Oct 2025 08:02:23 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 19
Connection: close
```


Response CONTENT

```
<html>CONTENIDO DE LA WEB </html>
```

# Estatus
 Programa que revisa el estado de mi aplicacion.

```python
def saludo():
    print("Hola, mundo!")

saludo()
```

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-api-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: flask-api
  template:
    metadata:
      labels:
        app: flask-api
    spec:
      containers:
      - name: flask-api
        image: louisev/flask-api:v2
        ports:
        - containerPort: 5000

```

```Dockerfile
# Usa una imagen base de Python con la versión 3.9
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requerimientos (para instalar dependencias)
COPY requirements.txt /app

# Instala las dependencias usando pip
RUN pip install -r requirements.txt

# Copia el código fuente al contenedor
COPY app.py /app

# Expone el puerto 5000 (puerto en el que Flask ejecutará la API)
EXPOSE 5000

# Comando para correr la aplicación
CMD ["python", "app.py"]
```

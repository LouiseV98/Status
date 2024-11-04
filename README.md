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

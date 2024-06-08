# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de tu aplicación al contenedor
COPY example.py .

# Instala las dependencias de tu aplicación
RUN pip install fastapi uvicorn requests geopy

# Expone el puerto 8000 para que se pueda acceder a la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["uvicorn", "example:app", "--host", "0.0.0.0", "--port", "8000"]


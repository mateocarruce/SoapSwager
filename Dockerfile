# Usar la imagen base de Python 3.11
FROM python:3.11-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo requirements.txt y el código fuente al contenedor
COPY requirements.txt /app/
COPY app.py /app/

# Instalar las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que el servidor SOAP estará disponible
EXPOSE 8000
EXPOSE 5000

# Comando para ejecutar la aplicación cuando el contenedor se inicie
CMD ["python", "app.py"]

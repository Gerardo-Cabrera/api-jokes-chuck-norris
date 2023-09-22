# Instrucciones

- Clonar el repositorio en un directorio en el equipo.
- Acceder al repositorio clonado.
- Instalar Python si no está instalado.
- Instalar **virtualenv** utilizando el comando: **pip install virtualenv** para poder crear entornos virtuales e instalar las dependencias correspondientes.
- Crear entorno virtual mediante el comando: **virtualenv nombredelentorno** (por convención se le nombra **venv**).
- Si se está en el directorio donde se creó el entorno virtual, activarlo mediante el comando: **source /venv/Scripts/activate** para Windows y **source /venv/bin/activate** para Linux o Mac. En ambos casos se puede desactivar usando el comando: **deactivate**.
- Una vez activado el entorno virtual ejecutar el siguiente comando: **pip install -r requirements.txt** para instalar las dependencias que se utilizarán en el proyecto.
- Una vez instaladas las dependencias, como una de ellas es el microframework **Flask**, se puede utilizar el comando: **flask run** para ejecutar el archivo que contiene el endpoint de la API para consultar los chistes.
- Se puede probar la API en **Postman** copiando la **url** mostrada al ejecutar el comando del paso anterior y agregando al final **/jokes** para acceder al endpoint, el cual si no se especificó ninguna configuración debería ser **http://127.0.0.1:5000/jokes** y al realizar la petición debería mostrar 25 chistes cada vez que se ejecute.

Pasos para levantar el proyecto:

1)Disponer de una bd postgres local llamada "vehiculos"
2)Generar un entorno para instalar las dependencias del proyecto: python -m venv .venv
3)Instalar las dependencias necesarias del proyecto: pip install -r requirements.txt
4)Iniciar el proyecto con uvicorn: uvicorn main:app --reload
5)Importar la coleccion de postman
6)Obtener el token mediante su endpoint correspondiente para despues asi poder usar el resto de los endpoints
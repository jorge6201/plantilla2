# Esta es una aplicacion basica que utiliza FastAPI para crear una API restful.
from fastapi import FastAPI
from router.router import user # Importamos el router que hemos creado

# Creamos una instancia de FastAPI
app = FastAPI()
#app = FastAPI(docs_url=None, redoc_url=None)  # Deshabilitamos la documentacion de la API  

# Incluimos el router en la aplicacion
app.include_router(user)



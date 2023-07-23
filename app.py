from fastapi import FastAPI

from src.models.database import Database

app = FastAPI()
db_conn = Database()

@app.on_event("startup")
async def startup_event():
    print('Starting up app...')
 

@app.on_event("shutdown")
def shutdown_event():
    print('Shutting down app...')
    db_conn.disconnect()


@app.get("/")
def root():
    db_conn.get_db_version()
    return {"Hello": "World"}

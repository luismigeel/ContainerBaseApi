from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI(
    title="Template",
    version="0.0.1"
    )


@app.get('/')
async def root():
    return {'message': 'Hello World'}
from fastapi import FastAPI
import requests

requests.request(method='GET', url='https://github.com/FOSSLingo/resources/archive/refs/heads/main.zip' )

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello, world!"}
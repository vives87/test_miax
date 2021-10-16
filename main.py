from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def home():
    return {"Hello":"FastAPI"}

@app.get("/test")
def home():
    return {"Hola"}

@app.get("/sum")
def suma(a:int, b:int):
    return a+b
from fastapi import FastAPI;

app = FastAPI()

@app.get('/')
def index():
    return {"data": {"name" :"Imran Shah"}}


@app.get('/about')
def index():
    return {"data":"About Page"}


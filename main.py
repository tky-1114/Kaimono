from fastapi import FastAPI, Query, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import asyncio

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory="templates")

class Item(BaseModel):
    name: str

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(
        request = request, 
        name = "index.html"
    )

@app.get("/grandma")
def grandma(request: Request):
    return templates.TemplateResponse(
        request=request,
        name = "grandma.html"
    )

@app.get("/daughter")
def daughter(request: Request):
    return templates.TemplateResponse(
        request=request,
        name = "daughter.html"
    )

@app.post('/item')
def item(item: Item):
    print(item)
    return item
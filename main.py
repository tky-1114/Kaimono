from fastapi import FastAPI, Query, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import asyncio
from database import add_item, get_items

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory="templates")

class Item(BaseModel):
    name: str
    num: int
    details: str
    deadline: str

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

    items = get_items()

    return templates.TemplateResponse(
        request=request,
        name = "daughter.html",
        context={"items": items}
    )

@app.post('/item')
def item(item: Item):
    add_item(item.name, item.num, item.details, item.deadline)
    print(item)
    return item
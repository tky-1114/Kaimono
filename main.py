from fastapi import FastAPI, Query, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import asyncio
from database import add_item, get_items, delete_items, update_status

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory="templates")

class Item(BaseModel):
    name: str
    num: int
    details: str
    deadline: str

class StatusUpdate(BaseModel):
    status: int

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(
        request = request, 
        name = "index.html"
    )

@app.get("/grandma")
def grandma(request: Request):

    items = get_items()

    return templates.TemplateResponse(
        request=request,
        name = "grandma.html",
        context={"items": items}
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
    
    return RedirectResponse(
        url="/grandma",
        status_code=303
    )

@app.delete("/item/{item_id}")
def remove_item(item_id: int):
    delete_items(item_id)
    return 0

@app.put('/item/{item_id}/status')
def change_status(item_id: int, data: StatusUpdate):
    update_status(item_id, data.status)
    return 0
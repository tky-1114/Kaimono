from fastapi import FastAPI, Query, Request
from fastapi.templating import Jinja2Templates
import asyncio

app = FastAPI()

templates = Jinja2Templates(directory="templates")

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
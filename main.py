from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", 
    )


@app.get("/recetas", response_class=HTMLResponse)
async def recetas(request: Request):
    return templates.TemplateResponse(
        request=request, name="recetas.html",
    )

@app.get("/tips", response_class=HTMLResponse)
async def tips(request: Request):
    return templates.TemplateResponse(
        request=request, name="tips.html",
    )
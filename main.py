from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse
import pathlib
from src.routes import notes, tags, contacts

# from src.routes.contacts import router

app = FastAPI()

app.include_router(contacts.router, prefix="/auth")
# app.include_router(tags.router, prefix="/api")
# app.include_router(notes.router, prefix="/api")
app.include_router(contacts.router, prefix="/contacts")

templates = Jinja2Templates(directory="src/templates")

# app.include_router(contacts_router)

favicon_path = pathlib.Path("src/favicon/favicon.ico")


@app.get("/favicon.ico", response_class=FileResponse)
def get_favicon():
    return favicon_path


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}

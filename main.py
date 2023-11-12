from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse
import pathlib
from src.routes import auth, notes, tags, contacts

# from src.routes.contacts import router

app = FastAPI()

app.include_router(auth.router, prefix="/api/auth")
# app.include_router(tags.router, prefix="/api")
# app.include_router(notes.router, prefix="/api")
app.include_router(contacts.router, prefix="/api/contacts")

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


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="localhost", port="8000", reload=True)

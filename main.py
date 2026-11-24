from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse

from check_account import check_account
from create_account import create_account

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def main_page(request: Request):
    return templates.TemplateResponse(request, "index.html", {})

@app.get("/success", response_class=HTMLResponse)
def success(request: Request):
    return templates.TemplateResponse(request, "success.html", {})

@app.get("/fail", response_class=HTMLResponse)
def fail(request: Request):
    return templates.TemplateResponse(request, "fail.html", {})

@app.get("/login", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse(request, "login.html", {})

@app.get("/loginsuccess", response_class=HTMLResponse)
def loginsuccess(request: Request):
    return templates.TemplateResponse(request, "loginsuccess.html", {})

@app.get("/loginfail", response_class=HTMLResponse)
def loginfail(request: Request):
    return templates.TemplateResponse(request, "loginfail.html", {})

@app.post("/")
def register(email = Form(...), username = Form(...), password = Form(...)):
    if create_account(email, username, password):
        return RedirectResponse(url="/success", status_code=303)
    else:
        return RedirectResponse(url="/fail", status_code=303)

@app.post("/login")
def login_post(username = Form(...), password = Form(...)):
    if check_account(username, password):
        return RedirectResponse(url="/loginsuccess", status_code=303)
    else:
        return RedirectResponse(url="/loginfail", status_code=303)

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette import status

import driver_database as dd


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount('/static', StaticFiles(directory='static'), name='static')


app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse("/static/image/favicon.ico")


@app.get('/')
async def root(request: Request):
    data = await dd.get_data()

    return templates.TemplateResponse(
        name="root.html",
        context={"request": request, "tododict": data},
        status_code=status.HTTP_200_OK
    )


@app.get("/delete/{id}")
async def delete_todo(request: Request, id: str):
    data = await dd.get_data()
    del data[id]
    await dd.write_data(data=data)

    return RedirectResponse(
        url="/",
        status_code=status.HTTP_307_TEMPORARY_REDIRECT
    )


@app.post("/add")
async def add_todo(request: Request):
    data = await dd.get_data()
    newdata = dict()
    i = 1
    for id in data:
        newdata[str(i)] = data[id]
        i += 1
    formdata = await request.form()
    newdata[str(i)] = formdata["newtodo"]

    await dd.write_data(newdata)

    return RedirectResponse(
        url="/",
        status_code=status.HTTP_303_SEE_OTHER
        )

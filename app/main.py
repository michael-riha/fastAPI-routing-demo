from typing import Union
from enum import Enum

from fastapi import FastAPI, Request

app = FastAPI()


# https://fastapi.tiangolo.com/es/advanced/custom-response/#redirectresponse
from fastapi.responses import RedirectResponse
@app.get("/")
def redirect_to_home(request: Request):
    #return {"raw_url": request.url._url}
    return RedirectResponse(request.url._url+"home")

@app.get("/hello")
def read_root():
    return {"Hello": "World"}


@app.get("/integer/{int_id}")
def read_item(int_id: int, q: Union[str, None] = None):
    return {"int_id": int_id, "q": q}

# https://fastapi.tiangolo.com/tutorial/path-params/#path-convertor
@app.get("/file/path/{file_path:path}")
async def show_file_path(file_path: str):
    return {"file_path": file_path}

# https://fastapi.tiangolo.com/advanced/custom-response/#fileresponse -> https://stackoverflow.com/a/62939520
from fastapi.responses import FileResponse
@app.get("/file/{file_path:path}")
async def respond_file_content(file_path: str):
    return FileResponse("app/"+file_path)

# https://fastapi.tiangolo.com/tutorial/path-params/#return-enumeration-members
class ModelName(str, Enum):
    bonus = "bonus"
    user = "user"
    group = "group"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.bonus:
        return {"model_name": model_name, "message": "Seems like you got an BONus!"}

    if model_name.value == "user":
        return {"model_name": model_name, "message": "You want's to get the User?"}

    return {"model_name": model_name, "message": "That is the model you are looking for?"}

# https://fastapi.tiangolo.com/advanced/custom-response/#html-response
from fastapi.responses import HTMLResponse
@app.get("/home/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look, some HTML Markup!</h1>
        </body>
    </html>
    """
from fastapi import FastAPI
from starlette.responses import RedirectResponse


app = FastAPI(
    title="Template",
    version="0.0.1",
    openapi_url="/openapi.json"
    )


@app.get(path='/',
         summary="index for template",
         tags=["index"])
async def index():
    """
    It redirects the user to the /docs page.
    :return: RedirectResponse is a class from starlette.responses
    """
    return RedirectResponse("/docs")
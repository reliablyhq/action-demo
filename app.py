import datetime
import itertools
import sys

from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.middleware.errors import ServerErrorMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, PlainTextResponse
from starlette.templating import Jinja2Templates

import uvicorn

templates = Jinja2Templates(directory='templates')

app = Starlette(debug=True)
app.mount('/static', StaticFiles(directory='statics'), name='static')
app.add_middleware(ServerErrorMiddleware)
counter = itertools.count(0, 1)
version = f"{sys.version_info.major}.{sys.version_info.minor}"


@app.route('/')
async def homepage(request):
    template = "index.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)


@app.route("/msg")
async def message(request):
    message = f"Hello world! From Starlette running on Uvicorn with Gunicorn in Alpine."
    return JSONResponse({"message": message, "version": version})

@app.route('/dt')
async def mydatetime(request):
    print(datetime.datetime.now())
    return JSONResponse({'hello': 'world', 'now': str(datetime.datetime.now())})


@app.route('/health')
async def health(request: Request) -> PlainTextResponse:
    return PlainTextResponse(content=b"")


@app.route("/metrics")
async def metrics(request: Request):
    content, http_headers = render(
        app.registry, [request.headers.get("accept", "application/json")])
    return PlainTextResponse(content, headers=http_headers)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

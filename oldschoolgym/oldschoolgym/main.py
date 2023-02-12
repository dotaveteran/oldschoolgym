from typing import Union

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(
    title="GymAPI"
)


@app.get("/", include_in_schema=False)  # Auto-redirect to Swagger (temporary)
def read_root():
    return RedirectResponse('/docs')


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

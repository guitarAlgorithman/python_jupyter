from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

inventory = {
    1: {"name": "dada",
        "prince": 3.99,
        "brand": "N"},
    2: {"name": "palta",
        "prince": 3.99,
        "brand": "N"},
}

@app.get("/get-item/{item_id}")
async def get_item(item_id: int=Path(None,description="debe ser un int")):
    print(item_id)
    return inventory[item_id]

@app.get("/get-by-name")
async def get_item(name:Optional[str]=None, test : int):
    print(name)
    for i in inventory:
        if inventory[i]["name"]==name:
            return inventory[i]
    return {"Data":"Not found"}

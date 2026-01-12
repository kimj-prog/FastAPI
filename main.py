from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False

items = []

@app.get("/")
def root():
    return {"Hello": "World"}

##adds items to the items list 
@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

## returns list of items up to 10 elements
@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]

## gets the item at the specified index, if no item exists at that idnex 404 status code is used to show the user the item is not found instead of printing out a confusing error
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail= "Item not found")
from fastapi import FastAPI
from pydantic import BaseModel


# Test body,path, query

class Item(BaseModel):
    name : str
    description : str | None
    price : float
    tax : float | None


# Tạo ra một đối tượng fastapi
app = FastAPI()

@app.put("/items/{item_id}")
async  def update_item(item_id: int,item :Item,q : str | None) :
    result = {"item_id":item_id,**item.dict()}
    if q :
        result.update({"q":q})
    return result
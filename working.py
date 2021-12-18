from fastapi import FastAPI, Path, Query,HTTPException,status
from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str]=None
    price: Optional[float]=None
    brand: Optional[str] = None



app = FastAPI()

inventory = {
}


@app.get('/get-item/{item_id}')  # path parameter
def get_item(item_id: int = Path(None, description="The ID of the item you like to view", gt=0)):
    return inventory[item_id]

# combine path paramter and query parameter


@app.get('/get-by-name')  # query parameter
def get_item(*,name: Optional[str] = Query(None, title="Name", description="Name of item.", max_length=10)):
    print(inventory)
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    
    raise HTTPException(status_code=404,detail='Item name not found.')


@app.post('/create-item/{item_id}')
def create_item(item_id:int, item: Item):  # we have item for request body
    if item_id in inventory:
        raise HTTPException(status_code=400,detail='Item ID already exists.')

    # inventory[item_id] = {'name': item.name,
    #                       'brand': item.brand, 'price': item.price}
    inventory[item_id] = item
    return inventory[item_id]

@app.put('/update-item/{item_id}')
def update_item(item_id:int,item:UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404,detail='Item ID not exists.')
    
    if item.name !=None:
        inventory[item_id].name = item.name
        
    if item.price !=None:
        inventory[item_id].price = item.price
        
    if item.brand !=None:
        inventory[item_id].brand = item.brand
    
    return inventory[item_id]

@app.delete('/delete-item') 
def delete_item(item_id:int=Query(...,description="The ID of the item to delete",gt=0)):
    if item_id not in inventory:
        raise HTTPException(status_code=404,detail='Item ID not exists.')
    del inventory[item_id]
    return {'success':'item deleted!!'}
from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    
    with open("squareNumber.json", "w") as outf:
        json.dump(int(item_id) * int(item_id), outf)

    return {"item_id": int(item_id) * int(item_id)}
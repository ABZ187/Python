from fastapi import FastAPI
from enum import Enum

app = FastAPI()


# class AvailableCuisine(str, Enum):
#     Indian: "Indian"
#     American: "American"
#     Italian: "Italian"


food = {'Indian': ["Samosa", "idli"],
        'American': ["Hotdog"],
        'Italian': ["Pizza", "Ravioli"]}

valid=food.keys()

@app.get("/cuisine/{cuisine}")
async def get_items(cuisine):
    return food.get(cuisine)

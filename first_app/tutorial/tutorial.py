# from typing import Union

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))

def get_name(f_name,l_name):
    final = f_name.capitalize()+","+l_name.lower()
    print(final)
    
get_name("zeeshan","zafar")

def get_name_and_age(name: str, age: int):
    result = name.capitalize() + " age is " + str(age)
    return result

print(get_name_and_age("Farhan", 18))

def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)
        
price = {
    "Ali": 500.4,
    "Sharjeel": 44,
    "mahad": 33
}

process_items(price)



# classes practice in Fast API tutorial

class Person:
    def __init__(self , name: str):
        self.name = name
        
def my_name(new_per:Person):
    return new_per.name

person_instance = Person("Zeeshan")

print(my_name(person_instance))

#Another example of Pydantic

from datetime import datetime
from pydantic import BaseModel,PositiveInt

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None
    tastes: dict[str,PositiveInt]
    
external_data = {
    'id': 123,
    'signup_ts': '2019-06-01 12:22',  
    'tastes': {
        'wine': 9,
        b'cheese': 7,  
        'cabbage': '1',  
    },
}

user = User(**external_data)

print(user.tastes)



from pydantic import ValidationError
class Usser(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]


exxternal_data = {'id': 'not an int', 'tastes': {}}  

try:
    Usser(**exxternal_data)  
except ValidationError as e:
    print(e.errors())
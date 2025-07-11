from pydantic import BaseModel, HttpUrl
from typing import List

class Product(BaseModel):
    id: int
    title: str
    description: str
    price: float
    old_price: float
    stock: int  
    brand: str
    memory:str
    intern_memory: str
    color: str
    seller: str
    image_url: str 
    image_related:str
    image_related2:str
    image_related3:str
    payment_methods: List[str]
    warranty: str   
    description_detail: str
    product_related: str
    product_related2: str
    product_related3: str
    price_related : float
    price_related2 : float
    price_related3 : float

from pydantic import BaseModel, HttpUrl
from typing import List

class Product(BaseModel):
    id: int
    title: str
    description: str
    price: float
    stock: int
    seller: str
    image_url: str  # Esto valida que sea una URL válida
    payment_methods: List[str]
    warranty: str   
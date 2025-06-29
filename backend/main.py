from fastapi import FastAPI, HTTPException
import json, os
from typing import List, Optional # Import Optional for the single product endpoint
from models.product import Product
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


app = FastAPI()
'''
Here is the path where is the data product

'''
DATA_PATH = "data/products.json"

app.mount("/static", StaticFiles(directory="static"), name="static")

'''
This is the 

'''
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Puerto por defecto de Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Here is the load, in the json about new product
def read_products():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_products(products):
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(products, f, indent=4)

#Here is the return about all products
@app.get("/api/products", response_model=List[Product])
def get_products():
    raw_data = read_products()
    return [Product(**item) for item in raw_data]

#Endpoint to get a single product by ID
@app.get("/api/products/{product_id}", response_model=Product)
def get_product_by_id(product_id: int):
    """
    Fetches a single product by its ID.
    Raises a 404 HTTPException if the product is not found.
    """
    products = read_products()
    #Here make the search of products for ID
    #Recorremos y realizamos la busqueda de productos por ID
    for product_data in products:
        if product_data["id"] == product_id:
            return Product(**product_data)
    raise HTTPException(status_code=404, detail="Product not found")

#This endpoint was develop for the moment of create a new product
@app.post("/api/products", response_model=Product)
def create_product(product: Product):
    products = read_products()
    if any(p["id"] == product.id for p in products):
        raise HTTPException(status_code=400, detail="Producto con ese ID ya existe.")
    products.append(product.dict())
    write_products(products)
    return product
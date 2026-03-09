from fastapi import FastAPI

app = FastAPI()

# Products list
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 599, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True},
    {"id": 4, "name": "USB Cable", "price": 199, "category": "Electronics", "in_stock": False},

    # Added for Task 1
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False}
]

# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to My E-commerce Store API"}

# Task 1 endpoint
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }

# Task 2 endpoint
@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):

    result = [
        p for p in products 
        if p["category"].lower() == category_name.lower()
    ]

    if not result:
        return {"error": "No products found in this category"}

    return {
        "category": category_name,
        "products": result,
        "total": len(result)
    }
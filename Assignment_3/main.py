 
# IMPORT REQUIRED LIBRARIES
 
from fastapi import FastAPI, Query, Response, status
from pydantic import BaseModel, Field
from typing import Optional, List


 
# CREATE FASTAPI APPLICATION
 
app = FastAPI()

 
# DATABASE (TEMPORARY MEMORY STORAGE)
 

# List of products in the store
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 599, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True},
    {"id": 4, "name": "USB Cable", "price": 199, "category": "Electronics", "in_stock": False},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False}
]

# store customer orders
orders = []

# store feedback
feedback = []


 
# DAY 1 TASKS
 
# HOME ENDPOINT
 
@app.get("/")
def home():
    """
    Root API endpoint
    Displays welcome message
    """
    return {"message": "Welcome to My E-commerce Store API"}


 
# GET ALL PRODUCTS
 
@app.get("/products")
def get_products():
    """
    Returns all products in the store
    """
    return {
        "products": products,
        "total": len(products)
    }

 
# FILTER PRODUCTS BY CATEGORY
 
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


 
# SHOW ONLY IN-STOCK PRODUCTS
 
@app.get("/products/instock")
def get_instock():

    available = [
        p for p in products
        if p["in_stock"]
    ]

    return {
        "in_stock_products": available,
        "count": len(available)
    }


 
# STORE SUMMARY
 
@app.get("/store/summary")
def store_summary():

    in_stock_count = len([p for p in products if p["in_stock"]])
    out_stock_count = len(products) - in_stock_count
    categories = list(set([p["category"] for p in products]))

    return {
        "store_name": "My E-commerce Store",
        "total_products": len(products),
        "in_stock": in_stock_count,
        "out_of_stock": out_stock_count,
        "categories": categories
    }


 
# SEARCH PRODUCTS BY NAME
 
@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    results = [
        p for p in products
        if keyword.lower() in p["name"].lower()
    ]

    if not results:
        return {"message": "No products matched your search"}

    return {
        "keyword": keyword,
        "results": results,
        "total_matches": len(results)
    }


# BONUS – BEST DEALS
 
@app.get("/products/deals")
def get_deals():

    cheapest = min(products, key=lambda p: p["price"])
    expensive = max(products, key=lambda p: p["price"])

    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }

 
# DAY 2 TASKS
 
# FILTER PRODUCTS USING QUERY PARAMETERS
# Example:
# /products/filter?category=Electronics&max_price=1000
 
@app.get("/products/filter")
def filter_products(
    category: str = Query(None),
    max_price: int = Query(None),
    min_price: int = Query(None)
):

    result = products

    if category:
        result = [p for p in result if p["category"].lower() == category.lower()]

    if max_price:
        result = [p for p in result if p["price"] <= max_price]

    if min_price:
        result = [p for p in result if p["price"] >= min_price]

    return {"filtered_products": result}

 
# GET PRODUCT PRICE ONLY

@app.get("/products/{product_id}/price")
def get_product_price(product_id: int):

    for product in products:
        if product["id"] == product_id:
            return {
                "name": product["name"],
                "price": product["price"]
            }

    return {"error": "Product not found"}


 
# CUSTOMER FEEDBACK MODEL
 
class CustomerFeedback(BaseModel):

    customer_name: str = Field(..., min_length=2)
    product_id: int = Field(..., gt=0)
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = Field(None, max_length=300)


# POST FEEDBACK
 
@app.post("/feedback")
def submit_feedback(data: CustomerFeedback):

    feedback.append(data.dict())

    return {
        "message": "Feedback submitted successfully",
        "feedback": data.dict(),
        "total_feedback": len(feedback)
    }


 
# PRODUCT SUMMARY DASHBOARD
 
@app.get("/products/summary")
def product_summary():

    in_stock = [p for p in products if p["in_stock"]]
    out_stock = [p for p in products if not p["in_stock"]]

    expensive = max(products, key=lambda p: p["price"])
    cheapest = min(products, key=lambda p: p["price"])

    categories = list(set(p["category"] for p in products))

    return {
        "total_products": len(products),
        "in_stock_count": len(in_stock),
        "out_of_stock_count": len(out_stock),
        "most_expensive": expensive,
        "cheapest": cheapest,
        "categories": categories
    }


 
# BULK ORDER MODEL
 
class OrderItem(BaseModel):
    product_id: int
    quantity: int


class BulkOrder(BaseModel):
    company_name: str
    contact_email: str
    items: List[OrderItem]


 
# BULK ORDER API
 
@app.post("/orders/bulk")
def place_bulk_order(order: BulkOrder):

    confirmed = []
    failed = []
    grand_total = 0

    for item in order.items:

        product = next((p for p in products if p["id"] == item.product_id), None)

        if not product:
            failed.append({"product_id": item.product_id, "reason": "Product not found"})

        elif not product["in_stock"]:
            failed.append({"product_id": item.product_id, "reason": "Out of stock"})

        else:
            subtotal = product["price"] * item.quantity
            grand_total += subtotal

            confirmed.append({
                "product": product["name"],
                "quantity": item.quantity,
                "subtotal": subtotal
            })

    return {
        "company": order.company_name,
        "confirmed": confirmed,
        "failed": failed,
        "grand_total": grand_total
    }


 
# ORDER STATUS TRACKING
 
class OrderRequest(BaseModel):
    product_id: int
    quantity: int


@app.post("/orders")
def place_order(order: OrderRequest):

    order_data = {
        "order_id": len(orders) + 1,
        "product_id": order.product_id,
        "quantity": order.quantity,
        "status": "pending"
    }

    orders.append(order_data)

    return {"order": order_data}


@app.get("/orders/{order_id}")
def get_order(order_id: int):

    for order in orders:
        if order["order_id"] == order_id:
            return {"order": order}

    return {"error": "Order not found"}


@app.patch("/orders/{order_id}/confirm")
def confirm_order(order_id: int):

    for order in orders:
        if order["order_id"] == order_id:
            order["status"] = "confirmed"
            return {"message": "Order confirmed", "order": order}

    return {"error": "Order not found"}


# DAY 3 TASKS – CRUD OPERATIONS
 
 
# PRODUCT MODEL FOR ADDING PRODUCT
 
class NewProduct(BaseModel):
    name: str
    price: int
    category: str
    in_stock: bool = True


 
# HELPER FUNCTION
# FIND PRODUCT BY ID
 
def find_product(product_id: int):

    for p in products:
        if p["id"] == product_id:
            return p
    return None



# ADD NEW PRODUCT

@app.post("/products", status_code=201)
def add_product(product: NewProduct, response: Response):

    for p in products:
        if p["name"].lower() == product.name.lower():
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"error": "Product already exists"}

    next_id = max(p["id"] for p in products) + 1

    new_product = {
        "id": next_id,
        "name": product.name,
        "price": product.price,
        "category": product.category,
        "in_stock": product.in_stock
    }

    products.append(new_product)

    return {
        "message": "Product added successfully",
        "product": new_product
    }


 
# UPDATE PRODUCT
 
@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    price: Optional[int] = None,
    in_stock: Optional[bool] = None
):

    product = find_product(product_id)

    if not product:
        return {"error": "Product not found"}

    if price is not None:
        product["price"] = price

    if in_stock is not None:
        product["in_stock"] = in_stock

    return {"message": "Product updated", "product": product}


 
# DELETE PRODUCT
 
@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    product = find_product(product_id)

    if not product:
        return {"error": "Product not found"}

    products.remove(product)

    return {"message": f"{product['name']} deleted successfully"}


 
 


 
# INVENTORY AUDIT
 
@app.get("/products/audit")
def product_audit():

    in_stock_list = [p for p in products if p["in_stock"]]
    out_stock_list = [p for p in products if not p["in_stock"]]

    stock_value = sum(p["price"] * 10 for p in in_stock_list)

    priciest = max(products, key=lambda p: p["price"])

    return {
        "total_products": len(products),
        "in_stock_count": len(in_stock_list),
        "out_of_stock_products": [p["name"] for p in out_stock_list],
        "total_stock_value": stock_value,
        "most_expensive": priciest
    }

# GET SINGLE PRODUCT
 
@app.get("/products/{product_id}")
def get_single_product(product_id: int):

    product = find_product(product_id)

    if not product:
        return {"error": "Product not found"}

    return product
 
# APPLY DISCOUNT TO CATEGORY
 
@app.put("/products/discount")
def bulk_discount(
    category: str = Query(...),
    discount_percent: int = Query(..., ge=1, le=99)
):

    updated = []

    for p in products:
        if p["category"].lower() == category.lower():

            p["price"] = int(p["price"] * (1 - discount_percent / 100))
            updated.append(p)

    if not updated:
        return {"message": f"No products found in category {category}"}

    return {
        "message": f"{discount_percent}% discount applied",
        "updated_products": updated
    }
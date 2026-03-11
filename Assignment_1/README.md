# FastAPI Internship Training — Day 1 Assignment

## Project Overview

This project is part of the **FastAPI Internship Training Program (Day 1)**.
The goal of this assignment is to understand the basics of **FastAPI**, build a simple API, and practice creating multiple endpoints for a small **E-commerce Store System**.

In this project, I build a **REST API** that manages products in a store. The API allows users to:

* View all products
* Filter products by category
* Check which products are in stock
* View store summary information
* Search for products by name
* Get the cheapest and most expensive product (Bonus task)

This project helps beginners understand how **backend APIs work**.

 

# What is FastAPI?

**FastAPI** is a modern, high-performance web framework used to build APIs with Python.

It is based on:

* **Python 3.7+**
* **Type hints**
* **ASGI server (Uvicorn)**

FastAPI is widely used because it is:

* Very **fast**
* Easy to **learn**
* Automatically generates **interactive API documentation**

FastAPI automatically creates documentation using **Swagger UI**, which allows us to test APIs directly in the browser.

 

 ### File Description

**main.py**
Contains the FastAPI application and all API endpoints.

**README.md**
Documentation explaining the project and how to run it.

**Output Screenshots**
Screenshots of API responses taken from Swagger UI.

 

# Requirements

To run this project, you need:

* Python 3.8 or higher
* FastAPI
* Uvicorn

 

# Installation Guide (For Beginners)

### Step 1 — Install Python

Download Python from:

https://www.python.org/downloads/

Verify installation:

```
python --version
```

 

### Step 2 — Install FastAPI

Open **Command Prompt or Terminal** and run:

```
pip install fastapi
```

 

### Step 3 — Install Uvicorn Server

```
pip install uvicorn
```

Uvicorn is the **ASGI server used to run FastAPI applications**.

  
 
# Running the Application

Navigate to the folder containing `main.py`.

Example:

```
cd FastAPI_Assignment
```

Then run the server:

```
uvicorn main:app --reload
```

Explanation:

* `main` → Python file name
* `app` → FastAPI object inside the file
* `--reload` → Automatically reloads server when code changes

 

# Access the API

After running the server, open the browser and go to:

```
http://127.0.0.1:8000
```

You will see:

```
Welcome to My E-commerce Store API
```

 

# Swagger Documentation

FastAPI automatically creates interactive API documentation.

Open:

```
http://127.0.0.1:8000/docs
```

This page allows you to:

* View all endpoints
* Test APIs
* Send requests
* See responses

 

# API Endpoints

## 1. Get All Products

Endpoint:

```
GET /products
```

Description:

Returns the complete list of products available in the store.

Example Response:

```
{
  "products": [...],
  "total": 7
}
```

 

## 2. Filter Products by Category

Endpoint:

```
GET /products/category/{category_name}
```

Example:

```
/products/category/Electronics
```

Description:

Returns only products belonging to the selected category.

If the category does not exist, an error message is returned.

 

## 3. Show Only In-Stock Products

Endpoint:

```
GET /products/instock
```

Description:

Returns only the products that are currently available in stock.

Response also includes the count of available products.

 
## 4. Store Summary

Endpoint:

```
GET /store/summary
```

Description:

Provides a summary of the store including:

* Total number of products
* Number of products in stock
* Number of products out of stock
* Available categories

Example Response:

```
{
 "store_name": "My E-commerce Store",
 "total_products": 7,
 "in_stock": 5,
 "out_of_stock": 2,
 "categories": ["Electronics", "Stationery"]
}
```

---

## 5. Search Products

Endpoint:

```
GET /products/search/{keyword}
```

Example:

```
/products/search/mouse
```

Description:

Allows users to search products by name.

Search is **case-insensitive**.

Examples:

* mouse → Wireless Mouse
* BOOK → Notebook

---

# Bonus Feature

## Cheapest and Most Expensive Product

Endpoint:

```
GET /products/deals
```

Description:

Returns:

* The cheapest product (Best Deal)
* The most expensive product (Premium Pick)

This feature uses Python's `min()` and `max()` functions.

 

# Technologies Used

* Python
* FastAPI
* Uvicorn
* Swagger UI

 

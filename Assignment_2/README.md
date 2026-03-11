# FastAPI Internship Training — Day 2 Assignment

## Project Overview

This project is a continuation of my **FastAPI Internship Training (Day 2)**.

On Day 1, I built a simple **E-commerce API** using FastAPI with basic GET endpoints to view and filter products.

On Day 2, I expanded the project by adding more practical backend features such as:

* Filtering data using query parameters
* Validating request data using Pydantic
* Creating POST APIs to send data to the server
* Updating data using PATCH APIs
* Building a simple order tracking system

These features help simulate how real-world backend systems handle **user input, validation, and data updates**.

The goal of this assignment is to understand how APIs work beyond simple data retrieval and learn how backend services manage user requests.

 

# What I Learned in Day 2

During this assignment, I explored several new FastAPI concepts that are commonly used in backend development.

### Query Parameters

Query parameters allow users to filter results directly from the URL.

For example:

```
/products/filter?category=Electronics
```

This returns only the products that belong to the **Electronics** category.

Users can also filter by price range:

```
/products/filter?min_price=100&max_price=1000
```

 

### Data Validation with Pydantic

FastAPI uses **Pydantic models** to validate incoming data.

For example, in the **customer feedback system**, I added validation rules such as:

* Customer name must have a minimum length
* Product ID must be a positive number
* Rating must be between 1 and 5
* Comments are optional

This ensures that the API only accepts **valid and structured data**.

 

# Day 2 API Endpoints

## 1. Filter Products

Endpoint:

```
GET /products/filter
```

This endpoint allows users to filter products using optional parameters like:

* category
* minimum price
* maximum price

Example:

```
/products/filter?category=Electronics
```

The API returns a list of products that match the filter conditions.

 

## 2. Get Product Price

Endpoint:

```
GET /products/{product_id}/price
```

This endpoint returns only the **name and price** of a specific product instead of the full product details.

Example:

```
/products/2/price
```

Response:

```
{
 "name": "Notebook",
 "price": 99
}
```

This type of endpoint is useful when applications only need **specific data instead of the full object**.

 

## 3. Customer Feedback System

Endpoint:

```
POST /feedback
```

This API allows customers to submit feedback for a product.

Example request:

```
{
 "customer_name": "Kavya",
 "product_id": 1,
 "rating": 5,
 "comment": "Great product"
}
```

The feedback data is validated using **Pydantic models** before being stored.

This helps ensure that incorrect or incomplete data is rejected.

 

## 4. Product Summary Dashboard

Endpoint:

```
GET /products/summary
```

This endpoint provides a quick overview of the store.

It returns useful information such as:

* Total number of products
* Number of products in stock
* Number of products out of stock
* Most expensive product
* Cheapest product
* List of available product categories

This type of endpoint is useful for building **admin dashboards or analytics views**.

 

## 5. Bulk Order System

Endpoint:

```
POST /orders/bulk
```

This feature allows companies to place **bulk orders** that contain multiple products.

Example request:

```
{
 "company_name": "Tech Corp",
 "contact_email": "tech@corp.com",
 "items": [
   {"product_id": 1, "quantity": 5},
   {"product_id": 2, "quantity": 3}
 ]
}
```

The API checks if the products exist and whether they are in stock.

The response includes:

* Successfully confirmed items
* Failed items (if any)
* Total cost of the order

 

# Bonus Feature — Order Status Tracker

As an additional task, I implemented a **simple order tracking system**.

In real-world systems, orders are usually not confirmed immediately. Instead, they go through a processing stage.

This feature simulates that workflow.

### 1. Place an Order

```
POST /orders
```

When a new order is created, its status is set to:

```
pending
```

---

### 2. View an Order

```
GET /orders/{order_id}
```

This endpoint retrieves the details of a specific order.

If the order ID does not exist, the API returns:

```
{"error": "Order not found"}
```

 

### 3. Confirm an Order

```
PATCH /orders/{order_id}/confirm
```

This endpoint updates the order status from:

```
pending → confirmed
```

This simulates the process where a warehouse or system approves the order.

 

# Key Takeaways

By completing the Day 2 assignment, I learned how to:

* Use query parameters to filter API results
* Validate request data using Pydantic models
* Create POST APIs for sending data to the server
* Update existing data using PATCH APIs
* Design simple backend workflows like order tracking

These concepts are important for building **real-world backend applications**.

 

# Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* Swagger UI
 


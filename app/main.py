from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# Multiple path parameters
@app.get("/users/{user_id}/posts/{post_id}")
def get_user_post(user_id: int, post_id: int):
    return {"user_id": user_id, "post_id": post_id}

# Query parameters with validation
@app.get("/products/")
def read_products(
    skip: int = 0,
    limit: int = 10,
    category: Optional[str] = None
):
    return {
        "skip": skip,
        "limit": limit,
        "category": category
    }

@app.post("/items/")
def create_item(item: dict):
    return item

if __name__ == "__main__":
    app.run(debug=True)
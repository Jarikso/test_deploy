import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI()


@app.get("/items")
def get_items():
    items = [
        {
            "id": 1,
            "name": "Docker",
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Docker_logo.png/250px-Docker_logo.png",
        },
        {
            "id": 2,
            "name": "Nginx",
            "img": "https://nginx.org/img/nginx_logo_dark.png",
        },
        {
            "id": 3,
            "name": "GitHub",
            "img": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
        },
    ]
    random.shuffle(items)
    return items


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # "http://localhost:5173",
        "http://194.87.43.206",
        # "https://site-test-deploy1.ru",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

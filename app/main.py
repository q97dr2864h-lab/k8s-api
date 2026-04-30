from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/users")
def users():
    return [
        {"id": 1, "name": "Jey"},
        {"id": 2, "name": "Admin"}
    ]

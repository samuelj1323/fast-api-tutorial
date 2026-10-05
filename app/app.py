from fastapi import FastAPI

app = FastAPI()


# Always a pydantic obj or a python dict
@app.get("/hello-world")
def hello_world():
    return {"message": "Hello world"}


# Hello

from fastapi import FastAPI

app = FastAPI()


@app.get("/wallet")
async def root():
    return {"message": "Hello World"}

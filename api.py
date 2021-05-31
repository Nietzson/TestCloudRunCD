from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return "111Hello from Cloud Run CD MARCHE PAS PUtAIN"
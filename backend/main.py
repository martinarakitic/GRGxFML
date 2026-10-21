from fastapi import FastAPI

app = FastAPI(
    title="GRGxFAM API",
    description="API za automobilsku zajednicu i car meetove",
    version="0.1.0",
)


@app.get("/")
def home():
    return {
        "message": "Welcome to GRGxFAM!",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}

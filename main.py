import time

from fastapi import FastAPI
from prometheusrock import PrometheusMiddleware, metrics_route
from app.routers import health
from app.routers import dynamodb

app = FastAPI()

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", metrics_route)

app.include_router(health.router)
app.include_router(dynamodb.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

from fastapi import FastAPI
from v1.routers import router
from mangum import Mangum
import os

# Will be blank for local dev usage and add /prod for AWS deployments
app_prefix = "" if os.getenv("LOCAL") else "/prod"

app = FastAPI(
    title="Cryptocurrency API",
    description="API to track current prices and trading signals",
    openapi_prefix=app_prefix,
)
app.include_router(router, prefix="/v1")


@app.get("/")
def read_root():
    return {"Hello Medium Reader": "from FastAPI & API Gateway. Go to /docs to see documentation."}


# to make it work with AWS Lambda, we create a handler object
handler = Mangum(app=app)

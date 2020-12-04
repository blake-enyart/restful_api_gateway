from fastapi import APIRouter
import json

router = APIRouter()


@router.get("/welcome")
async def welcome():
    """Test adding a new endpoint"""
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": "Hello from Lambda!",
        "headers": {"Content-Type": "application/json"},
    }

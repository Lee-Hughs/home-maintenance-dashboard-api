from fastapi import APIRouter

from app.services import dynamodb
from app.models.common import Item

router = APIRouter(
    prefix="/dynamodb",
    tags=["Health"]
)

@router.get('/tables')
def get_tables():
    return dynamodb.list_tables()

@router.put('/item')
def put_item(request: Item):
    data = request.dict()
    return dynamodb.put_item(data)

@router.get('/items')
def get_items():
    return dynamodb.get_items()

@router.patch('/item/{id}/{display_name}')
def patch_item(id: str, display_name: str):
    return dynamodb.mark_item_complete(id, display_name)
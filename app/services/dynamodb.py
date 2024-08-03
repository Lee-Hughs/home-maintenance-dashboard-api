"""
Services relating to DynamoDB
"""
import os
from datetime import date

from app.controllers.dynamodb import DynamoDbClient

DYNAMODB_TABLE_NAME = os.environ.get("DYNAMODB_TABLE_NAME")

def list_tables():
  with DynamoDbClient() as client:
    return client.list_tables()

def put_item(request: dict):
  print(request)
  print(type(request))
  with DynamoDbClient() as client:
    return client.put_item(DYNAMODB_TABLE_NAME, request)

def get_items():
  with DynamoDbClient() as client:
    return client.scan_items(DYNAMODB_TABLE_NAME)

def mark_item_complete(id: str, display_name: str):
  with DynamoDbClient() as client:
    return client.update_item(
      table_name=DYNAMODB_TABLE_NAME,
      key={
        'id': {
          'S': id
        },
        'display_name': {
          'S': display_name
        }
      },
      update_expression="SET last_completed = :val",
      expression_attribute_values  = {
        ':val': {
          'S': date.today().strftime("%Y-%m-%d")
        }
      }
    )
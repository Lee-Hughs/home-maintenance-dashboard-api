"""
Controller Class For DynamoDB
"""
import boto3
import os

class DynamoDbClient:
  """
  This class wraps DynamoDB Calls
  """
  __endpoint_url = os.environ.get("AWS_ENDPOINT_URL")
  __aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
  __aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
  __aws_default_region = os.environ.get("AWS_DEFAULT_REGION")
  boto_client = None

  def __enter__(self):
    """
    Executed when class is created
    :return:
    """
    self.boto_client = boto3.client(
      service_name="dynamodb",
      endpoint_url=self.__endpoint_url,
      aws_access_key_id=self.__aws_access_key_id,
      aws_secret_access_key=self.__aws_secret_access_key,
      region_name=self.__aws_default_region
    )
    return self
  
  def __exit__(self, exc_type, exc_value, traceback):
    """
    Executed when class is destroyed
    """
    self.boto_client.close()
    return
  
  def list_tables(self):
    response = self.boto_client.list_tables()
    return response
  
  def put_item(self, table_name: str, item: dict):
    response = self.boto_client.put_item(
      TableName=table_name,
      Item={
        'id': {
          'S': item['id'],
        },
        'display_name': {
          'S': item['display_name']
        },
        'last_completed': {
          'S': item['last_completed'].strftime("%Y-%m-%d")
        },
        'cadence': {
          'N': str(item['cadence'])
        }
      })
    return response

  def scan_items(self, table_name: str):
    response = self.boto_client.scan(
      TableName=table_name,
      Limit=100
    )
    return response
  
  def update_item(self, table_name: str, key: dict, update_expression: str, expression_attribute_values):
    response = self.boto_client.update_item(
      TableName=table_name,
      Key=key,
      UpdateExpression=update_expression,
      ExpressionAttributeValues=expression_attribute_values
    )
    return response

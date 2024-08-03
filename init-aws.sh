#!/bin/bash

echo "Checking if table already exists"

awslocal dynamodb describe-table --table-name home-maintenance

if [ "$?" -ne 0 ]
then
   echo "Table does not exist. Init DynamoDB resources";

   awslocal dynamodb create-table \
      --table-name home-maintenance \
      --attribute-definitions AttributeName=id,AttributeType=S \
      AttributeName=display_name,AttributeType=S \
      --key-schema AttributeName=id,KeyType=HASH \
      AttributeName=display_name,KeyType=RANGE \
      --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
else
   echo "Table already exists"
fi

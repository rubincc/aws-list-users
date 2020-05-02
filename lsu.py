#!/usr/bin/env python
# 02.05.2020 - CRC
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/iam-example-managing-users.html#id3

import boto3

# Create IAM client
iam_client = boto3.client('iam')

# List users with the pagination interface
paginator = iam_client.get_paginator('list_users')

for response in paginator.paginate():
    print(response)

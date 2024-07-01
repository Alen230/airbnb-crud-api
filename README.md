# airbnb-crud-api
# Airbnb CRUD API using AWS Lambda, API Gateway, and DynamoDB

This repository contains the code and configuration for a CRUD API built using AWS Lambda, API Gateway, and DynamoDB. The project is designed to demonstrate the practical application of a cloud strategy for Airbnb.

## Table of Contents
- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
  - [1. Setting Up AWS Account](#1-setting-up-aws-account)
  - [2. Creating and Configuring DynamoDB Table](#2-creating-and-configuring-dynamodb-table)
  - [3. Creating Lambda Function](#3-creating-lambda-function)
  - [4. Setting Up API Gateway](#4-setting-up-api-gateway)
  - [5. Testing the API](#5-testing-the-api)
  - [6. Setting Up GitHub Repository](#6-setting-up-github-repository)
- [Example API Requests](#example-api-requests)
- [Directory Structure](#directory-structure)

## Project Overview
This project demonstrates the deployment of a sample cloud infrastructure for Airbnb using AWS Free Tier services. It includes setting up AWS resources such as Lambda, API Gateway, and DynamoDB to create a serverless architecture that handles CRUD operations.

## Requirements
- AWS Free Tier Account
- AWS CLI configured with your credentials
- Python 3.x
- Postman or curl for testing API endpoints

## Setup Instructions

### 1. Setting Up AWS Account
1. **Create AWS Account**: Sign up for an AWS Free Tier account.
2. **Configure IAM Roles**: Set up Identity and Access Management (IAM) roles with appropriate permissions to ensure secure access to AWS resources.
3. **Billing Alerts**: Configure billing alerts to monitor usage and costs.

### 2. Creating and Configuring DynamoDB Table
1. **Navigate to DynamoDB**: Open the DynamoDB service in the AWS Management Console.
2. **Create a New Table**:
   - Table name: `AirbnbListings`
   - Primary key: `id` (string)

### 3. Creating Lambda Function
1. **Create Lambda Function**:
   - In the AWS Management Console, navigate to the Lambda service.
   - Click `Create function`.
   - Choose `Author from scratch`.
   - Function name: `AirbnbCRUD`
   - Runtime: `Python 3.x`
   - Role: `Create a new role with basic Lambda permissions`
   - Click `Create function`.

2. **Add Lambda Function Code**:
   - In the Lambda function code editor, delete any existing code.
   - Copy and paste the code from `lambda_function.py`.

3. **Set the Handler**:
   - In the Function code section, set the Handler field to `lambda_function.lambda_handler`.

4. **Configure IAM Role Permissions**:
   - Click on the role name in the Lambda function configuration page.
   - Add an inline policy with the following JSON to grant access to DynamoDB:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:BatchGetItem",
                "dynamodb:BatchWriteItem",
                "dynamodb:ConditionCheckItem",
                "dynamodb:DeleteItem",
                "dynamodb:GetItem",
                "dynamodb:PutItem",
                "dynamodb:Query",
                "dynamodb:Scan",
                "dynamodb:UpdateItem"
            ],
            "Resource": "*"
        }
    ]
}

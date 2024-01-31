Project Overview

This project presents the design and implementation of a serverless application using AWS Lambda, API Gateway, and DynamoDB for user management. 
The application provides HTTPApi endpoint for user creation, retrieval, and data processing. 
The Serverless Framework is employed to define and deploy the AWS resources, including Lambda functions and DynamoDB table and HttpApi . 
The project follows best practices for serverless architecture, emphasizing scalability, security, and cost-effectiveness.

Key Components:
AWS Lambda Function: Create User, Get User, Delete User.
API Gateway: Defines Http API endpoint for user creation, retrieval, and deleting.
DynamoDB: Utilizes a DynamoDB table named "UserRegistrationTable" to store user data. Implements a simple schema with a primary key for efficient data retrieval.
Serverless Application Model (SAM): SAM templates are used to define AWS resources, including Lambda functions and DynamoDB tables.
•	Enables easy deployment and management of resources through the Serverless Framework.

Development Process:
Requirements Gathering: 
Detailed functional and non-functional requirements were gathered, defining user stories and use cases.
Architecture Design:
API structure and endpoints, Lambda functions were defined in the Serverless Framework configuration (serverless.yaml).
Function Development and Testing:
Lambda functions were developed in Python, incorporating user creation, retrieval, and data processing logic.
Unit tests were implemented using the unit test module to ensure the correctness of individual functions.
Resource Creation and Deployment:
SAM templates were written to define AWS resources, including the DynamoDB table and Lambda functions.
Resources were deployed using the Serverless Framework, and automation was integrated into a continuous integration/continuous deployment (CI/CD) pipeline.
Environment Deployment:
The application was deployed to staging for testing, and configurations for API Gateway and Lambda integrations were verified.
Production Deployment:
The application was safely deployed to the production environment.

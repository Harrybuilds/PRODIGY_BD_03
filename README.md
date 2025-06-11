# Django Rest API with Authentication and Authorization using JSON Web Token (JWT)

*Task*
Implement authentication and authorization using JSON Web Tokens (JWT)

- Add user registration and login endpoints.
- Store hashed passwords using a library like bcrypt.
- On successful login, generate and return a JWT token to the client.
- Protect certain routes (e.g. /users or /profile) to be accessible only by authenticated users using the JWT token.
- Implement role-based access control (e.g. admin, user, owner) to restrict access to specific endpoints.
- Implement caching to optimize the performance of your API.
    - Integrate Redis to cache the results of frequently access endpoints (e.g. fetching all users)
    - Implement cache invalidation strategies when data changes (e.g., updating or delete a user)
    - Set cache expiration for certain data to ensure it stays fresh
    - Measure the performance improvements (e.g., response times before and after caching)



# PRODIGY_BD_02

## Django Rest API with Persistent Storage with Database Integration

** Task **

'''
Extend the previous REST API to use a relational database(e.g., MYSQL, MongoDB) for persistent storage

- Integrate a SQL or NoSQL  database using an ORM/ODM
- Use database migtrations if required to create the users table with the appropraite schema
- Implement connection pooling and environment-specific configurations using .env files
- Use environment variables for database credentials.
'''

*previous task*

# PRODIGY_BD_01
## Basic REST API with CRUD Operations

*TASK*
"
Create an API with endpoints to perform basic CRUD (Create, Read, Update Delete)
operations on a user's resource

- Each user should have fields: id(UUID), name, email and age
- Use an in-memory data structure (like an hashmap) for storage
- Ensure proper status code and error handling (e.g., 404 for not found, 400 for bad requests)
- include basic input validation (e.g., checking if email is valid)
"


## Requirement
 - Python 3.8+
 - MYSQL Server
 - pip (pythonpackage manager)

------

##  Setup Instruction

### 1. clone the repository
```bash
git clone https://github.com/Harrybuilds/Prodigy_BD_03.git
cd access ```



## Features

    - Full CRUD operations on User
    - Uses MYSQL as a relational database
    - Persistent storage with ORM (Django ORM)
    - Environment-specific configurations using `.env`
    - Secure handling of database credentials
    - Connection pooling(MYSQL)
    - Input validation and Error handling
    - UUID as primary key for users
    - JWT Token implemented
    - Role-based access control 


------

## Example API Endpoints

Methods          Endpoint                    Description
POST            /api/register/              Creates a new user
POST            /api/login/                 login a user and return a JWT token
GET             /api/profile/               allows only authenticated users visit this endpoint
[GET,POST,PUT,DELETE]  /api/admin_only/     allows only authenticated users with admin role visit this endpoint
[GET,POST,PUT,DELETE]  /api/staff_only/     allows only authenticated users with staff role visit this endpoint
[GET,POST,PUT,DELETE]  /api/staffs/         allows only authenticated users with staff or admin role visit this endpoint
[GET,POST,PUT,DELETE]  /api/all_users/     allows only authenticated users with user role visit this endpoint

-------

# Tools Used
*Django 5.x
*MYSQL 8+
*Python Decouple
*mysqlclient
*pyjwt
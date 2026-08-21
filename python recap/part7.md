# Part 7: FastAPI architecture, creating an app, path parameters, query parameters, request bodies, Pydantic models, validation, response models, status codes, HTTPException, automatic OpenAPI/Swagger docs

## 7.1 What is FastAPI?

FastAPI is a python web framework for buildings APIs
At a high level:

```
Client
   ↓
HTTP Request
   ↓
FastAPI
   ↓
Your Python endpoint
   ↓
Business logic
   ↓
Database / external services
   ↓
FastAPI
   ↓
HTTP Response
   ↓
Client
```

FastAPI is particularly popular because it provides

- type-hint-based validation
- automatic API documentation
- async support
- dependency injection
- high performance
- integration with Pydantic

## 7.2 Yor first FastAPI application

The basic structure:

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
```

Let's break it down
_app = FastAPI()_
creates the FastAPI application instance

Then:
_@app.get("/")_
is a **decorator**
Remember 4?
It registers the function as the handler for:
_/\_
using HTTP GET
Then:

```
def root():
    return {"message": "Hello World"}
```

is the endpoint function

## 7.3 Path Parameters

suppose we want:
_/users/123_
where _123_ represents the user ID.

FastAPI:

```
@app.get("/users/{user_id}")
def get_user(user_id: int)
    return {"user_id": user_id}
```

if the request is:
_GET /users/123_
FastAPI extracts:
_user_id = 123_

The type hint:
_user_id: int_
also tells FastAPI that the value should be an integer

So:
_/users/123_
works
But:
_/users/abs_
will fail validation

This is one of the advantages of FastAPI's type-hint-driven design

## 7.4 Query Parameters

Now suppose we want:
_/users?limit=10&active=true_
These are **query parameters**

FastAPI can infer them from function parameters:

```
@app.get("/users")
def get_users(limit: int = 10, active: bool = True):
    return {
        "limit": limit,
        "active": active
    }
```

Here:
limit
active
are query parameters because they aren't part og the path

Compare:
_/users/{users_id}_ -> path parameter
versus:
_/users?limit=10_ -> query parameter

## 7.5 Path vs Query

This distinction is extremely important

### Path

Use when identifying a specific resource:
/users/123
_123_ identifies _which user_

### Query

Use for filtering, searching, pagination, sorting, optimal parameters:
_/users?limit=10&offset=20_

Think
**Path -> identify resource**
**Query -> modify/filter the request**

## 7.6 Request Body

Now imagine creating a user

The client sends:
_POST /users_
with:
{
"name": "Omkar",
"age": 21
}
We could manually parse dictionaries, but FastAPI gives us **Pydantic Models**

## 7.7 Pydantic Model

```
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    age: int

#then:

@app.post("/users")
def create_user(user: UserCreate)
    return user
```

Now FastAPI understands:
The request body should match the _UserCreate_ schema

For ex:
{
"name": "Omkar",
"age": 21
}
is valid

## 7.8 Why Pydantic?

Pydantic provides **data validation and parsing**
Suppose the client sends:
{
"name": "Omkar",
"age": "hello"
}
FastAPI/Pydantic can reject it because:
age -> expected integer
"hello" -> invalid
This is much safer than blindly trusting client input

## 7.9 Validation is a Backend Developer's Responsibility

Never Assume:
"The frontend will send correct data"
Clients can send:
wrong types, missing fields, invalid values, malicious input, unexpected data
Your backend needs validation
Pydantic helps enforce the expected structure

## 7.10 Pydantic Field Constraints

You can add constraints

```
from pydantic import BaseModel, Field

class UserCreate(BadeModel)
    name: str
    age: int = Field(gt=0)
```

Now:
{
"name": "Omkar",
"age": -5
}
fails validation

For a fintech API, validation becomes especially important
For ex:

```
from decimal import Decimal
from Pydantic import BaseModel, Field

class Investment(BaseModel):
    symbol: str
    amount: Decimal = Field(gt=0)
```

Cause we don't want an investment amount of: _-50000_ passing through unchecked

## 7.11 Response Models

Pydantic models aren't only for requests
You can define the expected response:

```
class UserResponse(BaseModel):
    id: int
    name: str

#Then:

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return{
        "id": user_id,
        "name": "Omkar"
    }
```

This helps ensure the API response follows the expected schema
It also improves the generated API documentation

## 7.12 HTTP Status Codes in FastAPI

You can specify the status code:

```
from fastapi import FastAPI, status

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate)
    return user
```

## 7.13 HTTPException

Suppose:

```
@app.get("users/{user_id}")
def get_user(user_id: int):
    user = find_user(user_id)

    if user is None:
        ...
```

_500 Internal Server Error_
because the server didn't unexpectedly fail
The user simply doesn't exist.

Use:

```
from fastapi import HTTPException

raise HTTPException(
    status_code=404,
    detail="User not found"
)
```

The client receives an appropriate HTTP error

## 7.14 Why _HTTPException_ Matters

Imagine:
_GET /users/999_
If user 999 doesn't exist:
_404 Not Found_
is correct

If your database crashes unexpectedly
_500 Internal Server Error_
is appropriate

The backend should distinguish **expected application errors** from **unexpected server failures**

## 7.15 Automatic Documentation

One of FastAPI's great features is automatic API documentation
FastAPI generates an **OpenAPI schema** from your routes, types, Pydantic models, etc
This gives you interactive documentation, commonly available at: _/docs_
and an alternative documentation interface at: /redoc

"FastAPI automatically generates OpenAPI documentation from the application's routes and type definitions, providing interactive API documentation"
This is extremely important when frontend developers or other services need to understand your API

## Part 7 - Quiz

Q1 - Path vs Query
_/users/123?active=true&limit=10_
Identify: path param, query param. Then explain when you'd use path param versus a query param
/user/123 -> path param; ?active=true&limit=10 -> query param
I will use path param when I want to access a particular data with its referenced id, user 123. I would use query para when filtering, paginating, through data

Q2 - Pydantic
Write a Pydantic model called: _PortfolioCreate_
with:
name: string
initial_balance: Decimal
risk_score: integer that must be between 1 and 10
Use Pydantic validation.

```
from pydantic import BaseModel, Field
from decimal import Decimal

class PortfolioCreate(BaseModel):
    name: str
    initial_balance: Decimal = Field(gt=0)
    risk_score: int = Field(ge=1, le=10)
```

Q3 - FastAPI endpoint
Write a FastAPI endpoint:
_GET /portfolios/{portfolio_id}_
Where:

- _portfolio_id_ must be an integer
- if the portfolio doesn't exist, return 404
- otherwise return the portfolio
  You can fake the database with:
  _portfolio = None_ or a simple dict

```
from fastapi import FastAPI, HTTPException

app = FastAPI()

portfolio = {
    "id": 1,
    "name": "My Portfolio",
    "balance": 10000
}

@app.get("/portfolios/{portfolio_id}")
def get_portfolio(portfolio_id: int):

    if portfolio_id != portfolio["id"]:
        raise HTTPException(
            status_code=404,
            detail="Portfolio not found"
        )

    return portfolio
```

Q4 - Why is Pydantic useful in FastAPI
Pydantic is useful for performing request body validation and it is also used to send expected output in the response too, it is also used create a Pydantic model which is used to ceate a Schema -> expected data from the user, if it the expected input doesn't match the pydantic model it simply doesn't validate it and considers it invalid

"Pydantic allows FastAPI to define and validate the structure and types of incoming and outgoing data. It parses request data into typed Python objects, validates constraints such as required fields and numeric ranges, and can also define response schemas. These models are additionally used by FastAPI to generate accurate OpenAPI documentation."

# Part 7 — Key Takeaways

Path parameters identify specific resources; query parameters are commonly used for filtering, searching, pagination and optional behavior.
Pydantic models define the expected structure and validation rules for API data.
FastAPI uses Python type hints + Pydantic to validate input and generate OpenAPI documentation.
HTTPException should be used for expected HTTP errors such as 404, rather than allowing them to become 500 errors.
FastAPI's route decorators connect HTTP methods/paths to Python endpoint functions.

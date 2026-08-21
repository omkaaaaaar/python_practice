# Part 6: What an API is, client/server model, HTTP request/response, URLs, HTTP methods, GET/POST/PUT/PATCH/DELETE, headers, request body, JSON, status codes, REST principles

## 6.1 What is an API?

Imagine you have a mobile banking application,
The mobile app needs to ask the backend:
"Give me Omkar's portfolio"
The mobile app shouldn't directly access the database

Instead:

```
Mobile App
    |
    | HTTP request
    ↓
Backend API
    |
    ↓
Database

The backend processes the request and sends back a response:

Database
    ↓
Backend API
    |
    | HTTP response
    ↓
Mobile App
```

An API(**Application Programming Interface**) is essentially a defined way for software systems to communicate with each other
For a web backend, this commonly happens over **HTTP**

## 6.2 Client and Server

Two important terms:

### Client

The system making the request
Ex: browser, mobile app, frontend React application, another backend service, Postman, Python HTTP client

### Server

The system receiving and processing the request
In this case:
_FastAPI application_
So:
Client → HTTP Request → FastAPI Server
Client ← HTTP Response ← FastAPI Server

## 6.3 What is HTTP?

**HTTP = HyperText Transfer Protocol**
It's a protocol that defines how clients and servers communicate over the web

## 6.4 HTTP Request

Suppose the client wants:
_GET /users/123_
Conceptually, the request contains:
HTTP Request
│
├── Method
├── URL/path
├── Headers
└── Body (sometimes)
Example:
GET /users/123 HTTP/1.1
Host: example.com
Authorization: Bearer ...

## 6.5 HTTP Response

The server sends back:
HTTP Response
│
├── Status code
├── Headers
└── Body
For ex:

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 123,
    "name": "Omkar"
}


So the basic flow is:
CLIENT
   |
   | HTTP REQUEST
   | method + URL + headers + body
   ↓
SERVER
   |
   | HTTP RESPONSE
   | status + headers + body
   ↓
CLIENT
```

This is the foundation of everything we'll do in FastAPI

## 6.6 URL

Consider:
*https://api.example.com/users/123?active=true*
Break it down:
https://
↓
scheme

api.example.com
↓
host

/users/123
↓
path

?active=true
↓
query parameter

In FastAPI, these concepts become:
_@app.get("/users/{user*id}")*
and:
_/users/123_
would give:
_user_id = 123_
We'll do this properly in Part 7

## 6.7 HTTP Methods

The major methods you need to know:

```
| Method | Typical purpose                          |
| ------ | ---------------------------------------- |
| GET    | Retrieve data                            |
| POST   | Create a resource / perform an operation |
| PUT    | Replace/update a resource                |
| PATCH  | Partially update a resource              |
| DELETE | Delete a resource                        |
```

### GET

Ex:
_GET /users/123_
Meaning:
"Give me user 123"
Generally, GET should not modify server state

### POST

Ex:
_POST /users_
Body:
{
"name": "Omkar",
"email": "omkar@example.com"
}
Meaning:
"Create a new user"

### PUT

Suppose:
_/users/123_
Current user:
{
"name": "Omkar",
"email": "old@example.com"
}
A PUT might send the complete replacement
{
"name": "Omkar Patkar",
"email": "new@example.com"
}
Think:
**PUT = replace/update the resource represntation, it requires to change all the info of that user**

## 6.8 PATCH

PATCH is generally used for a partial update
For ex:
_PATCH /users/123_
Body:
{
"email": "new@example.com"
}
Only the email changes

We don't necessarily need to send the entire user
"PUT generally represents replacing the resource, while PATCH represents a partial modication"

## 6.9 DELETE

_DELETE /users/123_
Meaning:
Delete user 123
Simple.

## 6.10 Status Codes

These are extremely important for FastAPI
Think of them in categories

### 2xx -> Success

Common:
200 OK
201 Created
204 No Content

### 4xx -> Client-side/request problem

Common:
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
422 Unprocessable Content

### 5xx -> Server-side problem

Common:
500 Internal Server Error
502 Bad Gateway
503 Service Unavailable

## 6.11 The important ones for interview

### 200 OK

Request succeeded
Typical GET:
GET /users/123
→ 200

### 201 Created

A new resource was successfully created
Typical:
POST /users
→ 201

### 204 No Content

Successful operation, but no response body
Common example:
DELETE /users/123
→ 204

### 400 Bad Request

The request is malformed or invalid

### 401 Unauthorized

The client has **not successfully authenticated**
Think:
"Who are you?"

### 403 Forbidden

The client is authenticated but **doesn't have permission**
Think:
"I know who you are, but you're not allowed to do this"
This distinction is frequently asked

### 404 Not Found

The requested resource doesn't exist
GET /users/999999
→ 404

### 500 Internal Server Error

Something unexpected went wrong on the server
You generally don't want to intentionally return _500_ for normal validation/business errors

## 6.12 JSON

JSON is a common format for exchanging data over APIs
Ex:
{
"name": "Omkar",
"age": 21,
"active": true
}

JSON supports concepts like:
string
number
boolean
null
array
object

Python equivalents are roughly:
JSON object → dict
JSON array → list
string → str
number → int/float
true/false → True/False
null → None

FastAPI will handle much of the conversion and validation for us

## 6.13 Headers

Headers provide **metadata** about the request/response
For ex:
Content-Type: application/json
Authorization: Bearer <token>

_Content-Type_
Tells the server what format the body is in
For JSON:
_Content-Type: application/json_

**Authorization**
Often used to send authentication credentials/token information
We'll revisit this when discussing FastAPI dependencies

## 6.14 Request Body

For something like:
_POST /orders_
the client might send:
{
"symbol": "AAPL",
"quantity": 10,
"price": "225.40"
}
The body contains the data being sent to the server
FastAPI + Pydantic will later let us define exactly what that body should look like

## 6.15 REST

REST isn't simply: "An API that uses HTTP"
It's an architectural style based on principles around resources, representations, statelessnes, and standard HTTP semantics

Instead of:
/getUser
/createUser
/deleteUser

you generally model resources:
GET /users/123
POST /users
PATCH /users/123
DELETE /users/123

The **HTTP method describes the operation**, while the **URL identifies the resource**
That's a very useful mental model

## 6.16 Ex: Portfolio API

Imagine we're building fintech backend
**GET portfolio**
_GET /portfolios/123_
**Create portfolio**
_POST /portfolios_
**Update portfolio**
_PATCH /portfolios/123_
**Delete portfolio**
_DELETE /portfolios/123_
This is the exact mental model we'll use in Part 9

## Part 6 Quiz

Q1 - Explain the complete HTTP request/response cycle
-> A client wants to retrieve a user's portfolio, the client will send a HTTP request to the server side, the server will analyze the request and the body(if it is available) and the server will fetch the user's portfolio from the database and will send it back to the client through a HTTP response
"The client sends an HTTP request containing information such as the method, URL, headers, and potentially a request body. The server receives and processes the request, performs any required business logic or database operations, and constructs an HTTP response containing a status code, headers, and potentially a response body. The client receives and processes that response."

Q2 - Methods
For each operation, choose the most appropriate HTTP method:
A. Retrieve portfolio 123
B. Create a new portfolio
C. Change only the portfolio's name
D. Delete portfolio 123

A. HTTP GET request
B. PUT
C. PATCH
D. DELETE

Q3 - Status code:
What status code would you normally return for:
A. Successful GET - 200
B. Successfully created a new resource 201
C. Resource doesn't exist - 404
D. User isn't authenticated - 401
E. User is authenticated but doesn't have permission - 403
F. Unexpected server error - 500

Q4 - REST design
Which API design is more RESTful, and why?
Option A
POST /createUser
GET /getUser/123
POST /deleteUser/123
Option B
POST /users
GET /users/123
DELETE /users/123
Explain the principle behind your choice.
-> The option B is more restful cause it is more direct approach
"Option B is more RESTful because the URL represents the resource, /users, while the HTTP method describes the operation being performed. We use POST to create a user, GET to retrieve one, and DELETE to remove one, rather than putting the operation itself into the URL."

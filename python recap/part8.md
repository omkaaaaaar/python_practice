# Part 8: FastAPI Dependency Injection, _Depends()_, dependency functions, shared dependencies, database session dependencies, authentication dependencies, dependency chains, _yield_ dependencies, middleware, request/response lifecycle, middleware vs dependencies

## 8.1 First: What is Dependency Injection?

Suppose you have:

```
def get_user():
    ...
```

and your endpoint needs a database connection
One approach would be:

```
@app.get("/users")
def get_users():
    db = create_database_connection()
    ...
```

But now **every endpoint has to know how to create the database connection**
That's bad because:
duplicated code, difficult testing, difficult resource management, endpoints become coupled to infrastructure
Instead we can say:
"This endpoint needs a database session. Someone else should provide it"
That's **dependency injection**

## 8.2 The Basic FastAPI Example

FastAPI uses:
_Depends()_
Example:

```
from fastapi import Depends, FastAPI

app = FastAPI()

def get_database():
    return "database connection"

@app.get("/users")
def get_users(db = Depends(get_database)):
    retutn {"database": db}
```

FastAPI sees:
_Depends(get_database)_
and understands:
"Before calling _get_users_, I need to execute _get_database()_ and give its result to the _db_ parameter"

Conceptually:

```
HTTP request
     ↓
FastAPI
     ↓
get_database()
     ↓
db
     ↓
get_users(db)
     ↓
response
```

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

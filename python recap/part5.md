# Part 5: async/await, synchronous vs asychronous execution, event loop, corouties, asyncio.gather(), I/O-bound vs CPU-bound work, blocking calls inside async functions, concurrency vs parallelism

## 5.1 First: Synchronous Python

Forget _async_ for a moment
Imagine a program does:

_result1 = call_api_1()_
_result2 = call_api_2()_
_result3 = call_api_3()_

if each API call takes 1 second:
_call_api_1 -> 1 sec_
_call_api_2 -> 1 sec_
_call_api_3 -> 1 sec_
_Total ~ 3 seconds_

The program waits for each operation to finish before moving to the next one
That's **synchronous execution**

## 5.2 The problem: I/O waiting

Now imagine:

```
Your Python program
      |
      ↓
Make HTTP request
      |
      ↓
WAIT................................
      |
      ↓
Server responds
```

During the waiting period, your CPU isn't necessarily doing useful Python work

Other examples of I/O waiting:

- HTTP requests
- database queries
- reading from a network
- waiting for files
- Redis requests
  This is where asynchronous programming becomes useful

## 5.3 What does _async_ mean?

You can define a coroutine function:

```
async def fetch_data():
    return "data"
```

Calling it:
_result = fetch_data()_
does **not** immediately give you "data"

It gives you a **coroutine object**

You normally executes it using:
_result = await fetch_data()_
inside another async function

## 5.5 The Event Loop

This is the concept interviewers often ask about
Think of the event loop as a **manager coordinating asynchronous tasks**
Imagine:

```
             Event Loop
                 |
       ┌─────────┼─────────┐
       ↓         ↓         ↓
    Task A     Task B     Task C
       |         |         |
    waiting    running   waiting
       |         |         |
       └─────────┼─────────┘
                 ↓
          resume when ready
```

Suppose Task A is waiting for a database response
Instead of sitting idle: Task A -> WAIT, CPU -> WAIT
the event loop can run Task B

When Task A's I/O is ready, the event loop can resume it
This is why async programming can handle many **I/O-bound operations efficiently**

## 5.6 asyncio.sleep() - the easiest demonstration

Consider:

```
import asyncio

async def task():
    print("Start")
    await asyncio.sleep(2)
    print("End")
```

_asyncio.sleep()_ is asynchronous
While the task is sleeping, the event loop can run other tasks

## 5.7 Sequential async execution

```
import asyncio

async def task(name):
    print(f"{name} started")
    await asyncio.sleep(2)
    print(f"{name} finished")

async def main():
    await task("A")
    await task("B")
```

Even though these functions are _async_, this is still effectively **sequential**
A starts
A waits 2 sec
A finishes
B starts
B waits 2 sec
B finishes
Approximately
**4 seconds**
This is a very important point:
**Using _async_ does not automatically mean your operations execute concurrently**

## 5.8 _asyncio.gather_

Now:

```
import asyncio

async def task(name):
    print(f"{name} started")
    await asyncio.sleep(2)
    print(f"{name} finished")


async def main():
    await asyncio.gather(
        task("A"),
        task("B")
    )
```

Now both tasks can make progress concurrently
Conceptually:
A ── waiting ────────── finish
B ── waiting ────────── finish
Instead of:
A ───────── finish
.............B ───────── finish
Total time is roughly **2 seconds**, not 4
That's the power of async concurreny for I/O-bound tasks

## 5.9 Concurreny vs Parallelism

### Concurrency

Multiple tasks **make progress during overlapping periods**
Async Python is primarily about concurrency

### Parallelism

Multiple tasks literally execute **at the same time**, often using multiple CPU cores.

For example:
Core 1 → Task A
Core 2 → Task B

Asyncio's event loop generally runs Python code on a single thread, switching between tasks when they await.

"Asyncio provides concurrency, especially useful for I/O-bound work. Parallelism is a different concept involving simultaneous execution, often across multiple CPU cores."

## 5.10 I/O-bound vs CPU-bound

This ditinction is **very important**

### I/O-bound

The program spends significant time waiting for something ecternal
Ex: HTTP API, Database, Redis, File/network I/O
Async is often excellent here

### CPU-bound

The program spends most of its time doing computation
Ex: Large numerical calculation, Image processing, Machine learning computation, Complex data processing
Simply making the function _async_ doesn't make CPU-heavy work faster
If we do:

```
async def calculate():
    for i in range(10**9):
        ...
```

the event loop can be blocked by that CPU-heavy computation

## 5.11 The Most important Async Mistake

Suppose you're writing FastAPI:

```
@app.get("/data")
async def get_data():
    result = requests.get("https://example.com")
    return result.json()
```

This is problematic
Why?
_requests.get()_ is a **synchronous/blocking** operation
While it waits:
requests.get()
↓
WAIT
↓
event loop blocked
Other async requests may be unable to make progress efficiently

## 5.12 Better approach

Use an ansynchronous HTTP client:

```
asysnc with httpx.AsyncClient() as client:
    response = await client.get("https://example.com")
```

Now the network operation can yield control back to the event loop while waiting.
FastAPI commonly works with this async model

## 5.13 Another Common Mistake

Don't do:

```
async def main():
    time.sleep(5)
```

_time.sleep()_ blocks the thread
Istead:

```
async def main():
    await asyncio.sleep(5)
```

The second version cooperates with the event loop

Interview Question:
"What's wrong with using _time.sleep()_ inside an async function?"
_time.sleep()_ is blocking. It blocks the event-loop thread, preventing another asynchronous tasks from making progress during the sleep. I'd use _await asyncio.sleep()_ for asynchronous delays

## 5.14 Async in FastAPI

You'll eventually see:

```
@app.get("/users")
async def get_user:
    users = await fetch_users()
    return users
```

The endpoint itself is a coroutine
If _fetch_users()_ performs async database/network I/O:
Request
↓
FastAPI
↓
async endpoint
↓
await database/network
↓
event loop handles other work
↓
I/O completes
↓
endpoint resumes
↓
response

This is one of the fundamental reasons async frameworks like FastAPI can handle many concurrent I/O bound requests efficiently

## Part 5 - Quiz

Q1 - Interview explaination
**What is the event loop, and what does _await_ do?**
The event loop is kind of a manager which manage all the tasks concurrently, the await tells the event loop that this task will take time to process and to look after the other task till the task which will take time gets finished, the event loop thereafter looks after the other tasks and comes back to the task which had await to execute it after a particular time(mentioned/ or time not mentioned) and executes it if there is a output available

Q2 - Sequential vs concurrent
What is the approximate runtime of this?

```
async def task():
    await asyncio.sleep(2)

async def main():
    await task()
    await task()

# and this

async def main():
    await asyncio.gather(
        task(),
        task()
    )
```

the aprox runtime of the first snippet is 4 sec, cause even though it is in an async function thet output is written/called sequentially so task will take 2+2 seconds.
the aprox runtime of the second snippet is 2 sec, cause it involes the gathering of both the task, so suppose task1 process takes 2sec, while executing task1 the task2 also gets executed

Q3 - Find the problem
What is wrong with this FastAPI endpoint?

```
@app.get("/users")
async def get_users():
    response = requests.get("https://api.example.com/users")
    return response.json()
```

Although the function called is asynchronous, but the http request - requests.get is a synchronours http client, we should use async httpclient to get it work asynchronously

Q4 - CPU vs I/O
You're building a portfolio backend.
Which of these are good candidates for async?
A. Waiting for PostgreSQL to return query results
B. Waiting for an external market-data API
C. Calculating a huge numerical simulation that takes 10 seconds of CPU time
D. Waiting for Redis
Choose the appropriate ones and explain why
-> Everything except the C is a good candidate for async, cause while waiting for A,B and D we can perform another tasks(coroutinely) but for C we will have to wait, it will block the event loop for 10s

# Part 5 — Key Takeaways

- async defines a coroutine; await allows an async operation to suspend while the event loop handles other work.
- asyncio.gather() allows multiple async tasks to make progress concurrently.
- Async Python is especially useful for I/O-bound operations such as databases, HTTP APIs and Redis.
- Blocking operations such as requests.get() or time.sleep() can block the event loop and should generally be avoided inside async endpoints.
- Concurrency ≠ parallelism: asyncio primarily provides concurrency through cooperative scheduling.

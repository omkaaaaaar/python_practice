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

## 5.5

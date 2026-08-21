import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

async def task1(name1):
    print(f"{name1} started")
    await asyncio.sleep(2)
    print(f"{name1} finished")

async def task2(name2):
    print(f"{name2} started")
    await asyncio.sleep(1)
    print(f"{name2} finished")

async def main_task():
    await task1("Omkar")
    await task2("Om")

asyncio.run(main_task())

''' Output
A starts
A waits 2 sec
A finishes
B starts
B waits 2 sec
B finishes
'''
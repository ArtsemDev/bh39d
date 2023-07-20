# # from threading import Thread, Timer, current_thread, Lock, Semaphore, Barrier, Event, local
# from time import sleep
# # from queue import Queue
# from multiprocessing import Process, Queue, Event, Barrier, Semaphore, Lock, current_process
#
#
# lock1 = Lock()
# semaphore1 = Semaphore(value=5)
# barrier1 = Barrier(5)
# event1 = Event()
# q = Queue()
#
#
# def foo():
#     with open('foo.txt', 'w', encoding='utf-8') as file:
#         for _ in range(10):
#             file.write('hello\n')
#             sleep(1)
#
#
# def bar():
#     with open('bar.txt', 'w', encoding='utf-8') as file:
#         for _ in range(10):
#             file.write('world\n')
#             sleep(1)
#
#
# def baz():
#     for _ in range(10):
#         with semaphore1:
#             with lock1:
#                 print(current_process().name)
#             sleep(1)
#
#
# def func1():
#     sleep(3)
#     q.put('Some string')
#     event1.set()
#
#
# def func2():
#     event1.wait()
#     event1.clear()
#     item = q.get()
#     print(item)
#
#
# if __name__ == '__main__':
#     # foo_thread = Timer(
#     #     interval=5,
#     #     function=foo,
#     # )
#     # bar_thread = Thread(
#     #     target=bar,
#     #     name='Bar Thread'
#     # )
#     # foo_thread.start()
#     # bar_thread.start()
#     # threads = [Thread(target=baz, name=f'Thread-{i}') for i in range(100)]
#     # for thread in threads:
#     #     thread.start()
#     thread1 = Process(target=func1)
#     thread2 = Process(target=func2)
#     thread1.start()
#     thread2.start()


from asyncio import (
    Event,
    Semaphore,
    Barrier,
    Queue,
    Lock,
    sleep,
    current_task,
    create_task,
    run,
    get_event_loop
)


# async def foo():
#     for _ in range(10):
#         print(current_task().get_name())
#         await sleep(1)


# async def main():
#     tasks = [create_task(foo(), name=f'Task-{i}') for i in range(10)]
#     for task in tasks:
#         await task


# if __name__ == '__main__':
#     run(main())


async def foo(a, b, c):
    return a * b * c


async def main():
    print(await foo(4, 5, 6))


if __name__ == '__main__':
    run(main())

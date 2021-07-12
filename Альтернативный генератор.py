# def task(name, queue):
#     while not queue.empty():
#         count = queue.get()
#         total = 0
#         time.sleep(3)
#         print(f"Task {name} running")
#         for x in range(count):
#             total += 1
#             yield
#         print(f"Task {name} total: {total}")
#
#
# def run_generator():
#     """
#     Это основная точка входа в программу
#     """
#     # Создание очереди работы
#     work_queue = queue.Queue()
#
#     # Размещение работы в очереди
#     for work in [15, 10, 5, 2]:
#         work_queue.put(work)
#
#     # Создание задач
#     tasks = [task("One", work_queue), task("Two", work_queue)]
#
#     # Запуск задач
#     done = False
#     while not done:
#         for t in tasks:
#             try:
#                 next(t)
#             except StopIteration:
#                 tasks.remove(t)
#             if len(tasks) == 0:
#                 done = True
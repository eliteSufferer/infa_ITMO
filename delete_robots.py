queue = input()  # читаем очередь роботов

# считаем количество сломанных и исправных роботов
broken_count = queue.count('В')
working_count = queue.count('W')

# если очередь уже соответствует условиям, выводим ее и выходим
if queue.startswith('В' * broken_count) and queue.endswith('W' * working_count):
    print(0)
    print(queue)
    exit()

# удаляем лишние роботы
removed_count = abs(broken_count - working_count)
if broken_count > working_count:
    queue = queue[removed_count:]
else:
    queue = queue[:-removed_count]

# выводим результат
if queue:
    print(removed_count)
    print(queue)
else:
    print("НИКОГО НЕ ОСТАЛОСЬ")
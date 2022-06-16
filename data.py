# ##########Для выполнения задания нужно написать парсер системных процессов команды 'ps aux' на языке Python с
# использованием стандартной библиотеки и модуля subprocess. Парсер должен вывести в стандартный вывод в качестве
# результата работы следующую информацию (все цифры и данные для примера): Отчёт о состоянии системы: Пользователи
# системы: 'root', 'user1', ... Процессов запущено: 833 Пользовательских процессов: root: 533 user1: 231 ... Всего
# памяти используется: 45.7% Всего CPU используется: 33.2% Больше всего памяти использует: (%имя процесса,
# первые 20 символов если оно длиннее) Больше всего CPU использует: (%имя процесса, первые 20 символов если оно
# длиннее) Так же этот отчёт должен быть сохранён в отдельный txt файл с названием текущей даты и времени проверки.
# Например, 10-12-2021-12:15-scan.txt
import subprocess


def get_processes():
    output = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE).stdout.readlines()
    headers = [h for h in ' '.join(str(output[0]).strip().split()).split() if h]
    raw_data = map(lambda s: s.strip().split(None, len(headers) - 1), output[1:])
    return [dict(zip(headers, r)) for r in raw_data]


processes = get_processes()


def get_unique_users():
    users = [i["b'USER"].decode('utf-8') for i in processes]
    return sorted(list(set([x for x in users if users.count(x) > 1])))


def get_processes_count():
    return len(processes)


def get_processes_count_for(user: str):
    processes_count = 0
    for process in processes:
        if process["b'USER"] == bytes(user, 'utf-8'):
            processes_count = processes_count + 1
    return processes_count


def get_user_processes_count_dict():
    user_processes_dict = {}
    for user in get_unique_users():
        user_processes_dict[user] = get_processes_count_for(user)
    print(user_processes_dict)


def get_memory_for_all_processes():
    values = [(i['%MEM']) for i in processes]
    memory = [value.decode('utf-8') for value in values]
    final_number = 0
    for process in memory:
        final_number = final_number + float(process)
    return final_number


def get_cpu_for_all_processes():
    values = [(i['%CPU']) for i in processes]
    cpu = [value.decode('utf-8') for value in values]
    final_cpu = 0
    for process in cpu:
        final_cpu = final_cpu + float(process)
    return final_cpu


def get_most_memory_consuming_process_name():
    newlist = sorted(processes, key=lambda d: d['%MEM'], reverse=True)
    values = [i["COMMAND\\n'"].decode('utf-8') for i in newlist]
    process_name = values[0]
    print(values)
    if len(process_name) > 20:
        process_name = process_name[:20]
    return process_name


def get_most_cpu_consuming_process_name():
    newlist = sorted(processes, key=lambda d: d['%CPU'], reverse=True)
    values = [i["COMMAND\\n'"].decode('utf-8') for i in newlist]
    process_name = values[0]
    print(values)
    if len(process_name) > 20:
        process_name = process_name[:20]
    return process_name


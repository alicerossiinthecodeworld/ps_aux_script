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
    values = [str(i["b'USER"]) for i in processes]
    users = [value.replace("b'", "") for value in values]
    final_user_list = [user.replace("'", "") for user in users]
    return sorted(list(set([x for x in final_user_list if final_user_list.count(x) > 1])))


def get_processes_count():
    return len(processes)



import data


def format_the_report(file):
    file.write("Отчёт о состоянии системы:\n")
    file.write(f"Пользователи системы:{data.get_unique_users()}\n")
    file.write(f"Процессов запущено:{data.get_processes_count()}\n")
    file.write("Пользовательских процессов:\n")
    for user in data.get_unique_users():
        file.write(f"{user} : {data.get_processes_count_for(user)}\n")
    file.write(f"Всего памяти используется:{data.get_memory_for_all_processes()}%\n")
    file.write(f"Всего cpu используется:{data.get_cpu_for_all_processes()}%\n")
    file.write(f"Больше всего памяти использует: {data.get_most_memory_consuming_process_name()}%\n")
    file.write(f"Больше всего CPU использует: {data.get_most_cpu_consuming_process_name()}%\n")

import sys
from datetime import datetime

import data


def format_the_report():
    report = ""
    report += "Отчёт о состоянии системы:\n"
    report += f"Пользователи системы:{data.get_unique_users()}\n"
    report += f"Процессов запущено:{data.get_processes_count()}\n"
    report += "Пользовательских процессов:\n"
    for user in data.get_unique_users():
        report += f"{user} : {data.get_processes_count_for(user)}\n"
    report += f"Всего памяти используется:{data.get_memory_for_all_processes()}%\n"
    report += f"Всего cpu используется:{data.get_cpu_for_all_processes()}%\n"
    report += f"Больше всего памяти использует: {data.get_most_memory_consuming_process_name()}\n"
    report += f"Больше всего CPU использует: {data.get_most_cpu_consuming_process_name()}\n"
    return report


def write_report_to_file(report, filename):
    with open(filename, "w") as f:
        f.write(report)
        return f


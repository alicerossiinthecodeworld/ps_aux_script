import sys
from datetime import datetime

import formatter

report = formatter.format_the_report()
report_filename = f"{datetime.now().strftime('%d-%m-%Y-%H:%M-scan')}.txt"
report_file = formatter.write_report_to_file(report, report_filename)
sys.stdout.write(report)


import sys
from datetime import datetime

import formatter

report = formatter.format_the_report()
report_file = formatter.write_report_to_file(report)
sys.stdout.write(report)


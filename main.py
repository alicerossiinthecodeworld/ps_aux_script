from datetime import datetime

import formatter

filename = datetime.now().strftime("%d-%m-%Y-%H:%M-scan")
f = open(filename + '.txt', 'w')
formatter.format_the_report(f)



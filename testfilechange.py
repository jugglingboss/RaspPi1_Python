import time
with open('/var/www/html/Data.txt','r') as f:
    newlines = []
    for line in f.readlines():
        newlines.append(line.replace('Blinds are closed', 'Blinds are opening'))
with open('/var/www/html/Data.txt', 'w') as f:
    for line in newlines:
        f.write(line)
time.sleep(16)
with open('/var/www/html/Data.txt','r') as f:
    newlines = []
    for line in f.readlines():
        newlines.append(line.replace('Blinds are opening', 'Blinds are open'))
with open('/var/www/html/Data.txt', 'w') as f:
    for line in newlines:
        f.write(line)
time.sleep(300)
with open('/var/www/html/Data.txt','r') as f:
    newlines = []
    for line in f.readlines():
        newlines.append(line.replace('Blinds are open', 'Blinds are closing'))
with open('/var/www/html/Data.txt', 'w') as f:
    for line in newlines:
        f.write(line)
time.sleep(12.9)
with open('/var/www/html/Data.txt','r') as f:
    newlines = []
    for line in f.readlines():
        newlines.append(line.replace('Blinds are closing', 'Blinds are closed'))
with open('/var/www/html/Data.txt', 'w') as f:
    for line in newlines:
        f.write(line)
import re



member_id_line = 'NM1*IL*1*'

with open('edi') as f:
    for line in f:
        if (line.__contains__('NM1*IL*1*')):
            ID_Line = line
            print(line)

x = re.search('\d{11}', ID_Line)

print(x.group()[9:])

dependants = int(x.group()[9:])

print(dependants)


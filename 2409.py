
f = open('2409.txt', 'r')
print(f.read())
f.close()

f = open('2409.txt', 'w')
f.write('formula1')
print(f.write)
f.close()

f = open('2409.txt', 'r')
print(f.readlines())
f.close()

f = open('2409.txt', 'a')
f.writelines(['good', 'day'])
f.close()

f = open('2409.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines]
d = {lines[1]:lines[2], lines[3]: int(lines[4])}
int(s) = {'ip', '192.168.111.1', 'port', '22'}
print(d)
f.close()

#это конфигурация
ip
192.168.111.1
port
22

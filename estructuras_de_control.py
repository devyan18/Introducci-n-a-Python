# if
if True != True:
    print('No se ejecuta')
elif True == True:
    print('Se ejecuta')
else:
    print('Se ejecuta')

# while
while False:
    print('Se ejecuta')

mi_lista = [10, 20, 30, 40, 50]

for i in mi_lista:
    print(x)

for i in range(0, 10, 1):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i, x in enumerate(mi_lista):
    print(i, x)

# esto no
for i in range(0, len(mi_lista)):
    print(i, mi_lista[i])


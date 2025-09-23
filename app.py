import socket
print("Hello world")

hostname = socket.gethostname()
print(f"Hostname: ")

IpAddress = socket.gethostbyname(hostname)
print(f"IP Address: {IpAddress}")

for i in range(10):
    print(i)
    
a = int(input("Dame el primer numero:"))
b = int(input("Dame el segundo numero"))
print(f"La suma de {a} + {b} es igual a {a+b}")

print(f"La resta de {a} - {b} es igual a {a-b}")

print (f"El producto de {a} * {b} es igual a {a*b}")
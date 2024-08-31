"""
Created on Friday 30/08/24

@author: Victor Mendoza
"""

print("Este programa simula la secuencia 'Fibonacci'")
x = int(input("\nIngrese hasta que número quiere que terminé la secuencia: "))
num1 = 0
num2 = 1

for i in range(x):
    
    sec = num2 + num1
    num2 = num1
    num1 = sec

    print(f"\n{sec}")
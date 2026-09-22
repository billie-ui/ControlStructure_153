#Write a PYTHON program to print odd numbers up to n!
n = int(input("masukan bilangan ganjil:"))

print (f"bilangan ganjil hingga {n}:")
for i in range (1, n + 1, 2):
    print(i, end=" ")
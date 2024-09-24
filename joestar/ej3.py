from collections import Counter
print([n for n,  c in Counter(input("Ingrese numeros:").split()).items()if c > 1])
def f(s):
    print(s.isalnum())
    print(s.isdigit())
    print(s.islower())
    print(s.isupper())
    print(s.isspace())

s1='abC'
print("Dla s1:\n")
f(s1)
s2='123'
print("Dla s2:\n")
f(s2)
s3='pies'
print("Dla s3:\n")
f(s3)
s4=' '
print("Dla s4:\n")
f(s4)
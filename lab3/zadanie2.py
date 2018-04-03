import os
f=open("jubel.mp3", "rb")
print(f.name,f.mode )
if f.closed:
    print("plik jest zamkniety")
else:
    print("plik jest otwarty")
f.close()
if f.closed:
    print("plik jest zamkniety")
else:
    print("plik jest otwarty")

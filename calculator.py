import random

angka_rahasia = random.randint(1, 10)

print ("=== GAME TEBAK ANGKA ===")

tebakan = int(input("Tebak angka (1-10): "))

if tebakan == angka_rahasia:
    print ("🎉 Benar!")
else:
    print (f"Salah! Jawabannya {angka_rahasia}")

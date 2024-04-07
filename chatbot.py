import re
import random

sapaan = ["Halo, apakah ada yang bisa saya bantu?","Hai!","Yo!"]

while True:
    x = input("User\t: ")
    if re.findall(r'halo|hai', x):
        print("Bot\t:", random.choice(sapaan))
    else:
        print("Bot\t: Aku tidak paham")


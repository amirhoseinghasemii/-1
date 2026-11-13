import random

secret = random.randint(1, 100)
count = 0
win = False

while count < 10:
    user = int(input("عدد مورد نظر را حدس بزن: "))
    count += 1

    if user == secret:
        print("تبریک! شما برنده شدید.")
        win = True
        break

    if user < secret:
        print("عدد بزرگتری انتخاب کن.")
    else:
        print("عدد کوچکتری انتخاب کن.")

if win == False:
    print("شما باختید!")
    print("عدد صحیح:", secret)
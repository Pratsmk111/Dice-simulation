import random
again=True
while again:
    print(random.randint(1,6))
    another_roll=input("want to play again?,(y/n)")
    if another_roll=="y":
        continue
    else:
        break
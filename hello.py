import random
count = 0
x = random.randint(0,100)
y = int(input("Guess the number 0-100\n"))
while y!=x:
    if y < x:
        print("Too Low")
        y = int(input("Guess again: \n"))
        count+=1
    elif y>x:
        print("Too High")
        y = int(input("Guess again: \n"))
        count+=1
print("It took you: "+ str(count) + " tries.")
print("YOU GOT IT!!!")
    

'''
#1 - from john bryce practises


def oddornot(number: int):
    if (float(number) % 2.0 == 0):
        return 0 # retrun 0 if the number is even
    return 1 # retrun 1 if the number is odd

userNumber = input("Enter number to check if is even or odd :")
print (f"number 0 - even , number 1 - odd : {oddornot(userNumber)}")

#2 - from john bryce practises


def checkAverage(LIST_NUMBER: list):
    average = 0
    for i in LIST_NUMBER:
        average += int(i)
   
    average = average / len(LIST_NUMBER)
    return average # retrun average

LIST_NUMBER = [10,20,30,40]
print(f"The average is : {checkAverage(LIST_NUMBER)}")



#3 - from john bryce practises


def howMuchDigits(num: str):
    count=0
    for i in num:
        count += 1
    return count

num = input("Enter the number please:")
print(f"{howMuchDigits(num)}")

'''
#4 - from john bryce practises

print(76/20)

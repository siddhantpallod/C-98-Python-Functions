# num = input("Enter A Value: ")

# for i in range(2, int(num)):
#     if(int(num) % i == 0):
#         print("Not Prime")
#         break
# else:
#     print("Prime")



def countWords():
    fileName = input("Enter A File Name: ")
    count = 0
    file = open(fileName,'r')
    for line in file:
        words = line.split(',')
        count = count + len(words)
        print(words)
    print(count)

countWords()

# def primeNo():
#     input1 = int(input("Enter the first value: "))
#     input2 = int(input("Enter the second value: "))
#     for num in range(input1,input2):
#         if (num > 1):
#             for i in range(2,num):
#                 if (num % i == 0):
#                     break
#             else:
#                 print(num)

# primeNo()


# def leapYear():
#     year = int(input("Enter A Year: "))
#     if(year % 4 == 0):
#         print('Leap Year')
#     else:
#         print('Not A Leap Year')
    
# leapYear()
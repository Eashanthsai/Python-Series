Numbers = (10,23, 45, 67, 89, 90, 12, 33, 56, 78)
evensum = 0
for number in Numbers:
    if number % 2 == 0:
        evensum += number
print("The sum of the even numbers in the tuple is : " , evensum)
Numbers = (12,45,87,23,78,3,97,35,4,3,79,86,5,3,9)
largest = Numbers[0]
for number in Numbers:
    if number >largest:
        largest = number

print("The Largest number amongn the numbers in the tuple is : " , largest)
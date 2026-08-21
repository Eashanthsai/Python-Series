Students = (
    ("Kalyan",99),
    ("Eashanth",98),
    ("Isthiyaz",97),
    ("Hemalatha",96)
)
topper = Students[0]
for student in Students:
    if student[1] > topper[1]:
        topper = student
print(f""" The topper of the class is : {topper[0]} 
      With Marks : {topper[1]} out of 100.
""")
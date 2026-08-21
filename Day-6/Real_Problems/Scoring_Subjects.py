Subjects = (
    ("Pyhton" , 90),
    ("Java" , 80),
    ("C" , 88),
    ("C++", 95)
)

for subject in Subjects:
    if subject[1] >= 85:
        print(f"""
    The subject or languages that THe students is good at is :   {subject[0]  }
""")
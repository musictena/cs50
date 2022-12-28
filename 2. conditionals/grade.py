score = int(input("Score: "))

if 90 >= score <= 100:
    print ("Grade: A")
elif 90 < score >= 80: #chaining conditonals
    print("Grade: B")
elif score >= 70:
    print("Grade C")
elif score < 70 and score >= 60:
    print ("Grade D")
else:
    print ("Grade: F")
score = int(input("What score did you get on your test? "))
if score > 90 or score == 90:
    print("Your letter grade is A")
elif score < 90 and score > 80 or score == 80:
    print("Your letter grade is B")
elif score < 80 and score > 70 or score == 70:
    print("Your letter grade is C")
elif score < 70 and score > 60 or score == 60:
    print("Your letter grade is D")
elif score < 60:
    print("Your letter grade is F")

print(
    """  Exam Grader  """
)

grade = int(input("Enter the achieved grade: "))
level = int(input("Enter the level you are working at (1/2): "))
if 101 > grade > -1 and 3 > level > 0:
    if level == 1 and grade < 50:
        print("FAIL")
    elif level == 1 and 49 < grade < 61:
        print("PASS")
    elif level == 1 and 60 < grade < 71:
        print("MERIT")
    elif level == 1 and grade > 70:
        print("DISTINCTION")
    elif grade < 40:
        print("FAIL")
    elif 39 < grade < 50:
        print("PASS")
    elif 49 < grade < 66:
        print("MERIT")
    elif grade > 66:
        print("DISTINCTION")
else:
    print("Input a valid grade/level!")

# Chat gpt version 

# print("Exam Grader")

# grade = int(input("Enter the achieved grade: "))
# level = int(input("Enter the level you are working at (1/2): "))

# if not (0 < grade < 101) or not (1 < level < 3):
#     print("Input a valid grade/level!")
# else:
#     if level == 1:
#         if grade < 50:
#             print("FAIL")
#         elif 49 < grade < 61:
#             print("PASS")
#         elif 60 < grade < 71:
#             print("MERIT")
#         else:
#             print("DISTINCTION")
#     else:
#         if grade < 40:
#             print("FAIL")
#         elif 39 < grade < 50:
#             print("PASS")
#         elif 49 < grade < 66:
#             print("MERIT")
#         else:
#             print("DISTINCTION")

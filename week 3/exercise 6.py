number = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for i in range(len(number)):
    if number[i] >= 75:
        print("First")
    if number[i] >- 70 and number[i] < 75:
        print("Upper second")
    if number[i] >=60 and number[i] < 70:
        print("Second")
    if number[i] >= 50 and number[i] < 60:
        print("Third")
    if number[i] >= 45 and number[i] < 50:
        print("F1 Sup")
    if number[i] >= 40 and number[i] < 45:
        print("F2")
    if number[i] < 40:
        print("F3")
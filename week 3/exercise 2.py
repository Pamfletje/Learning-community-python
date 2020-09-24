days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
start_day_nr = int(input("What is the starting day number?"))
length = int(input("What is the length of your wonderful holiday?"))
print("You will return on a", days[(length + start_day_nr - 1)%7])

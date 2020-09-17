# Question 1
a = "All "
b = "work "
c = "and "
d = "no "
e = "play "
f = "makes "
g = "Jack "
h = "a "
i = "dull "
j = "boy."

print(a+b+c+d+e+f+g+h+i+j)

# Question 2
print(6 * (1 - 2))

# Question 4
bruce = 6
print(bruce + 4)

# Question 5
annual_interest_rate = 0.01
number_of_times_receiving_interest_per_year = 1
ask_user = float(input("What is your current amount of money you want to invest?"))
Return = ask_user * (1 + annual_interest_rate/number_of_times_receiving_interest_per_year)
print(Return)

# Question 7
current_time = 14
print("The time the alarm goes of will be at", (14 + 51) % 24)

# Question 8
ask_user_time = int(input("What hour is it?"))
ask_user_wait = int(input("In how many hours will your alarm go off?"))
print("Your alarm will go off at", (ask_user_time+ask_user_wait) % 24)
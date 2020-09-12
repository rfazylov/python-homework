from sys import argv

working_hour = int(argv[1])
hour_cost = int(argv[2])
bonus = int(argv[3])

salary = working_hour * hour_cost + bonus
print(salary)

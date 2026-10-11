total_chores=4
completed=0
while completed<total_chores:
    answer=input("have you completed your chores (yes/no)")
    if answer=="yes":
        print("Good Job")
        completed=completed+1
    else:
        print("please complete your chores")
    print("chores left",total_chores-completed)
print("all chores completed")
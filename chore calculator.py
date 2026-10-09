total_chores = 4
orignal_count = total_chores
print(f"you have {orignal_count} chores to finish today!\n")


completed_count = 0
chore_num = 1

while chore_num <= total_chores:

     if chore_num == 1: next_chore= "make your bed"
     elif chore_num == 2: next_chore = "feed the pet"
     elif chore_num ==3: next_chore = "take out the trash"
     else: next_chore = "wash the dishes"

     answer = input(f"have you finished: {next_chore} (yes\no): ")


     if answer == "yes":
          completed_count += 1
          chore_num += 1
          print("great job! chore completed.")
     else:
          print("okay, finish it and check again")

     print("chores remaining:", total_chores - completed_count)
     print()


     print("====== ALL CHORES COMPLETE!======")
     print("great work finishing your entire checklist today!\n")
print("now let's  safely peek at an infinate loop...")
test_value=0
safety_counter=0
while test_value<=0:
     print("this condition never changes, so this would run forever")
     safety_counter += 1
     if safety_counter == 3:
        print("(stopping here on purpose - a real infinate loop never stops on it's own)")
        break

print("\n======= CHORE CHECKLIST SUMMARY=========")
print("chores assighned today:", orignal_count)
print("chores completed:", completed_count)
print("chores remaining:", total_chores - completed_count)
print("==============================================================")

     
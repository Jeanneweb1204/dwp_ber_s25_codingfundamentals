value = 23
quota= 78
if value >= quota:
    print("done")
else:
    print("Not done")

print("##ex 2")
value1 = 56
quota= 75
if value1 >= quota:
    print(0)
else:
    print(int(quota - value1) )  

print("## exercice3")
def fruit_remain(fruit_picked,fruit_quota):
    if fruit_picked >= fruit_quota:
        print(0)
    else:
        print(str(fruit_quota - fruit_picked))
fruit_remain(45,87)
fruit_remain(23,34)
fruit_remain(30,30)

print("## exercice 4")
def is_friday_off(fruits_picks,fruits_quote):
    if fruits_picks 
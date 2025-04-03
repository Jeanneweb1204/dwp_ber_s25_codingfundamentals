print("## Exercice 0")
scores = [5, 6, 6, 13, 6, 16, 2, 4, 6, 15, 3, 7, 20, 3, 24, 24, 1, 23, 3, 3, 3, 21, 7, 2, 12] 
lenght=len(scores)
print(lenght)

print("## Exercice 1")
list.copy(scores)
print(scores)
scores.count('3')

print("## Exercice 2")
list.copy(scores)
print(scores)
print(max(scores))

print("## Exercice 3")
list_1 = ["foo", 2, "bar", 3, "baz", "spam", 4]
list_2 = ["1", 2, "3", 3, "4", "foo", "pasm", "bar"]
combs=[]
for x in list_1:
    for y in list_2:
        if x==y:
            combs.append((x,y))
            print(combs)
print("## Exercice 4")
all_numbers = [111, 32, -9, -45, -17, 9, 85, -10]
for positive_numbers in all_numbers:
    if positive_numbers>=0:
        print(positive_numbers)
        

print("## Exercice 5")

reverse_this_list = [10, 20, 30, 40, 50]
reverse_this_list.reverse()
print(reverse_this_list)

print("## Exercice 6")
scores = [5, 6, 6, 13, 6, 16, 2, 4, 6, 15, 3, 7, 20, 3, 24, 24, 1, 23, 3, 3, 3, 21, 7, 2, 12]
for s in sorted(set(scores)):
    print(s)

print("## Exercice 7")
country_capital=[("Burundi=Bujumbura"),("Rwanda=Kigali"),("Tanzanie=Dodoma"),("Ouganda=kampala"),("Kenya=Nairobie")]
print(country_capital)
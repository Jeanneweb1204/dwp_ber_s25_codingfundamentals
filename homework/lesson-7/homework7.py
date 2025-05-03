def items():
    shopping_list = []
    print("Enter items for your shopping list.")
    print("Type 'done' when you are finished.")
    print("✅ begining the loop")
    while True:
        item = input("Enter an item 'done' to finish: ")
        if not item:
            pass
        elif item in shopping_list:
            continue
        elif item == 'done':
            break
        else: 
            shopping_list.append(item)

    print("Your shopping list:")
    index =1
    for item in shopping_list:
        print(f"{index}. {item}")  
        index += 1 
    print(f"Total items: {len(shopping_list)}")
items()
print("💚 loop finished")

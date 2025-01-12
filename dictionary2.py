groceries = {"apples":5, "pineapple":3, "watermelon":2, "blueberry":7, "strawberry":4}
print("apples" in groceries)

for i in groceries:
    print(i, groceries[i])

groceries["banana"] = 6
print(groceries)
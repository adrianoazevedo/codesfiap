# Store data

shops = [
    ["Kibon Sorveteria", 4.9, 6.99],
    ["Sukiya", 4.6, 7.99],
    ["A Feijoada", 4.4, 9.90],
    ["Makis Place", 4.7, 7.99],
    ["Giraffas carrefour", 4.4, 5.99],
    ["Viena", 4.4, 12.49],
]

# Algorithm

size = len(shops)

for i in range(size - 1):
    swapped = False
    for j in range(size - i - 1):
        if shops[j][1] < shops[j + 1][1]:
            shops[j], shops[j + 1] = shops[j + 1], shops[j]
            swapped = True
        elif shops[j][1] == shops[j + 1][1]:
            if shops[j][2] > shops[j + 1][2]:
                shops[j], shops[j + 1] = shops[j + 1], shops[j]            
    if not swapped:
        break

# Display

print("-"*30)
print("Empresas ordenadas:")
print("~"*30)

for index in range(size):
    print("#{} {}".format(index + 1,  shops[index][0]))
    print("    \u2605"" {} | Frete: $ {} \n".format(shops[index][1],  shops[index][2]))

print("-"*30)
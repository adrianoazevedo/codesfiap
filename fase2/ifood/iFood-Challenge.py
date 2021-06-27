# FIAP - CONNECTION

# iFood Challenge

##### TEAM TechDendê #####

# ADRIANO AZEVEDO SANTOS - adr_ba@yahoo.com.br
# Iago Tavares dos Santos - iagotavares.st@gmail.com
# João Vitor Ribeiro Bastos - jvrbastos1@gmail.com
# Leandro Oliveira Sena - leo.sena777@gmail.com



# restaurants data
# Format: [name, score, shipping]

restaurants = [
    ["Kibon Sorveteria", 4.9, 6.99],
    ["Sukiya", 4.6, 7.99],
    ["A Feijoada", 4.4, 9.90],
    ["Makis Place", 4.7, 7.99],
    ["Giraffas carrefour", 4.4, 5.99],
    ["Viena", 4.4, 12.49],
]

# Sorting algorithm 

# Sort by score.
# Tiebreaker criterion: lowest shipping

size = len(restaurants)

for i in range(size - 1):
    swapped = False
    for j in range(size - i - 1):
        if restaurants[j][1] < restaurants[j + 1][1]:
            restaurants[j], restaurants[j + 1] = restaurants[j + 1], restaurants[j]
            swapped = True
        elif restaurants[j][1] == restaurants[j + 1][1]:
            if restaurants[j][2] > restaurants[j + 1][2]:
                restaurants[j], restaurants[j + 1] = restaurants[j + 1], restaurants[j]            
    if not swapped:
        break

# Display datas

print("-"*30)
print("Empresas ordenadas:")
print("~"*30)

for index in range(size):
    print("#{} {}".format(index + 1,  restaurants[index][0]))
    print("   \u2605"" {} | Frete: R$ {} \n".format(restaurants[index][1],  restaurants[index][2]))
    
print("-"*30)
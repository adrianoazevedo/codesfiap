empresas = [
    ["Empresa 4", 4, 4],
    ["Empresa 2", 2, 2],
    ["Empresa 3", 3, 3],
    ["Empresa 1", 1, 1],
    ["Empresa 5", 5, 5],        
]

empresasOrganizadas = [empresas[0]] 
# [["Empresa 3", 3, 3]]

for index in range(1, len(empresas)):  

  # print("{} > {}".format(empresas[index][1], maior))
  # print(empresas[index][1] > )

  if (empresas[index][1] > empresas[index-1][1]):
    empresasOrganizadas.insert(index-1,empresas[index])
    print('insert')
  else:
    print('append')
    empresasOrganizadas.insert(index+1,empresas[index])
 
print(empresasOrganizadas)






shops = [
    ["Kibon Sorveteria", 4.9, 6.99],
    ["Sukiya", 4.6, 7.99],
    ["A Feijoada", 4.4, 9.90],
    ["Makis Place", 4.7, 7.99],
    ["Giraffas carrefour", 4.4, 5.99],
    ["Viena", 4.4, 12.49],    
]
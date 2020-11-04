''' 
weight : cheese's weight 
costCheese: cost of cheese
price: price of cheese

'''
costCheese = input("Input the cost of cheese ")
costCheese=float(costCheese)

print('1kg chees =', costCheese, 'grn')
print('weight, g\t', 'price, grn\t')
for weight in range(50, 1050, 50):
    price = costCheese / 1000 * weight
    print(weight, '\t', '\t' ,round(price,2))

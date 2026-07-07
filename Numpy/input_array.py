import numpy as np
monthly_sales=np.random.randint(1000,5000, size=12)
discount_sales=[]
for sale in monthly_sales:
    discount=(sale*0.1)
    discount_sales.append(float(sale-discount)) #float is used to convert the value into float type
print(discount_sales)

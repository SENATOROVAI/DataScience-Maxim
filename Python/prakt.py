products = {
    "ноутбук": 5000,
    "смартфон": 20000,
    "наушники": 1000,
    "монитор": 10000,
    "клавиатура": 500,
    "мышь": 200,
    "роутер": 1500,
    "принтер": 5000,
    "флешка": 1000,
    "жесткий диск": 3000
}
def calculate_order_cost(products, *args):
    sl = {}
    for i in args:
        if i in products.keys():
            sl[i] = sl.get(i, 0) + 1
    sm = 0
    for v, k in sl.items():
        sm += v * products[k]
    return sl
    
    
    return sl
total_cost= calculate_order_cost(products, 'ноутбук', 'роутер') 
print(total_cost) # 6500


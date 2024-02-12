workers = [['Ivan', 'Ivanov', 100000, 2], ['Petr', 'Petrov', 150000, 2], ['Sidor', 'Sidorov', 200000, 3]]
for i in workers:
    if i[3] < 2:
        i[3] = 'junior'
    elif 2 <= i[3] <= 5:
        i[3] = 'middle'
    else:
        i[3] = 'senior'
    print(i[0] + ' ' +  i[1] + ' is ' + i[3])
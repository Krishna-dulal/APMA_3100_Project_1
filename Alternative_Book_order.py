

orders = 0
books = ['calculus', 'physics', 'chemistry', 'history', 'litrature', 'french', 'astronomy']
N = len(books)
for i in range(N):
    for j in range(N):
        if i != j:
            for k in books:
                if k != i and k != j:
                    for l in books:
                        if l != i and l != j and l != k:
                            orders += 1
print('Orders: ')
print(orders)
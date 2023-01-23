
orders = 0
books = ['calculus', 'physics', 'chemistry', 'history', 'litrature', 'french', 'astronomy']

for a in books:
    for b in books:
        if a != b:
            for c in books:
                if c != a and c != b:
                    for d in books:
                        if d != a and d != b and d != c:
                            orders += 1
print(orders)
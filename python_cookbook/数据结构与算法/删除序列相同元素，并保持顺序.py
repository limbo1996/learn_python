def dedup(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
            print('a')

    

a = [1, 5, 2, 1, 9, 1, 5, 10]  
c = dedup(a)  
next(c)
list(dedup(a))

def dedup(items, key = None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

list(dedup(a, key=lambda d: (d['x'],d['y'])))
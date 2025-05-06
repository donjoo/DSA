import random

def unique_random_generator(collection):
    items = list(set(collection))  # Make a copy to avoid modifying original
    random.shuffle(items)     # Shuffle for random order
    
    while items:
        yield items.pop()
    
    raise StopIteration("No unique elements remaining.")


list1 = [3,2,1,4,4,2,3,6,4]
res = unique_random_generator(list1)
for i in res:
    print(i)




# Merge two dictionaries manually, with the second dictionary's 
# value overwriting the first on key conflict.
#  (Twist: keep both values in a list):
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

def update(dict1,dict2):
    keys = dict1.keys()
    for k,v in dict2.items():
        if k in keys:
            dict1[k] = [dict1[k],v]
        else:
            dict1[k] = v
    return dict1
    
print(update(dict1,dict2))
import array as arr

def x2(a): 
    tmp = a
    tmp.extend(a)
    
    return a

a1 = arr.array('i', [1, 2, 3])
print (a1)
b1 = x2(a1)
print (b1)
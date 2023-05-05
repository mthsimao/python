x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

if ( max(x)>5 ) & (min(x)<16):
    x= [i + 2 for i in x]
else:
    if (max(x)<5) :
        x= [i + 4 for i in x]
    else:
        x= [i + 42 for i in x]

print(x)


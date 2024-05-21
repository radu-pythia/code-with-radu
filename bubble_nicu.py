from matplotlib import pyplot as pt

to_sort= [3,0,1,8,7,2,5,4,6,9]
counter_miscari=True
while counter_miscari==True:
    counter_miscari=False
    for i in range(len(to_sort)-1):
        if to_sort[i]>to_sort[i+1]:
            temp=to_sort[i]
            to_sort[i]=to_sort[i+1]
            to_sort[i+1]=temp
            counter_miscari=True
print(to_sort)
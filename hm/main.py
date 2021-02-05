a = "abc"                           #1
b = "efghg"                         #2
n1 = len(a)                         #3
n2 = len(b)                         #4
c = ""                              #5
ml = max(len(a), len(b))            #6
i = 0                               #7
k = 1                               #8
while(i < ml):                      #9
    while(i < n1 and k > 0):        #10
        c += a[i]                   #11
        k -=1                       #12
    k = 1                           #13
    while(i < n2 and k > 0):        #14
        c += b[i]                   #15
        k -=1                       #16
    k = 1                           #17
    i+=1                            #18

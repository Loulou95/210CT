import random
def fun(B):

    squarelist =[]
    a=1
    for i in range(B):
            s=a**2
            a=a+1
            if s<=B:
                squarelist.append(s)
                highestperfect = squarelist[len(squarelist)-1]

    else:


            pass
    return highestperfect

B=int(input("Enter a number"))
print (fun(B))


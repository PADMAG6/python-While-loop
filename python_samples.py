//fibonacci 
q= int(input("enter input terms: "))
n1, n2 = 0,1
count = 0
if q <= 0:
    print("go for next process")
elif q == 1:
    print("fibnonserice process up to" + q + "term")
    print(n1)
else:
    print("fibanonserices")
    while count < q:
        print("s")
        w = n1 + n2
        n1 = n2
        n2 = w
        #print("q")
        count += 1
        
        
 //palindrom
q=str(input("enter input terms: "))
#print(q[::-1])
#q1 = reversed(q)
if q == q[::-1]:
    print("palindrom")
else:
    print("not palindrom")
    
    
//print * in triangle shape 
for i in range(0,5):
    print("*"*i)  //multiplying '*'(star) charecter with i times.

        
        

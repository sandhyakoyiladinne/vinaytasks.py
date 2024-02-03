##Spiral matrix(4)
# n=int(input("Enter no of rows:"))
# m=[list(map(int,input().split())) for i in range(n)]
# top=0
# bottom=n-1
# left=0
# right=n-1
# while top<=bottom and left<=right:
#     for i in range(left,right+1):
#         print(m[top][i], end=" ")

#     top=top+1
#     for i in range(top,bottom+1):
#         print(m[i][right],end=" ")
        
#     right=right-1
#     for i in range(right,left-1,-1):
#         print(m[bottom][i],end=" ")
        
#     bottom=bottom-1
#     for i in range(bottom,top-1,-1):
#         print(m[i][left],end=" ")
        
#     left=left+1



##(1)target
# n=list(map(int,input().split()))
# t=int(input("Enter the target:"))
# i=0
# a=[]
# while i<len(n):
#     cs=n[i]+n[i+1]
#     if cs==t:
#         a.append(i)
#         a.append(i+1)   
#         break
#     i=i+1
# print(a)


##(2)Pythagorean triplet 
# n,m=map(int,input().split())
# l=[list(map(int,input().split())) for i in range(n)]
# c=[]
# d=[]
# for i in range(n):
#     for j in range(m):
#         if i==j:
#            c.append(l[i][j])
# print()
# i=0
# j=m-1
# while i<n and j>=0:
#     d.append(l[i][j])
#     i=i+1
#     j=j-1
                
#print(c)
#print(d)


####(3)
# l=int(input("Enter the limit:"))
# for i in range(1,l+1):
#     a=i
#     for j in range(i+1,l+1):
#         b=j
#         for k in range(j+1,l+1):
#             c=k
#             if a*a+b*b==c*c:
#                 print(a," ",b," ",c)
# print()


# n,m=map(int,input().split())
# l=[list(map(int,input().split())) for i in range(n)]
# a=[]
# c=0
# b=[]
# for i in range(n): 
#     for j in range(m):
#         for k in range(n):
#             for p in range(m):
#                 if l[i][j]==l[k][p]:
#                     c=c+1
#                     a.append(l[i][j])
# else:
#     b.append(l[i][j])
                    
            
# print(b)
            
    
        

            
        
        
        
        
        
        
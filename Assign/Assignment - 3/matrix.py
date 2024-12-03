from matrix import *

def minit(rows,col,val=0,inc=0):
    mat=[]
    for i in range(rows):
        mat.append([])
        
        for j in range(col):
            mat[i].append(val)
            val+=inc
    return mat

def mprint(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j],",end=")
        print()
    print()
        
        
def madd(mat1,mat2):
    mat3=[]
    for i in range(0,len(mat1)):
        mat3.append([])
        for j in range(len(mat1[i])):
            mat3[i].append(mat1[i][j]+mat2[i][j])   
    return mat3     
        
mat1 = minit(4,4,1,0)
mat2=minit(4,4,10,2)

mprint(mat1)
mprint(mat2)

mat3=madd(mat1,mat2)
mprint(mat3)

#-*- coding:utf-8 –*-
#选择排序
def selectSort(a):
    for i in range(1,len(a)):
        small=a[i-1]
        j=i
        while(j<len(a)):
            if a[j] < small :
                small=a[j]
                a[j]=a[i-1]
                a[i-1]=small
            j=j+1
    return a
a=[1,0,3,12,5]
print selectSort(a)

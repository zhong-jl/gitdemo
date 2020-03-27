#merge sort(A)
#以下函数完成子表的划分
def splitsort(seq):  
   #如果子表长度为1，则直接返回该表
    if len(seq)<=1:  
        return seq
    #否则，取表正中位置，记为mid
    mid=int(len(seq)/2)
    #分别对左右半表进行划分
    print('mid=',mid)
    print('left=',seq[:mid])
    print('right=',seq[mid:])
    left=splitsort(seq[:mid])  
    right=splitsort(seq[mid:])
    #对每个最小单位的子表进行排序且归并
    return mergesort(left,right)  

# 以下函数完成两个子表的归并 
def mergesort(left,right):
    #定义一个临时表result存储归并后的有序结果
    result=[]  
    i,j=0,0  
    while i<len(left) and j<len(right):  
        if left[i]<=right[j]:  
            result.append(left[i])
            print(result)
            i+=1  
        else:  
            result.append(right[j])
            print(result)
            j+=1  
    result+=left[i:]  
    result+=right[j:]
    print('result=',result)
    return result  
  
if True:  
    A=[12,7,49,78,19,33,66,50,51,80] 
    import time
    start=time.perf_counter()
    print(splitsort(A))
    end=time.perf_counter()
    print('归并排序花费时间：',end-start)

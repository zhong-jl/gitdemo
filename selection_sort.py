#selection sort(A)
import time
start=time.clock()
A=[12,7,49,78,19,33,66,50,51,80]
#从第1个元素开始处理，直到第N-1个元素
for i in range(0,9,1):
    #将A[i]到A[N]的最小元素找出来，放到A[i]中
    for j in range(i+1,10,1):
    #A[i+1]至A[N]中的每个元素都与A[j]比大小
    #若遇到某个A[j]比A[i]小，则交换值，使A[i]中始终为待排序部分的最小值
        if A[j]<A[i]:
            temp=A[j]
            A[j]=A[i]
            A[i]=temp
    print(A)
end=time.clock()
print(A)
print('选择排序花费时间：',end-start)

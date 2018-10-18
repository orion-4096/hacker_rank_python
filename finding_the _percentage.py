if __name__ == '__main__':
    n=int(input())
    ls=[]
    sum1=0
    percentage=0
    mls=[]
    for i in range(n):
        ls=input().split()
        for j in range(1,4):
            ls[j]=float(ls[j])
        mls=mls+ls
        ls=[]
        
    sname=input()
    total_elements=len(mls)
    for i in range(total_elements):
        if mls[i]==sname:
            
            sum1=mls[i+1] + mls[i+2] + mls[i+3]
            percentage= sum1/3
            print('%1.2f'%(percentage))
        
    
    
    
   
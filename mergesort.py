def mergesort(arr):
    if (len(arr))==1 : return arr
    
    else:
        le= len(arr)
        mid=le/2
        l=arr[:mid]
        r=arr[mid:]
        mergesort(l)
        mergesort(r)
        i=0
        j=0
        k=0
        
        while (i<len(l) and j<len(r)):
            if(l[i]<r[j]):
                arr[k]=l[i]
                i=i+1
                k=k+1
            else:
                arr[k]=r[j]
                j=j+1
                k=k+1
        
        while i < len(l):
            arr[k] = l[i] 
            i+=1
            k+=1
            
        while j < len(r): 
            arr[k] = r[j] 
            j+=1
            k+=1

    return -1
if __name__== '__main__':
    arr1=[5,2,1,6,8,4,7,3]
    print(arr1)
    mergesort(arr1)
    print(arr1)
    
        
        




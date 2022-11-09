#Given a string, recursively remove adjacent duplicate characters from the string.
#The output string should not have any adjacent duplicates. See following examples.


def removeDuplicate(arr):
    arr=list(arr)        
    pointer=-1;
    for i in range(len(arr)):
        if(pointer==-1 or arr[pointer]!=arr[i]):
            pointer+=1;
            arr[pointer]=arr[i];
        elif (arr[pointer]==arr[i]):
            pointer-=1;
    arr=arr[0:pointer];
    print(arr);
    
removeDuplicate([8,6,9,88,8,8,8,2,5,5,2])
            
        
#Check for Palindrome -No Stack

def checkPanildrome(val):
    j=len(val)-1;
    i=0;
    palin=False
    while i<=j and val[i]==val[j]:
        j-=1;
        i+=1;
        palin=True;
        if(i==j):
            break;
    if(i<j):
        print("Not Palindrome");
    else:
        print(" palindrome");
        
checkPanildrome('madam')
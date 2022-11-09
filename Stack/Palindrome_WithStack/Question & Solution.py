#Check for Palindrome -With Stack
stackStr=[];
def stackPush(val):
    global stackStr;
    stackStr.append(val);
    
def stackPop():
    global stackStr;
    
    return stackStr.pop();
    

def palindrome(arr):
    palin=False;
    for i in arr:
        stackPush(i);
    for i in arr:
        print(i);  
        if i==stackPop():
            global stackStr;           
            palin=True;
        else:
            palin=False;
            break;
    return palin;

val="";

print(palindrome("madam"))
        
        
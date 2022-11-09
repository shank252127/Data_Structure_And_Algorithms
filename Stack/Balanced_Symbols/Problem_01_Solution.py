#Dictionary containing all the opening symbol as a key and closing symbol as values;
symbolMapping={"(":")", "{":"}","[":"]"};
#Stack:
symbolStack=[];

equation=input("Please enter the equation");
print(equation)
for i in equation:
    if i in symbolMapping.keys():
        symbolStack.append(i);       
    elif i in symbolMapping.values():
        lastEleStack=symbolStack[len(symbolStack)-1]
        if(len(symbolStack)==0):
            print("Error: Stack is empty; Unbalanced Symbol");
            break;
        elif i==symbolMapping[lastEleStack]:
            symbolStack.pop();           
            
#Checking whether the stack is empty or not:
if(len(symbolStack)==0):
    print("Balanced Equations");
else:
    print("Unbalanced Equation");
    
        
    


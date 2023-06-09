operators=['^','/','*','+','-','(',')']
priority={'^':3,'/':2,'*':2,'-':1,'+':1}
def infixTOpostfix(infix):
    stack=[]
    postfix=''
    for term in infix :
        if term not in operators:
            postfix+=term
            #print(postfix)
        elif term=='(':
            stack.append(term)
        elif term==')':
            while stack[-1]!='(':
                postfix+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and priority[term]<=priority[stack[-1]]:
                postfix+=stack.pop()
            stack.append(term)
    while stack:
        postfix+=stack.pop()
    return postfix
expression=input("Enter InfixExpressoin:")
print("Corresponding PostfixExpression:",infixTOpostfix(expression))            

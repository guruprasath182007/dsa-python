OPERATORS=set(['+','-','*','/','(',')','^'])
PRIORTITY={'+':1,'-':1,'*':2,'/':2,'^':3}
def infix_to_postfix(expression):
    stack=[]
    output=''
    for ch in expression:
        if ch not in OPERATORS:
            output+=ch
        elif ch=='(':
            stack.append('(')
        elif ch==')':
            while stack and stack[-1]!='(':
                output+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and PRIORTITY[ch]<=PRIORTITY[stack[-1]]:
                output+=stack.pop()
            stack.append(ch)
    while stack:
         output+=stack.pop()
    return output
expression=input('Enter infix expression:')
print('infix expression:',expression)
print('postfix expression:',infix_to_postfix(expression))

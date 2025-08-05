class Node:
    def __init__(self,coeff,pow):
        self.coeff=coeff
        self.pow=pow
        self.next=None
class polynomial:
    def __init__(self):
        self.head=None
    def append(self,coeff,pow):
        new_node=Node(coeff,pow)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
    def printpolynomial(self):
        temp=self.head
        result=[]
        while temp:
            result.append(f"{temp.coeff}X^{temp.pow}")
            temp=temp.next
        print("+".join(result))
    def addpolynomial(self,p1,p2):
        a=p1
        b=p2
        newHead=Node(0,0)
        c=newHead
        while a is not None or b is not None:
            if a is None:
                c.next=b
                break
            elif b is None:
                c.next=a
                break
            elif a.pow==b.pow:
                c.next=Node(a.coeff+b.coeff,a. pow)
                a=a.next
                b=b.next
            elif a. pow>b. pow:
                c.next=Node(a.coeff,a. pow)
                a=a.next
            else:
                c.next=Node(b.coeff,b. pow)
                b=b.next
            c=c.next
        return newHead.next
poly1=polynomial()
poly1.append(5,3)
poly1.append(4,2)
poly1.append(2,0)
poly2=polynomial()
poly2.append(5,1)
poly2.append(5,0)
print("First polynomial:")
poly1.printpolynomial()
print("Second polynomial:")
poly2.printpolynomial()
result=polynomial()
result.head=result.addpolynomial(poly1.head,poly2.head)
print("resultant polynomial:")
result.printpolynomial()

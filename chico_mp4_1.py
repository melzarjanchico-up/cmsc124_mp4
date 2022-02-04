"""
    FILE:       chico_mp4_1.py
    ABOUT:      An implementation that accepts any expression and convert it into infix, prefix, or postfix - depening on the input given.

    NAME:       Melzar Jan E. Chico
    COURSE:     CMSC124 B
    DATE:       18 December 2021
    TASK:       Machine Problem 4 - Expressions (No. 1)

    CREDITS:    1. YouTube. (2013). Infix, Prefix and Postfix. YouTube. Retrieved December 13, 2021, from https://www.youtube.com/watch?v=jos1Flt21is&amp;list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&amp;index=19. 
                2. YouTube. (2013). Evaluation of Prefix and Postfix expressions using stack. YouTube. Retrieved December 13, 2021, from https://www.youtube.com/watch?v=MeRb_1bddWg&amp;list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&amp;index=20. 
                3. YouTube. (2013). Infix to Postfix using stack. YouTube. Retrieved December 13, 2021, from https://www.youtube.com/watch?v=vq-nUF0G4fI&amp;list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&amp;index=21. 
                4. Infix, Prefix and Postfix Expressions. (n.d.). 4.9. Infix, Prefix and Postfix Expressions - Problem Solving with Algorithms and Data Structures. Retrieved December 13, 2021, from https://runestone.academy/runestone/books/published/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html. 
                5. Infix, postfix, and prefix conversion. Coding Ninjas Blog. (2021, September 10). Retrieved December 13, 2021, from https://www.codingninjas.com/blog/2021/09/06/infix-postfix-and-prefix-conversion/. 
"""

################################
##### Stack Implementation #####
################################

class Stack:
    def __init__(self) -> None:
        self.__stackList = []

    def push(self, item) -> None:
        self.__stackList.append(item)

    def pop(self) -> None:
        if not self.empty():
            self.__stackList.pop(-1)
    
    def empty(self) -> bool:
        return not self.__stackList
    
    def size(self) -> int:
        return len(self.__stackList)

    def top(self):
        if not self.empty():
            return self.__stackList[-1]
        return None


############################
##### Helper Functions #####
############################

def isOperator(char: str) -> bool:
    return char in ('+','-','*','/','^')

def isOperand(char: str) -> bool:
    return char.isalnum()

def getPrec(opr: str) -> bool:
    precedenceDict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return precedenceDict[opr] if isOperator(opr) else 0

def compPrec(op1: str, op2: str, isPostfix: bool) -> bool:
    op1Weight = getPrec(op1)
    op2Weight = getPrec(op2)

    if isPostfix:
        return op1Weight >= op2Weight
    else:
        return op1Weight > op2Weight


################################
##### Conversion Functions #####
################################

# * 1. Infix to Postfix
def infixToPostFix(infix: str) -> str:
    stack = Stack()
    infix = '(' + infix + ')'
    postfix = ''
    
    for chr in infix:
        if isOperand(chr):
            postfix += chr
        elif chr == '(':
            stack.push('(')
        elif isOperator(chr):
            while (not stack.empty() and stack.top() != '(' and compPrec(stack.top(), chr, True)):
                postfix += stack.top()
                stack.pop()
            stack.push(chr)
        elif chr == ')':
            while (not stack.empty() and stack.top() != '('):
                postfix += stack.top()
                stack.pop()
            stack.pop()
        else:
            raise Exception('Unknown char encounted in in->post conversion')

    while (not stack.empty()):
        postfix += stack.top()
        stack.pop()

    return postfix

# * 2. Infix to Prefix
def infixToPrefix(infix: str) -> str:
    stack = Stack()
    infix = ('(' + infix + ')')[::-1]
    prefix = ''
    
    for chr in infix:
        if isOperand(chr):
            prefix += chr
        elif chr == ')':
            stack.push(')')
        elif isOperator(chr):
            while (not stack.empty() and stack.top() != ')' and compPrec(stack.top(), chr, False)):
                prefix += stack.top()
                stack.pop()
            stack.push(chr)
        elif chr == '(':
            while (not stack.empty() and stack.top() != ')'):
                prefix += stack.top()
                stack.pop()
            stack.pop()
        else:
            raise Exception('Unknown char encounted in in->pre conversion')

    while (not stack.empty()):
        prefix += stack.top()
        stack.pop()

    return prefix[::-1]

# * 3. Postfix to Infix
def postfixToInfix(postfix: str):
    stack = Stack()

    for chr in postfix:
        if isOperand(chr):
            stack.push(chr)
        elif isOperator(chr):
            rightOp = stack.top()
            stack.pop()
            leftOp = stack.top()
            stack.pop()
            tempExp = '(' + leftOp + chr + rightOp + ')'
            stack.push(tempExp)
        else:
            raise Exception('Unknown char encounted in post->in conversion')

    return stack.top()
        
# * 4. Prefix to Infix
def prefixToInfix(prefix: str):
    stack = Stack()

    for chr in reversed(prefix):
        if isOperand(chr):
            stack.push(chr)
        elif isOperator(chr):
            leftOp = stack.top()
            stack.pop()
            rightOp = stack.top()
            stack.pop()
            tempExp = '(' + leftOp + chr + rightOp + ')'
            stack.push(tempExp)
        else:
            raise Exception('Unknown char encounted in pre->in conversion')

    return stack.top()

# * 5. Postfix to Prefix
def postfixToPrefix(postfix: str):
    infix = postfixToInfix(postfix)
    prefix = infixToPrefix(infix)

    return prefix

# * 6. Prefix to Postfix
def prefixToPostfix(prefix: str):
    infix = prefixToInfix(prefix)
    postfix = infixToPostFix(infix)

    return postfix

##########################
##### Notation Class #####
##########################

class Converter:
    def __init__(self, expStr: str) -> None:
        self.__notType = None
        self.__infix = None
        self.__prefix = None
        self.__postfix = None
        self.convert(expStr)

    def convert(self, exp: str) -> None:
        if isOperator(exp[0]):
            self.__notType = 1
            self.__infix = prefixToInfix(exp)
            self.__prefix = exp
            self.__postfix = prefixToPostfix(exp)

        elif isOperator(exp[-1]):
            self.__notType = 2
            self.__infix = postfixToInfix(exp)
            self.__prefix = postfixToPrefix(exp)
            self.__postfix = exp

        else:
            self.__notType = 0
            self.__infix = exp
            self.__prefix = infixToPrefix(exp)
            self.__postfix = infixToPostFix(exp)

    def display(self) -> None:
        resStr = (
            f"\tInfix {'INPUT' if self.__notType == 0 else 'equivalent'} : {self.__infix}\n"
            f"\tPrefix {'INPUT' if self.__notType == 1 else 'equivalent'} : {self.__prefix}\n"
            f"\tPostfix {'INPUT' if self.__notType == 2 else 'equivalent'} : {self.__postfix}\n"
        )

        print(resStr)
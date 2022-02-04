"""
    FILE:       chico_mp4_2.py
    ABOUT:      An implementation that evaluates an infix, prefix, or postfix notaition.

    NAME:       Melzar Jan E. Chico
    COURSE:     CMSC124 B
    DATE:       18 December 2021
    TASK:       Machine Problem 4 - Expressions (No. 2)

    CREDITS:    1. YouTube. (2013). Infix, Prefix and Postfix. YouTube. Retrieved December 13, 2021, from https://www.youtube.com/watch?v=jos1Flt21is&amp;list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&amp;index=19. 
                2. YouTube. (2013). Evaluation of Prefix and Postfix expressions using stack. YouTube. Retrieved December 13, 2021, from https://www.youtube.com/watch?v=MeRb_1bddWg&amp;list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&amp;index=20. 
                3. YouTube. (2013). Infix to Postfix using stack. YouTube. Retrieved December 13, 2021, from https://www.youtube.com/watch?v=vq-nUF0G4fI&amp;list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&amp;index=21. 
                4. Infix, Prefix and Postfix Expressions. (n.d.). 4.9. Infix, Prefix and Postfix Expressions - Problem Solving with Algorithms and Data Structures. Retrieved December 13, 2021, from https://runestone.academy/runestone/books/published/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html. 
                5. Infix, postfix, and prefix conversion. Coding Ninjas Blog. (2021, September 10). Retrieved December 13, 2021, from https://www.codingninjas.com/blog/2021/09/06/infix-postfix-and-prefix-conversion/. 
"""

from chico_mp4_1 import Stack, isOperator, isOperand, compPrec

################################
##### Conversion Functions #####
################################

def infixToPostFix(infixList):
    stack = Stack()
    postfixList = []
    
    for chr in infixList:
        if isOperand(chr):
            postfixList.append(chr)
        elif chr == '(':
            stack.push('(')
        elif isOperator(chr):
            while (not stack.empty() and stack.top() != '(' and compPrec(stack.top(), chr, True)):
                postfixList.append(stack.top())
                stack.pop()
            stack.push(chr)
        elif chr == ')':
            while (not stack.empty() and stack.top() != '('):
                postfixList.append(stack.top())
                stack.pop()
            stack.pop()
        else:
            raise Exception('Unknown char encounted in in->post conversion')

    while (not stack.empty()):
        postfixList.append(stack.top())
        stack.pop()

    return postfixList


def prefixToInfix(prefixList):
    stack = Stack()

    for chr in reversed(prefixList):
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

    joinedInfix = stack.top()
    infixList = []
    tempStr = ''

    for chr in joinedInfix:
        if isOperand(chr):
            tempStr += chr
        elif isOperator(chr) or chr == '(' or chr == ')':
            if tempStr:
                infixList.append(tempStr)
            infixList.append(chr)
            tempStr = ''
        else:
            raise Exception('Unknown char encounted in the infix-list conversion')

    return infixList

def prefixToPostfix(prefixList):
    infixList = prefixToInfix(prefixList)
    postfixList = infixToPostFix(infixList)

    return postfixList

###########################
##### Evaluator Class #####
###########################

class Evaluator:
    def __init__(self, rawStr: str) -> None:
        self.__postList = self.toPostfixList(rawStr.split())
        self.__stack = Stack()

    def toPostfixList(self, rawList):
        if isOperator(rawList[0]):
            return prefixToPostfix(rawList)
        elif isOperator(rawList[-1]):
            return rawList
        else:
            return infixToPostFix(rawList)

    def solve(self, x, y, op) -> int:
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            return x / y
        elif op == '^':
            return x ** y

    def evaluate(self) -> int:
        for chr in self.__postList:
            if chr.isnumeric():
                self.__stack.push(chr)

            elif isOperator(chr):
                rightOp = int(self.__stack.top())
                self.__stack.pop()
                leftOp = int(self.__stack.top())
                self.__stack.pop()
                self.__stack.push(self.solve(leftOp, rightOp, chr))
            else:
                raise Exception('Unknown char encounted in the evaluation')

        if self.__stack.size() > 1:
            raise Exception('There was an unused operand in the expression.')

        return int(self.__stack.top())
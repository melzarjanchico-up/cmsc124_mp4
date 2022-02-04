# CMSC124 MP4: Expressions
**Name**: Melzar Jan E. Chico  
**Year & Section**: BS ComSci III - CMSC 124B  
**Date**: 18 December 2021

### ☑️ Instructions

1. Create a program that will accept an expression in infix notation and is capable of converting it to prefix as well as postfix notation. Similarly, you should also be able to accept an expression in prefix notation and convert it to infix and postfix notation; and accept an expression in postfix notation, and convert it to infix and prefix notation. Assume likewise that an expression can be erroneous, thus provide appropriate error-handling schemes.
2. Use the same algorithms you have implemented in #1 to accept an expression (this time variables are actual numbers) and evaluate them to give the final answer. For clarity purposes, separate each token with a space. Also, assume that user may input erroneous expressions, so include exception handling in your implementation

### ☑️ Scope of Work
I have written all of the code from my machine problem, with some of the code & algorithm adopted/inspired from the Internet. Here they are to be specific:

#### for chico_mp4_1.py
- `Stack()` - implemented by myself based on my past DS lessons
- `isOperator()`, `isOperand()` - implemented by myself
- `getPrec()`, `compPrec()` - written by myself, algo & implementation mycodeschool
- `infixToPostFix()` - written by myself, algo & implementation from mycodeschool
- `infixToPrefix()` - written by myself, algo from
- `postfixToInfix()` - written by myself, algo from
- `prefixToInfix()` - written by myself, algo from
- `postfixToPrefix()`, `prefixToPostfix()` - implemented by myself
- `Converter()` - implemented by myself

#### for chico_mp4_2.py
- Some of the classes & functions are borrowed from chico_mp4_1.py
- `infixToPostFix()` - written by myself, algo & implementation from mycodeschool
- `infixToPrefix()` - written by myself, 
- `prefixToPostfix()` - written by myself, 
- `Evaluator()` - written by myself

#### for chico_mp4_main.py
- I made everything in this python file

### ☑️ References

1. YouTube. (2013). Infix, Prefix and Postfix. YouTube. Retrieved December 13, 2021, from https://www.youtube.com/watch?v=jos1Flt21is&amp;list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&amp;index=19. 
2. YouTube. (2013). Evaluation of Prefix and Postfix expressions using stack. YouTube. Retrieved December 13, 2021, from https://www.youtube.com/watch?v=MeRb_1bddWg&amp;list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&amp;index=20. 
3. YouTube. (2013). Infix to Postfix using stack. YouTube. Retrieved December 13, 2021, from https://www.youtube.com/watch?v=vq-nUF0G4fI&amp;list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&amp;index=21. 
4. Infix, Prefix and Postfix Expressions. (n.d.). 4.9. Infix, Prefix and Postfix Expressions - Problem Solving with Algorithms and Data Structures. Retrieved December 13, 2021, from https://runestone.academy/runestone/books/published/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html. 
5. Infix, postfix, and prefix conversion. Coding Ninjas Blog. (2021, September 10). Retrieved
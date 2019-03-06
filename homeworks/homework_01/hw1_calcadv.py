#!/usr/bin/env python
# coding: utf-8

def allowed_nums(): 
    return '0123456789.'

AllowedOperators = { 
    '-':float.__sub__, 
    '+':float.__add__,
    '*':float.__mul__,
    '/':float.__truediv__,
}

Priority = {
    '*':3,
    '/':3,
    '+':2,
    '-':2,
    '(':1,
}

def check_symbols(expression): 
    allowed_symbols=Set('0123456789-+*/ ().'); 
    if Set(expression).issubset(allowed_symbols): 
        return True

def check_brackets(expression):
    bracketsAmount=0            
    for symbol in expression:   
        if symbol=='(':         
            bracketsAmount+=1
        elif symbol==')':      
            bracketsAmount-=1
    if bracketsAmount!=0:       
        return False            
    return True                 

def return_Polish_record(expression): 
    isSearch=False
    stack = []
    outstring=''
    iter=0
    for symbol in expression:
        if symbol=='-':
            try:
                if expression[iter+1] in allowed_nums():
                    outstring+=symbol
                    iter+=1
                    continue
            except IndexError:
                pass
        if symbol==')':
            i=0
            for elem in stack:
                if elem=='(':
                    pos=i
                i+=1
            if pos<len(stack):
                stack.pop(pos)
            k=len(stack)
            while k>pos:
                outstring+=stack.pop()
                k-=1
            outstring+=') '
        if symbol in allowed_nums():
            try:
                if expression[iter+1] in allowed_nums():
                    outstring+=symbol
                else:
                    outstring+=symbol+' '
            except IndexError:
                outstring+=symbol+' '
        if symbol=='(':
            stack.append(symbol)
            outstring+=' ('
        if symbol in AllowedOperators.keys():
            if not stack:
                stack.append(symbol)
            else:
                if Priority[symbol]>Priority[stack[-1]]:
                    stack.append(symbol)
                else:
                    cnt=0
                    for elem in stack:
                        if elem=='(':
                            while cnt<len(stack):
                                if Priority[stack[cnt]]>=Priority[symbol]:
                                    outstring+=stack.pop(cnt)+' '
                                cnt+=1
                            stack.append(symbol)
                            isSearch=True
                            break
                        cnt+=1
                        if not isSearch:
                            for elem in stack:
                                if Priority[elem]>=Priority[symbol]:
                                    i=0
                                    while stack[i]!=elem:
                                        i+=1
                                    outstring+=stack.pop(i)+' '
                            stack.append(symbol)
        iter+=1
    for elem in reversed(stack):
        outstring+=elem+' '
    return outstring

def calculate(expression):
    stack = []
    number=''
    iter=0
    if check_brackets(expression) == False:
        return None
    if expression=='': 
        return None
    for symbol in expression: 
        if symbol=='-':     
            try:            
                if expression[iter+1] in allowed_nums(): 
                    number+=symbol                         
                    iter += 1
                    continue                               
            except IndexError:     
                pass              
        if symbol in allowed_nums():     
            number+=symbol              
            iter += 1
            continue                     
        if number!='':                    
            num=float(number)              
            stack.append(num)            
            number=''                     
        if not symbol in AllowedOperators.keys():       
            iter+=1
            continue
        try:
            number2=stack.pop()
            number1=stack.pop()
        except IndexError:
            return None
        try:
            result=AllowedOperators[symbol](number1,number2)
            
        except ZeroDivisionError:
            return None
        iter+=1
        stack.append(result);
    if len(stack)!=1:
        return None
    res=str(stack.pop())
    return res


def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''
    return calculate(return_Polish_record(input_string))
    raise NotImplementedError

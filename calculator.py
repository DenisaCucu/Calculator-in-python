class Calculator(object):
    def read(self) :
        '''read input from stdin'''
        return input('> ')
    
    def eval(self, string) :
        '''evaluates an infix arithmetic expression '''
        operators = [] #stack for operators
        values = [] #stack for values
        string = string.replace(" ","")
        token =""

        for char in string :
            if self.is_numeric(char):
                token += char
            else :
                if token :
                    if "." in token :
                        values.append(float(token))
                    else :
                        values.append(int(token))
                    token=""

            if char in "+-*/" :
                while (operators and operators[-1] in "+-*/" and (char in "+-" or operators[-1] in "*/")) : #ensures the precedence and associativity of expression
                    operator = operators.pop()
                    r = values.pop()
                    l = values.pop()
                    if operator == '+' :
                        values.append(l + r)
                    elif operator == '-' :
                        values.append(l - r)
                    elif operator == '*' :
                        values.append(l * r)
                    elif operator == '/' :
                        if r == 0 :
                            raise CalculatorException("Impartire cu 0")
                        values.append(l / r)
                operators.append(char)
            elif char == '(' :
                operators.append(char)
            elif char == ')' :
                while operators and operators[-1] != '(':
                    operator = operators.pop()
                    r = values.pop()
                    l = values.pop()
                    if operator == '+' :
                        values.append(l + r)
                    elif operator == '-' :
                        values.append(l - r)
                    elif operator == '*' :
                        values.append(l * r)
                    elif operator == '/' :
                        if r == 0 :
                            raise CalculatorException("Impartire cu 0")
                        values.append(l / r)
                if not operators or operators [-1] != '(' :
                    raise CalculatorException("Paranteze lipsa")
                operators.pop() #eliminate the paranthesis

        if token :
            if "." in token :
                values.append(float(token))
            else :
                values.append(int(token)) 
            
        while operators :
            operator = operators.pop()
            r = values.pop()
            l = values.pop()
            if operator == '+' :
                values.append(l + r)
            elif operator == '-' :
                values.append(l - r)
            elif operator == '*' :
                values.append(l * r)
            elif operator == '/' :
                if r == 0 :
                    raise CalculatorException("Impartire cu 0")
                values.append(l / r)        

        if len(values) == 1:
            return values[0]
        else :
            raise CalculatorException("Expresie nevalida")
        
    def is_numeric(self, token):
        try :
            int(token)
            return True
        except ValueError:
            return False
    
    def loop(self) :
        """read a line of input, evaluate and print it
        repeat the above until the user types 'quit'. """
        while True :
            line = self.read()
            if line == "quit" :
                break
            try :
                result = self.eval(line)
                print(result)
            except CalculatorException as ce:
                print(ce)

class CalculatorException(Exception) :
    def __init__(self, message):
        super().__init__(message)

if __name__ == '__main__':
    calc = Calculator()
    calc.loop()
import os

class Calculator:
    def __init__(self):
        self.isEnd = False
        self.a = 0
    
    def allclear(self):
        """Clear everything and start again"""
        os.system('cls')
        self.a = 0 # set a to default value
        self.display() # start calculator again
    
    def clear(self, solve):
        """Clear the last entry"""
        remove = 0
        for s in reversed(solve):
            if s.isdigit():
                remove += 1
            elif s in '+-*/' and remove > 0:
                break
            elif s in '+-*/' and remove == 0:
                remove = 1
                break

        solve = solve[:-remove]
        return solve

    
    def display(self):  
        print("""---------\nOperations Guide:\n'+': Addition\n'-': Subtraction\n'*': Multiplication\n'/': Division\n'ac': Clear all entries\n'exit': Exit calculator\n---------""")
        while not self.isEnd:
            solve = input('Calculate: ')
            
            if solve == 'exit':
                self.isEnd = True
                break
            
            elif solve == 'ac':
                self.allclear()
                break
            
#             elif solve == 'c':
#                 self.a = self.clear(str(self.a))
            
            else:
                if solve[0] in '+-*/': # string starts with operator
                    solve = str(self.a) + solve
                elif solve[0].isdigit(): # string starts with number, discard previous result
                    pass
                else:
                    print('Invalid operation.')
                    break

                result = int(eval(solve))
                print(result)
                self.a = result

calc = Calculator()
calc.display()

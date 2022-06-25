from termcolor import colored
import os
import time

STRING = "B111C1111BB"
DELAY = .1


def clear(): return os.system('cls')


class TuringMachine:
    def __init__(self, s) -> None:
        self.tape = s
        self.index = 1
        self.state = 'q0'
        self.finish = False

    def toRight(self):
        self.index += 1

    def toLeft(self):
        self.index += -1
        if self.index < 0:
            raise Exception("saa")

    def next(self):
        pass

    def read(self):
        value = self.s[self.index]
        return value

    def write(self, x):
        self.tape[self.index] = x

    def setState(self, x):
        self.state = x

    def run(self):
        while(not self.finish):
            self.next()
            time.sleep(DELAY)

    def print(self):
        s = self.tape
        value = self.tape[self.index]
        state = self.state
        s = ''.join([str(elem) for elem in s])
        print('value: ', value, ', state: ', state)
        print(s[:self.index] + colored(s[self.index], 'red') + s[self.index + 1:])


class MultiplingMachine(TuringMachine):
    def __init__(self, s) -> None:
        super().__init__(s)

    def next(self):
        value = self.tape[self.index]
        state = self.state
        clear()
        self.print()

        if value == '1' and state == 'q0':
            self.write('1')
            self.toRight()
            self.setState('q0')
        elif value == 'C' and state == 'q0':
            self.write('C')
            self.toRight()
            self.setState('q1')
        elif value == '1' and state == 'q1':
            self.write('1')
            self.toRight()
            self.setState('q1')
        elif value == 'B' and state == 'q1':
            self.write('C')
            self.toLeft()
            self.setState('q2')

        elif value == '1' and state == 'q2':
            self.write('1')
            self.toLeft()
            self.setState('q2')

        elif value == 'C' and state == 'q2':
            self.write('C')
            self.toRight()
            self.setState('q3')
        elif value == 'X' and state == 'q3':
            self.write('X')
            self.toRight()
            self.setState('q3')
        elif value == '1' and state == 'q3':
            self.write('X')
            self.toLeft()
            self.setState('q4')
        elif value == 'X' and state == 'q4':
            self.write('X')
            self.toLeft()
            self.setState('q4')
        elif value == 'C' and state == 'q4':
            self.write('C')
            self.toLeft()
            self.setState('q5')

        elif value == 'Y' and state == 'q5':
            self.write('Y')
            self.toLeft()
            self.setState('q5')

        elif value == '1' and state == 'q5':
            self.write('Y')
            self.toRight()
            self.setState('q6')
        elif value == 'Y' and state == 'q6':
            self.write('Y')
            self.toRight()
            self.setState('q6')
        elif value == 'C' and state == 'q6':
            self.write('C')
            self.toRight()
            self.setState('q7')
        elif value == '1' and state == 'q7':
            self.write('1')
            self.toRight()
            self.setState('q7')
        elif value == 'X' and state == 'q7':
            self.write('X')
            self.toRight()
            self.setState('q7')
        elif value == 'C' and state == 'q7':
            self.write('C')
            self.toRight()
            self.setState('q8')
        elif value == '1' and state == 'q8':
            self.write('1')
            self.toRight()
            self.setState('q8')
        elif value == 'B' and state == 'q8':
            self.write('1')
            self.tape.append('B')
            self.toLeft()
            self.setState('q9')
        elif value == '1' and state == 'q9':
            self.write('1')
            self.toLeft()
            self.setState('q9')
        elif value == 'C' and state == 'q9':
            self.write('C')
            self.toLeft()
            self.setState('q10')
        elif value == '1' and state == 'q10':
            self.write('1')
            self.toLeft()
            self.setState('q10')
        elif value == 'X' and state == 'q10':
            self.write('X')
            self.toLeft()
            self.setState('q10')
        elif value == 'C' and state == 'q10':
            self.write('C')
            self.toLeft()
            self.setState('q5')
        elif value == 'B' and state == 'q5':
            self.write('B')
            self.toRight()
            self.setState('q11')
        elif value == 'Y' and state == 'q11':
            self.write('1')
            self.toRight()
            self.setState('q11')
        elif value == 'C' and state == 'q11':
            self.write('C')
            self.toRight()
            self.setState('q3')
        elif value == 'C' and state == 'q3':
            self.write('B')
            self.toRight()
            self.setState('q12')
            print("finish")
            self.finish = True


s = list(STRING)
MultiplingMachine(s).run()
print(s)

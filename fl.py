from mimetypes import init
from operator import index
from termcolor import colored
import os
import time

STRING = "B11111B111C1BB"
DELAY = 0


def clear(): return os.system('cls')


class TuringMachine:
    def __init__(self, s, initialIndex) -> None:
        self.tape = s
        self.index = initialIndex
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
        clear()
        s = self.tape
        value = self.tape[self.index]
        state = self.state
        s = ''.join([str(elem) for elem in s])
        print('value: ', value, ', state: ', state)
        print(s[:self.index] + colored(s[self.index], 'red') + s[self.index + 1:])


class MultiplingMachine(TuringMachine):
    def __init__(self, s, ins) -> None:
        super().__init__(s, ins)

    def next(self):
        value = self.tape[self.index]
        state = self.state
        # self.print()

        if value == '1' and state == 'q0':
            self.write('1')
            self.toRight()
            self.setState('q0')
        elif value == 'C' and state == 'q0':
            self.write('C')
            self.toRight()
            self.setState('q1')
        elif value == 'J' and state == 'q1':
            self.toRight()
        elif (value == '1') and state == 'q1':
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
        elif value == 'J' and state == 'q2':
            self.toLeft()

        elif value == 'C' and state == 'q2':
            self.write('C')
            self.toRight()
            self.setState('q3')
        elif value == 'X' and state == 'q3':
            self.write('X')
            self.toRight()
            self.setState('q3')
        elif value == 'J' and state == 'q3':
            self.toRight()

        elif value == '1' and state == 'q3':
            self.write('X')
            self.toLeft()
            self.setState('q4')
        elif value == 'J' and state == 'q3':
            self.toLeft()
        elif value == 'X' and state == 'q4':
            self.write('X')
            self.toLeft()
            self.setState('q4')
        elif value == 'J' and state == 'q4':
            self.toLeft()
        elif value == 'C' and state == 'q4':
            self.write('C')
            self.toLeft()
            self.setState('q5')
        elif value == 'J' and state == 'q4':
            self.toLeft()

        elif value == 'Y' and state == 'q5':
            self.write('Y')
            self.toLeft()
            self.setState('q5')
        elif value == 'J' and state == 'q5':
            self.toLeft()
        elif value == '1' and state == 'q5':
            self.write('Y')
            self.toRight()
            self.setState('q6')
        elif value == 'J' and state == 'q5':
            self.toRight()
        elif value == 'Y' and state == 'q6':
            self.write('Y')
            self.toRight()
            self.setState('q6')
        elif value == 'J' and state == 'q6':
            self.toRight()
        elif value == 'C' and state == 'q6':
            self.write('C')
            self.toRight()
            self.setState('q7')
        elif value == 'J' and state == 'q6':
            self.toRight()

        elif value == '1' and state == 'q7':
            self.write('1')
            self.toRight()
            self.setState('q7')
        elif value == 'J' and state == 'q7':
            self.toRight()

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
        elif value == 'J' and state == 'q8':
            self.toRight()

        elif value == 'B' and state == 'q8':
            self.write('1')
            self.tape.append('B')
            self.toLeft()
            self.setState('q9')
        elif value == '1' and state == 'q9':
            self.write('1')
            self.toLeft()
            self.setState('q9')
        elif value == 'J' and state == 'q9':
            self.toLeft()

        elif value == 'C' and state == 'q9':
            self.write('C')
            self.toLeft()
            self.setState('q10')
        elif value == '1' and state == 'q10':
            self.write('1')
            self.toLeft()
            self.setState('q10')
        elif value == 'J' and state == 'q10':
            self.toLeft()

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
        elif value == 'J' and state == 'q11':
            self.toRight()

        elif value == 'C' and state == 'q11':
            self.write('C')
            self.toRight()
            self.setState('q3')
        elif value == 'C' and state == 'q3':
            self.write('J')
            self.toLeft()
            self.setState('q12')
        elif value == 'X' and state == 'q12':
            self.write('J')
            self.toLeft()
            self.setState('q12')
        elif value == 'J' and state == 'q12':
            self.toLeft()

        elif value == 'C' and state == 'q12':
            self.setState('q13')
            self.finish = True
            self.tape.append('B')
            self.print()


class X5Machine(TuringMachine):
    def __init__(self, s, ins) -> None:
        super().__init__(s, ins)

    def next(self):
        state = self.state
        value = self.tape[self.index]

        self.print()
        if value == '1' and state == 'q0':
            self.write('1')
            self.toRight()
            self.setState('q0')
        elif value == 'J' and state == 'q0':
            self.toRight()

        elif value == 'B' and state == 'q0':
            self.write('B')
            self.toLeft()
            self.setState('q1')
        elif value == 'X' and state == 'q1':
            self.write('X')
            self.toLeft()
            self.setState('q1')
        elif value == 'J' and state == 'q1':
            self.toLeft()

        elif value == '1' and state == 'q1':
            self.write('X')
            self.toRight()
            self.setState('q2')
        elif value == 'X' and state == 'q2':
            self.write('X')
            self.toRight()
            self.setState('q2')
        elif value == 'J' and state == 'q2':
            self.toRight()

        elif value == 'B' and state == 'q2':
            self.write('B')
            MultiplingMachine(self.tape, self.index + 1).run()
            self.toLeft()
            self.setState('q1')
        elif value == 'B' and state == 'q1':
            self.write('B')
            self.toRight()
            self.setState('q4')
            self.finish = True
            self.print()
            print('finish')


s = list(STRING)
X5Machine(s, 1).run()

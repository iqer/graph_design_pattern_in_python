from abc import ABCMeta, abstractmethod
import abc

class Dispaly(metaclass=ABCMeta):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass
    
    @abstractmethod
    def print(self):
        pass
    
    
    def display(self):
        self.open()
        for i in range(5):
            self.print()
        self.close()


class CharDisplay(Dispaly):
    def __init__(self, ch) -> None:
        self.ch = ch

    def open(self):
        print('<<', end='')

    def print(self):
        print(self.ch, end='')
    
    def close(self):
        print('>>')


class StringDisply(Dispaly):
    def __init__(self, string) -> None:
        self.string = string

    def open(self):
        self.print_line()
    
    def print(self):
        print('|' + self.string + '|')
    
    def close(self):
        self.print_line()
    
    def print_line(self):
        print('+', end='')
        for i in range(len(self.string)):
            print('-', end='')
        print('+')


if __name__ == '__main__':
    d1 = CharDisplay('a')
    d2 = StringDisply('hello, world')
    d3 = '你好, 世界'
    d1.display()
    d2.display()
    d3.display()
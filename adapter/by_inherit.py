class Banner:

    def __init__(self, string) -> None:
        self._string = string

    def show_with_paren(self):
        print(f'({self._string})')
    
    def show_with_aster(self):
        print(f'*{self._string}*')


class PrintBanner(Banner):
    def __init__(self, string) -> None:
        super().__init__(string)

    def print_weak(self):
        self.show_with_paren()
    
    def print_strong(self):
        self.show_with_aster()

    
if __name__ == '__main__':
    p = PrintBanner('Hello')
    p.print_strong()
    p.print_weak()

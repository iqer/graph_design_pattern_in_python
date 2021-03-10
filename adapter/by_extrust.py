class Banner:
    def __init__(self, string) -> None:
        self._string = string

    def show_with_paren(self):
        print(f'({self._string})')
    
    def show_with_aster(self):
        print(f'*{self._string}*')


class PrintBanner:
    def __init__(self, string) -> None:
        self._banner = Banner(string)
    
    def show_weak(self):
        self._banner.show_with_paren()
    
    def show_strong(self):
        self._banner.show_with_aster()


if __name__ == '__main__':
    p = PrintBanner('hello')
    p.show_strong()
    p.show_weak()
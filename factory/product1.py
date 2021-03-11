from abc import ABCMeta, abstractmethod

class Product(metaclass=ABCMeta):

    @abstractmethod
    def use(self):
        pass


class Factory(metaclass=ABCMeta):
    
    def create(self, owner):
        self.product = self.create_product(owner)
        self.register_product(owner)
    
    @abstractmethod
    def create_product(self, owner):
        pass

    @abstractmethod
    def register_product(self, product):
        pass



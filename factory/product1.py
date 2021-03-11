from abc import ABCMeta, abstractmethod

class Product(metaclass=ABCMeta):

    @abstractmethod
    def use(self):
        pass


class Factory(metaclass=ABCMeta):
    
    def create(self, owner):
        self.product = self.create_product(owner)
        self.register_product(self.product)
        return self.product

    @abstractmethod
    def create_product(self, owner):
        pass

    @abstractmethod
    def register_product(self, product):
        pass


class IDCard(Product):
    def __init__(self, owner) -> None:
        print(f'制作{owner}的ID卡')
        self._owner = owner
    
    def use(self):
        print(f'使用{self._owner}的ID卡')

    def get_owner(self):
        return self._owner


class IDCardFactory(Factory):
    def __init__(self) -> None:
        self._owners = []

    def create_product(self, owner):
        return IDCard(owner)

    def register_product(self, product):
        self._owners.append(product.get_owner())
    
    def get_owners(self):
        return self._owners


if __name__ == '__main__':
    factory = IDCardFactory()
    card1 = factory.create('小明')
    card2 = factory.create('小红')
    card3 = factory.create('小刚')
    card1.use()
    card2.use()
    card3.use()

class Burger:
    '''
    This is the instance class that we will return.
    '''
    def __init__(self):
        '''
        Minimal constructor. All these properties will have
        to be set by the builder.
        '''
        self.bun = None
        self.cheese = None
        self.patty = None
    
    def set_bun(self, bun):
        '''
        All the setters of the instance class are as you'd
        expect. The instance class is mostly standard except
        for the minimal constructor.
        '''
        self.bun = bun

    def set_cheese(self, cheese):
        self.cheese = cheese

    def set_patty(self, patty):
        self.patty = patty
    
    def __str__(self):
        return f'{self.bun} {self.cheese} {self.patty}'

class BurgerBuilder:
    '''
    Builder class
    '''
    def __init__(self):
        '''
        Minimal constructor that creates our burger and returns
        and instance of our builder. Which we can build on.
        '''
        self.burger = Burger()
    
    def add_bun(self, bun):
        '''
        Builder method. Sets a property on the instance and
        returns the builder instance to be chained on.
        '''
        self.burger.set_bun(bun)
        return self

    def add_cheese(self, cheese):
        self.burger.set_cheese(cheese)
        return self

    def add_patty(self, patty):
        self.burger.set_patty(patty)
        return self

    def build(self):
        '''
        Build method returns the instance that
        we have been building
        '''
        return self.burger

if __name__ == '__main__':
    vegan_wheat_burger = BurgerBuilder().add_bun('Wheat').add_patty('Vegan').build()
    print(vegan_wheat_burger)

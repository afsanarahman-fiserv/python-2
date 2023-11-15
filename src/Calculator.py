class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result = 0
    
    def add(self):
        self.result = self.a + self.b

    def sub(self):
        self.result = self.a - self.b
    
    def mul(self):
        self.result = self.a * self.b
    
    def div(self):
        self.result = self.a / self.b

    def get_result(self):
        return self.result
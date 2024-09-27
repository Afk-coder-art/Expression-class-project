class Expression:
    def __init__(self, numa, numb, numc):
        self.num1 = numa
        self.num2 = numb
        self.num3 = numc
    def display(self):
        result = self.num1 + self.num2 + self.num3
        print("The result of adding {self.num1}, {self.num2} and {self.num3} is: {result}")

if __name__ == "__main__":
    num1 = (input("Enter your first number: "))
    num2 = (input("Enter your second number: "))
    num3 = (input("Enter your third number: "))
exp = Expression(num1, num2, num3)
exp.display()
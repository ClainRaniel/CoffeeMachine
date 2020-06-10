class CoffeeMachine:

    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def __str__(self):
        return f"""The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee} of coffee beans
{self.cups} of disposable cups
${self.money} of money"""

    def remaining(self):
        print()
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")
        print()

    def enough(self, lst):
        if self.water - lst[0] < 0:
            yield "water"
        if self.milk - lst[1] < 0:
            yield "milk"
        if self.coffee - lst[2] < 0:
            yield "coffee"
        if self.cups - lst[3] < 0:
            yield "cups"

    def buy(self, num):

        quantity = {
            1: [250, 0, 16, 4, 1],
            2: [350, 75, 20, 7, 1],
            3: [200, 100, 12, 6, 1]
        }.get(num, None)

        not_enough = list(self.enough(quantity))

        if not not_enough:
            print("I have enough resources, making you a coffee!")
            self.water -= quantity[0]
            self.milk -= quantity[1]
            self.coffee -= quantity[2]
            self.money += quantity[3]
            self.cups -= quantity[4]

        else:
            things = ", ".join(not_enough)
            print(f"Sorry, not enough {things}!")

    def fill(self):

        self.water += int(input('\nWrite how many ml of water do you want to add: '))
        self.milk += int(input('Write how many ml of milk do you want to add: '))
        self.coffee += int(input('Write how many grams of water do you want to add: '))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add: '))

    def take(self):
        print(f'I gave you ${self.money}')
        self.money -= self.money


obj1 = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    action = input(
        "Write action (buy, fill, take, remaining, exit):\n").lower().strip()
    if action == "exit":

        break

    elif action == "remaining":

        print(obj1)

    elif action == "buy":
        num = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n')
        if num == "back":
            continue
        else:
            obj1.buy(int(num))

    elif action == "fill":
        obj1.fill()

    elif action == "take":

        obj1.take()

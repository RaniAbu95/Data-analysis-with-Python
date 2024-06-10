# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# id: 316396787
# login: abura
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import math
import random

class Shape:
    """A base class representing a geometric shape."""
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass

    def __lt__(self, other):
        """Compare two shapes by their area and return True if self's area is less than other's."""
        return self.area() < other.area()

class Circle(Shape):
    """A class representing a circle."""

    def __init__(self, radius):
        """Create a Circle object with the given radius."""
        if (radius < 0):
            self.radius = 1
        self.radius = radius

    def get_radius(self):
        """Return the radius of the circle."""
        return self.radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate and return the perimeter of the circle."""
        return 2 * math.pi * self.radius

    def __str__(self):
        """Return a string representation of the circle."""
        return f"Circle:radius=[{self.radius}]"


class Rectangle(Shape):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Create a Rectangle object with the given width and height."""
        if (width < 0 or height < 0):
            width = 1
            height = 1
        self.height = height
        self.width = width

    def get_width(self):
        """Return the width of the rectangle."""
        return self.width

    def get_height(self):
        """Return the height of the rectangle."""
        return self.height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"Rectangle:width=[{self.width}],height=[{self.height}]"

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.height * self.width

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.height + self.width)


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, length):
        """Create a Square object with the given length."""
        if (length < 0):
            self.width = 1
            self.height = 1
        self.height = length
        self.width = length

    def get_width(self):
        """Return the width of the square."""
        return self.width

    def get_height(self):
        """Return the height of the square."""
        return self.height

    def __str__(self):
        """Return a string representation of the square."""
        return f"Square:length=[{self.height}]"


class ShapesCollection:
    """A class representing a collection of shapes."""

    def __init__(self):
        """Create a new ShapesCollection object."""
        self.shapes = []
        self.sum = 0

    def __len__(self):
        """Return the number of shapes in the collection."""
        sum = 0
        for a in self.shapes:
            sum += 1
        return sum

    def insert(self, s):
        """Insert a shape into the collection."""
        if not issubclass(type(s), Shape):
            raise ValueError("Only instances of Shape or its subclasses can be inserted.")
        if len(self.shapes) == 0:
            self.shapes.append(s)
        else:
            is_biggest = True
            for index, shape in enumerate(self.shapes):
                if s < shape:
                    self.shapes.insert(index, s)
                    is_biggest = False
                    break
            if is_biggest:
                self.shapes.append(s)
            self.sum += 1

    def __str__(self):
        """Return a string representation of the collection."""
        if not self.shapes:
            return "Shapes collection is empty."
        else:
            to_print = "Shapes in collection:"
            for s in self.shapes:
                to_print += f"\n{s}"
            return to_print

    def biggest_perimeter_diff(self):
        """Return the difference between the perimeters of the two shapes in the collection with the biggest difference
         in perimeter."""
        if len(self.shapes) < 2:
            return 0
        else:
            max_diff = 0
            for i in range(len(self.shapes)):
                for j in range(i + 1, len(self.shapes)):
                    cur_diff = abs(self.shapes[i].perimeter() - self.shapes[j].perimeter())
                    if cur_diff > max_diff:
                        max_diff = cur_diff
            return max_diff

    def same_area_as(self, s):
        """Return a list of shapes in the collection with the same area as the given shape s."""
        same_area_shapes = []
        for shape in self.shapes:
            if shape.area() == s.area():
                same_area_shapes.append(shape)
        return same_area_shapes

    def How_many_quadrilaterals(self):
        """Return the number of squares in the collection."""
        square_count = 0
        for shape in self.shapes:
            if isinstance(shape, Rectangle) and shape.get_width() == shape.get_height():
                square_count += 1
        return square_count

    def __getitem__(self, index):
        """Return the shape at the given index in the collection."""
        return self.shapes[index]

"""This class has the following attributes:
- first_name (string): first name of the person
- last_name (string): last name of the person
- address (string): address of the person
- id (int): identification number of the person

It also has the following methods:
- get_first_name(): returns the first name of the person
- get_last_name(): returns the last name of the person
- get_address(): returns the address of the person
- get_id(): returns the identification number of the person"""
class Person:
    def __init__(self, first_name, last_name, address, id):
        # Check if first/last name contains only letters and id contains only digits
        if not first_name.isalpha() or not last_name.isalpha() or not str(id).isdigit():
            self.__first_name = "Avi"
            self.__last_name="Cohen"
            self.__id = 300010000
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
        self.__id = id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def get_id(self):
        return self.__id

"""This class has the following attributes:
- account_number (int): account number of the bank account
- customer_details (Person object): contains details of the account holder
- account_balance (float): current balance in the account

It also has the following methods:
- str(): returns a string representation of the bank account
- get_account_balance(): returns the current balance of the bank account
- get_account_number(): returns the account number of the bank account
- set_balance(balance): sets the balance of the bank account to the given value"""
class Bank_account:
    def __init__(self, account_number, customer_details, account_balance):
        self.account_number = account_number
        self.customer_details = customer_details
        self.account_balance = account_balance

    def __str__(self):
        return f"Account: {self.account_number}\nName: {self.first_name} {self.last_name}\nBalance: {self.balance}"

    def get_account_balance(self):
        return self.account_balance

    def get_account_number(self):
        return self.account_number

    def set_balance(self, balance):
        self.account_balance = balance



"""This class inherits from the Bank_account class and has the following additional attributes:
- institution_name (string): name of the institution associated with the student account
- p (Person object): contains details of the account holder

It also has the following methods:
- str(): returns a string representation of the student account"""
class Student_account(Bank_account):
    def __init__(self, account_number, first_name, last_name, address, balance, institution_name):
        self.p = Person(first_name, last_name, address, id)
        super().__init__(account_number,self.p, balance)
        self.account_type = "student"
        self.institution_name = institution_name

    def __str__(self):
        return f"Student Account: {self.account_number}\nName: {self.p.get_first_name()} {self.p.get_last_name()}\n" \
               f"Balance: {self.get_account_balance()}"


"""This function allows the user to deposit a certain amount into a bank account. The function takes two arguments:
- accounts (list): a list of Bank_account objects
- account_num (int): the account number of the bank account into which the deposit is to be made

It prompts the user to enter the amount to be deposited, checks if the account exists, adds the amount to the account 
balance, and writes the transaction details to the 'myfile.txt' file."""
def deposit(accounts,account_num):
    amount = int(input("Enter amount to deposit: "))
    account = find_account(account_num,accounts)
    if account:
        account.set_balance(account.get_account_balance() + amount - 5)
        print("Deposit successful.")
    else:
        print("Account not found.")
    with open('myfile.txt', 'a') as f:
        f.write("Deposit<"+str(amount)+">,balance:<" + str(account.get_account_balance()) + ">\n")
        f.flush()

"""This function allows the user to withdraw a certain amount from a bank account. The function takes two arguments:
- accounts (list): a list of Bank_account objects
- account_num (int): the account number of the bank account from which the withdrawal is to be made

It prompts the user to enter the amount to be withdrawn, checks if the account exists, checks if the account has 
sufficient balance, deducts the amount from the account balance, and writes the transaction details to the 'myfile.txt' 
file.
"""
def withdraw(accounts,account_num):
    oper = "Withdraw"
    amount = int(input("Enter amount to withdraw: "))
    account = find_account(account_num,accounts)
    if account:
        if account.get_account_balance() >= amount:
            account.set_balance(account.get_account_balance() - amount - 5)
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")
    with open('myfile.txt', 'a') as f:
        f.write("Withdraw<"+str(amount)+">,balance:<" + str(account.get_account_balance()) + ">\n")
        f.flush()


"""This function takes the account number and the list of Bank_account objects as arguments and returns the Bank_account
object with the given account number.
"""
def find_account(account_num,accounts):
    for account in accounts:
        if account.get_account_number() == account_num:
            return account
    return None
"""This function takes a Bank_account object as an argument and prints its string representation."""
def print_account(a):
    print(str(a))
"""This function reads the transaction history from the 'myfile.txt' file and prints it to the console."""
def print_history():
    filename = "myfile.txt"
    with open(filename, "r") as f:
        contents = f.read()
        print(contents)


"""This function allows the user to create a new bank account. The function takes a list of Bank_account objects as an
argument. It prompts the user to enter details such as first name, last name, address, account balance, and account type.
It generates a random account number, creates a new Bank_account or Student_account object based on the account type,
appends the object to"""
def create_account(accounts):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    address = input("Enter address: ")
    balance = int(input("Enter starting balance: "))
    account_type = input("Enter account type (regular/student): ")
    # Generate a random number between 0 and 1000
    random_number = random.randint(0, 1000)
    if account_type.lower() == "student":
        institution = input("Enter institution: ")
        account = Student_account(random_number, first_name, last_name, address, balance, institution)
    else:
        p = Person(first_name,last_name,address,id)
        account = Bank_account(random_number, p, balance)
    accounts.append(account)
    with open('myfile.txt', 'w') as f:
        f.write("New account,balance:<"+str(balance)+">\n")
        f.flush()
        
"""MAIN FUNC THAT CONTROLS THE TESTS"""
def main():

    #Q1 TESTS
    c = Circle(5)
    r = Rectangle(10, 10)
    s = Square(10)
    sh = ShapesCollection()
    sh.insert(c)
    sh.insert(r)
    sh.insert(s)
    print("biggest_perimeter_diff: "+str(sh.biggest_perimeter_diff()))
    print("same_area_as: "+str(sh.same_area_as(s)))
    print("How_many_quadrilaterals(): "+str(sh.How_many_quadrilaterals()))
    print(str(sh))
    print(sh[0])

    #Q2 TESTS
    accounts = []
    create_account(accounts)
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Print\n4. Print History\n5. Exit")
        choice = input("Enter choice: ")
        toPrint=""
        if choice == "1":
            deposit(accounts,accounts[0].get_account_number())
        elif choice == "2":
            withdraw(accounts,accounts[0].get_account_number())
        elif choice == "3":
            print_account(accounts[0])
        elif choice == "4":
            print_history()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
main()



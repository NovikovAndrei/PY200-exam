import hashlib
import re
import random


class IdCounter:
    __id = 0

    def __init__(self):
        self._id = IdCounter.__id
        IdCounter.__id += 1

    def get_id(self):
        return self._id


class Password:

    def __init__(self, password):
        self.password = password
        self.is_valid_password()

    def get(self):
        return hashlib.sha256(self.password.encode()).hexdigest()

    def is_valid_password(self):
        if len(self.password) < 8:
            raise ValueError("Длина пароля должна быть не менее 8 символов")
        if not bool(re.search(r'[0-9]', self.password)):
            raise ValueError("В пароле должны быть цифры")
        if not bool(re.search(r'[a-zA-Z]', self.password)):
            raise ValueError("В пароле должны быть буквы")
        return "пароль валиден"


class Product(IdCounter):
    __id = 0

    def __init__(self, name, price, rating):
        super().__init__()
        self._id = Product.__id
        Product.__id += 1
        self._name = name
        self.is_valid_name()
        self._price = price
        self.is_valid_price()
        self._rating = float(rating)
        self.is_valid_rating(self._rating)

    @property
    def name(self):
        return self._name

    def is_valid_name(self):
        if not isinstance(self._name, str):
            raise TypeError("Имя может быть только строкой")
        return "Имя валидно"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self.is_valid_price()
        self._price = new_price

    def is_valid_price(self):
        if not isinstance(self.price, (int, float)):
            raise TypeError("Цена может быть только числом")
        if self.price <= 0:
            raise ValueError("Цена должна быть больше нуля")
        return "Цена валидна"

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        self.is_valid_rating(new_rating)
        self._rating = float(new_rating)

    @classmethod
    def is_valid_rating(cls, rating):
        if not isinstance(rating, (int, float)):
            raise TypeError("Рейтинг может быть только числом")
        if not 1 <= rating <= 5:
            raise ValueError("Рейтинг должен быть в диапазоне 1-5")
        return "Рейтинг Валиден"

    @staticmethod
    def generate_product():
        name = random.choice(open("data.txt", "r", encoding="utf8").read().split('\n'))
        price = round(random.uniform(100, 1000), 2)
        rating = round(random.uniform(1, 5), 2)
        return Product(name, price, rating)

    def __repr__(self):
        return f"{__class__.__name__}(name={self._name!r}, price={self.price}, rating={self.rating})"

    def __str__(self):
        return f"{self.get_id()}_{self.name}"


class Cart:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)

    def del_product(self, product):
        self.cart.remove(product)

    def __str__(self):
        return f"{self.cart}"


class User(IdCounter):
    __id = 0

    def __init__(self, username, password):
        super().__init__()
        self._username = username
        self.is_valid_username(username)
        self.__password = Password(password).get()
        self._cart = Cart()

    @property
    def cart(self):
        return self._cart

    @property
    def username(self):
        return self._username

    @classmethod
    def is_valid_username(cls, username):
        if not isinstance(username, str):
            raise TypeError("Имя пользователя может быть только типа str")
        if len(username) > 8:
            raise ValueError("Длина имени пользователя должна быть не больше 8-ми знаков")
        return "Имя пользователя валидно"

    def __str__(self):
        return f"ID={self.get_id()}, Имя пользователя:{self._username}, Пароль:*Password1*"

    def __repr__(self):
        return f"{__class__.__name__}(username={self._username!r}, password=*Password1*)"


class Store(Cart):
    def __init__(self):
        super().__init__()
        self.users = {}

    def authenticate(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        self.users[username] = {'info': User(username, password).__str__(), 'cart': Cart().cart}
        print(f"Пользователь {username} создан.")

    def check_cart(self, username):
        if len(self.users[username]['cart']) == 0:
            return "Корзина пуста"
        else:
            current_cart = [i.name for i in self.users[username]['cart']]
        return f"В вашей корзине: {current_cart}"

    def add_random_prod(self, username):
        random_product = Product.generate_product()
        self.users[username]['cart'].append(random_product)
        print(f"{username}, Вы добавили в корзину {random_product}")


if __name__ == "__main__":
    test_product = Product("test_product", 999, 3.33)
    store1 = Store()
    store1.authenticate()
    print(store1.users["client1"])
    print(store1.check_cart("client1"))
    store1.add_random_prod("client1")
    store1.add_random_prod("client1")
    store1.add_random_prod("client1")
    store1.add_product("test_product")
    print(store1.check_cart("client1"))

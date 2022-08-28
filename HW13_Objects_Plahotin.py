# Task 1

class Automobile:
    def __init__(self, model, year, brand, engine_volume, color, price):
        self.__model = 'tricycle'
        self.__year = 1886
        self.__brand = 'Benz'
        self.__engine_volume = 0
        self.__color = ''
        self.__price = 0

        self.set_model(model)
        self.set_year(year)
        self.set_brand(brand)
        self.set_engine_volume(engine_volume)
        self.set_color(color)
        self.set_price(price)

    def set_model(self, model: str):
        self.__model = model

    def get_model(self):
        return self.__model

    def set_year(self, year):
        if 1886 < year < 2023:
            self.__year = year
        else:
            self.__model = "DeLorean"
            self.__year = year

    def get_year(self):
        return self.__year

    def set_brand(self, brand):
        if 1886 < self.__year < 2023:
            self.__brand = brand
        else:
            self.__brand = 'DMC'

    def get_brand(self):
        return self.__brand

    def set_engine_volume(self, engine_volume):
        if engine_volume >= 0:
            self.__engine_volume = engine_volume
        else:
            self.__engine_volume = 'bicycle'

    def get_engine_volume(self):
        return self.__engine_volume

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_price(self, price):
        if str(price).isdigit() > 0:
            self.__price = price
        else:
            self.__price = 'Free sale'

    def get_price(self):
        return self.__price

    def info(self):
        return {'model': self.__model, 'year': self.__year, 'brand': self.__brand,
                'engine volume': self.__engine_volume, 'color': self.__color, 'price': self.__price}

    def __str__(self):
        return f'Model: {self.__model}\nYear: {self.__year}\nBrand: {self.__brand}\n' \
               f'Engine volume: {self.__engine_volume}\nColor: {self.__color}\nPrice: {self.__price}'


x = Automobile('BMW', 3000, 'i1', 3.0, 'red', -2000)
x.set_price(3000)
print(x)
y = Automobile('Korito', 2022, 'Ocinkovanoe', 0, 'Sriblo', 5000)
print(y)


# Task 2

class Book:
    def __init__(self, name, year, publisher, genre, author, price):
        self.__name = 'Bible'
        self.__year = 0
        self.__publisher = 'Magi'
        self.__genre = 'education'
        self.__author = 'Jesus'
        self.__price = 0

        self.set_name(name)
        self.set_year(year)
        self.set_publisher(publisher)
        self.set_genre(genre)
        self.set_author(author)
        self.set_price(price)

    def set_name(self, name):
        self.__name = name.capitalize()

    def get_name(self):
        return self.__name

    def set_year(self, year):
        self.__year = year

    def get_year(self):
        return self.__year

    def set_publisher(self, publisher):
        self.__publisher = publisher

    def get_publisher(self):
        return self.__publisher

    def set_genre(self, genre):
        self.__genre = genre

    def get_genre(self):
        return self.__genre

    def set_author(self, author):
        self.__author = author.capitalize()

    def get_author(self):
        return self.__author

    def set_price(self, price):
        if str(price).isdigit() > 0:
            self.__price = price
        else:
            self.__price = 'Free sale'

    def get_price(self):
        return self.__price

    def info(self):
        return {'name': self.__name, 'year': self.__year, 'publisher': self.__publisher,
                'genre': self.__genre, 'author': self.__author, 'price': self.__price}

    def __str__(self):
        return f'Book name: {self.__name}\nYear: {self.__year}\nPublisher: {self.__publisher}\n' \
               f'Book genre: {self.__genre}\nAuthor name: {self.__author}\nPrice: {self.__price}'


# Task 3

class Stadium:
    def __init__(self, name, open_date, country, city, capacity):
        self.__name = ''
        self.__open_date = ''
        self.__country = ''
        self.__city = ''
        self.__capacity = 0

        self.set_name(name)
        self.set_open_date(open_date)
        self.set_country(country)
        self.set_city(city)
        self.set_capacity(capacity)

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_open_date(self, open_date):
        self.__open_date = open_date

    def get_open_date(self):
        return self.__open_date

    def set_country(self, country):
        self.__country = country.capitalize()

    def get_country(self):
        return self.__country

    def set_city(self, city):
        self.__city = city.capitalize()

    def get_city(self):
        return self.__city

    def set_capacity(self, capacity):
        if capacity < 0:
            self.__capacity = 0
        else:
            self.__capacity = capacity

    def get_capacity(self):
        return self.__capacity

    def info(self):
        return {'name': self.__name, 'date': self.__open_date, 'country': self.__country,
                'city': self.__city, 'capacity': self.__capacity}

    def __str__(self):
        return f'Stadium name: {self.__name}\nOpen date: {self.__open_date}\nCountry: {self.__country}\n' \
               f'City: {self.__city}\nCapacity: {self.__capacity}'

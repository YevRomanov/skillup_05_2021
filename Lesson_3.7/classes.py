################################################
#################### Task 1 ####################                    
################################################
# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
# название модели, год выпуска, производителя, объем двигателя, цвет машины, цену.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте
# доступ к отдельным полям через методы класса.
# 
# 
class Car:
    def __init__(self, model, year, fabricator, engine, color, price):
        self.model = model
        self.year = year
        self.fabricator = fabricator
        self.engine = engine
        self.color = color
        self.price = price

    def get_car_name(self):
        return f"Model {self.model}"

    def get_car_info(self):
        return f"Year of production is {self.year}, fabricator: {self.fabricator}, engine {self.engine}, color {self.color}"

    def get_car_price(self):
        return f"Car's prise is {self.price}"

bmw = Car(
    model = "M8",
    year = 2021,
    fabricator = "bmw_company",
    engine = "5.0",
    color = "dark_blue",
    price = "180000 $"
    )

audi = Car(
    model = "RS7",
    year = 2021,
    fabricator = "audi_company",
    engine = 5.5,
    color = "ultraviolet",
    price = "176000 $" 
    )

print("If your car is BMW:")
print(bmw.get_car_name())
print(bmw.get_car_info())   
print(bmw.get_car_price())     

print("If your car is AUDI:")
print(audi.get_car_name())
print(audi.get_car_info())   
print(audi.get_car_price())    
# 
# 
# If your car is BMW:
# Model M8
# Year of production is 2021, fabricator: bmw_company, engine 5.0, color dark_blue
# Car's prise is 180000 $
# If your car is AUDI:
# Model RS7
# Year of production is 2021, fabricator: audi_company, engine 5.5, color ultraviolet
# Car's prise is 176000 $
# 
#  
# 
# 
################################################
#################### Task 2 ####################                    
################################################
# Реализуйте класс «Книга». Необходимо хранить в полях класса:
# название книги, год выпуска, издателя, жанр, автора, цену. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
# 
# 





class Car:
    #this is all the cars attributes
    def __init__(self):
        self.model_year = 0
        self.purchase_price = 0
        self.current_value = 0
    # this calculates the depreciation of the car
    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
        # Car depreciation formula
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)
    #this prints the relevent info of the car
    def print_info(self):
        print("Car's information:\n   Model year: {}\n   Purchase price: {}\n   Current value: {}"
        .format(year,price,self.current_value))

# this gets the inputs for the program
if __name__ == "__main__":    
    year = int(input()) 
    price = int(input())
    current_year = int(input())
# this is the order the program needs to run in    
    my_car = Car()
    my_car.model_year = year
    my_car.purchase_price = price
    my_car.calc_current_value(current_year)
    my_car.print_info()

# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 22:49:19 2023

@author: huyng
"""


class Car:
    def __init__(self, make, model, color, year, mileage):
        self.make=make
        self.model=model
        self.color=color
        self.year= year
        self.mileage=mileage
        
    def __str__(self):
        return ('\n\t Make   : %s\n\t Model  : %s\n\t Color  : %s\n\t Year   : %d\n\t Mileage: %d'
                %(self.make, self.model, self.color, self.year, self.mileage))
        
    
            
class Car_inventory:
    def __init__(self):
        self.cars= [Car('Honda','CRZ', 'Grey', 2015, 100000), Car('Toyota','Camry', 'Grey', 2015, 20000), 
                    Car('Kia','Soul', 'Green', 2015, 40000), Car('Toyota','Corolla ', 'Silver', 2015, 200000),
                    Car('Honda','CRZ', 'Black', 2018, 100000), Car('Toyota','RAV4', 'Pink', 2020, 20000), 
                    Car('Kia','Soul', 'Blue', 2019, 40000), Car('Toyota','Corolla ', 'Silver', 2015, 200000),
                    Car('Honda','CRV', 'Black', 2010, 400000), Car('Toyota','Highlander', 'White', 2018, 80000),
                    Car('Honda','CRZ', 'Black', 2018, 100000), Car('Toyota','RAV4', 'Yellow', 2021, 40000), 
                    Car('Dodge','Charger', 'Black', 2023, 4000), Car('Toyota','Corolla ', 'White', 2012, 300000)]
        self.mainLoop()
        
    def createCarfrominput (self):                   
        make = input('Please enter the make of the car: ')
        model = input('Please enter the model of the car: ')
        color = input('Please enter the color of the car: ')
        year = None
        while year is None:
            tempyear= None
            try:
                tempyear = int(input('Please enter the year of the car: '))
                if 1900 <= tempyear < 9999:
                    year = tempyear
                else:
                    print('Please print a year between 1900 and beyond.')
            except ValueError:
                print ('Please enter a valid numerical value.')
        mileage = None
        while mileage is None:
            tempmileage = None
            try:
                tempmileage = int(input('Please enter the mileage of the car: '))
                if tempmileage >= 0:
                    mileage = tempmileage
                else:
                    print ('Please entere a positive integer.')
            except ValueError:
                print ('Please enter a valid numerical value.')
        
        car = Car(make, model, color, year, mileage)
        return car
        
    def validIndex (self, prompt):
        index = None
        while index is None:
            tempindex= None
            try:
                tempindex = int(input(prompt))
                if 0 < tempindex < len(self.cars):
                    index = tempindex
                else:
                    print('Please enter an existing position.')
            except ValueError:
                print ('Please enter a valid numerical value.')
        return index
        
    def addCar (self):
        print ('- - - - - - - A D D   C A R - - - - - - -')
        print ('Currently, there are ' + str(len(self.cars)) + " cars in inventory.\n" +
               "Please enter the following information to add a car.")
        car= self.createCarfrominput()
        self.cars.append(car)
        
    def removeCar(self):
        print ('- - - - - - - R E M O V E   C A R - - - - - - -')
        print ('Currently, there are ' + str(len(self.cars)) + " cars in inventory.\n"
               'Enter a value from 0 to ' + str(len(self.cars)-1) + 
               ", with the first car starting at position 0.")
        index = (self.validIndex('Remove car at the position...:')+1)
        carToremove = self.cars[index]
        self.cars.remove(carToremove)
        
        
        # try:
        #     if len(self.cars) == 0:
        #         print ('There is nothing in inventory')
        #     else:
        #         index = int(input('Remove the position...:'))
        #         carToremove = self.cars[index]
        #         self.cars.remove(carToremove)
        # except IndexError:
        #     print ('Item does not exist.')
        # except ValueError:
        #     print ('Please enter a valid number.')
                
    def updateCar(self):
        print ('- - - - - - - U P D A T E   C A R - - - - - - -')
        print ('Currently, there are ' + str(len(self.cars)) + " cars in inventory.\n"
               'Enter a value from 0 to ' + str(len(self.cars)-1) + 
               ", with first car starting at position 0.")
        index = self.validIndex('Update car at the position...:')
        self.cars[index] = self.createCarfrominput()
        
        
        # try:
        #     if len(self.cars) == 0:
        #         print ('There is nothing in inventory')
        #     else:
        #         index = int(input('Update car at the position...:'))
        #         if 0 < index < len(self.cars): 
        #             self.cars[index] = self.createCarfrominput()
        #         else:
        #             print ('Please enter an existing position.')
        # except IndexError:
        #     print ('Item does not exist.')
        # except ValueError:
        #     print ('Please enter a valid number.')
    
    def viewInventory(self):
        if len(self.cars) == 0:
            print ('Inventory is empty.')
        else: 
            print ('- - - - - - - I N V E N T O R Y - - - - - - -\n')
            print ('Currently, there are ' + str(len(self.cars)) + " cars in inventory.\n")
            for pos,car in enumerate(self.cars):
                print (str(pos) + " : " + str(car) + "\n")
            print ('- - - - - - - I N V E N T O R Y - - - - - - -\n')

    def mainLoop (self):
        selection = 0
        while selection != '5':
            print()
            print (' 1 = Add a car')
            print (' 2 = Remove a car')
            print (' 3 = Update a car')
            print (' 4 = View inventory')
            print (' 5 = End') 
            
            selection = input('Please enter an option from 1 to 5...:')
            print()
            if selection == '1':
                self.addCar()
            elif selection == '2':
                self.removeCar()
            elif selection == '3':
                self.updateCar()
            elif selection == '4':
                self.viewInventory()
            else:
                break
        

Car_inventory()

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
        return ('Make: %s, Mo0del: %s, Color: %s, Year: %d, Mileage: %d.'%(self.make, self.model, self.color, self.year, self.mileage))
        
    
            
class Car_inventory:
    def __init__(self):
        self.cars= [Car('Honda','CRZ', 'Grey', 2015, 2000), Car('Toyota','Camry', 'Grey', 2015, 20000), 
                    Car('Kia','Soul', 'Green', 2015, 40000)]
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
        print ('- - - - - A D D   C A R - - - - -')
        car= self.createCarfrominput()
        self.cars.append(car)
        
    def removeCar(self):
        print ('- - - - - R E M O V E   C A R - - - - -')
        index = self.validIndex('Remove car at the position...:')
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
        print ('- - - - - U P D A T E   C A R - - - - -')
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
            print ('- - - - - I N V E N T O R Y - - - - -\n')
            for pos,car in enumerate(self.cars):
                print (str(pos) + " : " + str(car) + "\n")


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

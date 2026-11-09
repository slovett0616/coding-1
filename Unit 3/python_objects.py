# Python objects are digital representations of things 
# that can interact with one another

# Objects are collections of data that we use to 
# characterize things

# Example - A car is a object/ "Thing"
# characteristics of a car: engine, tires, battery, seats
# color, model, doors

# object Syntax
# when we want to make an object, we need to use a class
# keyword = object maker

# the class name ALWAYS is capitalized / Pascal Case

# we ALWAYS have to have def __init__(self)
# this code tells the computer how the object works and what it does
class RaceCar():
    def __init__(self):
        # Attributes - Characteristic data. data used to describe our 
        # object. This data can be changed or interacted with.
        tint = 50.0,
        color = "Blue",
        tireSize = 40,
        speedMax= 400,
        gasTank = 100

        # Methods - Functions (*that exist inside of a object)
        # These functions are designed EXCLUSIVELY for the object
        # they exist in.
        # Methods represent the behavior of the object
        
        def gasSystem():
            # need to have gas in order for car to run in game
            # as you drive more gas tank gets lower
            # if gastank == 0 game over
        
        def customize_color():
            # if unlock x change color to red
            # elif unlock y change color to green
        
        def customize_tires():
            # if user selects x change tire to 20

        def boost_Turbo():
            # increase speed value by 200
        

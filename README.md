ASSIGNMENT FOR SINGLETON

name it logger.py

create a Logger singleton class. 

It should create a file named 'logfile_[date_time].log' where [date_time] should be the date and time when it was created, with Year_month_day_hour_minute_second (example: logfile_2017_03_15_17_27_55.log)

create a log(message) method for the Logger class what saves the string message to the file

make some tests where you use the logger class


ASSIGNMENT FOR FACTORY

name it toy_factory.py

create a Toy Factory! Your factory should be able to produce three kind of toys:
- boat
- racecar
- space ship

the machine what makes the toys doesn't really care what toy it makes but it expects that the toy object it is creating has three methods what it will use to make the toy:
- prepare()
- make()
- package()

the methods in the Toy classes should print (log) what it is doing and the type of the toy (for ex. the boat's prepare should write 'preparing boat')

the ToyFactory class should have a make_toy(toy_name) method where the toy should be instantiated based on the toy_name. 

The prepare / make / package() methods of the created toy object should be called, in this order.

Your task is to create everything what is needed to fulfill the requirements. 
Also make tests for it so we can see that it's working. 
You may also use your Logger class for logging purposes. :)


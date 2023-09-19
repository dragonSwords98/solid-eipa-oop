# ASSIGNMENT: use OOP on this smart home class
# Inheritance
# Encapsulation
# Abstraction
# Polymorphism

# ASSIGNMENT:
# write a basic monolithic code class, then apply SOLID principles to it

class Appliance:
  name = ''
  power = False

  def __init__(self, name):
    self.name = name
    print('The name of this appliance is '.format(self.name))

  def cook(self, time, temperature):
    if (self.power):
      print('{} cooking for {} seconds at {} degrees F'.format(self.name, time, temperature))

  def power(self, on=True):
    self.power = on


class Oven(Appliance):
  def broil(self, time):
    if self.power and self.__checkWarranty():
      print('{} broiling for {} seconds'.format(self.name, time))

  def cook(self, time, temperature, light):
    if light:
      self.light = True
    if self.power:
      print('{} cooking for {} seconds at {} degrees F with the light set on as {}'.format(self.name, time, temperature, light))

  def __checkWarranty():
    # for simplicity sakes...
    return True


class Microwave(Appliance):
  def ding(self, time, intensity):
    if (self.power):
      print('{} microwaving something for {} seconds at {} intensity'.format(self.name, time, intensity))


# Appliance is an abstraction class for Oven and Microwave, allowing both classes to inherit cook and share methods and structure
# Oven and Microwave _inherit_ Appliance

# __check warranty is an example of an encapsulation, as this method is private and its access is only allowed thru methods called within Oven
# encapsulation also involves the idea of tucking unneeded variables and logic into modules and 'sub functions' so it is self-contained and not exposed outside those
# methods

# polymorphism is like the cook method in Oven, where it doesn't 'cook' the same way as the other inheriting classes


#S ingle Responsibility - each class here has only a single responsibility. Lets say we had an airfryer/oven, then it would be breaking that principle
#O pen-closed Principle - each class here is open to be extended by more methods, but closed to being modified to do something else. its more so creating unchangables rather than deciding what is changeable
#L iskov Principle - subclasses here are substitutable to their base class Appliance. Oven's cook method does not violate Liskov because it is not settings values that is not supposed to
# in the base class. Lets say Oven.cook() modified self.power, then that is a violation, because tests written for Oven.cook() will now not apply correctly if Oven.cook() was used in a test for Appliance.cook() because
# power would be modified unexpectedly by Oven's cook(), which isn't done in Appliance's cook()
#I nterface Segregation Principle - basically implies do many interfaces for specific clients / templates that only use what you need and dont take what you dont use; a generic interface would violate this, because sometimes in some cases
# it will not use certain things. that's a violation
#D ependency Inversion - classes should depend on interfaces or abstract classes, never depend on concrete classes and functions.

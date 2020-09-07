'''
Goals:
-Have more options
-Make code much more clean
'''

class Temperature:
  def __init__(self, degrees, kind):
    self.degrees = degrees
    self.kind = kind
  def input(self):
    Player_input = int(input("How many degrees?"))
    self.degrees = Player_input
  def Repeat():
    Re1 = input("Do you want to convert again? (Y) or (N)")
    if Re1 == "Y" or Re1 == "y":
      Setup()
    else:
      return None

class Fahrenheit(Temperature):
  def __init__(self, degrees, kind):
    super().__init__(degrees, kind) 
  def F_to_C(self):
    self.input() 
    # Fahrenheit to Celsius 
    x = (((self.degrees -32) * 5) /9)
    #using an F string
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'
    self.Repeat()
  def F_to_K(self):
    self.input()
    # Fahrenheit to Kelvin 
    x = ((((self.degrees-32)*5)/9)+273.15)
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'
    self.Repeat()
  def F_to_R(self):
    self.input()
    x = self.degrees + 459.67
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'
    self.Repeat()

class Celsius(Temperature):
  def __init__(self, degrees, kind):
    super().__init__(degrees, kind)
  def C_to_F(self):
    self.input()
    # Celsius to Fahrenheit
    x = (((self.degrees / 5) * 9)  + 32)
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'
    self.Repeat()
  def C_to_K(self):
    self.input()
    # Celsius to Kelvin 
    x = ( self.degrees + 273.15)
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'
    self.Repeat()
  def C_to_R(self):
    self.input()
    x = ((self.degrees * 9/5)+491.67)
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'
    self.Repeat()

class Kelvin(Temperature):
  def __init__(self, degrees, kind):
    super().__init__(degrees, kind)
  def K_to_F(self):
    self.input()
    # Kelvin to Fahrenheit
    x = ((9/5 * (self.degrees-273.15))+32) 
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'
    self.Repeat()
  def K_to_C(self):
    # Kelvin to Celsius
    self.input()
    x = (self.degrees - 273.15)
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'
    self.Repeat()
  def K_to_R(self):
    # Kelvin to Rankine
    self.input()
    x = self.degrees * 1.8
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'
    self.Repeat()

class Rankine(Temperature):
  def __init__(self, degrees, kind):
    super().__init__(degrees, kind)
  def R_to_F(self):
    # Rankine to Fahrenheit
    self.input()
    x = (self.degrees - 459.67)
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'
    self.Repeat()
  def R_to_C(self):
    # Rankine to Celsius 
    self.input()
    x = ((self.degrees - 459.67)*5/9)
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'
    self.Repeat()
  def R_to_K(self):
    # Rankine to Kelvin 
    self.input()
    x = (self.degrees *5/9)
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'
    self.Repeat()

#I like to call the functions that display the outputs Setup() but you can call it whatever you want. 
def Setup():
  print("Welcome to the Temperature converter!")
  Response = """What conversion do you want to do? \nFahrenheit to Celsius (1) Fahrenheit to Kelvin (2) Fahrenheit to Rankine(3) 
  \nCelsius to Fahrenheit (4) Celsius to Kelvin (5) Celsius to Rankine (6) \nKelvin to Fahrenheit (7) Kelvin to Celsius (8) Kelvin to Rankine (9) 
  \nRankine to Celsius (10) \nRankine to Fahrenheit (11) Rankine to Kelvin (12)
  """
  print(Response)
  #Temp1 is an instance of the Fahrenheit class, Temp2 is an instance of the Celsius class, and so on.
  Temp1 = Fahrenheit(0, "Fahrenheit")
  Temp2 = Celsius(0, "Celsius")
  Temp3 = Kelvin(0, "Kelvin")
  Temp4 = Rankine(0, "Rankine")
  while True:
   try:
    #using a dictionary to reduce the amount of if statements.
    options ={
    "1":Temp1.F_to_C, "2":Temp1.F_to_K, "3":Temp1.F_to_R, "4":Temp2.C_to_F, "5":Temp2.C_to_K, 
    "6":Temp2.C_to_R, "7":Temp3.K_to_F, "8":Temp3.K_to_C, "9":Temp3.K_to_R
    "10":Temp4.R_to_C, "11":Temp4.R_to_F, "12":Temp4.R_to_K 
    }  
    choice = input("Select the number of the conversion here: ")
    print(options[choice]())
    repeat = Temperature.Repeat()
    print(repeat)
    break
   except KeyError:
    print("Sorry, please type in the number of the conversion again")
    continue   
Setup()

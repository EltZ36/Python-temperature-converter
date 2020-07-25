class Temperature:
  def __init__(self, degrees, kind):
    self.degrees = degrees
    self.kind = kind
  
class Fahrenheit(Temperature):
  def __init__(self, degrees, kind):
    super().__init__(degrees, kind) 
  def __repr__(self):
    Player_input = int(input("How many degrees?"))
    self.degrees = Player_input 
    x = (((self.degrees -32) * 5) /9)
    #using an F string
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'

class Celsius(Temperature):
  def __init__(self, degrees, kind):
    super().__init__(degrees, kind)
  def __repr__(self):
    Player_input = int(input("How many degrees?"))
    self.degrees = Player_input 
    # Celsius to Fahrenheit
    x = (((self.degrees / 5) * 9)  + 32)
    return f'{self.degrees} degrees {self.kind} converts to {x} degrees.'
  
class Kelvin(Temperature):
  def __init__(self, degrees, kind):
    super().__init__(degrees, kind)
  def __repr__(self):
    Player_input = int(input("How many degrees?"))
    self.degrees = Player_input 
    # Kelvin to Fahrenheit
    x = ((9/5 * self.degrees)+32) 
    return f'{self.degrees} degrees {self.kind} converts to degrees.'

Temp1 = Fahrenheit(15, "Fahrenheit")
print(Temp1)
  
def Setup():
  print("Welcome to the Temperature converter!")
  Rep = int(input("What conversion do you want to do? Fahrenheit to Celsius (1), Celsius to Fahrenheit (2), or Celsius to Kelvin (3)?")
  if Rep == 1:
   D1 = Fahrenheit.degrees()
   F = Fahrenheit(D1, "Fahrenheit")
   print(F)
   Repeat()         
  elif Rep == 2:
   C = Celsius(16, "Centigrade")
   print(C)
   Repeat()
  elif Rep == 3:
   K = Kelvin(17, "Kelvin")
   print(K)
   Repeat()         
  else:
    Setup()
Setup()

def Repeat():
 Re1 = input("Do you want to convert again? (Y) or (N)")
 if Re1 == Y:
   Setup()
 else:
   Return None

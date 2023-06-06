### Classes ###

class MyEmptyPerson:
  pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
  def __init__(self, name, surname):
    self.nameee = name
    self.surnameee = surname

my_person = Person("Guillermo", "Garzón")
print(my_person.nameee)
print(my_person.surnameee)
print(f"{my_person.nameee} {my_person.surnameee}")

class Person:
  def __init__(self, name, surname, alias="Sin alias"):
    self.full_name = f"{name} {surname} ({alias})"
    self.__name = name # Propiedad Privada

  def get_name (self):
    return self.__name

  def walk (self):
    print(f"{self.full_name} Está caminando")

my_person = Person("Guillermo", "Garzón")
print(my_person.full_name)
print(my_person.get_name() )
my_person.walk()

my_other_person = Person("Guillermo", "Garzón", "Guille")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hector de León (el loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)
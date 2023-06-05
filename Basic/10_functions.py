### Functions ###

def my_function ():
  print("Esto es una función")

my_function ()  
my_function ()  

def sum_two_values ( first_value, second_value ):
  print(first_value + second_value)

sum_two_values(10, 30)
sum_two_values(10384, 12374.34)
sum_two_values("5", "3")

def sum_two_values_with_return ( first_value, second_value ):
  my_sum = first_value + second_value
  return my_sum

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name (name, surname):
  print(f"{name} {surname}")

print_name(surname = "Garzón", name = "Guillermo")

def print_name_with_default (name, surname, alias = "Sin alias"):
  print(f"{name} {surname} {alias}")

print_name_with_default("Guillermo", "Garzón")
print_name_with_default("Guillermo", "Garzón", "Guille")

def print_upper_texts (*texts):
  for text in texts:
    print(text.upper())

print_upper_texts("Hola", "Python", "Guille")
print_upper_texts("Hola")
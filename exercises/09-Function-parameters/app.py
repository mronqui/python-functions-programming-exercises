# Your code goes here:
def render_person(nombre, fecha, ojos, edad, sexo):
    return nombre + ' is a ' + str(edad) + ' years old ' + sexo + ' born in ' + fecha + ' with ' + ojos + ' eyes'


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))
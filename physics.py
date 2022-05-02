# return statement is necessary to retain the outcome of the function
from operator import ge
from webbrowser import get


def f_to_c(f_temp):
    return (f_temp - 32)*(5/9)
print(f_to_c(33))

f100_in_celcsius = f_to_c(100)
print(f100_in_celcsius)

def c_to_f(c_temp):
    return (c_temp * (9/5)) + 32
print(c_to_f(2))
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


def get_force(mass, acceleration):
    return mass * acceleration
train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass, c = 3*10**8):
    return mass * (c**2)
bomb_energy = get_energy(bomb_mass, )
print(bomb_energy)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

def get_work(accerlation, distance, mass):
    return get_force(mass, accerlation) * distance
force = get_work(train_acceleration, train_distance, train_mass)
print(force)

print("The GE train does " + str(force) + " Joules of work over " + str(train_distance) + " meters.")
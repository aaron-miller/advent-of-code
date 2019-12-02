"""
--- Day 1: The Tyranny of the Rocket Equation ---

Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas, he needs you to bring him measurements from fifty stars.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?
"""

from math import floor

def calc_module_fuel(mass):
    return floor(mass / 3.0) - 2

assert calc_module_fuel(12) == 2
assert calc_module_fuel(14) == 2
assert calc_module_fuel(1969) == 654
assert calc_module_fuel(100756) == 33583

modules = [
    89407, 103327, 75227, 80462, 147732, 127392, 147052, 67987, 69650, 63139, 117260, 75686, 146517, 147057, 91654, 96757, 123428, 118351, 84167, 73536, 59261, 139879, 85969, 93931, 125232, 62629, 107163, 105032, 124295, 112716, 72402, 137719, 126924, 59903, 102568, 63963, 145435, 54578, 141348, 77099, 64050, 60012, 131514, 81400, 118451, 124420, 124821, 51746, 72382, 125018, 130662, 116926, 73573, 117827, 101462, 85172, 123277, 62842, 91856, 61046, 57290, 86265, 59080, 55713, 88492, 138409, 134009, 114376, 86621, 107651, 146528, 135273, 87760, 134164, 141430, 133574, 109457, 110225, 147989, 74089, 55747, 61602, 139444, 111397, 95751, 133049, 129641, 101287, 88916, 83340, 140286, 88824, 66013, 65935, 141174, 105662, 97399, 91345, 120164, 80904,
]

from functools import reduce
print(reduce(lambda x,y: x + y, map(calc_module_fuel, modules)))

def calc_total_fuel(fuel_mass):
    req_fuel = calc_module_fuel(fuel_mass)
    if calc_module_fuel(req_fuel) > 0:
        return calc_total_fuel(req_fuel) + fuel_mass
    else:
        if req_fuel > 0:
            return req_fuel + fuel_mass
        else:
            return fuel_mass

assert calc_total_fuel(calc_module_fuel(14)) == 2
assert calc_total_fuel(calc_module_fuel(1969)) == 966
assert calc_total_fuel(calc_module_fuel(100756)) == 50346

print(reduce(lambda x,y: x + y, map(calc_total_fuel, map(calc_module_fuel, modules))))

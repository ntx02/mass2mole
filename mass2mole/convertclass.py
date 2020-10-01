#!/usr/bin/env python3

import masses


class ConvertClass:
    def __init__(self, element, mass):
        self.element = element
        self.mass = mass

    def convert(self):
        mass = self.mass
        element = self.element
        molmass = float(mass) / float(masses.by_name[self.element])
        return f"{mass} grams of {element} is equivalent to {molmass} moles."

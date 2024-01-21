#!/usr/bin/env python

name = input("What is your name? ")
location = input("Where are you travelling from? ")
leg_1 = float(input(f"How many miles have you travelled from {location}? "))
destination = input("What is your final destination? ")
leg_2 = float(input(f"How many miles left to {destination}? "))

distance  = leg_1 + leg_2

print(f"""
      \nHello, {name}, and welcome to your layover!
      We hope you had a pleasant journey from {location}.
      When you reach {destination}, you will have travelled {distance:,.2f} miles.\n
      """)
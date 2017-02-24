'''
Building a siple madlibs program that prompts the user for input and prints a Mad Libs story with the user's input.
'''

print("Mad libs has started!")
name = raw_input("Please enter a name: ")
adj1 = raw_input("Please enter an adjective: ")
adj2 = raw_input("Please enter an adjective: ")
adj3 = raw_input("Please enter an adjective: ")
verb1 = raw_input("Please enter a verb: ")
verb2 = raw_input("Please enter a verb: ")
verb3 = raw_input("Please enter a verb: ")
noun1 = raw_input("Please enter a noun: ")
noun2 = raw_input("Please enter a noun: ")
noun3 = raw_input("Please enter a noun: ")
noun4 = raw_input("Please enter a noun: ")
animal = raw_input("Please enter an animal: ")
food = raw_input("Please enter a food: ")
fruit = raw_input("Please enter a fruit: ")
num = raw_input("Please enter a number: ")
superhero = raw_input("Please enter a superhero: ")
country = raw_input("Please enter a country: ")
dessert = raw_input("Please enter a dessert: ")
year = raw_input("Please enter a year: ")


#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %s protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %s very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %s ruled the world." % (adj1, name, verb1, adj2, noun1, noun2, animal, food, verb2, noun3, fruit, adj3, name, verb3, num, name, superhero, superhero, name, country, dessert, name, year, noun4)

print(STORY)

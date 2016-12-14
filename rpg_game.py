import pygame
from random import randint
import math

class Character(object):
    def attack(self, enemy):
        enemy.health -= self.power
    def alive(self):
        if self.health > 0:
            return True
    def print_status(self):
        print "The %s has %d health and %d power." % (self.charType, self.health, self.power)

class Zombie(Character):
    charType = "Zombie"
    def __init__(self):
        self.power = 1
        
class Hero(Character):
    charType = "Hero"
    def __init__(self):
        self.health = 10
        self.power = 5

class Goblin(Character):
    charType="Goblin"
    def __init__(self):
        self.health = 6
        self.power = 2

def main():
    goblin = Goblin()
    hero = Hero()

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            print "You do %d damage to the goblin." % hero.power
            if not goblin.alive():
                print("The goblin is dead..")
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if goblin.alive():
            # Goblin attacks hero
            goblin.attack(hero)
            # print "The goblin does %d damage to you." % goblin.power
            if not hero.alive():
                print("You are dead..")

main()

"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time
from random import randint

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            hero.coins += self.bounty
            print("Hero receives %d bounty coins for killing %s.") % (self.bounty, self.name)
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

class Hero(Character):
    armor = 0
    evade = 0.0
    poison = False
    def __init__(self):
        super(Hero, self).__init__()
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)
    def attack(self, enemy):
        if self.poison:
            print "%s has poison on his blade, attack deals + 1 damage to %s" % (self.name, enemy.name)
            self.power +=1
        super(Hero, self).attack(enemy)
        if self.poison:
            self.power -= 1
            self.poison = False
    def receive_damage(self, points):
        evadeChance = float(self.evade / 20.0)
        evaded = random.random() < evadeChance
        print evadeChance
        print self.evade
        print (evaded)
        if evaded:
            print "%s has evaded the attack!" % (self.name)
            points = 0
            return
        if self.armor:
            # healthArmor = self.health + armor
            self.health += self.armor
            print "%s has %d armor, health increased to %d" % (self.name, self.armor, self.health)
        super(Hero, self).receive_damage(points)
        if self.armor:
            self.armor -= points

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

class Zombie(Character):
    def __init__(self):
        super(Zombie, self).__init__()
        self.name = 'Zombie'
        self.health = 5
        self.bounty = 2
    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            return

class Medic(Character):
    def __init__(self):
        super(Medic, self).__init__()
        self.name = "Medic"
        self.bounty = 4
    def receive_damage(self, points):
        super(Medic, self).receive_damage(points)
        plus2health = random.random() < 0.2
        if plus2health :
            self.health+=2
            print("Medic self healed +2 HP!")
class Knight(Character):
    def __init__(self):
        super(Knight, self).__init__()
        self.name = "Knight"
        self.health = 7
        self.power = 10
        self.bounty = 7
class Shadow(Character):
    def __init__(self):
        super(Shadow, self).__init__()
        self.name = 'Shadow'
        self.health = 1
        self.bounty = 4
        self.power = 2
    def receive_damage(self, points):
        recDamage = random.random() < 0.1
        if recDamage:
            print("Shadow evaded attack!!")
            points = 0
        super(Shadow, self).receive_damage(points)
class Mage(Character):
    def __init__(self):
        super(Mage, self).__init__()
        self.name = "Mage"
        self.health = 6
        self.power = 3
        self.bounty = 8
    def receive_damage(self, points):
        boostHP = random.random() < 0.4
        if boostHP:
            print("%s boosted health by 3 for this turn!") % (self.name)
            self.health+=3
        super(Mage, self).receive_damage(points)

    def attack(self, enemy):
        boostPWR = random.random() < 0.2
        if boostPWR:
            print("%s boosted power by 5 for this turn!") % (self.name)
            self.power += 5
        super(Mage, self).attack(enemy)


class Goblin(Character):
    def __init__(self):
        super(Goblin, self).__init__()
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.bounty = 2

class Wizard(Character):
    def __init__(self):
        super(Wizard, self).__init__()
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.bounty = 6

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if self.health > 0:
            if swap_power:
                print "%s swaps power with %s during attack" % (self.name, enemy.name)
                self.power, enemy.power = enemy.power, self.power
            super(Wizard, self).attack(enemy)
            if swap_power:
                self.power, enemy.power = enemy.power, self.power

class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            print "You defeated the %s" % enemy.name
            return True
        else:
            print "YOU LOSE!"
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)
class SuperTonic(object):
    cost = 10
    name = 'super tonic'
    def apply(self, character):
        character.health = 10
        print "%s's health increased to %d." % (character.name, character.health)
class Armor(object):
    cost = 10
    name = 'armor'
    def apply(self, hero):
        hero.armor+=2
        print "%s's armor increased to %d." % (hero.name, hero.armor)
class Evade(object):
    if Hero.evade < 100:
        cost = 5
        name = 'evade'
        def apply(self, hero):
            hero.evade+=2
            print "%s's evade increased to %d." % (hero.name, hero.evade)
    else:
        print("You cannot purchase any more Evade, you are maxed out...")
class Poison(object):
    cost = 3
    name = 'Poison'
    def apply(self, hero):
        hero.poison = True
        print ("%s's power increased to %d for one attack.")    %(hero.name, hero.power)
class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]

    items = [Tonic, Sword, SuperTonic, Armor, Evade]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero()
enemies = [Goblin(), Wizard(), Mage(), Shadow(), Knight(), Medic(), Zombie()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"

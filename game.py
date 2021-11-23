"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random
from random import uniform
import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	UNARMED_POWER = 20

	def __init__(self, name, power, min_level):
		self.__name = name
		self.power = power
		self.min_level = min_level

	@property
	def name(self):
		return self.__name

	@classmethod
	def make_unarmed(cls):
		return cls("Unarmed", cls.UNARMED_POWER, 1)


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""
	def __init__(self, name, max_hp, attack, defense, level):
		self.__name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = None
		self.hp = max_hp

	@property
	def name(self):
		return self.__name

	@property
	def weapon(self):
		return self.__weapon

	@weapon.setter
	def weapon(self, value):
		if value is None:
			value = Weapon.make_unarmed()
		if value.min_level > self.level:
			raise ValueError(value)
		self.__weapon = value

	@property
	def hp(self):
		return self.__hp

	@hp.setter
	def hp(self, value):
		self.__hp = utils.clamp(value, 0, self.max_hp)

	def compute_damage(self, personnage2):
		crit = random.random() <= 1/16
		modifier = (2 if crit else 1)*random.uniform(0.85, 1.0)
		return int(round((((((2*self.level/5)+2)*self.__weapon.power*self.attack/personnage2.defense)/50)+2)*modifier)), crit


def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	dmg, crit = attacker.compute_damage(defender)
	defender.hp -= dmg
	print(f"{attacker.name} used {attacker.weapon.name}")
	if crit:
		print("Critical hit !")
	print(f"\t{defender.name} took {dmg} dmg")


def run_battle(c1: Character, c2: Character):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	nb_tours = 1
	attacker, defender = c1, c2
	print(f"{attacker.name} starts a battle with {defender.name} !")
	while c1.hp > 0 or c2.hp > 0:
		deal_damage(attacker, defender)
		if c2.hp == 0:
			print(f"{defender.name} is sleeping with the fishes...")
			break
		nb_tours += 1
		attacker, defender = defender, attacker
	return nb_tours


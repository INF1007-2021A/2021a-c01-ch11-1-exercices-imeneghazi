from game import *


def main():
	c1 = Character("John Snow", 200, 150, 70, 70)
	c2 = Character("Arya Stark", 250, 100, 120, 60)

	c1.weapon = Weapon("Long sword", 100, 69)
	c2.weapon = Weapon("Dagger", 120, 1)

	turns = run_battle(c1, c2)
	print(f"The battle ended in {turns} turns.")


if __name__ == "__main__":
	main()


# Write your solutions for 1.5 here!
class superheroes:
	def __int__(self, name, superpower, strength):
		self.name=name
		self.superpower=superpower
		self.strength=strength
	def print_me(self):
		print(self.name +str( self.strength))

superhero = superheroes("tamara","fly", 10)
superhero.print_me()


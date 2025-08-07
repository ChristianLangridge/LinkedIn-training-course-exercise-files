class Shape:
	width = 5
	height = 5
	printChar = '#'

	def printRow(self, i):
		raise NotImplementedError("Will be implemented by children extending this class")

	def print(self):
		for i in range(self.height):
			self.printRow(i)


class Square(Shape):
	def printRow(self, i):
		print(self.printChar * self.width)

class RightTriangle(Shape):
	def printRow(self, i):
		    print(self.printChar * (i + 1))

class RandomTriangle(Shape):
	spacer = ' '
	def printRow(self, i):
		    print(self.spacer * (i + 2), self.printChar * (i + 1))

class EquilateralTriangle(Shape):
	height = 5
	width = height * 2 
	
	def printRow(self, i):
		TriangleWidth = i * 2 + 1
		Padding = int((self.width - TriangleWidth)/2)
		print(' ' * Padding + self.printChar * TriangleWidth)
		

a = EquilateralTriangle()
a.print()
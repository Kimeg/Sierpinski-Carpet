import pygame as pg

class Carpet:
	def __init__(self, x, y, x_offset, y_offset, depth, depth_limit, color=(255,255,255)):
		self.x = x
		self.y = y
		self.x_offset = x_offset
		self.y_offset = y_offset

		self.depth = depth
		self.depth_limit = depth_limit
		self.color = color
		self.carpets = []
		return

	def generate_offspring(self):
		if self.depth>=self.depth_limit:
			return

		''' Iteratively generate carpets of higher depths, skipping center carpet '''
		for i in range(3):
			for j in range(3):
				if i==1 and j==1:
					continue

				x = self.x+j*self.x_offset
				y = self.y+i*self.y_offset

				x_offset = int(self.x_offset/3)
				y_offset = int(self.y_offset/3)

				carpet = Carpet(x, y, x_offset, y_offset, self.depth+1, self.depth_limit)
				carpet.generate_offspring()

				self.carpets.append(carpet)
		return

	def render(self):
		if self.depth>=self.depth_limit:
			return

		x = self.x+self.x_offset
		y = self.y+self.y_offset

		pg.draw.rect(window, self.color, (x, y, self.x_offset, self.y_offset))

		for carpet in self.carpets:
			carpet.render()
		return

def main():
	carpet = Carpet(0, 0, X_OFFSET, Y_OFFSET, 0, DEPTH_LIMIT)
	carpet.generate_offspring()

	running = True
	while running:
		for event in pg.event.get():
			if event.type==pg.QUIT:
				running = False
				break

			''' Increment or decrement depth values to see how the structure changes '''
			if event.type==pg.KEYDOWN:
				if event.key==pg.K_w:
					if carpet.depth_limit<UPPER_LIMIT:
						carpet.depth_limit += 1
						carpet.carpets = []
						carpet.generate_offspring()
				elif event.key==pg.K_s:
					if carpet.depth_limit>LOWER_LIMIT:
						carpet.depth_limit -= 1
						carpet.carpets = []
						carpet.generate_offspring()

		window.fill((0, 0, 0))

		carpet.render()

		pg.display.update()

	pg.quit()
	return

if __name__=="__main__":
	WIDTH, HEIGHT = 800, 800

	DEPTH_LIMIT = 5 

	UPPER_LIMIT = 6
	LOWER_LIMIT = 1 

	X_OFFSET = int(WIDTH/3)
	Y_OFFSET = int(HEIGHT/3)

	pg.init()

	window = pg.display.set_mode((WIDTH, HEIGHT))
	pg.display.set_caption("Sierpinski Carpet")

	clock = pg.time.Clock()	

	main()

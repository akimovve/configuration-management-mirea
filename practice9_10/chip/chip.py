import pygame
import sys
from pathlib import Path
from random import randint

from pygame import Rect


class Chip:

	def __init__(self, font, rom):
		self.mem = [0] * 4096
		self.V = [0] * 16
		self.I = 0
		self.pc = 512
		self.sp = 0
		self.stack = [0] * 16
		self.scr = [0] * (64 * 32)
		self.key = [0] * 16
		self.delay_timer = 0
		self.sound_timer = 0
		for i in range(80):
			self.mem[i] = font[i]
		for i in range(len(rom)):
			self.mem[i + 512] = rom[i]


def step(chip):
	mem, V, stack, scr, key = chip.mem, chip.V, chip.stack, chip.scr, chip.key
	npc = chip.pc + 2
	opc = mem[chip.pc] << 8 | mem[chip.pc + 1]
	op1 = opc & 0xf000
	op2 = opc & 0xf00f
	op3 = opc & 0xf0ff

	if opc == 0x00e0:
		# TODO
		for i in range(len(scr)):
			scr[i] = 0

	elif opc == 0x00ee:
		chip.sp -= 1
		npc = stack[chip.sp]
		npc += 2

	elif op1 == 0x1000:
		npc = opc & 0x0fff

	elif op1 == 0x2000:
		stack[chip.sp] = chip.pc
		chip.sp += 1
		npc = opc & 0x0fff

	elif op1 == 0x3000:
		if V[(opc & 0x0f00) >> 8] == (opc & 0x00ff):
			npc = chip.pc + 4

	elif op1 == 0x4000:
		if V[(opc & 0x0f00) >> 8] != (opc & 0x00ff):
			npc = chip.pc + 4

	elif op1 == 0x5000:
		if V[(opc & 0x0f00) >> 8] == V[(opc & 0x00f0) >> 4]:
			npc = chip.pc + 4

	elif op1 == 0x6000:
		V[(opc & 0x0f00) >> 8] = (opc & 0x00ff)

	elif op1 == 0x7000:
		# TODO
		V[(opc & 0x0f00) >> 8] += (opc & 0x00ff)
		V[(opc & 0x0f00) >> 8] &= 0xff  #########

	elif op2 == 0x8000:
		V[(opc & 0x0F00) >> 8] = V[(opc & 0x00F0) >> 4]

	elif op2 == 0x8001:
		V[(opc & 0x0F00) >> 8] |= V[(opc & 0x00F0) >> 4]

	elif op2 == 0x8002:
		V[(opc & 0x0F00) >> 8] &= V[(opc & 0x00F0) >> 4]

	elif op2 == 0x8003:
		V[(opc & 0x0F00) >> 8] ^= V[(opc & 0x00F0) >> 4]

	elif op2 == 0x8004:
		V[(opc & 0x0F00) >> 8] += V[(opc & 0x00F0) >> 4]
		if V[(opc & 0x00F0) >> 4] > (0xFF - V[(opc & 0x0F00) >> 8]):
			V[0xF] = 1
		else:
			V[0xF] = 0

	elif op2 == 0x8005:
		# TODO
		if V[(opc & 0x00f0) >> 4] > V[(opc & 0x0f00) >> 8]:
			V[0xf] = 0
		else:
			V[0xf] = 1
		V[(opc & 0x0F00) >> 8] -= V[(opc & 0x00F0) >> 4]
		V[(opc & 0x0F00) >> 8] &= 0xff  #########

	elif op2 == 0x8006:
		V[0xF] = V[(opc & 0x0F00) >> 8] & 0x1
		V[(opc & 0x0F00) >> 8] >>= 1

	elif op2 == 0x8007:
		# TODO
		if V[(opc & 0x0F00) >> 8] > V[(opc & 0x00F0) >> 4]:
			V[0xF] = 0
		else:
			V[0xF] = 1
		V[(opc & 0x0F00) >> 8] = V[(opc & 0x00F0) >> 4] - V[(opc & 0x0F00) >> 8]
		V[(opc & 0x0F00) >> 8] &= 0xff  #########

	elif op2 == 0x800e:
		# TODO
		V[0xF] = V[(opc & 0x0F00) >> 8] & 0x80
		V[(opc & 0x0F00) >> 8] = V[(opc & 0x0F00) >> 8] << 1

	elif op1 == 0x9000:
		if V[(opc & 0x0F00) >> 8] != V[(opc & 0x00F0) >> 4]:
			npc = chip.pc + 4

	elif op1 == 0xa000:
		chip.I = opc & 0x0FFF

	elif op1 == 0xb000:
		npc = (opc & 0x0FFF) + V[0]

	elif op1 == 0xc000:
		V[(opc & 0x0F00) >> 8] = randint(0, 255) & (opc & 0x00FF)

	elif op1 == 0xd000:
		# TODO
		x = V[(opc & 0x0f00) >> 8]
		y = V[(opc & 0x00f0) >> 4]
		height = opc & 0x000f
		V[0xf] = 0

		for yline in range(height):
			pixel = mem[chip.I + yline]
			for xline in range(8):
				i = x + xline + ((y + yline) * 64)
				if pixel & (0x80 >> xline) != 0 and not (yline + y >= 32 or xline + x >= 64):
					if scr[i] == 1:
						V[0xf] = 1
					scr[i] ^= 1

	elif op3 == 0xe09e:
		if key[V[(opc & 0x0F00) >> 8]] != 0:
			npc = chip.pc + 4

	elif op3 == 0xe0a1:
		if key[V[(opc & 0x0F00) >> 8]] == 0:
			npc = chip.pc + 4

	elif op3 == 0xf007:
		V[(opc & 0x0F00) >> 8] = chip.delay_timer

	elif op3 == 0xf00a:
		# TODO
		k = -1
		for i in range(len(key)):
			if key[i] == 1:
				k = i
				break
		if k >= 0:
			V[(opc & 0x0F00) >> 8] = k
		else:
			chip.pc -= 2

	elif op3 == 0xf015:
		chip.delay_timer = V[(opc & 0x0F00) >> 8]

	elif op3 == 0xf018:
		chip.sound_timer = V[(opc & 0x0F00) >> 8]

	elif op3 == 0xf01e:
		if chip.I + V[(opc & 0x0F00) >> 8] > 0xFFF:
			V[0xF] = 1
		else:
			V[0xF] = 0
		chip.I += V[(opc & 0x0F00) >> 8]

	elif op3 == 0xf029:
		chip.I = V[(opc & 0x0F00) >> 8] * 0x5

	elif op3 == 0xf033:
		mem[chip.I] = V[(opc & 0x0F00) >> 8] // 100
		mem[chip.I + 1] = (V[(opc & 0x0F00) >> 8] // 10) % 10
		mem[chip.I + 2] = V[(opc & 0x0F00) >> 8] % 10

	elif op3 == 0xf055:
		for i in range(((opc & 0x0F00) >> 8) + 1):
			mem[chip.I + i] = V[i]
		chip.I += ((opc & 0x0F00) >> 8) + 1

	elif op3 == 0xf065:
		for i in range(((opc & 0x0F00) >> 8) + 1):
			V[i] = mem[chip.I + i]
		chip.I += ((opc & 0x0F00) >> 8) + 1

	else:
		print("invalid opcode 0x%x at 0x%x" % (opc, chip.pc))
		sys.exit(1)

	if chip.delay_timer > 0:
		chip.delay_timer -= 1
	if chip.sound_timer > 0:
		chip.sound_timer -= 1
	chip.pc = npc


font = Path("font.bin").read_bytes()
rom = Path("roms/tetris.rom").read_bytes()
chip = Chip(font, rom)

pygame.init()
pygame.display.set_caption("Chip game")

colors = [(0, 0, 0), (255, 255, 255)]
width, height = 64, 32
size = width * 10, height * 10
keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
		pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r,
		pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f,
		pygame.K_z, pygame.K_x, pygame.K_c, pygame.K_v
		]

screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))

while True:
	step(chip)

	for x in range(width):
		for y in range(height):
			screen.fill(colors[chip.scr[x + (y * width)]], Rect(x * 10, y * 10, 10, 10))
	pygame.display.flip()

	for event in pygame.event.get():
		event_type = -1
		if event.type == pygame.KEYDOWN:
			event_type = 1
		elif event.type == pygame.KEYUP:
			event_type = 0
		elif event.type == pygame.QUIT:
			sys.exit(0)

		if event_type == 0 or event_type == 1:
			if event.key in keys:
				i = keys.index(event.key)
				chip.key[i] = event_type

import keyboard

import sys
import time

import pygame

import utils
import cvrec
from settings import *

import pygame as p

p.init()
p.display.set_caption('Sim')
sound = pygame.mixer.Sound("assets/sound.flac")

surf = pygame.Surface(WIN_RES)

window = p.display.set_mode(OBS_RES)
from simulation import *
# p.init()


class App:
    def __init__(self):
        self.sound = sound

        self.surf = surf

        self.window =window
        self.font = p.font.Font(None, 30)
        self.clock = p.time.Clock()
        self.Sim = Simulation(self, WIN_RES,self.sound)
        self.prev = time.time()
        self.out = cvrec.get_out(utils.generate_file_name(r'output\vid','','mp4'), 60, WIN_RES[::-1])
        self.frame = 0

    def update(self, dt):
        self.frame += 1
        self.Sim.update(dt, self.frame)
        self.clock.tick(FPS)

    def draw(self):
        self.surf.fill(color=BG_COLOR)
        self.Sim.draw()

    def check_events(self):
        for event in p.event.get():
            if event.type == p.QUIT or (event.type == p.KEYDOWN and event.key == p.K_ESCAPE):
                self.out.release()
                p.quit()
                sys.exit()

    def run(self):
        while True:
            if keyboard.is_pressed('p'):
                continue
            if keyboard.is_pressed('o'):
                self.frame += 1
                if self.frame % 1000 != 0:
                    continue
            if keyboard.is_pressed('i'):
                self.frame += 1
                if self.frame % 10000 != 0:
                    continue
            if keyboard.is_pressed('r'):
                break
            self.check_events()
            t = time.time()
            self.update(t - self.prev)
            self.draw()
            self.window.blit(p.transform.rotozoom( self.surf,-90,720/1280), (0, 0))
            utils.debug(1 / (t - self.prev), 300)
            p.display.update()
            self.out.write(p.surfarray.array3d( self.surf)[:, :, ::-1])
            self.prev = t


if __name__ == '__main__':
    while True:
        app = App()
        app.run()

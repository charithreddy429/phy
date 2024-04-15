import keyboard

import sys
import time

import pygame

import utils
import cvrec
from settings import *
from simulation import *
import pygame as p

p.init()


class App:
    def __init__(self):
        p.init()
        p.display.set_caption('Sim')
        self.sound = pygame.mixer.Sound("sound.flac")
        self.surf = pygame.Surface(WIN_RES)
        self.window = p.display.set_mode(OBS_RES)
        self.font = p.font.Font(None, 30)
        self.clock = p.time.Clock()
        self.Sim = Simulation(self, WIN_RES,self.sound)
        self.prev = time.time()
        self.out = cvrec.get_out('happy.mp4', 60, WIN_RES[::-1])
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
            utils.debug(1 / (t - self.prev), 300)
            self.window.blit(p.transform.rotozoom( self.surf,90,720/1280), (0, 0))
            p.display.update()
            self.out.write(p.surfarray.array3d( self.surf)[:, :, ::-1])
            self.prev = t


if __name__ == '__main__':
    while True:
        app = App()
        app.run()

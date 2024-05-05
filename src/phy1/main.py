import keyboard

import sys

import pygame

import utils
import cvrec
from settings import *

import pygame as p
import cProfile
import pstats

p.init()
p.display.set_caption('Sim')
sound = pygame.mixer.Sound("assets/sound.flac")
st = False
surf = pygame.Surface(WIN_RES)

window = p.display.set_mode(OBS_RES)
from simulation import *


# p.init()


class App:
    def __init__(self, number):
        self.sound = sound

        self.surf = surf

        self.window = window
        self.font = p.font.Font(None, 30)
        self.clock = p.time.Clock()
        self.Sim = Simulation(self, WIN_RES, number, self.sound)
        self.prev = time.time()
        if REC:
            self.out = cvrec.get_out(utils.generate_file_name(r'output\vid', '', 'mp4'), 60, WIN_RES[::-1])
        self.frame = 0

    def update(self, dt):
        self.frame += 1
        self.Sim.update(dt, self.frame)
        # self.clock.tick(FPS)

    def draw(self):
        self.surf.fill(color=BG_COLOR)
        self.Sim.draw()

    def check_events(self):
        for event in p.event.get():
            if event.type == p.QUIT or (event.type == p.KEYDOWN and event.key == p.K_ESCAPE):
                if REC:
                    self.out.release()
                p.quit()
                sys.exit()

    def run(self):
        self.surf.fill((10, 10, 30))
        while True:
            # self.clock.tick(30)
            global st
            if keyboard.is_pressed('p'):
                if keyboard.is_pressed("a"):
                    if not st:
                        st = True
                    else:
                        continue
                else:
                    st = False
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
            if keyboard.is_pressed("c"):
                eval(input())
            self.check_events()
            t = time.time()
            self.update(t - self.prev)
            self.draw()
            self.window.blit(p.transform.rotozoom(self.surf, 0, 720 / 1280), (0, 0))
            utils.debug(1 / (t - self.prev + 1e-9), 300)
            utils.debug(self.frame)
            p.display.update()
            if REC:
                # if self.frame%5==0:
                # self.out.write(p.surfarray.array3d( self.surf)[:, :, ::-1])
                # self.out.write(p.surfarray.array3d(self.surf)[:, :, ::-1])
                pass
            self.prev = t

            # if self.frame>=100:
            #     break


if __name__ == '__main__':
    n = 2
    while True:
        n += 2
        app = App(n)
        app.run()
        # cProfile.run('app.run()','profile_results')
        # stats = pstats.Stats('profile_results')

        # Sort the results by time spent
        # stats.sort_stats('time')

        # Print the sorted results
        # stats.print_stats()

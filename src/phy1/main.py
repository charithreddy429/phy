import sys
import time
import utils
import  cvrec
from settings import *
from simulation import *
import pygame as p
p.init()


class App:
    def __init__(self):
        p.init()
        p.display.set_caption('Sim')
        self.surf = p.display.set_mode(WIN_RES)
        self.font = p.font.Font(None, 30)
        self.clock = p.time.Clock()
        self.Sim = Simulation(self,WIN_RES)
        self.prev = time.time()
        self.out= cvrec.get_out('happy.mp4',60,(720,1280))


    def update(self,dt):
        self.Sim.update(dt)
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
            self.check_events()
            t = time.time()
            self.update(t-self.prev)
            self.draw()
            utils.debug(1/(t-self.prev),300)
            p.display.update()
            self.out.write(p.surfarray.array3d( self.surf)[:, :, ::-1])
            self.prev = t


if __name__ == '__main__':
    app = App()
    app.run()



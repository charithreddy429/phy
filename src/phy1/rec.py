import numpy as np
import pygame as p
import utils


class Rec:

    def __init__(self, surf, position, velocity=None, wh=(10, 10), outcolor=(255,255,255),color=utils.rclr()):
        self.position = position
        if velocity is None:
            velocity = np.float64([0.0, 0.0])
        self.lpos = self.position - velocity
        self.wh = wh
        self.mass = 0
        self.thickness = np.float64([10.0, 10.0])
        self.outcolor = outcolor
        self.color  = color
        self.surf = surf
        self.rect = p.Rect(self.position[0], self.position[1], self.wh[0], self.wh[1])
        self.drawmode =1
    def update(self, dt):
        t = self.position.copy()
        self.position += (self.position - self.lpos)
        self.lpos = t

        # self.rect.topleft = ()  # Update rect position

    def draw(self):
        if self.drawmode%2:
            print(self.position,self.outcolor,int(self.thickness[0]))
            p.draw.rect(self.surf, self.outcolor, (*(self.position-self.thickness).astype(int), *(np.array(self.wh)+2*self.thickness).astype(int)),
                        int(self.thickness[0]))
        print(self.drawmode//2,self.drawmode)
        if self.drawmode//2:
            # print(self.position[0], self.position[1])
            p.draw.rect(self.surf, self.color, (int(self.position[0]), int(self.position[1]), *self.wh))
        # print(self.position,"draw")

    def collide(self, other_rec):
        # print("f")
        import numpy as np

        # Assuming diff_self, self.wh, other_rec.wh, self.thickness, and other_rec.thickness are numpy arrays
        diff_self = self.position - other_rec.position
        # Calculate the x and y components
        diff_self_x = diff_self[0]  # Assuming the x-axis is the first dimension
        diff_self_y = diff_self[1]  # Assuming the y-axis is the second dimension

        # Calculate the x and y components for the other_rec position
        other_rec_wh_x = other_rec.wh[0]  # Assuming the x-axis is the first dimension
        other_rec_wh_y = other_rec.wh[1]  # Assuming the y-axis is the second dimension

        # Calculate the x and y components for the self position
        self_wh_x = self.wh[0]  # Assuming the x-axis is the first dimension
        self_wh_y = self.wh[1]  # Assuming the y-axis is the second dimension

        # Calculate the x and y components for the thickness
        self_thickness_x = self.thickness[0]  # Assuming the x-axis is the first dimension
        self_thickness_y = self.thickness[1]  # Assuming the y-axis is the second dimension
        other_rec_thickness_x = other_rec.thickness[0]  # Assuming the x-axis is the first dimension
        other_rec_thickness_y = other_rec.thickness[1]  # Assuming the y-axis is the second dimension

        # Check conditions along the x-axis
        condition1_x = np.logical_xor((0 < diff_self_x - self.thickness).all(),
                                      (diff_self_x + self_wh_x + self_thickness_x < other_rec_wh_x).all())

        condition2_x = np.logical_xor((0 < -diff_self_x).all(),
                                      (-diff_self_x + other_rec_wh_x + other_rec_thickness_x < self_wh_x).all())

        # Check conditions along the y-axis
        condition1_y = np.logical_xor((0 < diff_self_y - self.thickness).all(),
                                      (diff_self_y + self_wh_y + self_thickness_y < other_rec_wh_y).all())

        condition2_y = np.logical_xor((0 < -diff_self_y).all(),
                                      (-diff_self_y + other_rec_wh_y + other_rec_thickness_y < self_wh_y).all())

        # Check if all elements of either condition are True

        if condition1_x.all() or condition2_x.all():
            # self.color = (255, self.color[1], self.color[2])

            vel_along_normal = (other_rec.getvelocity() - self.getvelocity())[0]
            normal = np.array([1, 0])

            impulse = -2 * vel_along_normal
            impulse /= 1
            if abs(self.mass) + abs(other_rec.mass) == 0:
                self.addvelocity(- impulse * normal / 2)
                other_rec.addvelocity(impulse * normal / 2)
            else:
                self.addvelocity(- impulse * normal * other_rec.mass / (abs(self.mass) + abs(other_rec.mass)))
                other_rec.addvelocity(impulse * normal * self.mass / (abs(self.mass) + abs(other_rec.mass)))

        else:
            pass
            # self.color = (0, self.color[1], self.color[2])

        if condition1_y or condition2_y:
            # self.color = (self.color[0], 255, self.color[2])

            vel_along_normal = (other_rec.getvelocity() - self.getvelocity())[1]
            normal = np.array([0, 1])

            impulse = -2 * vel_along_normal

            impulse /= 1
            if abs(self.mass) + abs(other_rec.mass) == 0:
                self.addvelocity(- impulse * normal / 2)
                other_rec.addvelocity(impulse * normal / 2)
            else:
                self.addvelocity(- impulse * normal * other_rec.mass / (abs(self.mass) + abs(other_rec.mass)))
                other_rec.addvelocity(impulse * normal * self.mass / (abs(self.mass) + abs(other_rec.mass)))

        else:
            pass
            # self.color = (self.color[0], 0, self.color[2])
        if condition1_y or condition2_y or condition2_x or condition1_x:
            return True
    def getvelocity(self):
        return self.position - self.lpos

    def addvelocity(self, v):
        self.lpos -= v


class RecSet:
    def __init__(self, recs: list[Rec]):
        self.recs = recs

    def draw(self):
        for i in self.recs:
            i.draw()

    def update(self, dt,frame):
        # print("fram")
        for i in self.recs:
            i.update(dt)
            print(i.getvelocity())
            if i.getvelocity()[0]!=i.getvelocity()[1]:
                print(i.getvelocity()[0],i.getvelocity()[1])
                # eval(input())

                # i.lpos= i.position-sum(i.getvelocity())/2
        # print(i.position)
        for i in range(len(self.recs)):
            for j in range(i + 1, len(self.recs)):
                if self.recs[i].collide(self.recs[j]):
                    utils.append_to_file("wa.txt",frame)

    def interact(self, *k):
        pass

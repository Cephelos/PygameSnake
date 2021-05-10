import pygame, random

pygame.init()
win = pygame.display.set_mode((500,500))
myfont = pygame.font.SysFont('Arial Black', 30)


class Snake:

    def __init__(self, x, y, xvel, yvel, goal, last_spaces=[], speed=1):
        self.x = x
        self.y = y

        self.xvel = xvel
        self.yvel = yvel
        self.goal = goal
        self.last_spaces = last_spaces
        self.speed = speed

    def draw(self):

        pygame.draw.rect(win, (50, 200, 50), (self.x, self.y, 25, 25))
        for i in self.last_spaces:
            pygame.draw.rect(win, (50, 50, 200), (i[0], i[1], 25, 25))
        pygame.draw.rect(win, (200, 50, 50), (self.goal[0], self.goal[1], 25, 25))





    def control_snake(self):
        global run
        global timer
        if timer % 5 == 0:
            self.last_spaces.append((self.x, self.y))
            self.last_spaces.pop(0)
            self.x += self.xvel
            self.y += self.yvel

        if keys[pygame.K_a] and self.xvel == 0:
            self.xvel = -25
            self.yvel = 0

        elif keys[pygame.K_d] and self.xvel == 0:
            self.xvel = 25
            self.yvel = 0

        elif keys[pygame.K_w] and self.yvel == 0:

            self.xvel = 0
            self.yvel = -25

        elif keys[pygame.K_s] and self.yvel == 0:
            self.xvel = 0
            self.yvel = 25

        if self.x > 500 or self.x < 0 or self.y > 500 or self.y < 0 or (self.x, self.y) in self.last_spaces[:-1]:
            run = False

    def collect_fruit(self):

        self.last_spaces.append((self.x, self.y))
        for i in range(100):
            self.goal = (random.randint(2, 18)*25, random.randint(2, 18)*25)
            if self.goal not in self.last_spaces:
                break



def draw_grid():
    for i in range(1, 20):
        pygame.draw.line(win, (0), (0, i*25), (500, i*25), 1)

    for i in range(1, 20):
        pygame.draw.line(win, (0), (i*25, 0), (i*25, 500), 1)


def message(msg, color):
    mesg = myfont.render(msg, True, color)
    win.blit(mesg, [0, 0])


global run
run = True

s = Snake(50, 50, 25, 0, (random.randint(2, 18)*25, random.randint(2, 18)*25))

global timer
timer = 0
while run:
    clock = pygame.time.Clock()
    clock.tick(30)
    win.fill((200, 200, 200))
    timer += 1
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    s.draw()
    s.control_snake()
    if (s.x, s.y) == s.goal:
        s.collect_fruit()
    draw_grid()
    pygame.display.update()

message("You Lose! Your Score:" + str(len(s.last_spaces)), (255, 0, 0))
pygame.display.update()
pygame.time.wait(5000)

pygame.quit()

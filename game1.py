import pygame
import time
import random
import win32com.client as wincl
import os

pygame.init()

# color adjustment
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 128)

# game window
width = 1100
height = 700
screen = pygame.display.set_mode((width, height))

# Time module
clock = pygame.time.Clock()

# for the caption
pygame.display.set_caption("PASSING HURDLES")

# Imp Variables
box_x = 495
box_y = 650
box_size_w = 150
box_size_h = 50
deve_box_x = 510
deve_box_y = 130
countdown = 0
timer = 0
car_num = 0
car_passed = 0
invisible = False
invisible_point = 500
used_invi = False
car_width = 85

# uploading the car image
car_1 = pygame.image.load("car1.jpg")
car_2 = pygame.image.load("car2.jpg")
car_3 = pygame.image.load("car3.jpg")
car_4 = pygame.image.load("car4.jpg")
car_5 = pygame.image.load("car5.jpg")
car_6 = pygame.image.load("car6.jpg")
car_7 = pygame.image.load("car7.jpg")
truck_1 = pygame.image.load("truck1.jpg")
truck_2 = pygame.image.load("truck2.jpg")
truck_3 = pygame.image.load("truck3.jpg")
bike_1 = pygame.image.load("bike1.jpg")
bike_2 = pygame.image.load("bike2.jpg")
bike_3 = pygame.image.load("bike3.jpg")
invi_img = pygame.image.load("invi.jpg")
invi_img = pygame.transform.scale(invi_img, (100, 100)).convert_alpha()

list_cars = [car_1, car_2, car_3, car_4, car_5, car_6, car_7]

# uploading background
backimg = pygame.image.load("blacky.jpg")
backimg = pygame.transform.scale(backimg, (width, height)).convert_alpha()
grass = pygame.image.load("grass.jpg")

#developer page
developer = pygame.image.load("developer.jpg")
developer = pygame.transform.scale(developer, (width, height)).convert_alpha()

#control page
control = pygame.image.load("controller.jpg")
control = pygame.transform.scale(control, (width, height)).convert_alpha()

def speak(str):
    ch4.pause()
    ch5.pause()
    spk = wincl.Dispatch("SAPI.SpVoice")
    spk.Speak(str)
    ch4.unpause()
    ch5.unpause()

# #text_objects_function
def text_object(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()

# uploading main starting image
starting_image = pygame.image.load("blackyy.jpg")
starting_image = pygame.transform.scale(starting_image, (width, height)).convert_alpha()
crash_img = pygame.image.load("crash_car.jpg")
crash_img = pygame.transform.scale(crash_img, (width, height)).convert_alpha()

# Select car image making blur
surf = pygame.image.load("select_cars.jpg")
surf = pygame.transform.scale(surf, (width, height)).convert_alpha()

# uploading instruction image
instruction_background = pygame.image.load("b4.jpg")
instruction_background = pygame.transform.scale(instruction_background, (width, height)).convert_alpha()

def text_screen(text, color, size, font, x, y):
    font = pygame.font.SysFont(font, size)
    screen_text = font.render(text,True,color)
    screen.blit(screen_text, [x, y])

def select_car():
    global car_num
    global point
    global invisible
    back = True
    i = 0
    while back:
        screen.blit(surf, (0, 0))
        screen.blit(list_cars[i], (int(width / 2) - 45, int(height / 2) - 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if i < len(list_cars) - 1:
            if mouse[0] > 635 and mouse[0] < 755 and mouse[1] > 370 and mouse[1] < 420:
                pygame.draw.rect(screen, white, (635, 370, 120, 50))
                if click == (1, 0, 0):
                    i += 1
                    clock.tick(2)
            else:
                pygame.draw.rect(screen, black, (635, 370, 120, 50))

            # calling of next text button
            smalltext = pygame.font.SysFont("freesansbold.++f", 20, bold=True)
            textsurface, textRect = text_object("NEXT ->", smalltext)
            textRect.center = (int((635 + (120 / 2))), int((370 + (50 / 2))))
            screen.blit(textsurface, textRect)

        if i > 0:
            if mouse[0] > 355 and mouse[0] < 575 and mouse[1] > 370 and mouse[1] < 420:
                pygame.draw.rect(screen, white, (355, 370, 120, 50))
                if click == (1, 0, 0):
                    i -= 1
                    clock.tick(2)
            else:
                pygame.draw.rect(screen, black, (355, 370, 120, 50))

            # calling of previous text button
            smalltext = pygame.font.SysFont("freesansbold.++f", 20, bold=True)
            textsurface, textRect = text_object("<- PREVIOUS", smalltext)
            textRect.center = (int((355 + (120 / 2))), int((370 + (50 / 2))))
            screen.blit(textsurface, textRect)

        if mouse[0] > 495 and mouse[0] < 615 and mouse[1] > 480 and mouse[1] < 530:
            pygame.draw.rect(screen, white, (495, 480, 120, 50))
            if click == (1, 0, 0):
                car_num = i
        else:
            pygame.draw.rect(screen, black, (495, 480, 120, 50))

        # calling of select text button
        smalltext = pygame.font.SysFont("freesansbold.++f", 20, bold=True)
        textsurface, textRect = text_object("SELECT", smalltext)
        textRect.center = (int((495 + (120 / 2))), int((480 + (50 / 2))))
        screen.blit(textsurface, textRect)

        if mouse[0] > 950 and mouse[0] < 1070 and mouse[1] > 550 and mouse[1] < 600:
            pygame.draw.rect(screen, white, (950, 550, 120, 50))
            if click == (1, 0, 0):
                back = False
        else:
            pygame.draw.rect(screen, black, (950, 550, 120, 50))

        # calling of back text button
        smalltext = pygame.font.SysFont("freesansbold.++f", 20, bold=True)
        textsurface, textRect = text_object("BACK", smalltext)
        textRect.center = (int((950 + (120 / 2))), int((550 + (50 / 2))))
        screen.blit(textsurface, textRect)

        if mouse[0] > width - 210 and mouse[0] < (width - 90) and mouse[1] > 170 and mouse[1] < 220:
            pygame.draw.rect(screen, white, (width - 210, 170, 120, 50))
            if click == (1, 0, 0):
                if not invisible:
                    if int(point) >= invisible_point:
                        invisible = True
                        point = int(point) - invisible_point
                        with open("point.txt", "w") as p:
                            p.write(str(point))

        else:
            pygame.draw.rect(screen, black, (width - 210, 170, 120, 50))

        # calling of Points text button
        smalltext = pygame.font.SysFont("freesansbold.++f", 25, bold=True)
        textsurface, textRect = text_object("500 POINTS", smalltext)
        textRect.center = (int((width - 210 + (120 / 2))), int((170 + (50 / 2))))
        screen.blit(textsurface, textRect)

        if invisible:
            text_screen("You have the invisibility power", black, 50, None, 60, height - 60)
        else:
            text_screen("You don't have the invisibility power", black, 50, None, 60, height - 60)
        text_screen("Car number " + str(car_num + 1) + " selected", black, 50, None, 60, height - 100)
        text_screen("Point :" + str(point), black, 50, None, 60, 60)
        text_screen("BUY POWER", black, 50, None, width - 260, 10)
        screen.blit(invi_img, (width - 200, 50))
        pygame.display.update()
        clock.tick(60)

# main loop
def starting_loop():

    pygame.mixer.stop()
    ch1.play(start_music, -1)

    start = True
    global countdown
    countdown = 1
    global used_invi
    global invisible
    if used_invi:
        invisible = False
        used_invi = False

    while start:
        screen.blit(starting_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
        text_screen("PASSING HURDLES", white, 100, None, 50, 50)

        # clicking and functioning of mouse button
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if mouse[0] > box_x + (2 * box_size_w) and mouse[0] < box_x + (3 * box_size_w) and mouse[1] > box_y and mouse[
            1] < box_y + box_size_h:
            pygame.draw.rect(screen, white, (box_x + (2 * box_size_w), box_y, box_size_w, box_size_h))
            if click == (1, 0, 0):
                select_car()
        else:
            pygame.draw.rect(screen, black, (box_x + (2 * box_size_w), box_y, box_size_w, box_size_h))

        # calling of EXIT text button
        smalltext = pygame.font.SysFont("freesansbold.++f", 20)
        textsurface, textRect = text_object("CAR CUSTOMIZATION", smalltext)
        textRect.center = (int((box_x + (2 * box_size_w) + (box_size_w / 2))), int((box_y + (box_size_h / 2))))
        screen.blit(textsurface, textRect)

        if mouse[0] > box_x and mouse[0] < box_x + box_size_w and mouse[1] > box_y and mouse[1] < box_y + box_size_h:
            pygame.draw.rect(screen, white, (box_x, box_y, box_size_w, box_size_h))
            if click == (1, 0, 0):
                game_loop()
        else:
            pygame.draw.rect(screen, black, (box_x, box_y, box_size_w, box_size_h))

        # calling of start text button
        smalltext = pygame.font.SysFont("freesansbold.++f", 20, bold=True)
        textsurface, textRect = text_object("START", smalltext)
        textRect.center = (int((box_x + (box_size_w / 2))), int(box_y + (box_size_h / 2)))
        screen.blit(textsurface, textRect)

        if mouse[0] > box_x + box_size_w and mouse[0] < box_x + (2 * box_size_w) and mouse[1] > box_y and mouse[
            1] < box_y + box_size_h:
            pygame.draw.rect(screen, white, (box_x + box_size_w, box_y, box_size_w, box_size_h))
            if click == (1, 0, 0):
                controller()
        else:
            pygame.draw.rect(screen, black, (box_x + box_size_w, box_y, box_size_w, box_size_h))

        # calling of controls text button
        smalltext = pygame.font.SysFont("freesansbold.++f", 20, bold=True)
        textsurface, textRect = text_object("CONTROLS", smalltext)
        textRect.center = (int((box_x + box_size_w + (box_size_w / 2))), int((box_y + (box_size_h / 2))))
        screen.blit(textsurface, textRect)

        if mouse[0] > box_x + (3 * box_size_w) and mouse[0] < box_x + (4 * box_size_w) and mouse[1] > box_y and mouse[
            1] < box_y + box_size_h:
            pygame.draw.rect(screen, white, (box_x + (3 * box_size_w), box_y, box_size_w, box_size_h))
            if click == (1, 0, 0):
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(screen, black, (box_x + (3 * box_size_w), box_y, box_size_w, box_size_h))

        # calling of EXIT text button
        smalltext = pygame.font.SysFont("freesansbold.++f", 20, bold=True)
        textsurface, textRect = text_object("EXIT", smalltext)
        textRect.center = (int((box_x + (3 * box_size_w) + (box_size_w / 2))), int((box_y + (box_size_h / 2))))
        screen.blit(textsurface, textRect)

        if mouse[0] > 510 and mouse[0] < 660 and mouse[1] > 130 and mouse[1] < 180:
            pygame.draw.rect(screen, white, (deve_box_x, deve_box_y, box_size_w, box_size_h))
            if click == (1, 0, 0):
                Developer()

        else:
            pygame.draw.rect(screen, black, (deve_box_x, deve_box_y, box_size_w, box_size_h))

        # calling of DEVELOPER text button
        smalltext = pygame.font.SysFont("freesansbold.++f", 20, bold=True)
        textsurface, textRect = text_object("DEVELOPER", smalltext)
        textRect.center = (int((deve_box_x + (box_size_w / 2))), int((deve_box_y + (box_size_h / 2))))
        screen.blit(textsurface, textRect)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

# pause function definitions part
def pause():
    flag = True
    global countdown
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(instruction_background, (0, 0))
        text_screen("PAUSED", black, 115, "freeshansbold.++f", 400, 150)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # for continue button
        if mouse[0] > 110 and mouse[0] < 260 and mouse[1] > 200 and mouse[1] < 250:
            pygame.draw.rect(screen, white, (110, 200, 150, 50))
            if click == (1, 0, 0):
                flag = False
        else:
            pygame.draw.rect(screen, black, (110, 200, 150, 50))

        # calling of Continue text button
        smalltext = pygame.font.SysFont("freesansbold.++f", 20, bold=True)
        textsurface, textRect = text_object("RESUME", smalltext)
        textRect.center = (int((110 + (150 / 2))), int((200 + (50 / 2))))
        screen.blit(textsurface, textRect)

        # for restart button
        if mouse[0] > 310 and mouse[0] < 460 and mouse[1] > 300 and mouse[1] < 350:
            pygame.draw.rect(screen, white, (310, 300, 150, 50))
            if click == (1, 0, 0):
                game_loop()
        else:
            pygame.draw.rect(screen, black, (310, 300, 150, 50))

        # calling of restart text button
        smalltext = pygame.font.SysFont("freesansbold.++f", 20, bold=True)
        textsurface, textRect = text_object("RESTART", smalltext)
        textRect.center = (int((310 + (150 / 2))), int((300 + (50 / 2))))
        screen.blit(textsurface, textRect)

        # for mainmenu button
        if mouse[0] > 510 and mouse[0] < 660 and mouse[1] > 400 and mouse[1] < 450:
            pygame.draw.rect(screen, white, (510, 400, 150, 50))
            if click == (1, 0, 0):
                starting_loop()
        else:
            pygame.draw.rect(screen, black, (510, 400, 150, 50))

        # calling of mainmenu text button
        smalltext = pygame.font.SysFont("freesansbold.++f", 20, bold=True)
        textsurface, textRect = text_object("MAIN MENU", smalltext)
        textRect.center = (int((510 + (150 / 2))), int((400 + (50 / 2))))
        screen.blit(textsurface, textRect)

        pygame.display.update()


# function for enemy car
def obstacle(obs_x, obs_y, obs):
    global obs_pic
    if obs == 0:
        obs_pic = list_cars[0]
    elif obs == 1:
        obs_pic = list_cars[1]
    elif obs == 2:
        obs_pic = list_cars[2]
    elif obs == 3:
        obs_pic = list_cars[3]
    elif obs == 4:
        obs_pic = list_cars[4]
    elif obs == 5:
        obs_pic = list_cars[5]
    elif obs == 6:
        obs_pic = list_cars[6]

    screen.blit(obs_pic, (int(obs_x), int(obs_y)))

#function for enemy truck
def truck(t_x, t_y, t):
    global t_pic
    global s_truck
    if t == 0:
        t_pic = truck_1
    elif t== 1:
        t_pic = truck_2
    elif t== 2:
        t_pic = truck_3
    screen.blit(t_pic, (int(t_x), int(t_y)))


#function for enemy bike
def bike(b_x, b_y, b):
    global b_pic
    global s_bike
    if b == 0:
        b_pic = bike_1
    elif b == 1:
        b_pic = bike_2
    elif b == 2:
        b_pic = bike_3
    screen.blit(b_pic, (int(b_x), int(b_y)))


# image appearing
def background():
    screen.blit(backimg, (0, 0))
    screen.blit(grass, (-100, 0))
    screen.blit(grass, (757, 0))

def Developer():
    flag_d = True
    while flag_d:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(developer,(0,0))
        # creating back button

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if mouse[0] > 945 and mouse[0] < 1095 and mouse[1] > 20 and mouse[1] < 70:
            pygame.draw.rect(screen, white, (945, 20, 150, 50))
            if click == (1, 0, 0):
                flag_d = False
        else:
            pygame.draw.rect(screen, black, (945, 20, 150, 50))

        # calling of BACK text button
        smalltext = pygame.font.SysFont("freesansbold.++f", 20, bold=True)
        textsurface, textRect = text_object("BACK", smalltext)
        textRect.center = (int((945 + (150 / 2))), int((20 + (50 / 2))))
        screen.blit(textsurface, textRect)

        pygame.display.update()

def controller():
    flag_c = True
    while flag_c:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(control, (0, 0))
        # creating back button

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if mouse[0] > 945 and mouse[0] < 1095 and mouse[1] > 20 and mouse[1] < 70:
            pygame.draw.rect(screen, white, (945, 20, 150, 50))
            if click == (1, 0, 0):
                flag_c = False
        else:
            pygame.draw.rect(screen, black, (945, 20, 150, 50))

        # calling of BACK text button
        smalltext = pygame.font.SysFont("freesansbold.++f", 20, bold=True)
        textsurface, textRect = text_object("BACK", smalltext)
        textRect.center = (int((945 + (150 / 2))), int((20 + (50 / 2))))
        screen.blit(textsurface, textRect)

        pygame.display.update()

def car(x, y):
    screen.blit(list_cars[car_num], (x, y))


def wreck():

    pygame.mixer.stop()
    ch3.play(car_crash_music, maxtime = 2000)

    crash = True
    while crash:
        screen.blit(crash_img, (0, 0))
        text_screen("Press enter to go to main menu", black, 50, None, 5, int(height / 1.5))
        text_screen("Press space to play again", black, 50, None, 5, int(height / 2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    starting_loop()
                if event.key == pygame.K_SPACE:
                    game_loop()

        pygame.display.update()

# the gameloop
flag = False

def game_loop():
    global event, moving_y
    global flag
    global countdown
    global timer
    global car_passed
    global point
    global invisible
    global used_invi
    global s_truck
    global s_bike

    pygame.mixer.stop()
    ch2.play(game_music, -1)

    use_invi = 0
    car_passed = 0
    x_change = 0
    x = int(width / 2) - 50
    y = height - 160
    obstacle_speed = 12
    obs = 0
    obs_x = random.randrange(200, 400)
    obs_y = -750
    t= 0
    t_x = random.randrange(450, 850)
    t_y = -750
    bike_height = 111
    bike_width = 50
    truck_height = 250
    truck_width = 91
    enemy_width = 70
    enemy_height = 117
    level_s = 0
    score = 0
    level = 0
    y2 = 10
    countdown = 1
    timer = time.time()
    power_time = 0
    multi = 0
    rotate = 0
    choice = random.randint(0, 1)

    if used_invi:
        invisible = False
        used_invi = False

    if (not os.path.exists("high_score.txt")):
        with open("high_score.txt", "w") as f:
            f.write("0")

    with open("high_score.txt", "r") as f:
        hiscore = f.read()

    while not flag:

        if countdown != 0:
            if countdown == 1:
                countdown = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = True
                # moving in x-y cordinates
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -5
                        rotate = 1
                    if event.key == pygame.K_RIGHT:
                        x_change = 5
                        rotate = 2
                    if event.key == pygame.K_q:
                        car_passed += 1
                    if event.key == pygame.K_w:
                        obstacle_speed -= 2

                    if invisible and multi == 0:
                        if event.key == pygame.K_e:
                            use_invi = 1
                            power_time = time.time()
                            multi = 1

                    if event.key == pygame.K_SPACE:
                        ch4.pause()
                        ch5.pause()
                        pause()
                        ch4.unpause()
                        ch5.unpause()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0
                        rotate = 0

            x += x_change

            # background moving
            moving_y = y2 % grass.get_rect().width
            screen.blit(grass, (-100, moving_y) )
            screen.blit(grass, (1057, moving_y ))
            screen.blit(backimg, (0, moving_y))
            screen.blit(grass, (-100, moving_y))
            screen.blit(grass, (1057, moving_y))

            y2 += obstacle_speed

            # calling background function
            obs_y -= (obstacle_speed / 4)
            obstacle(obs_x, obs_y, obs)
            obs_y += obstacle_speed

            t_y -= (obstacle_speed/4)
            t_y += obstacle_speed

            # calling car function
            if choice == 0:
                truck(t_x, t_y, t)
            else:
                bike(t_x, t_y, t)
            if rotate == 0:
                car(x, y)
            elif rotate == 1:
                rotate_car = pygame.transform.rotate(list_cars[car_num], 12)
                screen.blit(rotate_car, (x, y))
            else:
                rotate_car = pygame.transform.rotate(list_cars[car_num], -12)
                screen.blit(rotate_car, (x, y))

            if x > 1057 - car_width or x < 35:
                with open("high_score.txt", "w") as f:
                    f.write(str(hiscore))
                point = int(point) + car_passed
                with open("point.txt", "w") as p:
                    p.write(str(point))
                wreck()

            if obs_y > height:
                obs_y = 0 - enemy_height
                obs_x = random.randrange(70, width - 130)
                while t_x + 100 > obs_x and t_x - 100 < obs_x:
                    obs_x = random.randrange(70, width - 130)
                obs = random.randrange(0, 7)
                car_passed += 1
                level_s += 1
                score = score + 10
                if score > int(hiscore):
                    hiscore = score

            text_screen("SCORES: " + str(score), (0, 0, 0), 35, None, 100, 70)
            text_screen("HIGH SCORE: " + str(hiscore), black, 35, None, 100, 20)

            if level_s == 10:
                level += 1
                level_s = 0
                obstacle_speed += 2
                text_screen("LEVEL", (0, 0, 0), 100, None, int(width / 2.4), int(height / 2.5))
                text_screen(str(level), (0, 0, 0), 150, None, int(width / 2.1), int(height / 2))
                pygame.display.update()
                speak("Upgrading to level" + str(level))
                if level == 3:
                    ch4.stop()
                    ch5.play(car_speed_music, -1)

            if t_y > height:
                t_y = 0 - truck_height
                t_x = random.randrange(170, width-170)
                choice = random.randint(0, 1)
                t = random.randrange(0, 3)
                while t_x + 100 > obs_x and t_x - 100 < obs_x:
                    t_x = random.randrange(170, width - 170)

            if (not invisible) or ((invisible) and use_invi != 1):
                if y < obs_y + enemy_height:
                    if x >= obs_x and x <= obs_x + enemy_width or x + car_width >= obs_x and x + car_width <= obs_x + enemy_width:
                        with open("high_score.txt", "w") as f:
                            f.write(str(hiscore))
                        point = int(point) + car_passed
                        with open("point.txt", "w") as p:
                            p.write(str(point))
                        wreck()

                if choice == 0:
                    if y < t_y + truck_height:
                        if x >= t_x and x <= t_x + truck_width or x + car_width >= t_x and x + car_width <= t_x + truck_width:
                            wreck()
                else:
                    if y < t_y + bike_height:
                        if x >= t_x and x <= t_x + bike_width or x + car_width >= t_x and x + car_width <= t_x + bike_width:
                            wreck()
            else:
                if time.time() - power_time > 10:
                    if y < obs_y + enemy_height:
                        if x >= obs_x and x <= obs_x + enemy_width or x + car_width >= obs_x and x + car_width <= obs_x + enemy_width:
                            with open("high_score.txt", "w") as f:
                                f.write(str(hiscore))
                            point = int(point) + car_passed
                            with open("point.txt", "w") as p:
                                p.write(str(point))
                            wreck()

                    if choice == 0:
                        if y < t_y + truck_height:
                            if x >= t_x and x <= t_x + truck_width or x + car_width >= t_x and x + car_width <= t_x + truck_width:
                                wreck()
                    else:
                        if y < t_y + bike_height:
                            if x >= t_x and x <= t_x + bike_width or x + car_width >= t_x and x + car_width <= t_x + bike_width:
                                wreck()
                else:
                    text_screen("Invisible enabled", black, 50, None, width - 400, 60)
                    text_screen(str(10 - int(time.time() - power_time)), black, 50, None, width - 250, 100)
                    used_invi = True

        else:
            screen.blit(backimg, (0, moving_y))
            car(x, y)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = True
            if time.time() - timer <= 1:
                text_screen("3", black, 100, None, int(width / 2) - 20, int(height / 2) - 30)
            elif time.time() - timer <= 2:
                text_screen("2", black, 100, None, int(width / 2) - 20, int(height / 2) - 30)
            elif time.time() - timer <= 3:
                text_screen("1", black, 100, None, int(width / 2) - 20, int(height / 2) - 30)
            elif time.time() - timer <= 4:
                text_screen("GO!!", black, 100, None, int(width / 2) - 80, int(height / 2) - 30)
            else:
                countdown = 2
                ch4.play(car_start_music, -1)

        # updating the game
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

# calling of starting screen loop
if __name__ == "__main__":
    if (not os.path.exists("point.txt")):
        with open("point.txt", "w") as p:
            p.write("0")

    with open("point.txt", "r") as p:
        point = p.read()

    ch1 = pygame.mixer.Channel(0)
    ch2 = pygame.mixer.Channel(1)
    ch3 = pygame.mixer.Channel(2)
    ch4 = pygame.mixer.Channel(2)
    ch5 = pygame.mixer.Channel(2)

    start_music = pygame.mixer.Sound("start_bg.wav")
    start_music.set_volume(.2)
    game_music = pygame.mixer.Sound("loop_music.wav")
    game_music.set_volume(.15)
    car_crash_music = pygame.mixer.Sound("car_crash_glass.wav")
    car_crash_music.set_volume(.5)
    car_start_music = pygame.mixer.Sound("car_start.wav")
    car_start_music.set_volume(.08)
    car_speed_music = pygame.mixer.Sound("car_speed.wav")
    car_speed_music.set_volume(.09)

    starting_loop()
    pygame.quit()
    quit()

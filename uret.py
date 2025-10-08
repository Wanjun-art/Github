# import necessary libraries
import pygame
import math # for trigonometric functions
from datetime import datetime # to get current time

# initialize pygame
pygame.init()

# set up display
Screen_Width = 800
Screen_Height = 640 
screen=pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Analog uret")  

# define colors
Black=(0,0,0)
White=(255,255,255)
Red=(255,0,0)
Gray=(128,128,128)

# set up clock for controlling frame rate
clock=pygame.time.Clock()

# define center and radius
center_x=Screen_Width//2
center_y=Screen_Height//2
clock_radius=250

def draw_clock_face(surface):
    # draw clock face
    pygame.draw.circle(surface, White, (center_x, center_y), clock_radius, 5)
    # draw black dial border
    pygame.draw.circle(surface, Black, (center_x, center_y), 9)
    # draw center circle
    pygame.draw.circle(surface, White, (center_x, center_y), 7)
    
    # draw hour numbers and minute ticks
    # set up font
    font=pygame.font.SysFont('Arial', 40)
    for i in range(1,13):
        # calculate angle for each hour number
        # 0 hours = -90 degrees (pointing up)
        # math.pi/6 = 30 degrees and we subtract math.pi/2 to start from the top
        angle=i*math.pi/6 - math.pi/2
        # calculate position for each hour number
        # 0.8 is to position the numbers slightly inside the clock face
        x=center_x + int(clock_radius * 0.8 * math.cos(angle))
        y=center_y + int(clock_radius * 0.8 * math.sin(angle))
        # render and position the hour number
        text_surface=font.render(str(i), True, White)
        text_rect=text_surface.get_rect(center=(x,y))
        # draw the hour number on the surface
        surface.blit(text_surface, text_rect)
    # draw minute ticks
    for i in range(60):
        angle=i*math.pi/30 - math.pi/2
        # calculate start and end positions for each tick
        start_pos_x=center_x + int((clock_radius-5) * math.cos(angle))
        start_pos_y=center_y + int((clock_radius-5) * math.sin(angle))
        # every 5th tick is clear (for hours)
        if i % 5 == 0:
            end_pos_x=center_x+(clock_radius-30)*math.cos(angle)
            end_pos_y=center_y+(clock_radius-30)*math.sin(angle)
            pygame.draw.line(screen, White, (start_pos_x, start_pos_y), (end_pos_x, end_pos_y), 5)
    
        else:
            pygame.draw.line(surface, Gray, (start_pos_x, start_pos_y), (end_pos_x, end_pos_y), 2)

# main loop
running=True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    # get current time
    now=datetime.now()
    hour=now.hour % 12
    minute=now.minute
    second=now.second

    # clear screen
    screen.fill(Black)
    # draw clock face
    draw_clock_face(screen)

    # calculate angles for each hand
    # hour angle: each hour is 30 degrees, plus minute/60 of that
    # minute angle: each minute is 6 degrees, plus second/60 of that    
    # second angle: each second is 6 degrees
    # / 60 to convert to minutes or seconds
    hour_angle=(hour + minute / 60) * 30 - 90
    minute_angle=(minute + second / 60) * 6 - 90
    second_angle=second * (360/60) - 90

    # draw hands
    hour_x=center_x + int(clock_radius * 0.5 * math.cos(math.radians(hour_angle)))
    hour_y=center_y + int(clock_radius * 0.5 * math.sin(math.radians(hour_angle)))
    pygame.draw.line(screen, White, (center_x, center_y), (hour_x, hour_y), 10)

    minute_x=center_x + int(clock_radius * 0.7 * math.cos(math.radians(minute_angle)))
    minute_y=center_y + int(clock_radius * 0.7 * math.sin(math.radians(minute_angle)))
    pygame.draw.line(screen, White, (center_x, center_y), (minute_x, minute_y), 6)

    second_x=center_x + int(clock_radius * 0.9 * math.cos(math.radians(second_angle)))
    second_y=center_y + int(clock_radius * 0.9 * math.sin(math.radians(second_angle)))
    pygame.draw.line(screen, Red, (center_x, center_y), (second_x, second_y), 2)

    # update display
    pygame.display.flip()
    # control frame rate
    clock.tick(60)

# quit pygame
pygame.quit()
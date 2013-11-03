import pygame
import mandel

pygame.init()

black = [0, 0, 0]
white = [255, 255, 255]

width = 1280
height = 800

screen=pygame.display.set_mode([width, height])
pygame.display.set_caption("HAVE A MANDEL")

resolution = 1

width_r = int(width / resolution)
height_r = int(height / resolution)

print("Operating a %s x %s screen" % (width_r, height_r))

# Draw screen once
screen.fill(white)

def draw_mandel_section(real_length, real_offset, imag_length, imag_offset):
    for i in range(width_r):
        for j in range(height_r):
            real = ((i / width_r) * real_length) - real_offset
            imag = ((j / height_r) * imag_length) - imag_offset
            is_m, iterations = mandel.is_in_mandelbrot_set(complex(real, imag))
            if is_m:
                color = black
            else:
                r = round((iterations / mandel.max_iterations) * 255)
                g = round((iterations / mandel.max_iterations) * 150)
                b = round((iterations / mandel.max_iterations) * 150)
                color = [r, g, b]
            x = round((i / width_r) * width)
            y = round((j / height_r) * height)
            if resolution == 1:
                pygame.draw.circle(screen, color, [x, y], 0)
            else:
                rect = pygame.Rect(x, y, resolution, resolution)
                pygame.draw.rect(screen, color, rect)
        pygame.display.flip()

draw_mandel_section(3, 2, 2, 1)

# Start game
loop=True
while(loop):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            loop = False
    # pygame.display.flip()

pygame.quit()

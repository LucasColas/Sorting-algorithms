import pygame

Width, Height = 1500,700

Window = pygame.display.set_mode((Width, Height))

def update_window(Window):
    Window.fill((255,255,255))
    pygame.display.update()



def main():

    run = True

    while run:
        update_window(Window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                run = False

main()

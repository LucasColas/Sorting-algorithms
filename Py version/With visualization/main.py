import pygame

Width, Height = 1500,700

Window = pygame.display.set_mode((Width, Height))


def main():

    run = True

    while run:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                run = False

main()

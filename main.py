import pygame

white = (255, 255, 255)

Width, height = 900, 500

screen = pygame.display.set_mode((Width, height))

pygame.display.set_caption("Roter Baron Game")

fps = 60




def draw(): 
    screen.fill(white)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw()
    
    pygame.quit()
    
    
if __name__ == "__main__":
    main()
import pygame


class Button:
    def __init__(self, x, y, width, height, text, color, text_color=(255, 255, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.font = pygame.font.Font(None, 21)  # Police par défaut, taille 36

    def draw(self, screen):
        # Dessiner le rectangle
        pygame.draw.rect(screen, self.color, self.rect)

        # Dessiner le texte centré
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)


def main():
    pygame.init()
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    width = 500
    height = 500
    screen = pygame.display.set_mode((width, height))

    clock = pygame.time.Clock()
    running = True
    list_elmt = ["test1", "test2", "test3"]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        y = 50
        for element in list_elmt:

            button = Button(50, y, 150, 60, element, BLUE)
            button.draw(screen)
            y = y + 100
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()

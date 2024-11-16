import pygame
import random

from pygame import MOUSEBUTTONDOWN


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        score = 0
        mole_x = 16
        mole_y = 16
        clock = pygame.time.Clock()
        screen.fill("light green")
        if score == 0:
            screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_x, click_y = event.pos
                    if mole_x - 16 <= click_x <= mole_x + 16 and mole_y - 16 <= click_y <= mole_y + 16:
                        mole_x = random.randrange(0, 641)
                        mole_y = random.randrange(0, 513)
                        mole_x = (mole_x // 32) * 32 + 16
                        mole_y = (mole_y // 32) * 32 + 16
                        screen.fill("light green")
                        screen.blit(mole_image, mole_image.get_rect(center = (mole_x, mole_y)))
                        score += 1

            for i in range(0, 32):
                pygame.draw.line(screen, "black", (32 * i, 0), (32 * i, 512))
            for i in range(0, 32):
                pygame.draw.line(screen, "black", (0, 32 * i), (640, 32 * i))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

import pygame
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 32
WORLD_WIDTH = 50
WORLD_HEIGHT = 25

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Terraria-like Game")
clock = pygame.time.Clock()

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = 5

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        if keys_pressed[pygame.K_UP]:
            self.rect.y -= self.velocity
        if keys_pressed[pygame.K_DOWN]:
            self.rect.y += self.velocity

# World Class
class World:
    def __init__(self):
        self.tiles = self.generate_world()

    def generate_world(self):
        tiles = []
        for y in range(WORLD_HEIGHT):
            row = []
            for x in range(WORLD_WIDTH):
                tile_type = "grass" if y > WORLD_HEIGHT // 2 else "dirt"
                row.append(tile_type)
            tiles.append(row)
        return tiles

    def draw(self, screen):
        for y, row in enumerate(self.tiles):
            for x, tile_type in enumerate(row):
                if tile_type == "grass":
                    color = GREEN
                else:
                    color = BROWN
                pygame.draw.rect(screen, color, pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

# Game Class
class Game:
    def __init__(self):
        self.world = World()
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.all_sprites = pygame.sprite.Group(self.player)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys_pressed = pygame.key.get_pressed()
            self.player.update(keys_pressed)
            self.draw()

            clock.tick(60)

    def draw(self):
        screen.fill(BLACK)
        self.world.draw(screen)
        self.all_sprites.draw(screen)
        pygame.display.flip()

# Main Game Loop
def main():
    game = Game()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()

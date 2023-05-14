import pygame, sys


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.clock = pygame.time.Clock()
        self.speed = 2
        self.fps = 20
        self.world_map = 0
        self.menu = False

        self.player = pygame.Rect(100, 200, 64, 64)
        self.house_block = pygame.Rect(-50, -200, 400, 400)
        self.collision_list = [self.house_block.x]
        self.world_image = pygame.image.load(
            f"world_img/map2.png").convert_alpha()
        self.world_x = -1500
        self.world_y = -850

    def World(self, x, y):
        self.screen.blit(self.world_image, (x, y))

    def vänster(self):
        self.world_x += self.speed
        self.house_block.x += self.speed

    def höger(self):
        self.world_x -= self.speed
        self.house_block.x -= self.speed

    def upp(self):
        self.world_y += self.speed
        self.house_block.y += self.speed

    def ner(self):
        self.world_y -= self.speed
        self.house_block.y -= self.speed

    def text_objects(self, text, font):
        self.textsurface = font.render(text, True, (0, 0, 0))
        return self.textsurface, self.textsurface.get_rect()

    def message_display(self, text):
        self.largeText = pygame.font.Font('freesansbold.ttf', 20)
        self.TextSurf, self.TextRect = self.text_objects(text, self.largeText)
        self.TextRect.center = ((100, 100))
        self.screen.blit(self.TextSurf, self.TextRect)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):
        self.screen.fill((255, 255, 0))
        if self.world_map == 0:
            self.World(self.world_x, self.world_y)

        pygame.draw.rect(self.screen, (0, 200, 200), self.player, 3)
        pygame.draw.rect(self.screen, (0, 200, 200), self.house_block, 3)

    def update(self):
        self.clock.tick(self.fps)
        pygame.display.flip()
        self.player.centerx = 250
        self.player.centery = 250

        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_LEFT]:
            self.vänster()
            if self.player.colliderect(self.house_block):
                self.höger()
        if self.keys[pygame.K_RIGHT]:
            self.höger()
        if self.keys[pygame.K_UP]:
            self.upp()
        if self.keys[pygame.K_DOWN]:
            self.ner()

        if self.keys[pygame.K_c]:
            self.menu = True
            self.message_display("Hello")

    def run(self):
        while True:
            self.events()
            self.draw()
            self.update()
            #self.text_objects()
            self.message_display("hello")


if __name__ == "__main__":
    game = Game()
    game.run()

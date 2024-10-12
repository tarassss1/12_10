import pygame 
pygame.init()

window = pygame.display.set_mode((500,500))
background = pygame.image.load("photo.jpg")
background = pygame.transform.scale(background,(500,500))

class Player:
    def __init__(self,x,y,width,height,image):
        self.image = pygame.image.load(image) # завантажуємо зображення
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect(topleft=(x,y))
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 10
        if keys[pygame.K_s]:
            self.rect.y += 10  
        if keys[pygame.K_d]:
            self.rect.x += 10
        if keys[pygame.K_w]:
            self.rect.y -= 10

player = Player(100,100,100,100,"bird.png") # removebg

game = True
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    #window.fill((0,255,0)) 
    window.blit(background, (0,0))
    window.blit(player.image, player.rect)
    player.move()

    pygame.display.update()
    pygame.time.Clock().tick(60)

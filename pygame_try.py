import pygame
    
class GuidyGonzales:
    def __init__(self):
        self.pygame = pygame
        self.pygame.init()
        
        # Initialling color
        self.green = [0, 255, 0]
        self.red = [255, 0, 0]
        
        # set the screen.
        self.screen = self.pygame.display.set_mode([800,600])
        self.screen.fill(self.green)
        
        self.pygame.display.set_caption("Guidy Gonzales")
        
        # Drawing square.
        self.player = self.pygame.draw.rect(self.screen, self.red, self.pygame.Rect(30,30,30,30))
        
        self.pygame.display.flip()
        
        # Create clock.
        self.clock = pygame.time.Clock()
        
    def move_square(self):
        pass
    
    def handle_keys(self):
        """Handle when key pressed"""
        #https://www.pygame.org/docs/ref/key.html
        key = self.pygame.key.get_pressed()
        
        # Close the program if escape is pressed.
        if key[pygame.K_ESCAPE]:
            return False
        
        
        
        return True
            
    
    def main(self):
        run = True
        while run:
            self.pygame.event.get()
            run = self.handle_keys()
            
        self.pygame.display.quit()
        self.pygame.QUIT
                
    
    def main_back(self):
        """"""
        while self.player.x < self.screen.get_width():
            self.pygame.event.pump()
            self.player.move_ip(30,0)
            print(self.player)
            print(self.player.x)
            
            # Wait for 1 sec
            self.clock.tick(1)
            
            self.screen.fill(self.green)
            self.pygame.draw.rect(self.screen, self.red, self.player, 0)
            self.pygame.display.update()
        
        self.pygame.display.quit()
        self.pygame.QUIT
        

if __name__ == "__main__":
    game = GuidyGonzales()
    #game.main_back()
    game.main()


"""
size = width, height = 320, 240
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
"""
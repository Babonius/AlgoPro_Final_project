import pygame
pygame.init

class healths:
    def __init__(self):
        font_med = pygame.font.Font('AlgoPro_Final/Font/Pixeltype.ttf', 40)

        self.image = pygame.Surface((40,40))
        self.image.fill((240,240,240))
        self.rect = self.image.get_rect(center = (600,600))
        self.current_health = 100
        self.max_health = 100
        self.health_bar = 200
        self.health_ratio = self.max_health/self.health_bar

        self.image_a = pygame.Surface((40,40))
        self.image_a.fill((240,240,240))
        self.rect_a = self.image_a.get_rect(center = (600,600))
        self.current_a_health = 150
        self.max_a_health = 150
        self.health_a_bar = 200
        self.health_a_ratio = self.max_a_health/self.health_a_bar

        self.image_j = pygame.Surface((40,40))
        self.image_j.fill((240,240,240))
        self.rect_j = self.image_j.get_rect(center = (600,600))
        self.current_j_health = 200
        self.max_j_health = 200
        self.health_j_bar = 200
        self.health_j_ratio = self.max_j_health/self.health_j_bar

        self.image_m = pygame.Surface((40,40))
        self.image_m.fill((240,240,240))
        self.rect_m = self.image_m.get_rect(center = (600,600))
        self.current_m_health = 100
        self.max_m_health = 100
        self.health_m_bar = 200
        self.health_m_ratio = self.max_m_health/self.health_m_bar

        self.hp_txt = font_med.render("hp:",False,"black")
        self.hp_txt_rect = self.hp_txt.get_rect(center = (30,60))

        self.hp_m_txt = font_med.render("hp:",False,"black")
        self.hp_m_txt_rect = self.hp_m_txt.get_rect(center = (490,460))

        self.hp_m_txt_rect2 = self.hp_m_txt.get_rect(center = (540,50))

        #Health buff
        self.health_surf = pygame.image.load('AlgoPro_Final/Graphics/map/heart_pixelart.png').convert_alpha()
        self.health_surf_rect = self.health_surf.get_rect(center = (-220,55))

        self.health_surf2 = pygame.image.load('AlgoPro_Final/Graphics/map/heart_pixelart.png').convert_alpha()
        self.health_surf_rect2 = self.health_surf.get_rect(center = (920,55))
        

    def damaged(self,amount):
        if self.current_health > 0:
             self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0
    
    def pra_health(self,screen):
        pygame.draw.rect(screen, 'black', pygame.Rect(68, 48, 204, 24))
        pygame.draw.rect(screen, 'green', pygame.Rect(70, 50, 200, 20))
        pygame.draw.rect(screen,(255,0,0),(70,50,self.current_health/self.health_ratio,20))

        screen.blit(self.hp_txt,self.hp_txt_rect)

    def ari_damaged(self,amount):
        if self.current_a_health > 0:
             self.current_a_health -= amount
        if self.current_a_health <= 0:
            self.current_a_health = 0

    def ari_health(self,screen):
        pygame.draw.rect(screen, 'black', pygame.Rect(68, 48, 204, 24))
        pygame.draw.rect(screen, 'green', pygame.Rect(70, 50, 200, 20))
        pygame.draw.rect(screen,(255,0,0),(70,50,self.current_a_health/self.health_a_ratio,20))

        screen.blit(self.hp_txt,self.hp_txt_rect)
    
    def jude_health(self,screen):
        pygame.draw.rect(screen, 'black', pygame.Rect(68, 48, 204, 24))
        pygame.draw.rect(screen, 'green', pygame.Rect(70, 50, 200, 20))
        pygame.draw.rect(screen,(255,0,0),(70,50,self.current_j_health/self.health_j_ratio,20))

        screen.blit(self.hp_txt,self.hp_txt_rect)
    
    def jude_damaged(self,amount):
        if self.current_j_health > 0:
             self.current_j_health -= amount
        if self.current_j_health <= 0:
            self.current_j_health = 0
    
    def mink_damaged(self,amount):
        if self.current_m_health > 0:
             self.current_m_health -= amount
        if self.current_m_health <= 0:
            self.current_m_health = 0
    
    def mink_healed(self,amount):
        if self.current_m_health < self.max_m_health:
            self.current_m_health += amount
        if self.current_m_health >= self.max_m_health:
            self.current_m_health = self.max_m_health

    def mink_health(self,screen):
        pygame.draw.rect(screen, 'black', pygame.Rect(528, 448, 204, 24))
        pygame.draw.rect(screen, 'green', pygame.Rect(530, 450, 200, 20))
        pygame.draw.rect(screen,(255,0,0),(530,450,self.current_m_health/self.health_m_ratio,20))

        screen.blit(self.hp_m_txt,self.hp_m_txt_rect)
    
    def mink_health_surf(self,screen):
        pygame.draw.rect(screen, 'black', pygame.Rect(578, 38, 204, 24))
        pygame.draw.rect(screen, 'green', pygame.Rect(580, 40, 200, 20))
        pygame.draw.rect(screen,(255,0,0),(580,40,self.current_m_health/self.health_m_ratio,20))

        screen.blit(self.hp_m_txt,self.hp_m_txt_rect2)

    def health_gain(self,screen):
        screen.blit(self.health_surf,self.health_surf_rect)

    def health_gain2(self,screen):
        screen.blit(self.health_surf2,self.health_surf_rect2)
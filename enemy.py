import pygame
pygame.init

class enemies:

    screen = pygame.display.set_mode((800,720))

    def __init__(self):
        font_txt = pygame.font.Font('AlgoPro_Final/Font/Pixeltype.ttf', 27)
        font_big = pygame.font.Font('AlgoPro_Final/Font/Pixeltype.ttf', 50)
        font_med = pygame.font.Font('AlgoPro_Final/Font/Pixeltype.ttf', 40)
        
        self.fight_back = pygame.image.load('AlgoPro_Final/Graphics/map/fight_background.jpg')
        self.fight_back = pygame.transform.scale_by(self.fight_back,1.5)

        #Characters
    
        #minka fight
        self.mink_b = pygame.image.load('AlgoPro_Final/Graphics/Characters/back_minka.png').convert_alpha()
        self.mink_b = pygame.transform.scale_by(self.mink_b,12)
        self.mink_b_rect = self.mink_b.get_rect(center = (200,430))

        #Pra
        self.enemyPra = pygame.image.load('AlgoPro_Final/Graphics/Characters/npc/pra-npc.png').convert_alpha()
        self.Pra_rect = self.enemyPra.get_rect(center = (54,262))
        self.enemyPra = pygame.transform.scale_by(self.enemyPra,3)

        self.big_pra = pygame.image.load('AlgoPro_Final/Graphics/Characters/npc/pixelated_pra.png').convert_alpha()
        self.big_pra_rect = self.big_pra.get_rect(center = (600,222))

        #Ariel
        self.enemyAri = pygame.image.load('AlgoPro_Final/Graphics/Characters/npc/ari_npc.png').convert_alpha()
        self.Ari_rect = self.enemyAri.get_rect(center = (810,432))
        self.enemyAri = pygame.transform.scale_by(self.enemyAri,3)

        self.big_ari = pygame.image.load('AlgoPro_Final/Graphics/Characters/npc/pixelated_ari.png').convert_alpha()
        self.big_ari = pygame.transform.scale_by(self.big_ari,1.2)
        self.big_ari_rect = self.big_ari.get_rect(center = (600,222))

        #jude Mr
        self.jude = pygame.image.load('AlgoPro_Final/Graphics/Characters/npc/jude.png').convert_alpha()
        self.jude_rect = self.jude.get_rect(center = (-20,785))
        self.jude = pygame.transform.scale_by(self.jude,3)

        self.big_jude = pygame.image.load('AlgoPro_Final/Graphics/Characters/npc/pixelated_jude.png').convert_alpha()
        self.big_jude_rect = self.big_jude.get_rect(center = (600,222))
        self.big_jude = pygame.transform.scale_by(self.big_jude,1.2)

        #mr jude dialoge

        self.judename = font_txt.render("B o s s  J u d e : ",False,"White")
        self.judename_rect = self.judename.get_rect(topleft = (60,550))
        self.Djude = font_txt.render("H U H  A R E  Y O U  A P P R O A C H I N G  M E ? !",False,"White")
        self.Djude_rect = self.Djude.get_rect(center = (400,590))

        self.Djude2 = font_txt.render("N O T  W O R T H Y  T O  C H A L L E N G E  T H Y ! G O  F I G T H  A R I E L  I N F R O N T  O F  T H E  G Y M!",False,"White")
        self.Djude2_rect = self.Djude2.get_rect(center = (400,595))

        self.judeNamef = font_med.render("B o s s  J u d e:",False,"black")
        self.judeNamef_rect = self.judeNamef.get_rect(topleft = (10,10))

        #fighting UI
        self.fight_txt = font_med.render("What will you do?",False,"Black")
        self.fight_txt_rect = self.fight_txt.get_rect(center = (200,600))

        self.scratch_txt = font_big.render("SCRATCH",False,"White")
        self.scratch_txt_rect = self.scratch_txt.get_rect(center = (465,560))
        self.paw_txt = font_big.render("PAW",False,"White")
        self.paw_txt_rect = self.paw_txt.get_rect(center = (635,560))
        self.leave_txt = font_big.render("LEAVE THIS HUMAN",False,"White")
        self.leave_txt_rect = self.leave_txt.get_rect(center = (552,650))

        self.scratch_box = pygame.Rect(390, 520, 150, 75)
        self.paw_box = pygame.Rect(560, 520, 150, 75)
        self.leave_box = pygame.Rect(390, 610, 320, 75)
        

        #E button
        self.E_pop = pygame.image.load('AlgoPro_Final/Graphics/Buttons/E-Key.png').convert_alpha()
        self.E_rect = self.E_pop.get_rect(center = (440,310))

        #Fight and Go away button
        self.fight = font_big.render("FIGHT!",False,"White")
        self.fight_rect = self.fight.get_rect(center = (150,500))

        self.red_fight = pygame.Rect(50, 470, 200, 50)

        self.leave = font_txt.render("*Press E to leave this human*",False,"White")
        self.leave_rect = self.leave.get_rect(center = (400,630))

        self.leave_fight = font_txt.render("*Press E to leave this human*",False,"Black")
        self.leave_fight_rect = self.leave.get_rect(center = (400,450))

        #Pra dialogue
        self.praName = font_txt.render("Pranav: ",False,"White")
        self.praName_rect = self.praName.get_rect(topleft = (60,550))
        self.Dpra = font_txt.render("Aww look at this cute cat ! I wonder what it's doing out here? I'm going to take it home!",False,"White")
        self.Dpra_rect = self.Dpra.get_rect(center = (400,590))

        self.praName2 = font_txt.render("Pranav: ",False,"White")
        self.praName2_rect = self.praName.get_rect(topleft = (60,550))
        self.Dpra2 = font_txt.render("U G H  S H E S  S U C H  A  B E A S T ! M O M M Y Y Y !!",False,"White")
        self.Dpra2_rect = self.Dpra.get_rect(center = (400,590))

        self.praNamef = font_med.render("Pranav",False,"black")
        self.praNamef_rect = self.praName.get_rect(topleft = (10,10))

        # self.praNamef = font_med.render("Pranav",False,"black")
        # self.praNamef_rect = self.praName.get_rect(topleft = (10,10))

        #Ariel dialogue

        self.ariName = font_txt.render("Ariel: ",False,"White")
        self.ariName_rect = self.praName.get_rect(topleft = (60,550))
        self.Dari = font_txt.render("IS THAT MY CAT?! MINKA BINKA SMINKA LINKA DINKA JINKA GINKA?!",False,"White")
        self.Dari_rect = self.Dpra.get_rect(center = (470,590))

        self.ariName2 = font_txt.render("Ariel: ",False,"White")
        self.ariName2_rect = self.ariName2.get_rect(topleft = (60,550))
        self.Dari2 = font_txt.render("W H Y  W O U L D  U  D O  T H A T ?!  I 'M  Y O U R  O W N E R !",False,"White")
        self.Dari2_rect = self.Dari2.get_rect(center = (400,590))

        self.Dari3 = font_txt.render("W H Y  D O N ' T  Y O U  A T T A C K  P R A  F I R S T ?! O N  T H E  W E S T  H O U S E!",False,"White")
        self.Dari3_rect = self.Dari3.get_rect(center = (400,590))

        self.ariNamef = font_med.render("Ariel",False,"black")
        self.ariNamef_rect = self.ariNamef.get_rect(topleft = (10,10))

        #minka health
        self.mink_Name = font_med.render("Minka: ",False,"Black")
        self.mink_Name_rect = self.praName.get_rect(topleft = (465,415))

        #power Up
        self.mink_power = font_big.render("Y O U  G O T  A  P O W E R  U P !",False,"Black")
        self.mink_power_rect = self.mink_power.get_rect(center = (400,360))

        self.mink_power2 = font_med.render("A l l   a t t a c k s  + 2 0", False, "Black")
        self.mink_power_rect2 = self.mink_power2.get_rect(center = (400,400))

        self.mink_beat = font_big.render("Y O U  H A V E  B E A T E N  P R A !",False,"Black")
        self.mink_beat_rect = self.mink_beat.get_rect(center = (400,370))

        #Game over

        self.quit_txt = font_big.render("Q U I T",False,"Black")
        self.quit_txt_rect = self.quit_txt.get_rect(center=(400,595))

        self.game_over_txt = font_big.render("G A M E  O V E R !",False,"Black")
        self.game_over_txt_rect = self.game_over_txt.get_rect(center = (400,100))

        self.mink_death = pygame.image.load('AlgoPro_Final/Graphics/mink_death.png').convert_alpha()
        self.mink_death_rect = self.mink_death.get_rect(center = (445,360))

        self.quit_button = pygame.Rect(305, 565, 200, 50)

        #winner
        self.congrats_txt = font_big.render("C O N G R A T U L A T I O N S! ",False,"Black")
        self.congrats_txt_rect = self.congrats_txt.get_rect(center=(400,450))

        self.annoying_txt = font_big.render("O N  B E C O M I N G  T H E  M O S T  A N N O Y I N G  C A T !",False,"Black")
        self.annoying_txt_rect = self.annoying_txt.get_rect(center = (400,500))

        self.mink_celeb = pygame.image.load('AlgoPro_Final/Graphics/winner_cat.png').convert_alpha()
        self.mink_celeb_rect = self.mink_celeb.get_rect(center = (445,280))

        self.quit_win_txt = font_big.render("Q U I T",False,"Black")
        self.quit_win_txt_rect = self.quit_txt.get_rect(center=(400,595))

        self.quit_win_button = pygame.Rect(305, 565, 200, 50)

    
    def winner(self,screen):
        screen.fill("#FDFD96")

        screen.blit(self.congrats_txt,self.congrats_txt_rect)
        screen.blit(self.annoying_txt,self.annoying_txt_rect)
        screen.blit(self.mink_celeb,self.mink_celeb_rect)

        pygame.draw.rect(screen, 'black', pygame.Rect(300, 560, 210, 60))
        pygame.draw.rect(screen, "#D21404", self.quit_win_button)

        screen.blit(self.quit_win_txt,self.quit_win_txt_rect)

        
    def game_over(self,screen):
        screen.fill("#B2D3C2")

        screen.blit(self.game_over_txt,self.game_over_txt_rect)

        screen.blit(self.mink_death,self.mink_death_rect)

        pygame.draw.rect(screen, 'Black', pygame.Rect(300, 560, 210, 60))
        pygame.draw.rect(screen, "#D21404", self.quit_button)

        screen.blit(self.quit_txt,self.quit_txt_rect)
        

    def blitme(self,screen):
        screen.blit(self.enemyPra, self.Pra_rect)
        screen.blit(self.enemyAri,self.Ari_rect)
        screen.blit(self.jude,self.jude_rect)
    
    def collision_npc(self,screen):
        screen.blit(self.E_pop,self.E_rect)
    
    def text_box(self,screen):
        pygame.draw.rect(screen, 'White', pygame.Rect(45, 535, 710, 110))
        pygame.draw.rect(screen, 'Black', pygame.Rect(50, 540, 700, 100))
    
    def fight_button(self,screen):
        pygame.draw.rect(screen, 'White', pygame.Rect(45, 465, 210, 60))
        pygame.draw.rect(screen, "#D21404", self.red_fight)
        screen.blit(self.fight,self.fight_rect)
    
    def leave_instruction(self,screen):
        screen.blit(self.leave,self.leave_rect)

    def ari_dialogue(self,screen):
        screen.blit(self.Dari,self.Dari_rect)
        screen.blit(self.ariName,self.ariName_rect)
    
    def pra_dialogue(self,screen):
        screen.blit(self.Dpra,self.Dpra_rect)
        screen.blit(self.praName,self.praName_rect)
    
    def jude_dialogue(self,screen):
        screen.blit(self.Djude,self.Djude_rect)
        screen.blit(self.judename,self.judename_rect)
    
    def jude_sec_dialogue(self,screen):
        screen.blit(self.judename,self.judename_rect)
        screen.blit(self.Djude2,self.Djude2_rect)
    
    def jude_fight(self,screen):
        screen.blit(self.big_jude,self.big_jude_rect)

        pygame.draw.rect(screen, 'Black', pygame.Rect(0, 0, 305, 100)) 
        pygame.draw.rect(screen, 'Grey', pygame.Rect(0, 0, 300, 95))
        screen.blit(self.judeNamef,self.judeNamef_rect)

    def pra_fight(self,screen):
        screen.blit(self.big_pra,self.big_pra_rect)

        pygame.draw.rect(screen, 'Black', pygame.Rect(0, 0, 305, 100)) 
        pygame.draw.rect(screen, 'Grey', pygame.Rect(0, 0, 300, 95))
        screen.blit(self.praNamef,self.praNamef_rect)
    
    def ari_fight(self,screen):
        screen.blit(self.big_ari,self.big_ari_rect)

        pygame.draw.rect(screen, 'Black', pygame.Rect(0, 0, 305, 100)) 
        pygame.draw.rect(screen, 'Grey', pygame.Rect(0, 0, 300, 95))
        screen.blit(self.ariNamef,self.ariNamef_rect)
    
    def mink_fight(self,screen):
        screen.blit(self.fight_back,(-400,0))
        screen.blit(self.mink_b,self.mink_b_rect) 

        pygame.draw.rect(screen, 'Black', pygame.Rect(45, 500, 710, 200)) 
        pygame.draw.rect(screen, 'White', pygame.Rect(50, 505, 700, 190))
        pygame.draw.rect(screen, '#DE5D83', self.scratch_box)
        pygame.draw.rect(screen, '#DE5D83', self.paw_box)
        pygame.draw.rect(screen, '#D21404', self.leave_box)

        pygame.draw.rect(screen, 'Black', pygame.Rect(455, 400, 300, 100)) 
        pygame.draw.rect(screen, 'Grey', pygame.Rect(460, 405, 290, 95))
        screen.blit(self.mink_Name, self.mink_Name_rect)

        screen.blit(self.fight_txt,self.fight_txt_rect) 
        screen.blit(self.scratch_txt,self.scratch_txt_rect)
        screen.blit(self.paw_txt,self.paw_txt_rect)
        screen.blit(self.leave_txt,self.leave_txt_rect)
    
    def leave_fights(self,screen):
        screen.blit(self.leave_fight,self.leave_fight_rect)
    
    def pra_sec_dial(self,screen):
        screen.blit(self.praName2,self.praName2_rect)
        screen.blit(self.Dpra2,self.Dpra2_rect)

    def ari_sec_dial(self,screen):
        screen.blit(self.ariName2,self.ariName2_rect)
        screen.blit(self.Dari2,self.Dari2_rect)
    
    def ari_incase(self,screen):
        screen.blit(self.ariName2,self.ariName2_rect)
        screen.blit(self.Dari3,self.Dari3_rect)
        screen.blit(self.leave,self.leave_rect)
    
    def power_up(self,screen):
        screen.blit(self.fight_back,(-400,0))

        pygame.draw.rect(screen, 'Black', pygame.Rect(45, 270, 710, 200)) 
        pygame.draw.rect(screen, 'White', pygame.Rect(50, 275, 700, 190))

        screen.blit(self.mink_power,self.mink_power_rect)
        screen.blit(self.mink_power2,self.mink_power_rect2)
    
    def power_up2(self,screen):
        screen.blit(self.fight_back,(-400,0))

        pygame.draw.rect(screen, 'Black', pygame.Rect(45, 270, 710, 200)) 
        pygame.draw.rect(screen, 'White', pygame.Rect(50, 275, 700, 190))

        screen.blit(self.mink_beat,self.mink_beat_rect)


        
    
    
        





# pra = enemies()

import pygame
import sys
import enemy
import health

#Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800,720))
clock = pygame.time.Clock()

pra = enemy.enemies()
hati = health.healths()

#function to make the game run
def start_screen():
    font_big = pygame.font.Font('AlgoPro_Final/Font/Pixeltype.ttf', 50)

    welcome = font_big.render("W E L C O M E  T O  M I N K A ' S  A D V E N T U R E!",False,"Black")
    welcome_rect = welcome.get_rect(center = (400,50))

    start_txt = font_big.render("S T A R T",False,"Black")
    start_txt_rect = start_txt.get_rect(center = (408,564))

    mink_open = pygame.image.load('AlgoPro_Final/Graphics/Cat_start.png').convert_alpha()
    mink_open_rect = mink_open.get_rect(center = (445,360))
    

    start = pygame.Rect(305, 535, 200, 50)
    while True:
        screen.fill("#B2D3C2")
        screen.blit(mink_open,mink_open_rect)
        screen.blit(welcome, welcome_rect)

        pygame.draw.rect(screen, 'Black', pygame.Rect(300, 530, 210, 60))
        pygame.draw.rect(screen, "#D21404", start)
        screen.blit(start_txt,start_txt_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start.collidepoint(event.pos):
                    return True
        pygame.display.flip()
                
def game_over_screen():
    game_over = True

    while game_over:
        screen.fill("#B2D3C2")

        screen.blit(pra.game_over_txt,pra.game_over_txt_rect)

        screen.blit(pra.mink_death,pra.mink_death_rect)

        pygame.draw.rect(screen, 'Black', pygame.Rect(300, 560, 210, 60))
        pygame.draw.rect(screen, "#D21404", pra.quit_button)

        screen.blit(pra.quit_txt,pra.quit_txt_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if pra.quit_button.collidepoint(event.pos):
                        game_over = False
        
        pygame.display.flip()


def game_over_win_screen():
    game_over_win = True

    while game_over_win:
        screen.fill("#FDFD96")

        screen.blit(pra.congrats_txt,pra.congrats_txt_rect)
        screen.blit(pra.annoying_txt,pra.annoying_txt_rect)
        screen.blit(pra.mink_celeb,pra.mink_celeb_rect)

        pygame.draw.rect(screen, 'black', pygame.Rect(300, 560, 210, 60))
        pygame.draw.rect(screen, "#D21404", pra.quit_win_button)

        screen.blit(pra.quit_win_txt,pra.quit_win_txt_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if pra.quit_win_button.collidepoint(event.pos):
                        game_over_win = False
        
        pygame.display.flip()
                    
        

def game_run():

    map_surf = pygame.image.load('AlgoPro_Final/Graphics/map/Map.png').convert()
    map_surf = pygame.transform.scale_by(map_surf,3)
    map_rect = map_surf.get_rect(center = (473,369))

    mink_surf = pygame.image.load('AlgoPro_Final/Graphics/Characters/cat_sit.png').convert()
    mink_surf = pygame.transform.scale_by(mink_surf,3)  
    mink_rect = mink_surf.get_rect(center = (405,360))

    #Walls (crop image bla bla)
    bike_surf =  pygame.image.load('AlgoPro_Final/Graphics/bike.png').convert()
    bike_surf = pygame.transform.scale_by(bike_surf,2) 
    bike_rect = bike_surf.get_rect(topright = (52,562))

    hos_surf =  pygame.image.load('AlgoPro_Final/Graphics/hospital.png').convert()
    hos_surf = pygame.transform.scale_by(hos_surf,1.7) 
    hos_rect = hos_surf.get_rect(center = (400,260))

    gym_surf =  pygame.image.load('AlgoPro_Final/Graphics/gym.png').convert()
    gym_surf = pygame.transform.scale_by(gym_surf,1.7) 
    gym_rect = gym_surf.get_rect(topleft = (740,280))

    house1_surf =  pygame.image.load('AlgoPro_Final/Graphics/house_1.png').convert()
    house1_surf = pygame.transform.scale_by(house1_surf,1.9) 
    house1_rect = house1_surf.get_rect(topleft = (10,140))

    house2_surf =  pygame.image.load('AlgoPro_Final/Graphics/house2.png').convert()
    house2_surf = pygame.transform.scale_by(house2_surf,2.4) 
    house2_rect = house2_surf.get_rect(topleft = (-240,-340))

    left_surf =  pygame.image.load('AlgoPro_Final/Graphics/left.png').convert()
    left_surf = pygame.transform.scale_by(left_surf,2.5) 
    left_rect = left_surf.get_rect(topleft = (-645,-340))

    top_surf =  pygame.image.load('AlgoPro_Final/Graphics/top.png').convert()
    top_surf = pygame.transform.scale_by(top_surf,2.5) 
    top_rect = top_surf.get_rect(center = (600,-430))

    bot_surf =  pygame.image.load('AlgoPro_Final/Graphics/bottom.png').convert()
    bot_surf = pygame.transform.scale_by(bot_surf,2.5) 
    bot_rect = bot_surf.get_rect(center = (600,1100))

    right_surf =  pygame.image.load('AlgoPro_Final/Graphics/right.png').convert()
    right_surf = pygame.transform.scale_by(right_surf,2.5) 
    right_rect = right_surf.get_rect(center = (1400,360))

    house3_surf =  pygame.image.load('AlgoPro_Final/Graphics/house3.png').convert()
    house3_surf = pygame.transform.scale_by(house3_surf,2.5) 
    house3_rect = house3_surf.get_rect(center = (950,-200))

    rightb_surf =  pygame.image.load('AlgoPro_Final/Graphics/right_bush.png').convert()
    rightb_surf = pygame.transform.scale_by(rightb_surf,2.5) 
    rightb_rect = rightb_surf.get_rect(center = (1120,200))

    shop_surf =  pygame.image.load('AlgoPro_Final/Graphics/shop.png').convert()
    shop_surf = pygame.transform.scale_by(shop_surf,2.45) 
    shop_rect = shop_surf.get_rect(topleft = (400,624))

    #helath bar
    

    pygame.display.set_caption('MinkAdventure')
    run = True
    #For smooth movement
    move_up = False
    move_down = False
    move_left = False
    move_right = False
    #Button and collision
    collision = False
    E_button = False
    E_counter = 0
    #for dialogue to pop up
    P_dial = False
    pra2_dial = False
    A_dial = False
    ari2_dial = False
    J_dial = False
    j_dial_2 = False
    #fight images
    fight = False
    fight_a = False
    fight_j = False
    attack = 0
    current_time = 0
    button_time = 0
    turn = True
    #heart on screen
    heart1 = True
    heart2 = True
    heart_count = 0
    heart_count2 = 0

    # game_over = False
    # game_winner = False

    gaming = True
    
    while gaming:

        #blitting map under to make collision
        screen.blit(bike_surf,bike_rect)
        screen.blit(hos_surf,hos_rect)
        screen.blit(gym_surf,gym_rect)
        screen.blit(house1_surf,house1_rect)
        screen.blit(house2_surf,house2_rect)
        screen.blit(left_surf,left_rect)
        screen.blit(top_surf,top_rect)
        screen.blit(bot_surf,bot_rect)
        screen.blit(right_surf,right_rect)
        screen.blit(house3_surf,house3_rect)
        screen.blit(rightb_surf,rightb_rect)
        screen.blit(shop_surf,shop_rect)

        #To blit the enemies/character/and map to the screen
        screen.blit(map_surf,map_rect)
        pra.blitme(screen)
        screen.blit(mink_surf,mink_rect)
        

        current_time = pygame.time.get_ticks()

        # hati.health_gain(screen)
        hati.mink_health_surf(screen)

        
        for event in pygame.event.get():

            #to quit after death
                
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if pra.quit_button.collidepoint(event.pos):
            #         gaming = False
                
            #     elif pra.quit_win_button.collidepoint(event.pos):
            #         gaming = False

            #figthing


            if event.type == pygame.MOUSEBUTTONDOWN:
                if mink_rect.colliderect(pra.Pra_rect):
                    if pra.red_fight.collidepoint(event.pos): 
                        fight = True
                elif mink_rect.colliderect(pra.Ari_rect):
                    if pra.red_fight.collidepoint(event.pos):
                        if hati.current_health > 0:
                            turn = True
                        elif hati.current_health <= 0:
                            fight_a = True
                elif mink_rect.colliderect(pra.jude_rect):
                    if pra.red_fight.collidepoint(event.pos):
                        if hati.current_a_health > 0:
                            j_dial_2 = True 
                        elif hati.current_a_health <= 0:
                            fight_j = True


            if event.type == pygame.MOUSEBUTTONDOWN:
                if mink_rect.colliderect(pra.Pra_rect):
                    if pra.leave_box.collidepoint(event.pos):
                        fight = False
                        collision = False
                        P_dial = False
                elif mink_rect.colliderect(pra.Ari_rect):
                    if pra.leave_box.collidepoint(event.pos):
                        fight_a = False
                        collision = False
                        A_dial = False
                elif mink_rect.colliderect(pra.jude_rect):
                    if pra.leave_box.collidepoint(event.pos):
                        fight_j = False
                        collision = False
                        J_dial = False

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mink_rect.colliderect(pra.Pra_rect):
                    if pra.scratch_box.collidepoint(event.pos):
                        hati.damaged(35)
                        attack += 1
                        button_time = pygame.time.get_ticks()
                    elif pra.paw_box.collidepoint(event.pos):
                        hati.damaged(45)
                        attack += 1
                        button_time = pygame.time.get_ticks()
      
                elif mink_rect.colliderect(pra.Ari_rect): 
                    if pra.scratch_box.collidepoint(event.pos):
                        hati.ari_damaged(35)
                        attack += 1
                        button_time = pygame.time.get_ticks()
                    elif pra.paw_box.collidepoint(event.pos):
                        hati.ari_damaged(45)
                        attack += 1
                        button_time = pygame.time.get_ticks()
                
                elif mink_rect.colliderect(pra.jude_rect): 
                    if pra.scratch_box.collidepoint(event.pos):
                        hati.jude_damaged(55)
                        attack += 1
                        button_time = pygame.time.get_ticks()
                    elif pra.paw_box.collidepoint(event.pos):
                        hati.jude_damaged(65)
                        attack += 1
                        button_time = pygame.time.get_ticks()
                    
            # if event.type == pygame.MOUSEBUTTONDOWN:
            

            #collision
            if mink_rect.colliderect(pra.Pra_rect):
                E_button = True
                pra.collision_npc(screen) 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        collision = True
                        P_dial = True
                        E_counter += 1
                        if hati.current_health <= 0:
                            fight = False
                            P_dial = False
                            pra2_dial = True
                        
                        #To make d box dissapear after the second press and resets the E counter
                        if E_counter == 2 :
                            collision = False
                            pra2_dial = False
                            P_dial = False 
                            E_counter = 0

            elif mink_rect.colliderect(pra.Ari_rect):
                E_button = True
                pra.collision_npc(screen) 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        collision = True
                        A_dial = True
                        E_counter += 1
                        if hati.current_a_health <= 0:
                            fight_a = False
                            A_dial = False
                            ari2_dial = True
                        #To make d box dissapear after the second press and resets the E counter
                        if E_counter == 2:
                            collision = False
                            A_dial = False
                            ari2_dial = False
                            E_counter = 0
                            turn = False
                            j_dial_2 = False 
                            power = False
            
            elif mink_rect.colliderect(pra.jude_rect):
                E_button = True
                pra.collision_npc(screen) 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        collision = True
                        J_dial = True
                        E_counter += 1
                        #To make d box dissapear after the second press and resets the E counter
                        if E_counter == 2:
                            collision = False
                            J_dial = False
                            j_dial_2 = False
                            E_counter = 0
                            turn = False

            #heart buffs
            elif mink_rect.colliderect(hati.health_surf_rect) and heart_count == 0 :
                E_button = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        heart1 = False
                        hati.mink_healed(40)
                        heart_count += 1
            
            elif mink_rect.colliderect(hati.health_surf_rect2) and heart_count2 == 0 :
                E_button = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        heart2 = False
                        hati.mink_healed(50)
                        heart_count2 += 1

            
            else:
                #making sure that when user go away from NPC text,E button and collision is gone
                E_button = False
                collision = False
                P_dial = False
                pra2_dial = False
                A_dial = False
                ari2_dial = False
                E_counter = 0
                turn = False
                j_dial_2 = False
                J_dial = False
            
            collision_tol = 10

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    move_left = True
                if event.key == pygame.K_w:
                    move_up = True
                if event.key == pygame.K_s:
                    move_down = True
                if event.key == pygame.K_d:
                    move_right = True  

            #delete later
            if event.type == pygame.MOUSEMOTION:
                print(event.pos)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    move_left = False
                if event.key == pygame.K_w:
                    move_up = False
                if event.key == pygame.K_s:
                    move_down = False
                if event.key == pygame.K_d:
                    move_right = False
        
        if move_right and move_up:
            move_right = False
            move_up = False

        if move_left and move_up:
            move_left = False
            move_up = False

        if move_right and move_down:
            move_right = False
            move_down = False

        if move_left and move_down:
            move_left = False
            move_down = False

        if move_right:
            map_rect.x -= 10

            pra.Pra_rect.x -= 10 
            pra.Ari_rect.x -= 10
            pra.jude_rect.x -= 10
            
            bike_rect.x -= 10
            hos_rect.x -= 10
            gym_rect.x -= 10
            house1_rect.x -= 10
            house2_rect.x -= 10
            left_rect.x -= 10
            top_rect.x -= 10
            bot_rect.x -= 10
            right_rect.x -= 10
            house3_rect.x -= 10
            rightb_rect.x -= 10
            shop_rect.x -= 10

            hati.health_surf_rect.x -= 10
            hati.health_surf_rect2.x -= 10

            #To make the cat stay in bound
            if map_rect.x == -1499:
                mink_rect.x += 10
                map_rect.x += 10

                pra.Pra_rect.x += 10 
                pra.Ari_rect.x += 10
                pra.jude_rect.x += 10

                hati.health_surf_rect.x += 10
                hati.health_surf_rect2.x += 10

                bike_rect.x += 10
                hos_rect.x += 10
                gym_rect.x += 10
                house1_rect.x += 10
                house2_rect.x += 10
                left_rect.x += 10
                top_rect.x += 10
                bot_rect.x += 10
                right_rect.x += 10
                house3_rect.x += 10
                rightb_rect.x += 10
                shop_rect.x += 10

            if mink_rect.x < 345:
                mink_rect.x += 10
                map_rect.x += 10

                pra.Pra_rect.x += 10 
                pra.Ari_rect.x += 10
                pra.jude_rect.x += 10

                hati.health_surf_rect.x += 10
                hati.health_surf_rect2.x += 10

                bike_rect.x += 10
                hos_rect.x += 10
                gym_rect.x += 10
                house1_rect.x += 10
                house2_rect.x += 10
                left_rect.x += 10
                top_rect.x += 10
                bot_rect.x += 10
                right_rect.x += 10
                house3_rect.x += 10
                rightb_rect.x += 10
                shop_rect.x += 10


        if move_left:
            map_rect.x += 10
            bike_rect.x += 10
            hos_rect.x += 10
            gym_rect.x += 10
            house1_rect.x += 10
            house2_rect.x += 10
            left_rect.x += 10
            top_rect.x += 10
            bot_rect.x += 10
            right_rect.x += 10
            house3_rect.x += 10
            rightb_rect.x += 10
            shop_rect.x += 10

            pra.Pra_rect.x += 10 
            pra.Ari_rect.x += 10
            pra.jude_rect.x += 10
            
            hati.health_surf_rect.x += 10
            hati.health_surf_rect2.x += 10

            if map_rect.x == -29:
                mink_rect.x -= 10
                map_rect.x -= 10

                pra.Pra_rect.x -= 10 
                pra.Ari_rect.x -= 10
                pra.jude_rect.x -= 10
                
                hati.health_surf_rect.x -= 10
                hati.health_surf_rect2.x -= 10

                bike_rect.x -= 10
                hos_rect.x -= 10
                gym_rect.x -= 10
                house1_rect.x -= 10
                house2_rect.x -= 10
                left_rect.x -= 10
                top_rect.x -= 10
                bot_rect.x -= 10
                right_rect.x -= 10
                house3_rect.x -= 10
                rightb_rect.x -= 10
                shop_rect.x -= 10
                


            if mink_rect.x > 345:
                mink_rect.x -= 10
                map_rect.x -= 10

                pra.Pra_rect.x -= 10 
                pra.Ari_rect.x -= 10
                pra.jude_rect.x -= 10
                
                hati.health_surf_rect.x -= 10
                hati.health_surf_rect2.x -= 10

                bike_rect.x -= 10
                hos_rect.x -= 10
                gym_rect.x -= 10
                house1_rect.x -= 10
                house2_rect.x -= 10
                left_rect.x -= 10
                top_rect.x -= 10
                bot_rect.x -= 10
                right_rect.x -= 10
                house3_rect.x -= 10
                rightb_rect.x -= 10
                shop_rect.x -= 10

        if move_down:
            map_rect.y -= 10

            pra.Pra_rect.y -= 10 
            pra.Ari_rect.y -= 10
            pra.jude_rect.y -= 10

            bike_rect.y -= 10
            hos_rect.y -= 10
            gym_rect.y -= 10
            house1_rect.y -= 10
            house2_rect.y -= 10
            left_rect.y -= 10
            top_rect.y -= 10
            bot_rect.y -= 10
            right_rect.y -= 10
            house3_rect.y -= 10
            rightb_rect.y -= 10
            shop_rect.y -= 10
            

            hati.health_surf_rect.y -= 10
            hati.health_surf_rect2.y -= 10
            
            if map_rect.y == -1193:
                mink_rect.y += 10
                map_rect.y += 10

                pra.Pra_rect.y += 10
                pra.Ari_rect.y += 10
                pra.jude_rect.y += 10

                bike_rect.y += 10
                hos_rect.y += 10
                gym_rect.y += 10
                house1_rect.y += 10
                house2_rect.y += 10
                left_rect.y += 10
                top_rect.y += 10
                bot_rect.y += 10
                right_rect.y += 10
                house3_rect.y += 10
                rightb_rect.y += 10
                shop_rect.y += 10
                
                hati.health_surf_rect2.y += 10
                hati.health_surf_rect.y += 10
            if mink_rect.y < 303:
                mink_rect.y += 10
                map_rect.y += 10

                pra.Pra_rect.y += 10
                pra.Ari_rect.y += 10
                pra.jude_rect.y += 10

                hati.health_surf_rect.y += 10
                hati.health_surf_rect2.y += 10

                hos_rect.y += 10
                bike_rect.y += 10
                gym_rect.y += 10
                house1_rect.y += 10
                house2_rect.y += 10
                left_rect.y += 10
                top_rect.y += 10
                bot_rect.y += 10
                right_rect.y += 10
                house3_rect.y += 10
                rightb_rect.y += 10
                shop_rect.y += 10

        if move_up:
            map_rect.y += 10

            pra.Pra_rect.y += 10 
            pra.Ari_rect.y += 10
            pra.jude_rect.y += 10

            hati.health_surf_rect.y += 10
            hati.health_surf_rect2.y += 10

            bike_rect.y += 10
            hos_rect.y += 10
            gym_rect.y += 10
            house1_rect.y += 10
            house2_rect.y += 10
            left_rect.y += 10
            top_rect.y += 10
            bot_rect.y += 10
            right_rect.y += 10
            house3_rect.y += 10
            rightb_rect.y += 10
            shop_rect.y += 10
             
            if map_rect.y == -53:
                mink_rect.y -= 10
                map_rect.y -= 10

                pra.Pra_rect.y -= 10 
                pra.Ari_rect.y -= 10
                pra.jude_rect.y -= 10

                hati.health_surf_rect.y -= 10
                hati.health_surf_rect2.y -= 10

                hos_rect.y -= 10
                bike_rect.y -= 10
                gym_rect.y -= 10
                house1_rect.y -= 10
                house2_rect.y -= 10
                left_rect.y -= 10
                top_rect.y -= 10
                bot_rect.y -= 10
                right_rect.y -= 10
                house3_rect.y -= 10
                rightb_rect.y -= 10
                shop_rect.y -= 10

            if mink_rect.y > 303:
                mink_rect.y -= 10
                map_rect.y -= 10

                pra.Pra_rect.y -= 10 
                pra.Ari_rect.y -= 10
                pra.jude_rect.y -= 10

                hati.health_surf_rect.y -= 10
                hati.health_surf_rect2.y -= 10

                hos_rect.y -= 10
                bike_rect.y -= 10
                gym_rect.y -= 10
                house1_rect.y -= 10
                house2_rect.y -= 10
                left_rect.y -= 10
                top_rect.y -= 10
                bot_rect.y -= 10
                right_rect.y -= 10
                house3_rect.y -= 10
                rightb_rect.y -= 10
                shop_rect.y -= 10

        
        #For collide with the building
        collision_tol = 20
        if mink_rect.colliderect(bike_rect):
            if move_down and mink_rect.bottom <= bike_rect.top + collision_tol:
                mink_rect.y -= 10
            elif move_up and mink_rect.top >= bike_rect.bottom - collision_tol:
                mink_rect.y += 10
            elif move_right and mink_rect.right <= bike_rect.left + collision_tol:
                mink_rect.x -= 10
            elif move_left and mink_rect.left >= bike_rect.right - collision_tol:
                mink_rect.x += 10

        elif mink_rect.colliderect(hos_rect) or mink_rect.colliderect(hos_rect) and mink_rect.colliderect(house1_rect):
            if move_down and mink_rect.bottom <= hos_rect.top + collision_tol:
                mink_rect.y -= 10
            elif move_up and mink_rect.top >= hos_rect.bottom - collision_tol:
                mink_rect.y += 10
            elif move_right and mink_rect.right <= hos_rect.left + collision_tol:
                mink_rect.x -= 10
            elif move_left and mink_rect.left >= hos_rect.right - collision_tol:
                mink_rect.x += 10
        
        elif mink_rect.colliderect(gym_rect):
            if move_down and mink_rect.bottom <= gym_rect.top + collision_tol:
                mink_rect.y -= 10
            elif move_up and mink_rect.top >= gym_rect.bottom - collision_tol:
                mink_rect.y += 10
            elif move_right and mink_rect.right <= gym_rect.left + collision_tol:
                mink_rect.x -= 10
            elif move_left and mink_rect.left >= gym_rect.right - collision_tol:
                mink_rect.x += 10
        
        elif mink_rect.colliderect(house1_rect) or mink_rect.colliderect(house1_rect) and mink_rect.colliderect(hos_rect):
            if move_down and mink_rect.bottom <= house1_rect.top + collision_tol:
                mink_rect.y -= 10
            elif move_up and mink_rect.top >= house1_rect.bottom - collision_tol:
                mink_rect.y += 10
            elif move_right and mink_rect.right <= house1_rect.left + collision_tol:
                mink_rect.x -= 10
            elif move_left and mink_rect.left >= house1_rect.right - collision_tol:
                mink_rect.x += 10
        
        elif mink_rect.colliderect(house2_rect):
            if move_down and mink_rect.bottom <= house2_rect.top + collision_tol:
                mink_rect.y -= 10
            elif move_up and mink_rect.top >= house2_rect.bottom - collision_tol:
                mink_rect.y += 10
            elif move_right and mink_rect.right <= house2_rect.left + collision_tol:
                mink_rect.x -= 10
            elif move_left and mink_rect.left >= house2_rect.right - collision_tol:
                mink_rect.x += 10

        elif mink_rect.colliderect(left_rect):
            if move_down and mink_rect.bottom <= left_rect.top + collision_tol:
                mink_rect.y -= 10
            elif move_up and mink_rect.top >= left_rect.bottom - collision_tol:
                mink_rect.y += 10
            elif move_right and mink_rect.right <= left_rect.left + collision_tol:
                mink_rect.x -= 10
            elif move_left and mink_rect.left >= left_rect.right - collision_tol:
                mink_rect.x += 10
        
        elif mink_rect.colliderect(top_rect):
            if move_down and mink_rect.bottom <= top_rect.top + collision_tol:
                mink_rect.y -= 10
            elif move_up and mink_rect.top >= top_rect.bottom - collision_tol:
                mink_rect.y += 10
            elif move_right and mink_rect.right <= top_rect.left + collision_tol:
                mink_rect.x -= 10
            elif move_left and mink_rect.left >= top_rect.right - collision_tol:
                mink_rect.x += 10
        
        elif mink_rect.colliderect(bot_rect):
            if move_down and mink_rect.bottom <= bot_rect.top + collision_tol:
                mink_rect.y -= 10
            elif move_up and mink_rect.top >= bot_rect.bottom - collision_tol:
                mink_rect.y += 10
            elif move_right and mink_rect.right <= bot_rect.left + collision_tol:
                mink_rect.x -= 10
            elif move_left and mink_rect.left >= bot_rect.right - collision_tol:
                mink_rect.x += 10
        
        elif mink_rect.colliderect(right_rect):
            if move_down and mink_rect.bottom <= right_rect.top + collision_tol:
                mink_rect.y -= 10
            elif move_up and mink_rect.top >= right_rect.bottom - collision_tol:
                mink_rect.y += 10
            elif move_right and mink_rect.right <= right_rect.left + collision_tol:
                mink_rect.x -= 10
            elif move_left and mink_rect.left >= right_rect.right - collision_tol:
                mink_rect.x += 10
        
        elif mink_rect.colliderect(house3_rect):
            if move_down and mink_rect.bottom <= house3_rect.top + collision_tol:
                mink_rect.y -= 10
            elif move_up and mink_rect.top >= house3_rect.bottom - collision_tol:
                mink_rect.y += 10
            elif move_right and mink_rect.right <= house3_rect.left + collision_tol:
                mink_rect.x -= 10
            elif move_left and mink_rect.left >= house3_rect.right - collision_tol:
                mink_rect.x += 10
        
        elif mink_rect.colliderect(shop_rect):
            if move_down and mink_rect.bottom <= shop_rect.top + collision_tol:
                mink_rect.y -= 10
            elif move_up and mink_rect.top >= shop_rect.bottom - collision_tol:
                mink_rect.y += 10
            elif move_right and mink_rect.right <= shop_rect.left + collision_tol:
                mink_rect.x -= 10
            elif move_left and mink_rect.left >= shop_rect.right - collision_tol:
                mink_rect.x += 10
        
        elif mink_rect.colliderect(rightb_rect):
            if move_down and mink_rect.bottom <= rightb_rect.top + collision_tol:
                mink_rect.y -= 10
            elif move_up and mink_rect.top >= rightb_rect.bottom - collision_tol:
                mink_rect.y += 10
            elif move_right and mink_rect.right <= rightb_rect.left + collision_tol:
                mink_rect.x -= 10
            elif move_left and mink_rect.left >= rightb_rect.right - collision_tol:
                mink_rect.x += 10
                
                

        if heart1:
            hati.health_gain(screen)
        
        if heart2:
            hati.health_gain2(screen)
        
        if collision:
            pra.text_box(screen)
 
        if P_dial:
            pra.pra_dialogue(screen)
            pra.fight_button(screen)
            pra.leave_instruction(screen)

        if A_dial:
            pra.ari_dialogue(screen)
            pra.fight_button(screen)
            pra.leave_instruction(screen)
        
        if J_dial:
            pra.jude_dialogue(screen)
            pra.fight_button(screen)
            pra.leave_instruction(screen)
        
        if j_dial_2:
            pra.text_box(screen)
            pra.jude_sec_dialogue(screen)
            pra.leave_instruction(screen)

        if E_button:
            pra.collision_npc(screen)
        
        if fight_j:
            pra.mink_fight(screen)
            hati.mink_health(screen)
            pra.jude_fight(screen)
            hati.jude_health(screen)

        if fight:
            pra.mink_fight(screen)
            pra.pra_fight(screen)
            hati.pra_health(screen)
            hati.mink_health(screen)
            if hati.current_health <= 0:
                pra.power_up2(screen)
                pra.leave_fights(screen)
        
        if pra2_dial:
            pra.pra_sec_dial(screen)

        if ari2_dial:
            pra.ari_sec_dial(screen)
        
        if turn:
            pra.text_box(screen)
            pra.ari_incase(screen)
            
        
        if fight_a:
            pra.mink_fight(screen)
            pra.ari_fight(screen)
            hati.ari_health(screen)
            hati.mink_health(screen)
            if hati.current_a_health <= 0:
                pra.power_up(screen)
                pra.leave_fights(screen)
        
        # if game_over:
        #     pra.game_over(screen)
        
        # if game_winner:
        #     pra.winner(screen)
        
        if mink_rect.colliderect(pra.Pra_rect):
            if hati.current_health > 0:
                if current_time - button_time > 1000:
                    if attack == 1:
                        hati.mink_damaged(20)
                        attack = 0
                        current_time = 0
                        button_time = 0
            elif hati.current_health <= 0:
                attack = 0

        elif mink_rect.colliderect(pra.Ari_rect):
            if hati.current_a_health > 0:
                if current_time - button_time > 1000:
                    if attack == 1:
                        hati.mink_damaged(20)
                        attack = 0
                        current_time = 0
                        button_time = 0
            elif hati.current_a_health <= 0:
                attack = 0
        
        elif mink_rect.colliderect(pra.jude_rect):
            if hati.current_j_health > 0:
                if current_time - button_time > 1000:
                    if attack == 1:
                        hati.mink_damaged(25)
                        attack = 0
                        current_time = 0
                        button_time = 0
            elif hati.current_j_health <= 0:
                attack = 0
        
        if hati.current_m_health <= 0:
            gaming = False
            game_over_screen()
        
        if hati.current_j_health <= 0:
            gaming = False
            game_over_win_screen()

        # print (map_rect.x)
        # print (map_rect.y)
        # print (mink_rect.y)
        # print(current_time)
        # print(button_time)

        
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

start_game = start_screen()

if start_game:
    game_run()
from game.fight import*
from game.game import*
from game.fight import*

import sys

if __name__ == "__main__":
    initialisation()
    Clock = pygame.time.Clock()

    while True:
        
        click_cursor = False                                                 # la fonction si c'est cliqué
        X_AXIS, Y_AXIS = SCREEN.get_size()                                  # la taille de la fenêtre 

        for event in pygame.event.get():                                    # pour tout les evenements du jeu
            if event.type == pygame.QUIT:                                   # si l'élément est quitter 
                # fermer le programme
                pygame.quit()                                               # quitter la page pygame
                sys.exit()                                                  # fermer tout les processus en cours

            if event.type == pygame.KEYDOWN:                                # si c'est une touche préssée 
                if event.key == pygame.K_DELETE:                            # si la touche préssée est suppr
                    # fermer le programme
                    pygame.quit()                                           # quitter la page pygame
                    sys.exit()                                              # fermer tout les processus en cours

        if time_click < 18:                                                 # fait un cooldown pour chaque clique de la souris
            time_click += 1 
        
        if is_mouse:
            x, y = runcursor()                                              # avoir x et y de la fonction (crée)
            if event.type == pygame.MOUSEBUTTONDOWN and time_click == 18:   # si c'est clique souris et time_click qui est 15   
                click_cursor = True                                          # faire un clique souris
                time_click = 0
        else:
            try:
                import game.hand_detection as handdetection

                handdetection.hand_tracking.axis_x, handdetection.hand_tracking.axis_y = X_AXIS, Y_AXIS
                x, y = handdetection.hand_tracking.hand_x, handdetection.hand_tracking.hand_y               # transformer hand_x et hand_y en x et y
                handdetection.hand_tracking.scan_hands()
            
                if handdetection.hand_tracking.hand_closed:     click_cursor = True

                pygame.mouse.set_visible(True)                                                          #la souris de l'ordianteur est visible
            
                if handdetection.hand_tracking.hand_closed and time_click == 18:                        #si la main est fermée et time_click == 15
                    click_cursor = True                                            
                    time_click = 0

            except:
                error_install_modules = Text(X_AXIS, Y_AXIS).render("install modules !", False, (255, 255, 255))
                SCREEN.blit(error_install_modules, (X_AXIS//2.25, 1))                         # si c'est la main qui est utilisée ou la souris
        try:    
            if mainpage:
                SCREEN.fill((37,40,80)) 
                game_type = Page(X_AXIS//2.7, Y_AXIS//2.75, X_AXIS//4, Y_AXIS//10, game_type_color)
                game_type_text = pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//100 + Y_AXIS//100)).render("Play", False, color_text_game_button)

                SCREEN.blit(game_type_text, (X_AXIS//2.08, Y_AXIS//2.5))

                change_type = Page(X_AXIS//2.7, Y_AXIS//2, X_AXIS//4, Y_AXIS//10, change_type_color)
                change_type_text = pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//100 + Y_AXIS//100)).render("Change mode", False, color_text_change_type)                     #bouton changer de mode
                SCREEN.blit(change_type_text, (X_AXIS//2.195, Y_AXIS//1.8555))

                quit_type = Page(X_AXIS//2.7, Y_AXIS//1.566, X_AXIS//4, Y_AXIS//10, quit_type_color) 
                quit_type_text = pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//100 + Y_AXIS//100)).render("quit game", False, color_text_quit_type)                           #bouton quit
                SCREEN.blit(quit_type_text, (X_AXIS//2.156, Y_AXIS//1.483))

                if quit_type.collision(x, y) and click_cursor:
                    exit_game = True
                        

                if click_cursor and game_type.collision(x, y):  launchgame = True                                                    #lancer la partie
                if game_type.collision(x, y):   
                    game_type_color = (145, 145, 145)                                                                               #changer la couleur du bouton
                    color_text_game_button = (255, 255, 255)
                else:   
                    game_type_color = (200, 200, 200)
                    color_text_game_button = (10, 10, 10)

                if click_cursor and change_type.collision(x, y):
                    if is_mouse:    is_mouse = False                                                                                #changer de mode entre avec souris ou avec la main
                    else:   is_mouse = True

                if change_type.collision(x, y):   
                    change_type_color = (145, 145, 145)                                                                             #activer bouton du changement de mode
                    color_text_change_type = (255, 255, 255)
                else:   
                    change_type_color = (200, 200, 200)                                                                             #changer couleur du changement de mode
                    color_text_change_type = (10, 10, 10)

                if click_cursor and quit_type.collision(x, y):                                                    #activer bouton du bouton settings
                        pygame.quit()                                                                                                   #bouton quitter le jeu
                        sys.exit()
                if quit_type.collision(x, y):   
                    quit_type_color = (145, 145, 145)                                                                               #changer la couleur du bouton settings
                    color_text_quit_type = (255, 255, 255)
                else:   
                    quit_type_color = (200, 200, 200)
                    color_text_quit_type = (10, 10, 10)
                SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//200 + Y_AXIS//200)).render("The game can change", False, (255, 255, 255)), (1, Y_AXIS-70))

            if launchgame:                                                                                              #lancer le jeu
                opening += 1                                                                                            #lancer le temps de l'opening
                if opening >= 3*round(Clock.get_fps()):                                                                   #si l'opening est passé

                    if fight.is_fighting:
                        
                        fight.shuffle_order()                                                                           #mettre l'ordre aléatoire
                        fight.inventory_randomly()                                                                      #mettre des objets aléatoire
                        fight.is_fighting = False

                    if middle_music and pygame.mixer.music.get_pos() == -1:
                        Music("phonk\\phonk_boucle.ogg", SOUND, True)
                        middle_music = False

                    if sum(fight.hero_life) > 0 and sum(fight.ennemies_life) > 0:                                       #si un des deux n'a plus de vie

                        if fight.current_round == (len(fight.round)-1):                                                 #si len(fight.round) est égal à current_round
                            fight.current_round = 0

                        SCREEN.fill((37,40,80))
                        image += 1

                        if image >= round(Clock.get_fps())//2:                                                                  #animations
                            current_hero_image += 1                                                                             #les frames d'animations pour chaque image
                            image = 0
                        
                        if current_hero_image == 3: current_hero_image = 0                                                      #revenir à la première frames
                        
                        monster = Image(cookiemonster[current_hero_image], (X_AXIS//4, Y_AXIS//2))

                        baker_archer_collision = Page(X_AXIS//12, Y_AXIS//2.1, X_AXIS//15, Y_AXIS//5, (37, 40, 80))
                        baker_dwarf_collision = Page(X_AXIS//6.25, Y_AXIS//1.7, X_AXIS//15, Y_AXIS//5, (37, 40, 80))
                        baker_magician_collision = Page(X_AXIS//5.55, Y_AXIS//2.7, X_AXIS//15, Y_AXIS//5, (37, 40, 80))         #les persos pour cliquer
                        baker_warrior_collision = Page(X_AXIS//3.85, Y_AXIS//2, X_AXIS//15, Y_AXIS//5, (37, 40, 80))

                        if len(fight.ennemies) == 1:
                            monster_1 = Page(X_AXIS//1.35,Y_AXIS//1.9, X_AXIS//10, Y_AXIS//5, (37, 40, 80))                     #si un il y a 1 monstre

                        elif len(fight.ennemies) == 2:
                            monster_1 = Page(X_AXIS//1.35,Y_AXIS//3, X_AXIS//10, Y_AXIS//5, (37, 40, 80))
                            monster_2 = Page(X_AXIS//1.35,Y_AXIS//1.75, X_AXIS//10, Y_AXIS//5, (37, 40, 80))                     #si un il y a 2 monstre

                        elif len(fight.ennemies) == 3:
                            monster_1 = Page(X_AXIS//1.28,Y_AXIS//2.9, X_AXIS//10, Y_AXIS//5, (37, 40, 80))
                            monster_2 = Page(X_AXIS//1.28,Y_AXIS//1.75, X_AXIS//10, Y_AXIS//5, (37, 40, 80))                     #si un il y a 3 monstre
                            monster_3 = Page(X_AXIS//1.52,Y_AXIS//2, X_AXIS//10, Y_AXIS//5, (37, 40, 80))

                        SCREEN.blit(Image('socle.png', (X_AXIS//4, Y_AXIS//2.5)).load, (X_AXIS//12.7, Y_AXIS//2))
                        SCREEN.blit(Image('socle.png', (X_AXIS//4, Y_AXIS//2.5)).load, (X_AXIS//1.5, Y_AXIS//2))                   #les socles en dessous des persos

                        baker_archer_character = Image(heros[0][0][current_hero_image], (X_AXIS//10, Y_AXIS//5.5))
                        baker_dwarf_character = Image(heros[0][1][current_hero_image], (X_AXIS//10, Y_AXIS//5.5))
                        baker_magician_character = Image(heros[0][2][current_hero_image], (X_AXIS//10, Y_AXIS//5.5))               #dessiner les persos
                        baker_warrior_character = Image(heros[0][3][current_hero_image], (X_AXIS//10, Y_AXIS//5.5))

                        if fight.hero_life[0] > 0:
                            SCREEN.blit(baker_archer_character.load, (X_AXIS//15, Y_AXIS//2.1))                                                                     #dessiner les heros                 
                            
                            if X_AXIS > Y_AXIS: SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.hero_life[0]} {fight.hero[0].name}", False, color_names), (X_AXIS//12, Y_AXIS//1.5))
                            else:   SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.hero_life[0]}", False, color_names), (X_AXIS//10, Y_AXIS//1.5))
                        
                        if fight.hero_life[1] > 0:
                            SCREEN.blit(baker_dwarf_character.load, (X_AXIS//7, Y_AXIS//1.7))

                            if X_AXIS > Y_AXIS: SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.hero_life[1]} {fight.hero[1].name}", False, color_names), (X_AXIS//6.1, Y_AXIS//1.29))
                            else:   SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.hero_life[1]}", False, color_names), (X_AXIS//5.4, Y_AXIS//1.29))

                        if fight.hero_life[2] > 0 :
                            SCREEN.blit(baker_magician_character.load, (X_AXIS//6, Y_AXIS//2.7))

                            if X_AXIS > Y_AXIS: SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.hero_life[2]} {fight.hero[2].name}", False, color_names), (X_AXIS//5.6, Y_AXIS//1.79))
                            else:   SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.hero_life[2]}", False, color_names), (X_AXIS//4.9, Y_AXIS//1.79))

                        if fight.hero_life[3] > 0:
                            SCREEN.blit(baker_warrior_character.load, (X_AXIS//4.2, Y_AXIS//1.99))
                            
                            if X_AXIS > Y_AXIS: SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.hero_life[3]} {fight.hero[3].name}", False, color_names), (X_AXIS//4, Y_AXIS//1.45))
                            else:   SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.hero_life[3]}", False, color_names), (X_AXIS//3.6, Y_AXIS//1.45))           
                        
                        if fight.hero_life[0] < -1: fight.hero_life[0] = 0
                        if fight.hero_life[1] < -1: fight.hero_life[1] = 0
                        if fight.hero_life[2] < -1: fight.hero_life[2] = 0                      #pour pas depasser vers les nombres négatifs
                        if fight.hero_life[3] < -1: fight.hero_life[3] = 0

                        if len(fight.ennemies) == 1:
                            if fight.ennemies_life[0] > 0:
                                SCREEN.blit(monster.load, (X_AXIS//1.5,Y_AXIS//2.7))
                                SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.ennemies[0].name} {fight.ennemies_life[0]}", False, (255, 255, 255)), (X_AXIS//1.3,Y_AXIS//1.33))

                        elif len(fight.ennemies) == 2:
                            if fight.ennemies_life[0] > 0:
                                SCREEN.blit(monster.load, (X_AXIS//1.5, Y_AXIS//5))
                                SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.ennemies[0].name} {fight.ennemies_life[0]}", False, (255, 255, 255)), (X_AXIS//1.31, Y_AXIS//3.3))

                            if fight.ennemies_life[1] > 0:
                                SCREEN.blit(monster.load, (X_AXIS//1.5, Y_AXIS//2.4))
                                SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.ennemies[1].name} {fight.ennemies_life[1]}", False, (255, 255, 255)), (X_AXIS//1.31, Y_AXIS//1.24))    #si la liste des ennemies est égal à 2

                        elif len(fight.ennemies) == 3:
                            if fight.ennemies_life[0] > 0:
                                SCREEN.blit(monster.load, (X_AXIS//1.41, Y_AXIS//5))
                                SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.ennemies[0].name}{fight.ennemies_life[0]}", False, (255, 255, 255)), (X_AXIS//1.235, Y_AXIS//3.3))
            
                            if fight.ennemies_life[1] > 0:
                                SCREEN.blit(monster.load, (X_AXIS//1.41, Y_AXIS//2.45))
                                SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.ennemies[1].name} {fight.ennemies_life[1]}", False, (255, 255, 255)), (X_AXIS//1.235, Y_AXIS//1.24))   #si la liste des ennemies est égal à 1

                            if fight.ennemies_life[2] > 0:
                                SCREEN.blit(monster.load, (X_AXIS//1.7, Y_AXIS//3))
                                SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.ennemies[2].name} {fight.ennemies_life[2]}", False, (255, 255, 255)), (X_AXIS//1.46, Y_AXIS//2.27))

                        if fight.is_playing():                                                                                                  #si c'est autour des héros
                            menu_closed = Page(X_AXIS//1.78, Y_AXIS//15.5, X_AXIS//2.5, Y_AXIS//12, (37, 40, 80))
                            if game_choice:                                                                                                     #la fenetre
                                SCREEN.blit(Image("menu.png", (X_AXIS//2, Y_AXIS//1.07)).load, (X_AXIS//1.95, Y_AXIS//21))

                                if main_choice:
                                    attack_button = Page(X_AXIS//1.62, Y_AXIS//4, X_AXIS//3.5, Y_AXIS//9, color_attack_button)
                                    inventory_button = Page(X_AXIS//1.62, Y_AXIS//2.5, X_AXIS//3.5, Y_AXIS//9, color_heal_button)

                                    if X_AXIS > Y_AXIS:
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//50 + Y_AXIS//50)).render("ATTACK", False, (255, 255, 255)), (X_AXIS//1.42, Y_AXIS//3.75))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//50 + Y_AXIS//50)).render("INVENTORY", False, (255, 255, 255)), (X_AXIS//1.48, Y_AXIS//2.4))
                                    else:
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//100 + Y_AXIS//100)).render("ATTACK", False, (255, 255, 255)), (X_AXIS//1.42, Y_AXIS//3.75))     #le menu principal de la fenetre
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//100 + Y_AXIS//100)).render("INVENTORY", False, (255, 255, 255)), (X_AXIS//1.48, Y_AXIS//2.4))
                                    
                                    if_cursor = 0
                                    if attack_button.collision(x, y):   color_attack_button = (123, 95, 67)  
                                    else:   color_attack_button = (86, 66, 46)
                                        
                                    if inventory_button.collision(x, y):   color_heal_button = (123, 95, 67)
                                    else:   color_heal_button = (86, 66, 46)
                                            
                                    if inventory_button.collision(x, y) and click_cursor:   inventory_opened = True  
                                    if attack_button.collision(x, y) and click_cursor:  game_choice = False

                                if inventory_opened:  
                                    healing_potion_color = Page(X_AXIS//1.62, Y_AXIS//6, X_AXIS//3.5, Y_AXIS//25, healing_potion_color_page)
                                    SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"0{len(baker_inventory.content[5])}", False, (255, 255, 255)), (X_AXIS//1.2, Y_AXIS//6))   #le menu inventaire de la fenetre
                                    SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"healing potion", False, (255, 255, 255)), (X_AXIS//1.55, Y_AXIS//6))
                                                                                                                                                                                                                                
                                    if healing_potion_color.collision(x, y) and click_cursor and len(baker_inventory.content[5]) > 0:
                                        healing_potion_chosen = True
                                        game_choice = False

                                    knife_color = Page(X_AXIS//1.62, Y_AXIS//2.23, X_AXIS//3.5, Y_AXIS//25, knife_color_page)
                                    SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"0{len(baker_inventory.content[0])}", False, (255, 255, 255)), (X_AXIS//1.2, Y_AXIS//2.23))
                                    SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render("knife", False, (255, 255, 255)), (X_AXIS//1.55, Y_AXIS//2.23))
                                    if knife_color.collision(x, y) and click_cursor:
                                        inventory_opened = False
                                        knife_chosen = True

                                    sword_color = Page(X_AXIS//1.62, Y_AXIS//4.5, X_AXIS//3.5, Y_AXIS//25, sword_color_page)
                                    SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"0{len(baker_inventory.content[1])}", False, (255, 255, 255)), (X_AXIS//1.2, Y_AXIS//4.5))
                                    SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render("sword", False, (255, 255, 255)), (X_AXIS//1.55, Y_AXIS//4.5))
                                    if sword_color.collision(x, y) and click_cursor:
                                        inventory_opened = False
                                        sword_chosen = True
                                    
                                    bow_color = Page(X_AXIS//1.62, Y_AXIS//3.6, X_AXIS//3.5, Y_AXIS//25, bow_color_page)
                                    SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"0{len(baker_inventory.content[2])}", False, (255, 255, 255)), (X_AXIS//1.2, Y_AXIS//3.6))
                                    SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render("bow", False, (255, 255, 255)), (X_AXIS//1.55, Y_AXIS//3.6))
                                    if bow_color.collision(x, y) and click_cursor:
                                        inventory_opened = False
                                        bow_chosen = True
                                    
                                    crossbow_color = Page(X_AXIS//1.62, Y_AXIS//3, X_AXIS//3.5, Y_AXIS//25, crossbow_color_page)
                                    SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"0{len(baker_inventory.content[3])}", False, (255, 255, 255)), (X_AXIS//1.2, Y_AXIS//3))
                                    SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render("crossbow", False, (255, 255, 255)), (X_AXIS//1.55, Y_AXIS//3))
                                    if crossbow_color.collision(x, y) and click_cursor:
                                        inventory_opened = False
                                        crossbow_chosen = True
                                    
                                    magic_stick_color = Page(X_AXIS//1.62, Y_AXIS//2.55, X_AXIS//3.5, Y_AXIS//25, magic_stick_color_page)
                                    SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"0{len(baker_inventory.content[4])}", False, (255, 255, 255)), (X_AXIS//1.2, Y_AXIS//2.55))
                                    SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render("magic stick", False, (255, 255, 255)), (X_AXIS//1.55, Y_AXIS//2.55))
                                    if magic_stick_color.collision(x, y) and click_cursor:
                                        inventory_opened = False
                                        magic_stick_chosen = True

                                    if knife_color.collision(x, y): knife_color_page = (123, 95, 67)
                                    else:   knife_color_page = (86, 66, 46)
                                    
                                    if sword_color.collision(x, y): sword_color_page = (123, 95, 67)
                                    else:   sword_color_page = (86, 66, 46)
                                    
                                    if bow_color.collision(x, y): bow_color_page = (123, 95, 67)
                                    else:   bow_color_page = (86, 66, 46)
                                    
                                    if crossbow_color.collision(x, y): crossbow_color_page = (123, 95, 67)           #pour faire les animations quand on passe la souris sur les boutons
                                    else:   crossbow_color_page = (86, 66, 46)

                                    if magic_stick_color.collision(x, y): magic_stick_color_page = (123, 95, 67)
                                    else:   magic_stick_color_page = (86, 66, 46)

                                    if healing_potion_color.collision(x, y) and len(baker_inventory.content[5]) > 0: 
                                        healing_potion_color_page = (255, 0, 0)

                                    main_choice = False  
                                    if healing_potion_color.collision(x, y): healing_potion_color_page = (123, 95, 67)
                                    else:   healing_potion_color_page = (86, 66, 46)

                                    if menu_closed.collision(x, y): if_cursor = 2                                    
                                    else:   if_cursor = 0

                                    if menu_closed.collision(x, y) and click_cursor:                                #revenir sur le menu principal quand on est dans l'inventaire
                                        main_choice = True
                                        inventory_opened = False  
                                
                                if knife_chosen:
                                    if len(baker_inventory.content[0]) == 0:    
                                        inventory_opened = True
                                        knife_chosen = False

                                    if menu_closed.collision(x, y) and click_cursor:
                                        knife_chosen = False
                                        inventory_opened = True  

                                    if menu_closed.collision(x, y): if_cursor = 2
                                    else:   if_cursor = 0

                                    if len(baker_inventory.content[0]) >= 1:     
                                        Page(X_AXIS//1.62, Y_AXIS//6, X_AXIS//3.5, Y_AXIS//25, knife_color_page)       
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"damage: {baker_inventory.content[0][0].damage}", False, (255, 255, 255)), (X_AXIS//1.62, Y_AXIS//6))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"durability: {baker_inventory.content[0][0].durability}", False, (255, 255, 255)), (X_AXIS//1.34, Y_AXIS//6))

                                    if len(baker_inventory.content[0]) >= 2:
                                        Page(X_AXIS//1.62, Y_AXIS//4.5, X_AXIS//3.5, Y_AXIS//25, knife_color_page)
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"damage: {baker_inventory.content[0][1].damage}", False, (255, 255, 255)), (X_AXIS//1.62, Y_AXIS//4.5))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"durability: {baker_inventory.content[0][1].durability}", False, (255, 255, 255)), (X_AXIS//1.34, Y_AXIS//4.5))

                                    if len(baker_inventory.content[0]) >= 3:
                                        Page(X_AXIS//1.62, Y_AXIS//3.6, X_AXIS//3.5, Y_AXIS//25, knife_color_page)
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"damage: {baker_inventory.content[0][2].damage}", False, (255, 255, 255)), (X_AXIS//1.62, Y_AXIS//3.6))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"durability: {baker_inventory.content[0][2].durability}", False, (255, 255, 255)), (X_AXIS//1.34, Y_AXIS//3.6))


                                    if len(baker_inventory.content[0]) == 4:
                                        Page(X_AXIS//1.62, Y_AXIS//3, X_AXIS//3.5, Y_AXIS//25, knife_color_page)
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"damage: {baker_inventory.content[0][3].damage}", False, (255, 255, 255)), (X_AXIS//1.62, Y_AXIS//3))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"durability: {baker_inventory.content[0][3].durability}", False, (255, 255, 255)), (X_AXIS//1.34, Y_AXIS//3))
                                
                                if sword_chosen:
                                    if len(baker_inventory.content[1]) == 0:    
                                        inventory_opened = True
                                        sword_chosen = False

                                    if menu_closed.collision(x, y) and click_cursor:
                                        sword_chosen = False
                                        inventory_opened = True  

                                    if menu_closed.collision(x, y): if_cursor = 2
                                    else:   if_cursor = 0

                                    if len(baker_inventory.content[1]) >= 1:     
                                        Page(X_AXIS//1.62, Y_AXIS//6, X_AXIS//3.5, Y_AXIS//25, knife_color_page)       
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"damage: {baker_inventory.content[1][0].damage}", False, (255, 255, 255)), (X_AXIS//1.62, Y_AXIS//6))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"durability: {baker_inventory.content[1][0].durability}", False, (255, 255, 255)), (X_AXIS//1.34, Y_AXIS//6))

                                    if len(baker_inventory.content[1]) >= 2:
                                        Page(X_AXIS//1.62, Y_AXIS//4.5, X_AXIS//3.5, Y_AXIS//25, knife_color_page)
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"damage: {baker_inventory.content[1][1].damage}", False, (255, 255, 255)), (X_AXIS//1.62, Y_AXIS//4.5))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"durability: {baker_inventory.content[1][1].durability}", False, (255, 255, 255)), (X_AXIS//1.34, Y_AXIS//4.5))

                                    if len(baker_inventory.content[1]) >= 3:
                                        Page(X_AXIS//1.62, Y_AXIS//3.6, X_AXIS//3.5, Y_AXIS//25, knife_color_page)
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"damage: {baker_inventory.content[1][2].damage}", False, (255, 255, 255)), (X_AXIS//1.62, Y_AXIS//3.6))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"durability: {baker_inventory.content[1][2].durability}", False, (255, 255, 255)), (X_AXIS//1.34, Y_AXIS//3.6))


                                    if len(baker_inventory.content[1]) == 4:
                                        Page(X_AXIS//1.62, Y_AXIS//3, X_AXIS//3.5, Y_AXIS//25, knife_color_page)
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"damage: {baker_inventory.content[1][3].damage}", False, (255, 255, 255)), (X_AXIS//1.62, Y_AXIS//3))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"durability: {baker_inventory.content[1][3].durability}", False, (255, 255, 255)), (X_AXIS//1.34, Y_AXIS//3))


                                if bow_chosen:
                                    if len(baker_inventory.content[2]) == 0:    
                                        inventory_opened = True
                                        bow_chosen = False

                                    if menu_closed.collision(x, y) and click_cursor:
                                        bow_chosen = False
                                        inventory_opened = True  

                                    if menu_closed.collision(x, y): if_cursor = 2
                                    else:   if_cursor = 0

                                    if len(baker_inventory.content[2]) >= 1:     
                                        Page(X_AXIS//1.62, Y_AXIS//6, X_AXIS//3.5, Y_AXIS//25, knife_color_page)       
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"damage: {baker_inventory.content[2][0].damage}", False, (255, 255, 255)), (X_AXIS//1.62, Y_AXIS//6))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"durability: {baker_inventory.content[2][0].durability}", False, (255, 255, 255)), (X_AXIS//1.34, Y_AXIS//6))

                                    if len(baker_inventory.content[2]) >= 2:
                                        Page(X_AXIS//1.62, Y_AXIS//4.5, X_AXIS//3.5, Y_AXIS//25, knife_color_page)
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"damage: {baker_inventory.content[2][1].damage}", False, (255, 255, 255)), (X_AXIS//1.62, Y_AXIS//4.5))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"durability: {baker_inventory.content[2][1].durability}", False, (255, 255, 255)), (X_AXIS//1.34, Y_AXIS//4.5))

                                    if len(baker_inventory.content[2]) >= 3:
                                        Page(X_AXIS//1.62, Y_AXIS//3.6, X_AXIS//3.5, Y_AXIS//25, knife_color_page)
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"damage: {baker_inventory.content[2][2].damage}", False, (255, 255, 255)), (X_AXIS//1.62, Y_AXIS//3.6))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"durability: {baker_inventory.content[2][2].durability}", False, (255, 255, 255)), (X_AXIS//1.34, Y_AXIS//3.6))


                                    if len(baker_inventory.content[2]) == 4:
                                        Page(X_AXIS//1.62, Y_AXIS//3, X_AXIS//3.5, Y_AXIS//25, knife_color_page)
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"damage: {baker_inventory.content[2][3].damage}", False, (255, 255, 255)), (X_AXIS//1.62, Y_AXIS//3))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"durability: {baker_inventory.content[2][3].durability}", False, (255, 255, 255)), (X_AXIS//1.34, Y_AXIS//3))                        

                                if crossbow_chosen:
                                    if len(baker_inventory.content[3]) == 0:    
                                        inventory_opened = True
                                        crossbow_chosen = False

                                    if menu_closed.collision(x, y) and click_cursor:
                                        crossbow_chosen = False
                                        inventory_opened = True  

                                    if menu_closed.collision(x, y): if_cursor = 2
                                    else:   if_cursor = 0

                                    if len(baker_inventory.content[3]) >= 1:     
                                        Page(X_AXIS//1.62, Y_AXIS//6, X_AXIS//3.5, Y_AXIS//25, knife_color_page)       
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"damage: {baker_inventory.content[3][0].damage}", False, (255, 255, 255)), (X_AXIS//1.62, Y_AXIS//6))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"durability: {baker_inventory.content[3][0].durability}", False, (255, 255, 255)), (X_AXIS//1.34, Y_AXIS//6))

                                    if len(baker_inventory.content[3]) >= 2:
                                        Page(X_AXIS//1.62, Y_AXIS//4.5, X_AXIS//3.5, Y_AXIS//25, knife_color_page)
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"damage: {baker_inventory.content[3][1].damage}", False, (255, 255, 255)), (X_AXIS//1.62, Y_AXIS//4.5))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"durability: {baker_inventory.content[3][1].durability}", False, (255, 255, 255)), (X_AXIS//1.34, Y_AXIS//4.5))

                                    if len(baker_inventory.content[3]) >= 3:
                                        Page(X_AXIS//1.62, Y_AXIS//3.6, X_AXIS//3.5, Y_AXIS//25, knife_color_page)
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"damage: {baker_inventory.content[3][2].damage}", False, (255, 255, 255)), (X_AXIS//1.62, Y_AXIS//3.6))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"durability: {baker_inventory.content[3][2].durability}", False, (255, 255, 255)), (X_AXIS//1.34, Y_AXIS//3.6))


                                    if len(baker_inventory.content[3]) == 4:
                                        Page(X_AXIS//1.62, Y_AXIS//3, X_AXIS//3.5, Y_AXIS//25, knife_color_page)
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"damage: {baker_inventory.content[3][3].damage}", False, (255, 255, 255)), (X_AXIS//1.62, Y_AXIS//3))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"durability: {baker_inventory.content[3][3].durability}", False, (255, 255, 255)), (X_AXIS//1.34, Y_AXIS//3))
                                
                                if magic_stick_chosen:
                                    if len(baker_inventory.content[4]) == 0:    
                                        inventory_opened = True
                                        magic_stick_chosen = False

                                    if menu_closed.collision(x, y) and click_cursor:
                                        magic_stick_chosen = False
                                        inventory_opened = True  

                                    if menu_closed.collision(x, y): if_cursor = 2
                                    else:   if_cursor = 0
                                    
                                    if len(baker_inventory.content[2]) >= 1:     
                                        Page(X_AXIS//1.62, Y_AXIS//6, X_AXIS//3.5, Y_AXIS//25, knife_color_page)       
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"damage: {baker_inventory.content[4][0].damage}", False, (255, 255, 255)), (X_AXIS//1.62, Y_AXIS//6))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"durability: {baker_inventory.content[4][0].durability}", False, (255, 255, 255)), (X_AXIS//1.34, Y_AXIS//6))

                                    if len(baker_inventory.content[2]) >= 2:
                                        Page(X_AXIS//1.62, Y_AXIS//4.5, X_AXIS//3.5, Y_AXIS//25, knife_color_page)
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"damage: {baker_inventory.content[4][1].damage}", False, (255, 255, 255)), (X_AXIS//1.62, Y_AXIS//4.5))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"durability: {baker_inventory.content[4][1].durability}", False, (255, 255, 255)), (X_AXIS//1.34, Y_AXIS//4.5))

                                    if len(baker_inventory.content[2]) >= 3:
                                        Page(X_AXIS//1.62, Y_AXIS//3.6, X_AXIS//3.5, Y_AXIS//25, knife_color_page)
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"damage: {baker_inventory.content[4][2].damage}", False, (255, 255, 255)), (X_AXIS//1.62, Y_AXIS//3.6))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"durability: {baker_inventory.content[4][2].durability}", False, (255, 255, 255)), (X_AXIS//1.34, Y_AXIS//3.6))


                                    if len(baker_inventory.content[2]) == 4:
                                        Page(X_AXIS//1.62, Y_AXIS//3, X_AXIS//3.5, Y_AXIS//25, knife_color_page)
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"damage: {baker_inventory.content[4][3].damage}", False, (255, 255, 255)), (X_AXIS//1.62, Y_AXIS//3))
                                        SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//75 + Y_AXIS//75)).render(f"durability: {baker_inventory.content[4][3].durability}", False, (255, 255, 255)), (X_AXIS//1.34, Y_AXIS//3))

                            elif healing_potion_chosen and game_choice == False:
                                SCREEN.blit(Image("menu_closed.png", (X_AXIS//2, Y_AXIS//1.07)).load, (X_AXIS//1.95, Y_AXIS//21))

                                if menu_closed.collision(x, y) and click_cursor:    
                                    game_choice = True
                                    healing_potion_chosen = False
                                elif menu_closed.collision(x, y): if_cursor = 2
                                else:   if_cursor = 1

                                if baker_archer_collision.collision(x, y) and fight.hero_life[0] > 0:  
                                    SCREEN.blit(Image("pointer.png", (X_AXIS//50, Y_AXIS//18)).load, (X_AXIS//10,Y_AXIS//2.5))
                                    if_cursor = 2

                                if baker_archer_collision.collision(x, y) and fight.hero_life[0] > 0 and click_cursor:
                                    fight.hero_life[0] += healing_potion.heal
                                    if len(baker_inventory.content[5]) == 1:
                                        baker_inventory.content.remove(baker_inventory.content[5][0])
                                    if len(baker_inventory.content[5]) == 2:
                                        baker_inventory.content.remove(baker_inventory.content[5][1])
                                    fight.current_round += 1
                                    healing_potion_chosen = False
                                    game_choice = True

                                if baker_warrior_collision.collision(x, y) and fight.hero_life[3] > 0:  
                                    SCREEN.blit(Image("pointer.png", (X_AXIS//50, Y_AXIS//18)).load, (X_AXIS//3.75,Y_AXIS//2.35))
                                    if_cursor = 2 

                                if baker_warrior_collision.collision(x, y) and fight.hero_life[3] > 0 and click_cursor:
                                    fight.hero_life[3] += healing_potion.heal
                                    if len(baker_inventory.content[5]) == 1:
                                        baker_inventory.content.remove(baker_inventory.content[5][0])
                                    if len(baker_inventory.content[5]) == 2:
                                        baker_inventory.content.remove(baker_inventory.content[5][1])
                                    fight.current_round += 1
                                    healing_potion_chosen = False
                                    game_choice = True

                                if baker_dwarf_collision.collision(x, y) and fight.hero_life[1] > 0:  
                                    SCREEN.blit(Image("pointer.png", (X_AXIS//50, Y_AXIS//18)).load, (X_AXIS//5.5,Y_AXIS//1.9))
                                    if_cursor = 2 

                                if baker_dwarf_collision.collision(x, y) and fight.hero_life[1] > 0 and click_cursor:
                                    fight.hero_life[1] += healing_potion.heal
                                    if len(baker_inventory.content[5]) == 1:
                                        baker_inventory.content.remove(baker_inventory.content[5][0])
                                    if len(baker_inventory.content[5]) == 2:
                                        baker_inventory.content.remove(baker_inventory.content[5][1])
                                    fight.current_round += 1
                                    healing_potion_chosen = False
                                    game_choice = True

                                if baker_magician_collision.collision(x, y) and fight.hero_life[2] > 0:  
                                    SCREEN.blit(Image("pointer.png", (X_AXIS//50, Y_AXIS//18)).load, (X_AXIS//5,Y_AXIS//3.4))
                                    if_cursor = 2
                                
                                if baker_magician_collision.collision(x, y) and fight.hero_life[2] > 0 and click_cursor:
                                    fight.hero_life[2] += healing_potion.heal
                                    if len(baker_inventory.content[5]) == 1:
                                        baker_inventory.content.remove(baker_inventory.content[5][0])
                                    if len(baker_inventory.content[5]) == 2:
                                        baker_inventory.content.remove(baker_inventory.content[5][1])
                                    fight.current_round += 1
                                    healing_potion_chosen = False
                                    game_choice = True
                                    
                            elif game_choice == False and healing_potion_chosen == False:
                                SCREEN.blit(Image("menu_closed.png", (X_AXIS//2, Y_AXIS//1.07)).load, (X_AXIS//1.95, Y_AXIS//21))

                                if menu_closed.collision(x, y) and click_cursor:    game_choice = True
                                elif baker_archer_collision.collision(x, y):  if_cursor = 3
                                elif baker_warrior_collision.collision(x, y):  if_cursor = 3
                                elif baker_dwarf_collision.collision(x, y):  if_cursor = 3
                                elif baker_magician_collision.collision(x, y):  if_cursor = 3
                                elif menu_closed.collision(x, y): if_cursor = 2
                                else:   if_cursor = 1
                                
                                if len(fight.ennemies) == 1:
                                    if monster_1.collision(x, y) and fight.ennemies_life[0] > 0:   SCREEN.blit(Image("pointer.png", (X_AXIS//50, Y_AXIS//18)).load, (X_AXIS//1.28,Y_AXIS//2.35))
                                    
                                    if monster_1.collision(x, y) and click_cursor:
                                        animation_launched = True
                                        monster1_attack = True

                                if len(fight.ennemies) == 2:
                                    if monster_1.collision(x, y) and fight.ennemies_life[0] > 0:   SCREEN.blit(Image("pointer.png", (X_AXIS//50, Y_AXIS//18)).load, (X_AXIS//1.28,Y_AXIS//4.5))
                                    if monster_2.collision(x, y) and fight.ennemies_life[1] > 0:   SCREEN.blit(Image("pointer.png", (X_AXIS//50, Y_AXIS//18)).load, (X_AXIS//1.28,Y_AXIS//2.28))

                                    if monster_1.collision(x, y) and click_cursor:
                                        animation_launched = True
                                        monster1_attack = True
                                    
                                    if monster_2.collision(x, y) and click_cursor:
                                        animation_launched = True
                                        monster2_attack = True

                                if len(fight.ennemies) == 3:
                                    if monster_1.collision(x, y) and fight.ennemies_life[0] > 0:   SCREEN.blit(Image("pointer.png", (X_AXIS//50, Y_AXIS//18)).load, (X_AXIS//1.22,Y_AXIS//4.5))
                                    if monster_2.collision(x, y) and fight.ennemies_life[1] > 0:   SCREEN.blit(Image("pointer.png", (X_AXIS//50, Y_AXIS//18)).load, (X_AXIS//1.22,Y_AXIS//2.28))
                                    if monster_3.collision(x, y) and fight.ennemies_life[2] > 0:   SCREEN.blit(Image("pointer.png", (X_AXIS//50, Y_AXIS//18)).load, (X_AXIS//1.43,Y_AXIS//2.7))

                                    if monster_1.collision(x, y) and click_cursor:
                                        animation_launched = True
                                        monster1_attack = True
                                    
                                    if monster_2.collision(x, y) and click_cursor:
                                        animation_launched = True
                                        monster2_attack = True

                                    if monster_3.collision(x, y) and click_cursor:
                                        animation_launched = True
                                        monster3_attack = True
                            
                        if animation_launched:
                            attack_animation += 1

                            if attack_animation >= round(Clock.get_fps())//2:
                                attack_animation = 0
                                animation += 1

                            if monster1_attack and fight.ennemies_life[0] > 0:
                                if animation == 3:
                                    fight.ennemies_life[0] -= fight.round[fight.current_round].punch_damage
                                    print(fight.round[fight.current_round].name, "attacked", fight.ennemies[0].name)
                                    
                                    
                                    animation = 0
                                    fight.current_round += 1
                                    animation_launched = False
                                    game_choice = True
                                    monster1_attack = False
                                else:
                                    if_cursor = 0
                                    game_choice = False

                                    SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.round[fight.current_round].name} attacked {fight.ennemies[0].name}", False, (255, 255, 255)), (X_AXIS//1.8, Y_AXIS//2.5))

                                    if fight.round[fight.current_round] == baker_archer:    SCREEN.blit(Image(heros[1][0][animation], (X_AXIS//10, Y_AXIS//5.5)).load, (X_AXIS//1.8, Y_AXIS//2))
                                    if fight.round[fight.current_round] == baker_dwarf:     SCREEN.blit(Image(heros[1][1][animation], (X_AXIS//10, Y_AXIS//5.5)).load, (X_AXIS//1.8, Y_AXIS//2))  
                                    if fight.round[fight.current_round] == baker_magician:  SCREEN.blit(Image(heros[1][2][animation], (X_AXIS//10, Y_AXIS//5.5)).load, (X_AXIS//1.8, Y_AXIS//2))
                                    if fight.round[fight.current_round] == baker_warrior:   SCREEN.blit(Image(heros[1][3][animation], (X_AXIS//10, Y_AXIS//5.5)).load, (X_AXIS//1.8, Y_AXIS//2))

                            if monster2_attack and len(fight.ennemies) >= 2 and fight.ennemies_life[1] > 0:
                                if animation == 3:
                                    fight.ennemies_life[1] -= fight.round[fight.current_round].punch_damage
                                    print(fight.round[fight.current_round].name, "attacked", fight.ennemies[1].name)
                                    
                                    animation = 0
                                    
                                    fight.current_round += 1
                                    animation_launched = False
                                    game_choice = True
                                    monster2_attack = False
                                    
                                else:
                                    if_cursor = 0
                                    game_choice = False

                                    SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.round[fight.current_round].name} attacked {fight.ennemies[1].name}", False, (255, 255, 255)), (X_AXIS//1.8, Y_AXIS//2.5))

                                    if fight.round[fight.current_round] == baker_archer:    SCREEN.blit(Image(heros[1][0][animation], (X_AXIS//10, Y_AXIS//5.5)).load, (X_AXIS//1.8, Y_AXIS//2))
                                    if fight.round[fight.current_round] == baker_dwarf:     SCREEN.blit(Image(heros[1][1][animation], (X_AXIS//10, Y_AXIS//5.5)).load, (X_AXIS//1.8, Y_AXIS//2))  
                                    if fight.round[fight.current_round] == baker_magician:  SCREEN.blit(Image(heros[1][2][animation], (X_AXIS//10, Y_AXIS//5.5)).load, (X_AXIS//1.8, Y_AXIS//2))
                                    if fight.round[fight.current_round] == baker_warrior:   SCREEN.blit(Image(heros[1][3][animation], (X_AXIS//10, Y_AXIS//5.5)).load, (X_AXIS//1.8, Y_AXIS//2))

                            if monster3_attack and len(fight.ennemies) == 3 and fight.ennemies_life[2] > 0:
                                if animation == 3:
                                    fight.ennemies_life[2] -= fight.round[fight.current_round].punch_damage
                                    print(fight.round[fight.current_round].name, "attacked", fight.ennemies[2].name)

                                    animation = 0
                                    monster3_attack = False
                                    fight.current_round += 1
                                    animation_launched = False
                                    game_choice = True
                                else:
                                    if_cursor = 0
                                    SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.round[fight.current_round].name} attacked {fight.ennemies[2].name}", False, (255, 255, 255)), (X_AXIS//1.8, Y_AXIS//2.5))
                                    
                                    game_choice = False
                                    if fight.round[fight.current_round] == baker_archer:    SCREEN.blit(Image(heros[1][0][animation], (X_AXIS//10, Y_AXIS//5.5)).load, (X_AXIS//1.8, Y_AXIS//2))
                                    if fight.round[fight.current_round] == baker_dwarf:     SCREEN.blit(Image(heros[1][1][animation], (X_AXIS//10, Y_AXIS//5.5)).load, (X_AXIS//1.8, Y_AXIS//2))  
                                    if fight.round[fight.current_round] == baker_magician:  SCREEN.blit(Image(heros[1][2][animation], (X_AXIS//10, Y_AXIS//5.5)).load, (X_AXIS//1.8, Y_AXIS//2))
                                    if fight.round[fight.current_round] == baker_warrior:   SCREEN.blit(Image(heros[1][3][animation], (X_AXIS//10, Y_AXIS//5.5)).load, (X_AXIS//1.8, Y_AXIS//2))
                        
                        if not fight.is_playing():
                            monster_animation += 1
                            if choice_hero:
                                hero = random.randint( 0, len(fight.hero)-1)
                                choice_hero = False

                            if monster_animation >= 2*( round(Clock.get_fps())//2):
                                monster_animation = 0

                                fight.hero_life[hero] -= fight.round[fight.current_round].damage 

                                print(fight.round[fight.current_round].name, "attacked", fight.hero[hero].name)                     #c'est autour des monstres
                                fight.current_round += 1   
                                choice_hero = True
                            else:
                                SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.round[fight.current_round].name} attacked {fight.hero[hero].name}", False, (255, 255, 255)), (X_AXIS//2,Y_AXIS//2))

                        
                        Page(5, Y_AXIS//100, X_AXIS//7, Y_AXIS//25, (20, 20, 20))
                        if fight.hero_life[0] > 0:
                            Page(5 + X_AXIS//80, Y_AXIS//75, X_AXIS//7.4 - (X_AXIS//fight.hero_life[0]), Y_AXIS//30, (120,190,33))

                        SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.hero_life[0]}/65", False, (255, 255, 255)), (X_AXIS//25, Y_AXIS//75))
                        SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.hero[0].name}", False, (255, 255, 255)), (X_AXIS//6.5, Y_AXIS//75)) 

                        Page(5, Y_AXIS//18, X_AXIS//7, Y_AXIS//25, (20, 20, 20))
                        if fight.hero_life[1] > 0:
                            Page(5 + X_AXIS//80, Y_AXIS//17, X_AXIS//7.65 - (X_AXIS//fight.hero_life[1]), Y_AXIS//30, (120,190,33))

                        SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.hero_life[1]}/90", False, (255, 255, 255)), (X_AXIS//25, Y_AXIS//17))
                        SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.hero[1].name}", False, (255, 255, 255)), (X_AXIS//6.5, Y_AXIS//17))

                        Page(5, Y_AXIS//10, X_AXIS//7, Y_AXIS//25, (20, 20, 20))                                                                    #systeme de plus apparaitre lors que le pero n'a plus de vie
                        if fight.hero_life[2] > 0:
                            Page(5 + X_AXIS//80, Y_AXIS//9.7, X_AXIS//7.4 - (X_AXIS//fight.hero_life[2]), Y_AXIS//30, (120,190,33))
                        
                        SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.hero_life[2]}/60", False, (255, 255, 255)), (X_AXIS//25, Y_AXIS//9.7))
                        SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.hero[2].name}", False, (255, 255, 255)), (X_AXIS//6.5, Y_AXIS//9.7))
                        
                        Page(5, Y_AXIS//7, X_AXIS//7, Y_AXIS//25, (20, 20, 20))
                        if fight.hero_life[3] > 0:
                            Page(5 + X_AXIS//80, Y_AXIS//6.85, X_AXIS//8 - (X_AXIS//fight.hero_life[3]), Y_AXIS//30, (120,190,33))

                        SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.hero_life[3]}/125", False, (255, 255, 255)), (X_AXIS//30, Y_AXIS//6.85))
                        SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"{fight.hero[3].name}", False, (255, 255, 255)), (X_AXIS//6.5, Y_AXIS//6.85))

                        if fight.hero_life[0] > 65:     fight.hero_life[0] = 65
                        if fight.hero_life[1] > 90:     fight.hero_life[1] = 90
                        if fight.hero_life[2] > 60:     fight.hero_life[2] = 60
                        if fight.hero_life[3] > 125:    fight.hero_life[3] = 125

                    else:
                        if end_music and pygame.mixer.music.get_pos() == 0:
                            Music("phonk\\phonk_fin.ogg", SOUND)
                            end_music = False
                        SCREEN.fill((0, 0, 0))
                        if  sum(fight.hero_life):   SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//50 + Y_AXIS//50)).render("VICTORY", False, (255, 255, 255)), (X_AXIS//2.5, Y_AXIS//2.5))
                        else:   SCREEN.blit(pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//50 + Y_AXIS//50)).render("DEFEAT", False, (255, 255, 255)), (X_AXIS//2.5, Y_AXIS//2.5))
                
                else:
                    if start_music:
                        Music("phonk\\phonk.ogg", SOUND)         #la class music qui est utilisé avec la musique (créée)
                        start_music = False
                        
                    SCREEN.fill((0, 0, 0))
                    SCREEN.blit(Text(X_AXIS, Y_AXIS).render("in a world with corruption and madness, our heros will chase the bread thief and retake their recipe of the bread sacred ", False, (255, 255, 255)), (X_AXIS//30, Y_AXIS//6.85))
                    SCREEN.blit(Text(X_AXIS, Y_AXIS).render("they're going in a strange place and they discovered that", False, (255, 255, 255)), (X_AXIS//30, Y_AXIS//6))     #le lore du jeu
                    SCREEN.blit(Text(X_AXIS, Y_AXIS).render("even if someone die, if they have friend with them, he can help him even in death ", False, (255, 255, 255)), (X_AXIS//30, Y_AXIS//5.2))

            cursor = Image(f'{crosshair[if_cursor]}', ( 26, 26))
            SCREEN.blit(cursor.load, (x, y)) 
        except Exception as error:

            SCREEN.fill((0, 0, 0))
            SCREEN.blit(Text(X_AXIS, Y_AXIS).render(f"error {error}, the game needs to be restarted", False, (255, 255, 255)), (X_AXIS//30, Y_AXIS//6.85))

            print(error)
        information(X_AXIS, Y_AXIS, Clock)

        Clock.tick(FPS)
        pygame.display.flip()                                                                                               #le systeme d'image sur pygame
        pygame.display.update()
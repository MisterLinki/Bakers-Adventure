import pygame                                                                       # importer pygame (il sert à faire une fenêtre avec des fonctions expret pour les jeux)
import pyautogui                                                                    # importer pyautogui (il sert juste à prendre la résolution de l'écran)

click_cursor = False                                                                # créer la variable cliquer curseur False
is_mouse = True                                                                     # créer la variable si c'est la souris True

SOUND = 0.15                                                                        # la variable sound
FPS = 60                                                                            # les images maximales par secondes

x, y = 0, 0
if_cursor = 0
time_click = 0

image = 0
current_hero_image = 0

crosshair = [
            'cursor-png-1127.png', 
            'crosshair.png',
            'cursor_pointer.png',
            'nope_cursor.png'
            ]

cookiemonster = [
                'monstercookie\\monstercookie1.png', 
                'monstercookie\\monstercookie2.png', 
                'monstercookie\\monstercookie3.png'
                ]

heros = [[
        ['baker\\normal_animation\\baker_archer1.png','baker\\normal_animation\\baker_archer2.png','baker\\normal_animation\\baker_archer3.png'],                                                         
        # baker archer normal animation
        
        ['baker\\normal_animation\\baker_dwarf1.png','baker\\normal_animation\\baker_dwarf2.png','baker\\normal_animation\\baker_dwarf3.png'],                                                            
        # baker dwarf normal animation
        
        ['baker\\normal_animation\\baker_magician1.png','baker\\normal_animation\\baker_magician2.png','baker\\normal_animation\\baker_magician3.png'],                                                   
        # baker magician normal animation       
        
        ['baker\\normal_animation\\baker_warrior1.png','baker\\normal_animation\\baker_warrior2.png','baker\\normal_animation\\baker_warrior3.png']                                                       
        # baker warrior normal animation
        ],[   
        ['baker\\attack_animation\\baker_animation_archer_attack1.png','baker\\attack_animation\\baker_animation_archer_attack2.png','baker\\attack_animation\\baker_animation_archer_attack3.png'],      
        # baker archer attack animation
        
        ['baker\\attack_animation\\baker_animation_dwarf_attack1.png','baker\\attack_animation\\baker_animation_dwarf_attack2.png','baker\\attack_animation\\baker_animation_dwarf_attack3.png'],         
        # baker dwarf attack animation
        
        ['baker\\attack_animation\\baker_animation_magician_attack1.png','baker\\attack_animation\\baker_animation_magician_attack2.png','baker\\attack_animation\\baker_animation_magician_attack3.png'],
        # baker magician attack animation
        
        ['baker\\attack_animation\\baker_animation_warrior_attack1.png','baker\\attack_animation\\baker_animation_warrior_attack2.png','baker\\attack_animation\\baker_animation_warrior_attack3.png']    
        # baker warrior attack animation
        ]]
monster_animation = 0
attack_animation = 0
animation = 0
opening = 0
monster1_attack = False
monster2_attack = False
monster3_attack = False

exit_game = False
# les couleurs des blocks du jeu dans le menu

game_type_color = (200, 200, 200)                                                   # les couleurs du bouton "Play"
change_type_color = (200, 200, 200)                                                 # les couleurs du bouton "Change mode"
quit_type_color = (200, 200, 200)                                                   # les couleurs du bouton "quit game"
quit_type_color_yes = (200, 200, 200)
quit_type_color_no = (200, 200, 200)
color_text_game_button = (10, 10, 10)                                               # les couleurs du text "play"
color_text_change_type = (10, 10, 10)                                               # les couleurs du text "change mode"
color_text_quit_type = (10, 10, 10)                                                 # les couleurs du text "quit game"

color_attack_button = (50, 50, 50)
color_heal_button = (50, 50, 50)
color_names = (25, 25, 25)  

knife_color_page = (86, 66, 46)
sword_color_page = (86, 66, 46)
crossbow_color_page = (86, 66, 46)
bow_color_page = (86, 66, 46)
magic_stick_color_page = (86, 66, 46)
healing_potion_color_page = (86, 66, 46)

X_AXIS_GAME, Y_AXIS_GAME = pyautogui.size()                                         # avoir la resolution de l'écran
Y_AXIS_GAME -= 63                                                                   # -63 pour pas que le jeu sois en plein écran fenêtré

SCREEN = pygame.display.set_mode((X_AXIS_GAME, Y_AXIS_GAME), pygame.RESIZABLE)      # définir l'écran du jeu avec la résolution de l'ecran et pygame.RESIZABLE sert à pouvoir bouger l'écran (dans la partie responsive)
pygame.display.set_caption("Bakers Adventure")

def Text(X_AXIS, Y_AXIS):
    return pygame.font.SysFont('.\\Liberation Serif', (X_AXIS//150 + Y_AXIS//150))  # faire une fonction qui permet d'écrire ce qu'on veut avec la police liberation serif

mainpage = True                                                                     # ouvrir la page de menu
launchgame = False                                                                  # ouvrir la page du jeu
settings = False                                                                    # ouvrir la page des settings
game_inventory = False
game_choice = True
choice = False
main_choice = True
inventory_opened = False
animation_launched = False

choice_hero = True

knife_chosen = False
sword_chosen = False
bow_chosen = False
crossbow_chosen = False
magic_stick_chosen = False

healing_potion_chosen = False

start_music = True
middle_music = True
end_music = True


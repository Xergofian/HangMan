import os, keyboard
from keyboard_frame import list_keyboard
from time import sleep

from rich.console import Console, Style
from function_move import up_move, down_move, left_move, right_move
console = Console()
#==================style for button==================#

style_selected_item = Style(color = "yellow",blink2 = True, bold = True)
#====================================================#
# list_of_levels = os.listdir("Dictionary")
from rich import print
#from rich.padding import Padding
#test = Padding("Hello", (2, 4), style="on blue", expand=False)
#print(test)
clear = lambda: os.system('cls')
pointer_Index = [2,3]
list_Qwerty = [
                [' ','q',' ','w',' ','e',' ','r',' ','t',' ','y',' ','u',' ','i',' ','o',' ','p'],
                [' ',' ','a',' ','s',' ','d',' ','f',' ','g',' ','h',' ','j',' ','k',' ','l'],
                [' ',' ',' ','z',' ','x',' ','c',' ','v',' ','b',' ','n',' ','m',]
              ]


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def main_draw():
    clearConsole()
    draw(list_Qwerty)
    
 
def draw(list_qwerty):
    for i in range(len(list_qwerty)):
        for j in range(len(list_qwerty[i])):
            if( pointer_Index[0] == i and pointer_Index[1] == j and list_qwerty!=' '):
                for a in range(len(list_keyboard)):
                    for b in range(len(list_keyboard[a])):
                        temp_list = list_keyboard[a][b]
                        for k in range(len(temp_list)):
                            if temp_list[k] == list_qwerty[i][j].upper():
                                console.print(temp_list[k], style = style_selected_item, end="")
                            else:
                                console.print(temp_list[k], end="")
                        print()

play_F = True
wait_time = 0.2
main_draw()

while(play_F == True):
    
    if keyboard.is_pressed('up'):
        up_move(pointer_Index)
        sleep(wait_time)
        main_draw()
        
    if keyboard.is_pressed('down'):
        down_move(pointer_Index)
        sleep(wait_time)
        main_draw()
        
    if keyboard.is_pressed('left'):
        left_move(pointer_Index)
        sleep(wait_time)
        main_draw()
    
    if keyboard.is_pressed('right'):
        right_move(pointer_Index)
        sleep(wait_time)
        main_draw()
    
    if keyboard.is_pressed('esc'):
        play_F = False
    

'''
for i in range(len(list_keyboard)):
      for j in range(len(list_keyboard[i])):
            print(list_keyboard[i][j])
'''              
   
               

import pygame,sys,random
from checker_kings_engine import *
from pygame.locals import *

pygame.init()

#Open Pygame window
screen = pygame.display.set_mode((640, 480),RESIZABLE) #add RESIZABLE ou FULLSCREEN
#Icone
icone = pygame.image.load("checker_resources/checker_icon.png")
pygame.display.set_icon(icone)
#Title
pygame.display.set_caption("checker kings")
colors=pygame.color.THECOLORS["black"]
#http://svg_experimenten.deds.nl/draughtboard/draughts_diagram_maker.html
screen_title=pygame.image.load("checker_resources/checker_title2.png").convert()                           
board= pygame.image.load("checker_resources/board3.png").convert()
board_pos=(100,20)
green_light= pygame.image.load("checker_resources/green_light.png").convert()
green_light.set_colorkey((255,255,255))
red_light= pygame.image.load("checker_resources/red_light.png").convert()
red_light.set_colorkey((255,255,255))
sprite_liste=["checker_resources/circle_pieces.png","checker_resources/chess_pieces.png",
"checker_resources/ghost.png","checker_resources/sphere.png","checker_resources/smiley.png"]
sprite_liste_index=0
sprite_sheet=pygame.image.load(sprite_liste[sprite_liste_index]).convert_alpha()
scaled_sheet=pygame.transform.scale(sprite_sheet,(200,50)).convert_alpha()
blue=scaled_sheet.subsurface(150,0,50,50).convert_alpha()
b_king=scaled_sheet.subsurface(100,0,50,50).convert_alpha()
red=scaled_sheet.subsurface(50,0,50,50).convert_alpha()
r_king=scaled_sheet.subsurface(0,0,50,50).convert_alpha()
title=1
display_type=0
win_score=0
lose_score=0
draw_score=0
get_result=1
to_break=0
selected_pawn=[]
target=0
move=0
pawn_moves=[]
jump_pawn_moves=[]
jump_pawn_targets=[]
player_must_jump=0
cpu_must_jump=0
cpu_moves=0
jump_pawn=[]
second_jump_pawn=[]
selected=0
selected_jump=0
selected_jump_moves=[]
stop_appending=0
turn="player"
second_jump=0
time=0
depth=3
cpu_level=depth
cpu_first_turn=1
font=pygame.font.SysFont('Arial', 30)       
tab_pos=[[],[],[],[],[],[],[],[]]
record_tab=[ [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0], ]
copy_tab(tab=tab,tab_copy=record_tab)
score_record=[win_score,lose_score,draw_score]
x=board_pos[0]+20;y=board_pos[1]+20
for i in range(8):
      for j in range(8):
          tab_pos[i].append([x,y])
          x+=50
      y+=50
      x=board_pos[0]+20

      
pygame.key.set_repeat(400, 30)

while True:
    
  #loop speed limitation
  #10 frames per second is enought
  pygame.time.Clock().tick(10)
  
  while title:
        
        #loop speed limitation
        #10 frames per second is enought
        pygame.time.Clock().tick(10)

        for event in pygame.event.get():    #wait for events
            if event.type==pygame.QUIT:
               continuer=0
               pygame.quit()
               sys.exit()
        if event.type == KEYDOWN and event.key == K_f:
              if display_type==0:display_type=FULLSCREEN
              elif display_type==FULLSCREEN:display_type=0
              screen = pygame.display.set_mode((640,480),display_type)
        elif event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
              reintialize_tab();cpu_first_turn=1;get_result=1
              player_must_jump=0;cpu_must_jump=0;selected=0
              title=0;win_score=0;lose_score=0;draw_score=0
              cpu_level=3;depth=cpu_level
        screen.blit(screen_title,(0,0))
        pygame.display.flip()

              
  if turn=="player" and not player_must_jump:
        
     jump_pawn=[]
     jump_pawn_moves=[]
     jump_pawn_targets=[]

     if not second_jump:
        for i in range(8):
            for j in range(8):
                pos=[i,j]
                if tab[i][j]==1 or tab[i][j]==3:
                   if must_jump(pos,"player"):
                      player_must_jump=1
                      jump_pawn.append(pos)
                      move,target=get_jump_moves(pos,"player")
                      jump_pawn_moves.append(move)
                      jump_pawn_targets.append(target)
                         
     elif second_jump:
        pos=second_jump_pawn
        second_jump=0
        player_must_jump=1
        jump_pawn.append(pos)
        move,target=get_jump_moves(pos,"player")          
        jump_pawn_moves.append(move)
        jump_pawn_targets.append(target)
        
   
  for event in pygame.event.get():     #wait for events
    if event.type==pygame.QUIT:
      continuer=0
      pygame.quit()
      sys.exit()
      
    #keyboard commands
    if event.type == KEYDOWN:
     if turn=="player":
       if event.key == K_f:
          if display_type==0:display_type=FULLSCREEN
          elif display_type==FULLSCREEN:display_type=0
          screen = pygame.display.set_mode((640,480),display_type)
       if event.key == K_e:
          title=1
       if event.key == K_r:
          player_must_jump=0;selected=0;get_result=1
          copy(tab_copy=record_tab,tab=tab)
          win_score=score_record[0]
          lose_score=score_record[1]
          draw_score=score_record[2]
       if event.key == K_n:
          reintialize_tab();cpu_first_turn=1;get_result=1
          player_must_jump=0;cpu_must_jump=0;selected=0
       if event.key == K_RIGHT:
          if sprite_liste_index<len(sprite_liste)-1:
             sprite_liste_index+=1
       elif event.key == K_LEFT:
          if sprite_liste_index>=1:
             sprite_liste_index-=1
       if event.key == K_UP:
          if cpu_level<=8:
             cpu_level+=1
       elif event.key == K_DOWN:
          if cpu_level>=2:
             cpu_level-=1
       depth=cpu_level
       sprite_sheet=pygame.image.load(sprite_liste[sprite_liste_index]).convert_alpha()
       scaled_sheet=pygame.transform.scale(sprite_sheet,(200,50)).convert_alpha()
       blue=scaled_sheet.subsurface(150,0,50,50).convert_alpha()
       b_king=scaled_sheet.subsurface(100,0,50,50).convert_alpha()
       red=scaled_sheet.subsurface(50,0,50,50).convert_alpha()
       r_king=scaled_sheet.subsurface(0,0,50,50).convert_alpha()
    #mouse movement commands
    if event.type == MOUSEBUTTONDOWN:
       if cpu_win() or  player_win() or draw():
          reintialize_tab();cpu_first_turn=1;get_result=1
       if event.button == 1:
         if not cpu_win() and not player_win() and not draw():
          if turn=="player" and not player_must_jump: 
             if selected:
                for move in pawn_moves:
                    pos=selected_pawn
                    new_pos=move
                    move_pos=tab_pos[move[0]][move[1]]
                    if event.pos[0]>move_pos[0]and event.pos[0]<move_pos[0]+50 \
                    and event.pos[1]>move_pos[1]and event.pos[1]<move_pos[1]+50 :
                        copy_tab(tab=tab,tab_copy=record_tab)
                        score_record=[win_score,lose_score,draw_score]
                        move_pawn(pos,new_pos);to_break=1;selected=0;turn="cpu"
                        
          if turn=="player"and not player_must_jump:            
             for i in range(8):
                 if not to_break:
                   for j in range(8):
                     pos=tab_pos[i][j]
                     if tab[i][j]==1 or tab[i][j]==3:
                        if event.pos[0]>pos[0]and event.pos[0]<pos[0]+50 \
                        and event.pos[1]>pos[1]and event.pos[1]<pos[1]+50 :
                            if not selected:
                               selected=1;light_pos=pos
                               pawn_moves=get_pawn_moves([i,j])
                               selected_pawn=[i,j]
                               pawn_pos=pos=tab_pos[selected_pawn[0]][selected_pawn[1]]
                            elif selected:selected=0
                        if selected and not(event.pos[0]>pawn_pos[0]and event.pos[0]<pawn_pos[0]+50 \
                        and event.pos[1]>pawn_pos[1]and event.pos[1]<pawn_pos[1]+50) :
                            selected=0;to_break=1;break
              
          if turn=="player" and  player_must_jump:
             if selected_jump:stop_appending=1
             else:selected_jump_moves=[];stop_appending=0
             
             for i in range(len(jump_pawn_moves)):
                 if to_break:break
                 move=jump_pawn_moves[i]
                 for j in range(len(move)):
                     pos=jump_pawn[i]  
                     new_pos=jump_pawn_moves[i][j]
                     target=jump_pawn_targets[i][j]
                     jump_pos=tab_pos[new_pos[0]][new_pos[1]]
                     jump_pawn_pos=tab_pos[pos[0]][pos[1]]
                     if event.pos[0]>jump_pos[0]and event.pos[0]<jump_pos[0]+50 \
                     and event.pos[1]>jump_pos[1]and event.pos[1]<jump_pos[1]+50 :
                         if not stop_appending:
                            selected_jump=1
                            selected_jump_pos=jump_pos
                            selected_jump_moves.append([pos,new_pos,target])
                         else:selected_jump=0
                     if selected_jump and event.pos[0]>jump_pawn_pos[0]and event.pos[0]<jump_pawn_pos[0]+50 \
                        and event.pos[1]>jump_pawn_pos[1]and event.pos[1]<jump_pawn_pos[1]+50 :
                            for move in selected_jump_moves:
                                if pos==move[0]:
                                   copy_tab(tab=tab,tab_copy=record_tab)
                                   score_record=[win_score,lose_score,draw_score]
                                   pos=move[0];new_pos=move[1];target=move[2]
                                   jump(pos,new_pos,target)
                                   player_must_jump=0;selected_jump=0;to_break=1
                                   if not must_jump(new_pos,"player"):turn="cpu"
                                   else:second_jump_pawn=new_pos;second_jump=1
                            if to_break:break
                     if event.pos[0]>jump_pawn_pos[0]and event.pos[0]<jump_pawn_pos[0]+50 \
                     and event.pos[1]>jump_pawn_pos[1]and event.pos[1]<jump_pawn_pos[1]+50 :
                         copy_tab(tab=tab,tab_copy=record_tab)
                         score_record=[win_score,lose_score,draw_score]
                         jump(pos,new_pos,target)
                         player_must_jump=0
                         if not must_jump(new_pos,"player"):turn="cpu"
                         else:second_jump_pawn=new_pos;second_jump=1
                         to_break=1;break
                         
             if selected_jump and not(event.pos[0]>selected_jump_pos[0]and event.pos[0]<selected_jump_pos[0]+50 \
             and event.pos[1]>selected_jump_pos[1]and event.pos[1]<selected_jump_pos[1]+50) :
                selected_jump=0
  
          to_break=0
          

  if turn=="cpu" and not cpu_win() and not player_win() and not draw():
    
    time+=1
    if time==3:
     time=0
     if not cpu_must_jump:
           
        jump_pawn=[]
        jump_pawn_moves=[]
        jump_pawn_targets=[]
        
        if not second_jump:
           for i in range(8):
               for j in range(8):
                   pos=[i,j]
                   if tab[i][j]==2 or tab[i][j]==4:
                      if must_jump(pos,"cpu"):
                         cpu_must_jump=1
                         jump_pawn.append(pos)
                         move,target=get_jump_moves(pos,"cpu")
                         jump_pawn_moves.append(move)
                         jump_pawn_targets.append(target)
                      
        elif second_jump:
           pos=second_jump_pawn
           second_jump=0
           cpu_must_jump=1
           jump_pawn.append(pos)
           move,target=get_jump_moves(pos,"cpu")          
           jump_pawn_moves.append(move)
           jump_pawn_targets.append(target)
           

     if cpu_must_jump:
       copy_tab(tab=tab,tab_copy=tab_copy2)
       score=-10000
       alpha=-10000
       for i in range(len(jump_pawn_moves)):
         if not to_break:
           move=jump_pawn_moves[i]
           for j in range(len(move)):
               pos=jump_pawn[i]
               new_pos=jump_pawn_moves[i][j]
               target=jump_pawn_targets[i][j]
               jump_pos=tab_pos[new_pos[0]][new_pos[1]]
               index,value=recursive_jump(pos,new_pos,target,"cpu",index=[],value=[])
               result=recursive_play(depth,"min",alpha=alpha)
               copy(tab_copy=tab_copy2,tab=tab)
               if result>score:
                    score=result
                    alpha=score
                    best_move=[pos,new_pos,target]
       pos,new_pos,target=best_move[0],best_move[1],best_move[2]
       jump(pos,new_pos,target)
       cpu_must_jump=0
       if not must_jump(new_pos,"cpu"):turn="player"
       else:second_jump_pawn=new_pos;second_jump=1
       to_break=0
       
     elif turn=="cpu" and not cpu_must_jump and get_moves("cpu",can_move=1):
          if cpu_first_turn:
             cpu_first_turn=0
             cpu_moves=get_moves("cpu")
             choice=random.randint(0,len(cpu_moves)-1)
             selected_pawn=cpu_moves[choice]
             pawn_moves=get_pawn_moves(selected_pawn)
             choice=random.randint(0,len(pawn_moves)-1)
             pos=selected_pawn
             new_pos=pawn_moves[choice]
             move_pawn(pos,new_pos)
          else:
              best_move=get_best_move(depth)
              pos=best_move[0]
              new_pos=best_move[1]
              move_pawn(pos,new_pos)
          turn="player"
          
  
  if get_result:
     if cpu_win():lose_score+=1;get_result=0
     elif player_win():win_score+=1;get_result=0
     elif draw():draw_score+=1;get_result=0

  screen.fill((204,204,144))
  
  screen.blit(board,board_pos)
  if turn=="player" and  player_must_jump:
     for move in jump_pawn:
         pos=tab_pos[move[0]][move[1]];screen.blit(green_light,pos)
     for move in jump_pawn_moves:
         for move2 in move:
             pos=tab_pos[move2[0]][move2[1]];screen.blit(red_light,pos)
     for move in jump_pawn_targets:
         for move2 in move:
             pos=tab_pos[move2[0]][move2[1]];screen.blit(red_light,pos)
     if selected_jump:
        screen.blit(green_light,selected_jump_pos)    
  if selected:
     screen.blit(green_light,light_pos)
     for move in pawn_moves:
             pos=tab_pos[move[0]][move[1]]
             screen.blit(green_light,pos)
             
  for i in range(8):
      for j in range(8):
          pos=tab_pos[i][j]
          if tab[i][j]==1:screen.blit(blue,pos)
          elif tab[i][j]==3:screen.blit(b_king,pos)
          elif tab[i][j]==2 :screen.blit(red,pos)
          elif tab[i][j]==4:screen.blit(r_king,pos)
          
  if player_win():
     text=font.render(("you win"), True, (0,250,0));screen.blit(text,(270,195))
  elif cpu_win():
     text=font.render(("you lose"), True, (250,0,0));screen.blit(text,(265,195))
  elif draw():
     text=font.render(("draw"), True, (0,0,250));screen.blit(text,(285,195))

  text=font.render(("cpu:"), True, (250,250,250));screen.blit(text,(550,180))
  text=font.render((str(depth)), True, (250,250,250));screen.blit(text,(550,210))  
  text=font.render(("lose:"), True, (250,0,0));screen.blit(text,(550,60))
  text=font.render((str(lose_score)), True, (250,0,0));screen.blit(text,(550,90))  
  text=font.render(("win:"), True, (0,250,0));screen.blit(text,(550,0))
  text=font.render((str(win_score)), True, (0,250,0));screen.blit(text,(550,30))
  text=font.render(("draw:"), True, (0,0,250));screen.blit(text,(550,120))
  text=font.render((str(draw_score)), True, (0,0,250));screen.blit(text,(550,150))
     
  pygame.display.flip()
                         

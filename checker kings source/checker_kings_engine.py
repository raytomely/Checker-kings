


"""tab=[ [0,0,0,0,0,0,0,0],
      [0,0,1,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,2],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0], ]"""

tab=[ [0,2,0,2,0,2,0,2],
      [2,0,2,0,2,0,2,0],
      [0,2,0,2,0,2,0,2],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [1,0,1,0,1,0,1,0],
      [0,1,0,1,0,1,0,1],
      [1,0,1,0,1,0,1,0], ]

def render(tab=tab):
    print("\n")
    for i in tab:print(i)
r=render
def reintialize_tab():
    tab2=[ [0,2,0,2,0,2,0,2],
           [2,0,2,0,2,0,2,0],
           [0,2,0,2,0,2,0,2],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [1,0,1,0,1,0,1,0],
           [0,1,0,1,0,1,0,1],
           [1,0,1,0,1,0,1,0], ]
    copy(tab_copy=tab2,tab=tab)

def get_moves(turn,tab=tab,can_move=0):
    moves=[]
    able_to_move=0
    for i in range(8):
        for j in range(8):
            valide=0
            if turn=="cpu":
                if tab[i][j]==2 or tab[i][j]==4:
                   if i!=7 and j!=0 and tab[i+1][j-1]==0:valide=1
                   elif i!=7 and j!=7 and tab[i+1][j+1]==0:valide=1
                if tab[i][j]==4:
                   if i!=0 and j!=0 and tab[i-1][j-1]==0:valide=1
                   elif i!=0 and j!=7 and tab[i-1][j+1]==0:valide=1
            if turn=="player":
                if tab[i][j]==1 or tab[i][j]==3:
                   if i!=0 and j!=0 and tab[i-1][j-1]==0:valide=1
                   elif i!=0 and j!=7 and tab[i-1][j+1]==0:valide=1
                if tab[i][j]==3:
                   if i!=7 and j!=0 and tab[i+1][j-1]==0:valide=1
                   elif i!=7 and j!=7 and tab[i+1][j+1]==0:valide=1
            if valide:moves.append([i,j]);able_to_move=1
    if can_move: return able_to_move
    else:return moves
g=get_moves

def get_pawn_moves(pos,tab=tab):
    moves=[]        
    if tab[pos[0]][pos[1]]==2 or tab[pos[0]][pos[1]]==4 or tab[pos[0]][pos[1]]==3:
       if pos[0]!=7 and pos[1]!=0 and tab[pos[0]+1][pos[1]-1]==0:moves.append([pos[0]+1,pos[1]-1])
       if pos[0]!=7 and pos[1]!=7 and tab[pos[0]+1][pos[1]+1]==0:moves.append([pos[0]+1,pos[1]+1])
    if tab[pos[0]][pos[1]]==4 or tab[pos[0]][pos[1]]==1 or tab[pos[0]][pos[1]]==3:
       if pos[0]!=0 and pos[1]!=0 and tab[pos[0]-1][pos[1]-1]==0:moves.append([pos[0]-1,pos[1]-1])
       if pos[0]!=0 and pos[1]!=7 and tab[pos[0]-1][pos[1]+1]==0:moves.append([pos[0]-1,pos[1]+1])  
    return moves
p=get_pawn_moves

def must_jump(pos,turn,tab=tab):
    valide=0
    
    if turn=="player":
        if tab[pos[0]][pos[1]]==1 or tab[pos[0]][pos[1]]==3:
           if (pos[0]>1 and pos[1]>1) and (tab[pos[0]-1][pos[1]-1]==2 or tab[pos[0]-1][pos[1]-1]==4) \
           and (tab[pos[0]-2][pos[1]-2]==0):valide=1
           elif (pos[0]>1 and pos[1]<6) and (tab[pos[0]-1][pos[1]+1]==2 or tab[pos[0]-1][pos[1]+1]==4) \
           and (tab[pos[0]-2][pos[1]+2]==0):valide=1
        if tab[pos[0]][pos[1]]==3:
           if (pos[0]<6 and pos[1]>1) and (tab[pos[0]+1][pos[1]-1]==2 or tab[pos[0]+1][pos[1]-1]==4) \
           and (tab[pos[0]+2][pos[1]-2]==0):valide=1
           elif (pos[0]<6 and pos[1]<6) and (tab[pos[0]+1][pos[1]+1]==2 or tab[pos[0]+1][pos[1]+1]==4) \
           and (tab[pos[0]+2][pos[1]+2]==0):valide=1
           
    if turn=="cpu":
        if tab[pos[0]][pos[1]]==2 or tab[pos[0]][pos[1]]==4:
           if (pos[0]<6 and pos[1]>1) and (tab[pos[0]+1][pos[1]-1]==1 or tab[pos[0]+1][pos[1]-1]==3) \
           and (tab[pos[0]+2][pos[1]-2]==0):valide=1
           elif (pos[0]<6 and pos[1]<6) and (tab[pos[0]+1][pos[1]+1]==1 or tab[pos[0]+1][pos[1]+1]==3) \
           and (tab[pos[0]+2][pos[1]+2]==0):valide=1
        if tab[pos[0]][pos[1]]==4:
           if (pos[0]>1 and pos[1]>1) and (tab[pos[0]-1][pos[1]-1]==1 or tab[pos[0]-1][pos[1]-1]==3) \
           and (tab[pos[0]-2][pos[1]-2]==0):valide=1
           elif (pos[0]>1 and pos[1]<6) and (tab[pos[0]-1][pos[1]+1]==1 or tab[pos[0]-1][pos[1]+1]==3) \
           and (tab[pos[0]-2][pos[1]+2]==0):valide=1
  
    if valide:return 1
m= must_jump

def get_jump_moves(pos,turn,tab=tab):
    valide=0
    moves=[]
    target=[]
    
    if turn=="cpu":
        if tab[pos[0]][pos[1]]==2 or tab[pos[0]][pos[1]]==4:
           if (pos[0]<6 and pos[1]>1) and (tab[pos[0]+1][pos[1]-1]==1 or tab[pos[0]+1][pos[1]-1]==3) \
           and (tab[pos[0]+2][pos[1]-2]==0):valide=1;moves.append([pos[0]+2,pos[1]-2]);target.append([pos[0]+1,pos[1]-1])
           if (pos[0]<6 and pos[1]<6) and (tab[pos[0]+1][pos[1]+1]==1 or tab[pos[0]+1][pos[1]+1]==3) \
           and (tab[pos[0]+2][pos[1]+2]==0):valide=1;moves.append([pos[0]+2,pos[1]+2]);target.append([pos[0]+1,pos[1]+1])
        if tab[pos[0]][pos[1]]==4:
           if (pos[0]>1 and pos[1]>1) and (tab[pos[0]-1][pos[1]-1]==1 or tab[pos[0]-1][pos[1]-1]==3) \
           and (tab[pos[0]-2][pos[1]-2]==0):valide=1;moves.append([pos[0]-2,pos[1]-2]);target.append([pos[0]-1,pos[1]-1])
           if (pos[0]>1 and pos[1]<6) and (tab[pos[0]-1][pos[1]+1]==1 or tab[pos[0]-1][pos[1]+1]==3) \
           and (tab[pos[0]-2][pos[1]+2]==0):valide=1;moves.append([pos[0]-2,pos[1]+2]);target.append([pos[0]-1,pos[1]+1])
        
    if turn=="player":
        if tab[pos[0]][pos[1]]==1 or tab[pos[0]][pos[1]]==3:
           if (pos[0]>1 and pos[1]>1) and (tab[pos[0]-1][pos[1]-1]==2 or tab[pos[0]-1][pos[1]-1]==4) \
           and (tab[pos[0]-2][pos[1]-2]==0):valide=1;moves.append([pos[0]-2,pos[1]-2]);target.append([pos[0]-1,pos[1]-1])
           if (pos[0]>1 and pos[1]<6) and (tab[pos[0]-1][pos[1]+1]==2 or tab[pos[0]-1][pos[1]+1]==4) \
           and (tab[pos[0]-2][pos[1]+2]==0):valide=1;moves.append([pos[0]-2,pos[1]+2]);target.append([pos[0]-1,pos[1]+1])
        if tab[pos[0]][pos[1]]==3:
           if (pos[0]<6 and pos[1]>1) and (tab[pos[0]+1][pos[1]-1]==2 or tab[pos[0]+1][pos[1]-1]==4) \
           and (tab[pos[0]+2][pos[1]-2]==0):valide=1;moves.append([pos[0]+2,pos[1]-2]);target.append([pos[0]+1,pos[1]-1])
           if (pos[0]<6 and pos[1]<6) and (tab[pos[0]+1][pos[1]+1]==2 or tab[pos[0]+1][pos[1]+1]==4) \
           and (tab[pos[0]+2][pos[1]+2]==0):valide=1;moves.append([pos[0]+2,pos[1]+2]);target.append([pos[0]+1,pos[1]+1])

    if valide:return moves,target
j=get_jump_moves


def jump(pos,new_pos,target,tab=tab):
    if new_pos[0]!=0 and new_pos[0]!=7:
       tab[new_pos[0]][new_pos[1]]=tab[pos[0]][pos[1]]
    elif (new_pos[0]==0 or new_pos[0]==7) and (tab[pos[0]][pos[1]]==3 or tab[pos[0]][pos[1]]==4) :
       tab[new_pos[0]][new_pos[1]]=tab[pos[0]][pos[1]]
    elif new_pos[0]==0 and tab[pos[0]][pos[1]]==1:
         tab[new_pos[0]][new_pos[1]]=3
    elif new_pos[0]==7 and tab[pos[0]][pos[1]]==2:
         tab[new_pos[0]][new_pos[1]]=4
    tab[pos[0]][pos[1]]=0
    tab[target[0]][target[1]]=0

def recursive_jump(pos,new_pos,target,turn,tab=tab,index=[],value=[]):
    index.append([pos,new_pos,target])
    value.append([tab[pos[0]][pos[1]],tab[new_pos[0]][new_pos[1]],tab[target[0]][target[1]]])   
    if new_pos[0]!=0 and new_pos[0]!=7:
       tab[new_pos[0]][new_pos[1]]=tab[pos[0]][pos[1]]
    elif (new_pos[0]==0 or new_pos[0]==7) and (tab[pos[0]][pos[1]]==3 or tab[pos[0]][pos[1]]==4) :
       tab[new_pos[0]][new_pos[1]]=tab[pos[0]][pos[1]]
    elif new_pos[0]==0 and tab[pos[0]][pos[1]]==1:
         tab[new_pos[0]][new_pos[1]]=3
    elif new_pos[0]==7 and tab[pos[0]][pos[1]]==2:
         tab[new_pos[0]][new_pos[1]]=4
    tab[pos[0]][pos[1]]=0
    tab[target[0]][target[1]]=0
    if must_jump(new_pos,turn):
       pos=new_pos
       move,target=get_jump_moves(pos,turn)
       new_pos=move[0];target=target[0]
       recursive_jump(pos,new_pos,target,turn)
    return index,value
    
def move_pawn(pos,new_pos,tab=tab):
    index=[pos,new_pos]
    value=[tab[pos[0]][pos[1]],tab[new_pos[0]][new_pos[1]]]  
    if new_pos[0]!=0 and new_pos[0]!=7:
       tab[new_pos[0]][new_pos[1]]=tab[pos[0]][pos[1]]
    elif (new_pos[0]==0 or new_pos[0]==7) and (tab[pos[0]][pos[1]]==3 or tab[pos[0]][pos[1]]==4) :
       tab[new_pos[0]][new_pos[1]]=tab[pos[0]][pos[1]]
    elif new_pos[0]==0 and tab[pos[0]][pos[1]]==1:
         tab[new_pos[0]][new_pos[1]]=3
    elif new_pos[0]==7 and tab[pos[0]][pos[1]]==2:
         tab[new_pos[0]][new_pos[1]]=4
    tab[pos[0]][pos[1]]=0
    return index,value
    
def evalue(turn,tab=tab):
    score=0
    max_dist_diffrance=17
    if not cpu_win() and not player_win() and not draw():
       for i in range(8):
           for j in range(8):
               pos=[i,j]
               if tab[i][j]==2:score+=1+i+backed(pos)+near_king_row(pos)
               if tab[i][j]==1:score-=1+(7-i)+ near_king_row(pos)+backed(pos)
               if tab[i][j]==4:score+=20+distance_bonus(pos)#+blocking(pos)
               if tab[i][j]==3:score-=20#-blocking(pos)#+(distance_bonus(pos)*2)
       score+=empty_king_row()
    elif cpu_win():cont=cont_tab("cpu");"""print("win",+1000+cont)""";score= +1000+cont
    elif player_win():cont=cont_tab("player");"""print("lose",-1000+cont)""";score= -1000-cont
    elif draw():"""print("draw")""";score= 0
       
    return score
v=evalue

def player_win(tab=tab):
    player_win=1
    for i in range(8):
        for j in range(8):
            if tab[i][j]==2 or tab[i][j]==4:player_win=0
    if not get_moves("cpu",can_move=1):player_win=1
    for i in range(8):
        for j in range(8):
            pos=[i,j]
            if tab[i][j]==2 or tab[i][j]==4:
               if must_jump(pos,"cpu"):player_win=0
    return player_win

def cpu_win(tab=tab):
    cpu_win=1
    for i in range(8):
        for j in range(8):
            if tab[i][j]==1 or tab[i][j]==3:cpu_win=0
    if not get_moves("player",can_move=1):cpu_win=1
    for i in range(8):
        for j in range(8):
            pos=[i,j]
            if tab[i][j]==1 or tab[i][j]==3:
               if must_jump(pos,"player"):cpu_win=0
    return cpu_win

def draw(tab=tab):
    player=0
    cpu=0
    draw=0
    blue_king=0
    red_king=0
    if not cpu_win() and not player_win():
       for i in range(8):
           for j in range(8):
               pos=[i,j]
               if tab[i][j]==1 or tab[i][j]==3:player+=1
               elif tab[i][j]==2 or tab[i][j]==4:cpu+=1
       if player==1 and cpu==1:
          for i in range(8):
              for j in range(8):
                  pos=[i,j]
                  if tab[i][j]==3:blue_king=1
                  elif tab[i][j]==4:red_king=1
       if red_king and blue_king:draw=1
    return draw

tab_copy=[ [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0], ]

tab_copy2=[ [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0], ]


def copy_tab(tab=tab,tab_copy=tab_copy):
    for i in range(8):
        for j in range(8):
            tab_copy[i][j]=tab[i][j]
copy_tab()

def copy(tab_copy=tab_copy,tab=tab):
    for i in range(8):
        for j in range(8):
            tab[i][j]=tab_copy[i][j]

def distance_bonus(pos,tab=tab):
    to_break=0
    result=0
    king_dist=1000
    pawn_dist=-1000
    max_dist_diffrance=17
    target=0
    if tab[pos[0]][pos[1]]==2 or tab[pos[0]][pos[1]]==4:    
       for i in range(8):
           for j in range(8):
               if tab[i][j]==1 or tab[i][j]==3:
                  if cal_distance(pos,[i,j])<king_dist:
                     king_dist=cal_distance(pos,[i,j])
                     target=[i,j]
        
    if tab[pos[0]][pos[1]]==1 or tab[pos[0]][pos[1]]==3:
       for i in range(8):
           for j in range(8):
               if tab[i][j]==2 or tab[i][j]==4:
                  if cal_distance(pos,[i,j])<king_dist:
                     king_dist=cal_distance(pos,[i,j])
                     target=[i,j]
    if target!=0:result=(max_dist_diffrance-cal_distance(pos,target))-in_danger(pos)
    else:result=0
    return result

def cal_distance(pos,target):
    a=pos[0]-target[0]
    if a<0:a*=-1
    b=(pos[1]-target[1])*2
    if b<0:b*=-1
    result=a+b
    return result

def in_danger(pos,tan=tab):
    danger=0
    if tab[pos[0]][pos[1]]==2 or tab[pos[0]][pos[1]]==4:
       for i in range(8):
           for j in range(8):
               if tab[i][j]==1 or tab[i][j]==3:
                  attaker_pos=[i,j]
                  if must_jump(attaker_pos,"player"):
                     jump_pos,jump_target=get_jump_moves(attaker_pos,"player")
                     for target in jump_target:
                         if pos==target:danger=20
    elif tab[pos[0]][pos[1]]==1 or tab[pos[0]][pos[1]]==3:
       for i in range(8):
           for j in range(8):
               if tab[i][j]==2 or tab[i][j]==4:
                  attaker_pos=[i,j]
                  if must_jump(attaker_pos,"cpu"):
                     jump_pos,jump_target=get_jump_moves(attaker_pos,"cpu")
                     for target in jump_target:
                         if pos==target:danger=20
    return danger

def backed(pos,tab=tab):
    backed_back=0
    if tab[pos[0]][pos[1]]==2:
       if (pos[0]!=0 and pos[1]!=0) and (tab[pos[0]-1][pos[1]-1]==2 or tab[pos[0]-1][pos[1]-1]==4):backed_back+=1
       if (pos[0]!=0 and pos[1]!=7) and (tab[pos[0]-1][pos[1]+1]==2 or tab[pos[0]-1][pos[1]+1]==4):backed_back+=1
       if  pos[1]==0 or pos[1]==7:backed_back+=2
    elif tab[pos[0]][pos[1]]==1:
       if (pos[0]!=7 and pos[1]!=0) and (tab[pos[0]+1][pos[1]-1]==1 or tab[pos[0]+1][pos[1]-1]==3):backed_back+=1
       if (pos[0]!=7 and pos[1]!=7 )and (tab[pos[0]+1][pos[1]+1]==1 or tab[pos[0]+1][pos[1]+1]==3):backed_back+=1
       if  pos[1]==0 or pos[1]==7:backed_back+=2
    return backed_back

def empty_king_row(tab=tab):
    empty_row=0
    red_king_row=[[0,1],[0,3],[0,5],[0,7]]
    blue_king_row=[[7,0],[7,2],[7,4],[7,6]]
    for pos in red_king_row:
        if tab[pos[0]][pos[1]]==0 or tab[pos[0]][pos[1]]==3:empty_row-=5
    return empty_row

def near_king_row(pos,tab=tab):
    near=0
    if tab[pos[0]][pos[1]]==2:
       if pos[0]==6:near+=10
    elif tab[pos[0]][pos[1]]==1:
       if pos[0]==1:near+=10
    return near



def blocking(pos,tab=tab):
        blocked=0
        if tab[pos[0]][pos[1]]==4:
              if (pos[0]>1) and (tab[pos[0]-2][pos[1]]==1 or tab[pos[0]-2][pos[1]]==3): blocked+=5
              if (pos[0]<6) and (tab[pos[0]+2][pos[1]]==1 or tab[pos[0]+2][pos[1]]==3): blocked+=5
              if (pos[1]>1) and (tab[pos[0]][pos[1]-2]==1 or tab[pos[0]][pos[1]-2]==3): blocked+=5
              if (pos[1]<6) and (tab[pos[0]][pos[1]+2]==1 or tab[pos[0]][pos[1]+2]==3): blocked+=5
        elif tab[pos[0]][pos[1]]==3:
              if (pos[0]>1) and (tab[pos[0]-2][pos[1]]==2 or tab[pos[0]-2][pos[1]]==4): blocked+=5
              if (pos[0]<6) and (tab[pos[0]+2][pos[1]]==2 or tab[pos[0]+2][pos[1]]==4): blocked+=5
              if (pos[1]>1) and (tab[pos[0]][pos[1]-2]==2 or tab[pos[0]][pos[1]-2]==4): blocked+=5
              if (pos[1]<6) and (tab[pos[0]][pos[1]+2]==2 or tab[pos[0]][pos[1]+2]==4): blocked+=5
        return blocked-in_danger(pos)

def cont_tab(turn,tab=tab):
    cont=0
    if turn=="cpu":
       for i in range(8):
           for j in range(8):
               if tab[i][j]==2 or tab[i][j]==4:cont+=1
    if turn=="player":        
       for i in range(8):
           for j in range(8):
               if tab[i][j]==1 or tab[i][j]==3:cont+=1   
    return cont

def cancel_move(index,value,move_type,tab=tab):
    if move_type=="jump":
       for i in range(len(index)-1,-1,-1):
            move=index[i]
            for j in range(len(move)-1,-1,-1):
               pos=index[i][j]
               content=value[i][j]
               tab[pos[0]][pos[1]]=content
    elif move_type=="move":
         for i in range(len(index)):
               pos=index[i]
               content=value[i]
               tab[pos[0]][pos[1]]=content
             
    
def recursive_play(depth,turn,alpha=-10000,beta=10000,tab=tab):
  #print("depth",depth);r()
  if not cpu_win() and not player_win() and not draw()and depth!=0:
 
    if turn=="max":
       score=-10000
       jump_pawn=[]
       jump_pawn_moves=[]
       jump_pawn_targets=[]
       cpu_must_jump=0
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
       
       if cpu_must_jump:
          to_break=0
          for i in range(len(jump_pawn_moves)):
              if to_break:break
              move=jump_pawn_moves[i]
              for j in range(len(move)):
                  local_copy=[ [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0], ]
                  copy_tab(tab=tab,tab_copy=local_copy)
                  new_pos=jump_pawn_moves[i][j]
                  pos=jump_pawn[i]
                  target=jump_pawn_targets[i][j]
                  index,value=recursive_jump(pos,new_pos,target,"cpu",index=[],value=[])
                  if alpha<beta:
                     result=recursive_play(depth-1,"min",alpha=alpha)#+blocking(new_pos)#+(distance_bonus(new_pos)*2);print("max_score",result)
                  else:"""print("elagage alpha >= beta",alpha,beta)""";score=beta;to_break=1;break
                  copy(tab_copy=local_copy,tab=tab)
                  #result=evalue(turn)
                  #cancel_move(index,value,"jump")
                  if result>score:
                     score=result+20
                     best_move=[pos,new_pos,target]
          recursive_jump(best_move[0],best_move[1],best_move[2],"cpu")
          #print("max_jump pos new_pos target",best_move);r()
          #print("returning_score_from_max_jump depth",result,depth)
          return score
          
       if not cpu_must_jump and get_moves("cpu",can_move=1):
          moves=get_moves("cpu")
          to_break=0
          for move in moves:
              if to_break:break
              selected_pawn=move
              pawn_moves=get_pawn_moves(selected_pawn)
              for move in pawn_moves:
                  local_copy=[ [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0], ]
                  copy_tab(tab=tab,tab_copy=local_copy)
                  pos=selected_pawn
                  new_pos=move
                  index,value=move_pawn(pos,new_pos)#;print("max_pawn_moves",pawn_moves,"pos new_pos",pos,new_pos)
                  #print("if alpha<beta",alpha,beta)
                  if alpha<beta:
                     result=recursive_play(depth-1,"min",alpha=alpha)#+blocking(new_pos)#+(distance_bonus(new_pos)*2);print("max_score",result)
                  else:"""print("elagage alpha >= beta",alpha,beta)""";score=beta;to_break=1;break
                  copy(tab_copy=local_copy,tab=tab)
                  if result>score:
                     score=result
                     alpha=score
                     best_move=[pos,new_pos]
          move_pawn(best_move[0],best_move[1])#;print("max_best_move pos new_pos best_score",best_move,score);r()
          #print("returning_score_from_max_move depth",result,depth)
          return score
        
    if turn=="min":
       score=10000
       jump_pawn=[]
       jump_pawn_moves=[]
       jump_pawn_targets=[]
       player_must_jump=0
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
       
       if player_must_jump:
          to_break=0
          for i in range(len(jump_pawn_moves)):
              if to_break:break
              move=jump_pawn_moves[i]
              for j in range(len(move)):
                  local_copy=[ [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0], ]
                  copy_tab(tab=tab,tab_copy=local_copy)
                  new_pos=jump_pawn_moves[i][j]
                  pos=jump_pawn[i]
                  target=jump_pawn_targets[i][j]
                  index,value=recursive_jump(pos,new_pos,target,"player",index=[],value=[])
                  if beta>alpha:
                     result=recursive_play(depth-1,"max",beta=beta)#-distance_bonus(new_pos);print("min_result",result)
                  else:"""print("elagage beta <= alpha",beta,alpha)""";score=alpha;to_break=1;break
                  copy(tab_copy=local_copy,tab=tab)
                  #result=evalue(turn)
                  #cancel_move(index,value,"jump")
                  if result<score:
                     score=result-20
                     best_move=[pos,new_pos,target]
          recursive_jump(best_move[0],best_move[1],best_move[2],"player",index=[],value=[])
          #print("min_jump pos new_pos target best_score",best_move,score);r()
          #print("returning_score_from_min_jump depth",score,depth)
          return score
        
       if not player_must_jump and get_moves("player",can_move=1):
          moves=get_moves("player")
          to_break=0
          for move in moves:
              if to_break:break
              selected_pawn=move
              pawn_moves=get_pawn_moves(selected_pawn)
              for move in pawn_moves:
                  local_copy=[ [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0], ]
                  copy_tab(tab=tab,tab_copy=local_copy)
                  pos=selected_pawn
                  new_pos=move
                  index,value=move_pawn(pos,new_pos)#;print("min_pawn_moves",pawn_moves,"pos new_pos",pos,new_pos)
                  #print("if beta>alpha",beta,alpha)
                  if beta>alpha:
                     result=recursive_play(depth-1,"max",beta=beta)#-distance_bonus(new_pos);print("min_result",result)
                  else:"""print("elagage beta <= alpha",beta,alpha)""";score=alpha;to_break=1;break
                  copy(tab_copy=local_copy,tab=tab)
                  if result<score:
                     score=result
                     beta=score
                     best_move=[pos,new_pos]
          move_pawn(best_move[0],best_move[1])#;print("min_best_move pos new_pos best_score",best_move,score);r()
          #print("returning_score_from_min_move depth",score,depth)
          return score
        
  else:"""print("exit_recursion and evaluate")""";return evalue(turn)
  
      
def get_best_move(depth,turn="min",tab=tab,alpha=-10000,beta=10000):
    copy_tab(tab=tab,tab_copy=tab_copy2)   
    moves=get_moves("cpu")
    to_break=0
    score=-10000
    for move in moves:
        if not to_break:
           selected_pawn=move
           pawn_moves=get_pawn_moves(selected_pawn)
           for move2 in pawn_moves:
                pos=selected_pawn
                new_pos=move2
                #print("original_tab");r()
                move_pawn(pos,new_pos)#;print("get moves pos new_pos",moves,pos,new_pos)
                bonus=blocking(new_pos)
                result=recursive_play(depth,turn,alpha=alpha)+bonus
                if cpu_win():to_break=1#;r(tab=tab_copy2);print("original_tab")
                copy(tab_copy=tab_copy2,tab=tab)
                #print("get result move pos new_pos",result,pos,new_pos);r()
                if result>score:
                    score=result
                    alpha=score
                    best_move=[move,new_pos]
                    if to_break:break
    copy(tab_copy=tab_copy2,tab=tab)
    return best_move
gb=get_best_move





    


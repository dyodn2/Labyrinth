import random

threshold = 3

# 随机初始化迷宫
def initialize_labyrinth():
    labyrinth = [[0, 0, 1, 0, 0],
                 [0, 1, 1, 1, 1],
                 [1, 0, 1, 0, 1],
                 [1, 1, 1, 1, 1],
                 [0, 0, 1, 0, 0]]
    return labyrinth

# 打印迷宫
def print_labyrinth(labyrinth):
    for row in labyrinth:
        print(" ".join(map(str, row)))
    print()

# 检测当前位置的函数
def check_current_position(labyrinth, direction, row, col, pos)->list:
    result = []
    if direction == 'N':
        if pos[1]-1>=0 and labyrinth[pos[0]][pos[1]-1]==1:
            result.append('L')
        if pos[0]-1>=0 and labyrinth[pos[0]-1][pos[1]]==1:
            result.append('F')
        if pos[1]+1<col and labyrinth[pos[0]][pos[1]+1]==1:
            result.append('R')
    if direction == 'S':
        if pos[1]+1<col and labyrinth[pos[0]][pos[1]+1]==1:
            result.append('L')
        if pos[0]+1<col and labyrinth[pos[0]+1][pos[1]]==1:
            result.append('F')
        if pos[1]-1>=0 and labyrinth[pos[0]][pos[1]-1]==1:
            result.append('R')
    if direction == 'W':
        if pos[0]+1<row and labyrinth[pos[0]+1][pos[1]]==1:
            result.append('L')
        if pos[1]-1>=0 and labyrinth[pos[0]][pos[1]-1]==1:
            result.append('F')
        if pos[0]-1>=0 and labyrinth[pos[0]-1][pos[1]]==1:
            result.append('R')
    if direction == 'E':
        if pos[0]-1>=0 and labyrinth[pos[0]-1][pos[1]]==1:
            result.append('L')
        if pos[1]+1<col and labyrinth[pos[0]][pos[1]+1]==1:
            result.append('F')
        if pos[0]+1<row and labyrinth[pos[0]+1][pos[1]]==1:
            result.append('R')
    # print(direction, result)
    return result

# 移动的函数
def move_forward(pos, direction):
    if direction == 'N':
        print(f"Move forward to ({pos[0] - 1}, {pos[1]})")
        return pos[0] - 1, pos[1]
    elif direction == 'S':
        print(f"Move forward to ({pos[0] + 1}, {pos[1]})")
        return pos[0] + 1, pos[1]
    elif direction == 'W':
        print(f"Move forward to ({pos[0]}, {pos[1] - 1})")
        return pos[0], pos[1] - 1
    elif direction == 'E':
        print(f"Move forward to ({pos[0]}, {pos[1] + 1})")
        return pos[0], pos[1] + 1


# 转向的函数
def turn_left(direction):
    print("Turn left")
    if direction == 'N':
        result = 'W'
    elif direction == 'S':
        result = 'E'
    elif direction == 'W':
        result = 'S'
    elif direction == 'E':
        result = 'N'
    return result

def turn_right(direction):
    print("Turn right")
    if direction == 'N':
        result = 'E'
    elif direction == 'S':
        result = 'W'
    elif direction == 'W':
        result = 'N'
    elif direction == 'E':
        result = 'S'
    return result
    
def turn_around(direction):
    print("Turn around")
    if direction == 'N':
        result = 'S'
    elif direction == 'S':
        result = 'N'
    elif direction == 'W':
        result = 'E'
    elif direction == 'E':
        result = 'W'
    return result

def checkfinal(pos, exit_row, exit_col):
    if pos[0]==exit_row and pos[1]==exit_col:
        return True
    else:
        return False

# 广度优先遍历迷宫
def breadth_first_search(labyrinth):

    rows, cols = len(labyrinth), len(labyrinth[0])
    start_row, start_col = rows - 1, 2  # 起点在第五行第三列
    exit_row, exit_col = 0, 2  # 出口在第一行第三列
    
    # 初始化变量
    kk = 0
    direction = 'N'
    pos = [start_row, start_col]
    choice = ['F']
    routine = []
    path = []
    queue = []

    while len(check_current_position(labyrinth,direction,rows,cols,pos))==1:
        pi = check_current_position(labyrinth,direction,rows,cols,pos)
        if 'F' in pi:
            pos[0], pos[1] = move_forward(pos=pos,direction=direction)
        elif 'L' in pi:
            direction = turn_left(direction)
            pos[0], pos[1] = move_forward(pos=pos,direction=direction)
        elif 'R' in pi:
            direction = turn_right(direction)
            pos[0], pos[1] = move_forward(pos=pos,direction=direction)
    choice = check_current_position(labyrinth,direction,rows,cols,pos)
    queue.append((pos, direction, choice, routine))  # 初始化队列，每个元素是一个四元组(pos, direction, choice, routine)

    while queue and kk<=threshold:
        (_,_,choice,routine) = queue[0]
        queue.pop(0)
        if queue==None:
            queue = []
        if routine==None:
            routine = []
        
        # 从第一个分支点移动至当前弹出的分支点
        if len(list(routine))==0: # 这就是第一个分支点
            # 走到头到这一分支点（也可以不走，当前位置就是了）
            while len(check_current_position(labyrinth,direction,rows,cols,pos))==1:
                pi = check_current_position(labyrinth,direction,rows,cols,pos)
                if 'F' in pi:
                    pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                elif 'L' in pi:
                    direction = turn_left(direction)
                    pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                elif 'R' in pi:
                    direction = turn_right(direction)
                    pos[0], pos[1] = move_forward(pos=pos,direction=direction)

        else: # 前面还有其他分支点
            for i in range(len(routine)): # 遍历分支点的转向方式
                # 按照路径转向，然后走一步
                if routine[i]=='L':
                    direction = turn_left(direction)
                    pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                elif routine[i]=='R':
                    direction = turn_right(direction)
                    pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                elif routine[i]=='F':
                    pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                # 走到头
                while len(check_current_position(labyrinth,direction,rows,cols,pos))==1:
                    pi = check_current_position(labyrinth,direction,rows,cols,pos)
                    if 'F' in pi:
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                    elif 'L' in pi:
                        direction = turn_left(direction)
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                    elif 'R' in pi:
                        direction = turn_right(direction)
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
            # 最终到达弹出的分支点

        '''
        遍历弹出的分支点的所有分支，探到下一分支点并入队列
        '''
        if 'L' in choice: # 如果有左分支
            temp = routine.copy()
            temp.append('L')
            # 转向走一步
            direction = turn_left(direction)
            pos[0], pos[1] = move_forward(pos=pos,direction=direction)

            # 探到头
            while len(check_current_position(labyrinth,direction,rows,cols,pos))==1:
                pi = check_current_position(labyrinth,direction,rows,cols,pos)
                if 'F' in pi:
                    pos[0], pos[1] = move_forward(pos,direction)
                elif 'L' in pi:
                    direction = turn_left(direction)
                    pos[0], pos[1] = move_forward(pos,direction)
                elif 'R' in pi:
                    direction = turn_right(direction)
                    pos[0], pos[1] = move_forward(pos,direction)

            if len(check_current_position(labyrinth,direction,rows,cols,pos))==0: # 尽头是死路
                if checkfinal(pos, exit_row, exit_col):
                    print('Exit')
                    path = temp
                else:
                    print('Impasse')
                direction = turn_around(direction=direction) # 掉头
            
            else: # 尽头是分支
                print('Fork')
                queue.append((pos, direction, check_current_position(labyrinth,direction,rows,cols,pos), temp)) # 入队列
                direction = turn_around(direction=direction) # 掉头
            '''
            返回
            '''
            # 走一步
            pos[0], pos[1] = move_forward(pos=pos,direction=direction)
            for i in range(len(temp)): # 遍历分支点的转向方式
                # 走到头
                while len(check_current_position(labyrinth,direction,rows,cols,pos))==1:
                    pi = check_current_position(labyrinth,direction,rows,cols,pos)
                    if 'F' in pi:
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                    elif 'L' in pi:
                        direction = turn_left(direction)
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                    elif 'R' in pi:
                        direction = turn_right(direction)
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                # 按照路径转向（左右对调），然后走一步
                if i!=len(temp)-1:
                    if temp[-i-1]=='R':
                        direction = turn_left(direction)
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                    elif temp[-i-1]=='L':
                        direction = turn_right(direction)
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                    elif temp[-i-1]=='F':
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                else: # 到达起点后调整方向
                    if temp[-i-1]=='R':
                        direction = turn_right(direction)
                    elif temp[-i-1]=='L':
                        direction = turn_left(direction)
                    elif temp[-i-1]=='F':
                        direction = turn_around(direction)
            print('Back to origin\n')


        # 从第一个分支点移动至当前弹出的分支点
        if len(list(routine))==0: # 这就是第一个分支点
            # 走到头到这一分支点（也可以不走，当前位置就是了）
            while len(check_current_position(labyrinth,direction,rows,cols,pos))==1:
                pi = check_current_position(labyrinth,direction,rows,cols,pos)
                if 'F' in pi:
                    pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                elif 'L' in pi:
                    direction = turn_left(direction)
                    pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                elif 'R' in pi:
                    direction = turn_right(direction)
                    pos[0], pos[1] = move_forward(pos=pos,direction=direction)

        else: # 前面还有其他分支点
            for i in range(len(routine)): # 遍历分支点的转向方式
                # 按照路径转向，然后走一步
                if routine[i]=='L':
                    direction = turn_left(direction)
                    pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                elif routine[i]=='R':
                    direction = turn_right(direction)
                    pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                elif routine[i]=='F':
                    pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                # 走到头
                while len(check_current_position(labyrinth,direction,rows,cols,pos))==1:
                    pi = check_current_position(labyrinth,direction,rows,cols,pos)
                    if 'F' in pi:
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                    elif 'L' in pi:
                        direction = turn_left(direction)
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                    elif 'R' in pi:
                        direction = turn_right(direction)
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
            # 最终到达弹出的分支点

        
        if 'F' in choice: # 如果有中间分支
            temp = routine.copy()
            temp.append('F')
            # 走一步
            pos[0], pos[1] = move_forward(pos=pos,direction=direction)

            # 探到头
            while len(check_current_position(labyrinth,direction,rows,cols,pos))==1:
                pi = check_current_position(labyrinth,direction,rows,cols,pos)
                if 'F' in pi:
                    pos[0], pos[1] = move_forward(pos,direction)
                elif 'L' in pi:
                    direction = turn_left(direction)
                    pos[0], pos[1] = move_forward(pos,direction)
                elif 'R' in pi:
                    direction = turn_right(direction)
                    pos[0], pos[1] = move_forward(pos,direction)

            if len(check_current_position(labyrinth,direction,rows,cols,pos))==0: # 尽头是死路
                if checkfinal(pos, exit_row, exit_col):
                    print('Exit')
                    path = temp
                else:
                    print('Impasse')
                direction = turn_around(direction=direction) # 掉头
            else: # 尽头是分支
                print('Fork')
                queue.append((pos, direction, check_current_position(labyrinth,direction,rows,cols,pos), temp)) # 入队列
                direction = turn_around(direction) # 掉头
            
            '''
            返回
            '''
            # 走一步
            pos[0], pos[1] = move_forward(pos,direction)

            for i in range(len(temp)): # 遍历分支点的转向方式
                # 走到头
                while len(check_current_position(labyrinth,direction,rows,cols,pos))==1:
                    pi = check_current_position(labyrinth,direction,rows,cols,pos)
                    if 'F' in pi:
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                    elif 'L' in pi:
                        direction = turn_left(direction)
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                    elif 'R' in pi:
                        direction = turn_right(direction)
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                # 按照路径转向（左右对调），然后走一步
                if i!=len(temp)-1:
                    if temp[-i-1]=='R':
                        direction = turn_left(direction)
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                    elif temp[-i-1]=='L':
                        direction = turn_right(direction)
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                    elif temp[-i-1]=='F':
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                else: # 到达起点后调整方向
                    if temp[-i-1]=='R':
                        direction = turn_right(direction)
                    elif temp[-i-1]=='L':
                        direction = turn_left(direction)
                    elif temp[-i-1]=='F':
                        direction = turn_around(direction)
            print('Back to origin\n')
        

        # 从第一个分支点移动至当前弹出的分支点
        if len(list(routine))==0: # 这就是第一个分支点
            # 走到头到这一分支点（也可以不走，当前位置就是了）
            while len(check_current_position(labyrinth,direction,rows,cols,pos))==1:
                pi = check_current_position(labyrinth,direction,rows,cols,pos)
                if 'F' in pi:
                    pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                elif 'L' in pi:
                    direction = turn_left(direction)
                    pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                elif 'R' in pi:
                    direction = turn_right(direction)
                    pos[0], pos[1] = move_forward(pos=pos,direction=direction)

        else: # 前面还有其他分支点
            for i in range(len(routine)): # 遍历分支点的转向方式
                # 按照路径转向，然后走一步
                if routine[i]=='L':
                    direction = turn_left(direction)
                    pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                elif routine[i]=='R':
                    direction = turn_right(direction)
                    pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                elif routine[i]=='F':
                    pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                # 走到头
                while len(check_current_position(labyrinth,direction,rows,cols,pos))==1:
                    pi = check_current_position(labyrinth,direction,rows,cols,pos)
                    if 'F' in pi:
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                    elif 'L' in pi:
                        direction = turn_left(direction)
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                    elif 'R' in pi:
                        direction = turn_right(direction)
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
            # 最终到达弹出的分支点


        if 'R' in choice: # 如果有右分支
            temp = routine.copy()
            temp.append('R')
            # 转向走一步
            direction = turn_right(direction)
            pos[0], pos[1] = move_forward(pos=pos,direction=direction)

            # 探到头
            while len(check_current_position(labyrinth,direction,rows,cols,pos))==1:
                pi = check_current_position(labyrinth,direction,rows,cols,pos)
                if 'F' in pi:
                    pos[0], pos[1] = move_forward(pos,direction)
                elif 'L' in pi:
                    direction = turn_left(direction)
                    pos[0], pos[1] = move_forward(pos,direction)
                elif 'R' in pi:
                    direction = turn_right(direction)
                    pos[0], pos[1] = move_forward(pos,direction)

            if len(check_current_position(labyrinth,direction,rows,cols,pos))==0: # 尽头是死路
                if checkfinal(pos, exit_row, exit_col):
                    print('Exit')
                    path = temp
                else:
                    print('Impasse')
                direction = turn_around(direction=direction) # 掉头
            
            else: # 尽头是分支
                print('Fork')
                queue.append((pos, direction, check_current_position(labyrinth,direction,rows,cols,pos), temp)) # 入队列
                direction = turn_around(direction=direction) # 掉头
            
            '''
            返回
            '''
            # 走一步
            pos[0], pos[1] = move_forward(pos=pos,direction=direction)
            for i in range(len(temp)): # 遍历分支点的转向方式
                # 走到头
                while len(check_current_position(labyrinth,direction,rows,cols,pos))==1:
                    pi = check_current_position(labyrinth,direction,rows,cols,pos)
                    if 'F' in pi:
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                    elif 'L' in pi:
                        direction = turn_left(direction)
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                    elif 'R' in pi:
                        direction = turn_right(direction)
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                # 按照路径转向（左右对调），然后走一步
                if i!=len(temp)-1:
                    if temp[-i-1]=='R':
                        direction = turn_left(direction)
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                    elif temp[-i-1]=='L':
                        direction = turn_right(direction)
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                    elif temp[-i-1]=='F':
                        pos[0], pos[1] = move_forward(pos=pos,direction=direction)
                else: # 到达起点后调整方向
                    if temp[-i-1]=='R':
                        direction = turn_right(direction)
                    elif temp[-i-1]=='L':
                        direction = turn_left(direction)
                    elif temp[-i-1]=='F':
                        direction = turn_around(direction)
            print('Back to origin\n')
        
        print('Cycle',kk+1)
        print()
        kk+=1
    


# 主函数
def main():
    labyrinth = initialize_labyrinth()
    print("Initial Labyrinth:")
    print_labyrinth(labyrinth)

    print("Starting Breadth-First Search:")
    breadth_first_search(labyrinth)

if __name__ == "__main__":
    # main()
    labyrinth = initialize_labyrinth()
    print("Initial Labyrinth:")
    print_labyrinth(labyrinth)
    breadth_first_search(labyrinth)

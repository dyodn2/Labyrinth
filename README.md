# Labyrinth

## Map
自定义了测试地图，保存在initialize_labyrinth函数中。其中1代表通路，0代表断路，可根据实际情况调整

## Parameter
threshold: 大致等同于为BFS遍历的纵深

path: 数组变量，保存从起点前往终点的路径，其中元素依次表示到达每一个分岔口的转向策略

'L': 存在左转路径

'F': 存在直行路径

'R': 存在右转路径


## Interface
check_current_position,move_forward,turn_left,turn_right,turn_around,checkfinal: 控制车辆移动、转向、识别终点的函数，在该代码中进行了简单的打印输出实现，需用实际实现函数自行替换

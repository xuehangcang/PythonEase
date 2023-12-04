import tkinter as tk
import random

# 初始化窗口
root = tk.Tk()
root.title('动画速度挑战 - 赛车小游戏')
canvas = tk.Canvas(root, width=800, height=600, bg='gray')
canvas.pack()

# 创建赛车
car = canvas.create_rectangle(350, 500, 450, 550, fill='blue')


# 赛车移动逻辑
def move_left(event):
    canvas.move(car, -20, 0)
    check_all_collisions()


def move_right(event):
    canvas.move(car, 20, 0)
    check_all_collisions()


canvas.bind('<Left>', move_left)
canvas.bind('<Right>', move_right)
canvas.focus_set()

# 生成障碍物并移动
obstacles = []


def create_obstacle():
    """生成障碍物"""
    x0 = random.randint(100, 700)
    obstacle = canvas.create_rectangle(x0, 0, x0 + 50, 50, fill='red')
    obstacles.append(obstacle)
    move_obstacle(obstacle)


def move_obstacle(obstacle):
    """移动障碍物"""
    canvas.move(obstacle, 0, 10)
    if canvas.coords(obstacle)[1] < 600:
        root.after(100, lambda: move_obstacle(obstacle))
    else:
        canvas.delete(obstacle)
        obstacles.remove(obstacle)


# 碰撞检测逻辑
def check_collision(car, obstacle):
    """检测赛车与障碍物是否碰撞"""
    car_coords = canvas.coords(car)
    obstacle_coords = canvas.coords(obstacle)
    if (obstacle_coords[2] > car_coords[0] and
            obstacle_coords[0] < car_coords[2] and
            obstacle_coords[3] > car_coords[1] and
            obstacle_coords[1] < car_coords[3]):
        game_over()


def check_all_collisions():
    """检测赛车与所有障碍物是否碰撞"""
    for obstacle in obstacles:
        check_collision(car, obstacle)


# 游戏结束方法
def game_over():
    """游戏结束"""
    canvas.create_text(400, 300, text="游戏结束!", font=('宋体', 30), fill="white")
    for obstacle in obstacles:
        canvas.delete(obstacle)
    obstacles.clear()


# 定期生成障碍物
def schedule_obstacle():
    create_obstacle()
    root.after(2000, schedule_obstacle)


schedule_obstacle()

# 开启Tkinter主循环
root.mainloop()

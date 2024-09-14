import pygame
import sys
import random

# 初始化 Pygame
pygame.init()

# 设置屏幕大小（等比例放大）
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# 定义颜色
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)

# 定义蛇的块大小（等比例放大）
BLOCK_SIZE = 20

# 字体设置（调整字体大小）
font = pygame.font.SysFont('Arial', 30)

# 游戏主函数
def main():
    level = 1
    while True:
        game_loop(level)
        level += 1

# 游戏循环函数
def game_loop(level):
    # 初始化时钟
    clock = pygame.time.Clock()

    # 初始化蛇
    snake_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
    snake_body = [snake_pos[:]]
    direction = 'STOP'
    change_to = direction

    # 初始化食物
    food_pos = get_food_position(snake_body)
    food_spawn = True

    # 初始速度
    speed = level

    # 计分
    score = 1

    # 游戏开始界面
    start_game = False
    while not start_game:
        screen.fill(BLACK)
        show_message('Press any key to start', WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                start_game = True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # 主游戏循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 键盘输入
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        # 如果有方向改变，更新方向
        if change_to != 'STOP':
            direction = change_to

        # 根据方向移动蛇
        if direction == 'UP':
            snake_pos[1] -= BLOCK_SIZE
        if direction == 'DOWN':
            snake_pos[1] += BLOCK_SIZE
        if direction == 'LEFT':
            snake_pos[0] -= BLOCK_SIZE
        if direction == 'RIGHT':
            snake_pos[0] += BLOCK_SIZE

        # 增加蛇的长度
        if direction != 'STOP':
            snake_body.insert(0, list(snake_pos))
            if snake_pos == food_pos:
                score += 1
                food_spawn = False
            else:
                snake_body.pop()

        # 食物重生
        if not food_spawn:
            food_pos = get_food_position(snake_body)
            food_spawn = True

        # 填充背景
        screen.fill(BLACK)

        # 画蛇
        for pos in snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))

        # 画食物
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

        # 边界检测
        if snake_pos[0] < 0 or snake_pos[0] >= SCREEN_WIDTH:
            game_over()
            return
        if snake_pos[1] < 0 or snake_pos[1] >= SCREEN_HEIGHT:
            game_over()
            return

        # 自身碰撞检测
        for block in snake_body[1:]:
            if snake_pos == block:
                game_over()
                return

        # 当蛇的长度达到10，进入下一关
        if score >= 10:
            show_continue()
            return

        # 刷新屏幕
        pygame.display.flip()

        # 控制游戏速度
        clock.tick(5 * speed)

# 获取食物位置函数
def get_food_position(snake_body):
    while True:
        x = random.randrange(0, SCREEN_WIDTH, BLOCK_SIZE)
        y = random.randrange(0, SCREEN_HEIGHT, BLOCK_SIZE)
        if [x, y] not in snake_body:
            return [x, y]

# 游戏结束函数
def game_over():
    while True:
        screen.fill(BLACK)
        show_message('Game Over! Press R', WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# 显示继续函数
def show_continue():
    while True:
        screen.fill(BLACK)
        show_message('Level Up! Press C', WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# 显示信息函数
def show_message(message, color, x, y):
    text = font.render(message, True, color)
    rect = text.get_rect(center=(x, y))
    screen.blit(text, rect)

if __name__ == '__main__':
    main()
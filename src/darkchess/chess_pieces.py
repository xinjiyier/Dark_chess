import pygame
from darkchess.constant import Constant
from pygame.locals import *
import math

RED_ROLE = 0
BLACK_ROLE = 1

HIDDEN_STATE = 3
ACTIVE_STATE = 4
DEAD_STATE = 5
CHOOSED_STATE = 6

JIANG_TYPE = 11
SHI_TYPE = 12
XIANG_TYPE = 13
CHE_TYPE = 14
MA_TYPE = 15
PAO_TYPE = 16
ZU_TYPE = 17

to_left = (-Constant.box_width, 0)
to_right = (Constant.box_width, 0)
to_up = (0, -66)
to_down = (0, 66)

bg_image = pygame.image.load('../image/blankchess.png')


def can_eat(typea, typeb):
    if typea in (JIANG_TYPE, PAO_TYPE):
        return True
    elif typea in (SHI_TYPE, XIANG_TYPE, MA_TYPE, CHE_TYPE):
        if typea <= typeb:
            return True
    elif typea == ZU_TYPE:
        if typeb == JIANG_TYPE or typeb == ZU_TYPE:
            return True
    return False


def can_move_one_step(self, pos):
    # 首先判断移动方向，然后进行移动
    # 判断移动方向
    # 判断是否在棋盘之内
    if pos[0] < Constant.padding_left or pos[0] > Constant.chess_bg_width - Constant.padding_left or pos[
        1] < Constant.padding_top or pos[
        1] > Constant.chess_bg_height - Constant.padding_top:
        print("点击超出了范围")
    elif self.rect.left - Constant.box_width < pos[0] < self.rect.left and self.rect.top < pos[
        1] < self.rect.top + Constant.box_height:
        # 需要向左移动一位
        self.rect.left -= Constant.box_width
        print('需要向左移动一位')
        return True
    elif self.rect.left < pos[0] < self.rect.left + Constant.box_width and self.rect.top - Constant.box_height < pos[
        1] < self.rect.top:
        # 需要向上移动一位
        self.rect.top -= Constant.box_height
        print('需要向上移动一位')
        return True
    elif self.rect.left + Constant.box_width < pos[0] < self.rect.left + Constant.box_width * 2 and self.rect.top < pos[
        1] < self.rect.top + Constant.box_height:
        # 需要向右移动一位
        self.rect.left += Constant.box_width
        print('需要向右移动一位')
        return True
    elif self.rect.left < pos[0] < self.rect.left + Constant.box_width and self.rect.top + Constant.box_width < pos[
        1] < self.rect.top + Constant.box_height * 2:
        # 需要向下移动一位
        self.rect.top += Constant.box_height
        print('需要向下移动一位')
        return True


# -----------------------------------------------------------------------------------------1111 将
class JiangChess:
    def __init__(self, rect):
        self.r_image = pygame.image.load('../image/red_shuai.png')
        self.b_image = pygame.image.load('../image/black_jiang.png')
        self.position = x, y = 86, 66
        self.state = HIDDEN_STATE
        self.type = JIANG_TYPE
        self.role = RED_ROLE
        self.rect = self.b_image.get_rect()

    def getImage(self, role):
        if self.state == HIDDEN_STATE:
            return bg_image
        elif self.state == DEAD_STATE:
            return -1
        else:
            if role == RED_ROLE:
                return self.r_image
            elif role == BLACK_ROLE:
                return self.b_image
            else:
                print('传入参数有误，无法判断是红方还是黑方！')
                return -1

    def move(self, pos):
        return can_move_one_step(self, pos)

    # 将 可以吃 其它所有
    # 是否可吃需要满足两个条件
    # 1、是否满足该子的行走规律
    # 2、是否满足该子的吃子规律
    def eat(self, enemy_chess, pos, chess_list):
        if can_eat(self.type, enemy_chess.type):
            if self.move(pos):
                self.rect.left = enemy_chess.rect.left
                self.rect.top = enemy_chess.rect.top
                enemy_chess.state = DEAD_STATE
                enemy_chess.rect.left = -100
                enemy_chess.rect.top = -100
                return True
            else:
                print('点击位置不在范围内，无法吃子')
        return False


# ----------------------------------------------------------------------------------------2222 士
class ShiChess:
    def __init__(self, rect):
        self.r_image = pygame.image.load('../image/red_shi.png')
        self.b_image = pygame.image.load('../image/black_shi.png')
        self.position = x, y = 86, 66
        self.state = HIDDEN_STATE
        self.type = SHI_TYPE
        self.role = RED_ROLE
        self.rect = self.b_image.get_rect()

    def getImage(self, role):
        if self.state == HIDDEN_STATE:
            return bg_image
        elif self.state == DEAD_STATE:
            return -1
        else:
            if role == RED_ROLE:
                return self.r_image
            elif role == BLACK_ROLE:
                return self.b_image
            else:
                print('传入参数有误，无法判断是红方还是黑方！')
                return -1

    def move(self, pos):
        return can_move_one_step(self, pos)

    # 将 可以吃 其它所有
    # 是否可吃需要满足两个条件
    # 1、是否满足该子的行走规律
    # 2、是否满足该子的吃子规律
    def eat(self, enemy_chess, pos, chess_list):
        if can_eat(self.type, enemy_chess.type):
            if self.move(pos):
                self.rect.left = enemy_chess.rect.left
                self.rect.top = enemy_chess.rect.top
                enemy_chess.state = DEAD_STATE
                enemy_chess.rect.left = -100
                enemy_chess.rect.top = -100
                return True
            else:
                print('点击位置不在范围内，无法吃子')
        return False


# ----------------------------------------------------------------------------------------3333 象
class XiangChess:
    def __init__(self, rect):
        self.r_image = pygame.image.load('../image/red_xiang.png')
        self.b_image = pygame.image.load('../image/black_xiang.png')
        self.position = x, y = 86, 66
        self.state = HIDDEN_STATE
        self.type = XIANG_TYPE
        self.role = RED_ROLE
        self.rect = self.b_image.get_rect()

    def getImage(self, role):
        if self.state == HIDDEN_STATE:
            return bg_image
        elif self.state == DEAD_STATE:
            return -1
        else:
            if role == RED_ROLE:
                return self.r_image
            elif role == BLACK_ROLE:
                return self.b_image
            else:
                print('传入参数有误，无法判断是红方还是黑方！')
                return -1

    def move(self, pos):
        return can_move_one_step(self, pos)

    # 将 可以吃 其它所有
    # 是否可吃需要满足两个条件
    # 1、是否满足该子的行走规律
    # 2、是否满足该子的吃子规律
    def eat(self, enemy_chess, pos, chess_list):
        if can_eat(self.type, enemy_chess.type):
            if self.move(pos):
                self.rect.left = enemy_chess.rect.left
                self.rect.top = enemy_chess.rect.top
                enemy_chess.state = DEAD_STATE
                enemy_chess.rect.left = -100
                enemy_chess.rect.top = -100
                return True
            else:
                print('点击位置不在范围内，无法吃子')
        return False


# ----------------------------------------------------------------------------------------4444 马
class MaChess:
    def __init__(self, rect):
        self.r_image = pygame.image.load('../image/red_ma.png')
        self.b_image = pygame.image.load('../image/black_ma.png')
        self.position = x, y = 86, 66
        self.state = HIDDEN_STATE
        self.type = MA_TYPE
        self.role = RED_ROLE
        self.rect = self.b_image.get_rect()

    def getImage(self, role):
        if self.state == HIDDEN_STATE:
            return bg_image
        elif self.state == DEAD_STATE:
            return -1
        else:
            if role == RED_ROLE:
                return self.r_image
            elif role == BLACK_ROLE:
                return self.b_image
            else:
                print('传入参数有误，无法判断是红方还是黑方！')
                return -1

    def move(self, pos):
        return can_move_one_step(self, pos)

    # 将 可以吃 其它所有
    # 是否可吃需要满足两个条件
    # 1、是否满足该子的行走规律
    # 2、是否满足该子的吃子规律
    def eat(self, enemy_chess, pos, chess_list):
        if can_eat(self.type, enemy_chess.type):
            if self.move(pos):
                self.rect.left = enemy_chess.rect.left
                self.rect.top = enemy_chess.rect.top
                enemy_chess.state = DEAD_STATE
                enemy_chess.rect.left = -100
                enemy_chess.rect.top = -100
                True
            else:
                print('点击位置不在范围内，无法吃子')
        return False


# -----------------------------------------------------------------------------------------5555 车
class CheChess:
    def __init__(self, rect):
        self.r_image = pygame.image.load('../image/red_che.png')
        self.b_image = pygame.image.load('../image/black_che.png')
        self.position = x, y = 86, 66
        self.state = HIDDEN_STATE
        self.type = CHE_TYPE
        self.role = RED_ROLE
        self.rect = self.b_image.get_rect()

    def getImage(self, role):
        if self.state == HIDDEN_STATE:
            return bg_image
        elif self.state == DEAD_STATE:
            return -1
        else:
            if role == RED_ROLE:
                return self.r_image
            elif role == BLACK_ROLE:
                return self.b_image
            else:
                print('传入参数有误，无法判断是红方还是黑方！')
                return -1

    def move(self, pos):
        return can_move_one_step(self, pos)

    # 将 可以吃 其它所有
    # 是否可吃需要满足两个条件
    # 1、是否满足该子的行走规律
    # 2、是否满足该子的吃子规律
    def eat(self, enemy_chess, pos, chess_list):
        if can_eat(self.type, enemy_chess.type):
            if self.move(pos):
                self.rect.left = enemy_chess.rect.left
                self.rect.top = enemy_chess.rect.top
                enemy_chess.state = DEAD_STATE
                enemy_chess.rect.left = -100
                enemy_chess.rect.top = -100
                return True
            else:
                print('点击位置不在范围内，无法吃子')
        return False


# ----------------------------------------------------------------------------------------5555 炮
class PaoChess:
    def __init__(self, rect):
        self.r_image = pygame.image.load('../image/red_pao.png')
        self.b_image = pygame.image.load('../image/black_pao.png')
        self.position = x, y = 86, 66
        self.state = HIDDEN_STATE
        self.type = PAO_TYPE
        self.role = RED_ROLE
        self.rect = self.b_image.get_rect()

    def getImage(self, role):
        if self.state == HIDDEN_STATE:
            return bg_image
        elif self.state == DEAD_STATE:
            return -1
        else:
            if role == RED_ROLE:
                return self.r_image
            elif role == BLACK_ROLE:
                return self.b_image
            else:
                print('传入参数有误，无法判断是红方还是黑方！')
                return -1

    def move(self, pos):
        return can_move_one_step(self, pos)

    # 将 可以吃 其它所有
    # 是否可吃需要满足两个条件
    # 1、是否满足该子的行走规律
    # 2、是否满足该子的吃子规律
    def eat(self, enemy_chess, pos, chess_list):
        if can_eat(self.type, enemy_chess.type):
            if self.can_move_and_eat(enemy_chess, pos, chess_list):
                self.rect.left = enemy_chess.rect.left
                self.rect.top = enemy_chess.rect.top
                enemy_chess.state = DEAD_STATE
                enemy_chess.rect.left = -100
                enemy_chess.rect.top = -100
                return True
            else:
                print('点击位置不在范围内，无法吃子')
        return False

    def can_move_and_eat(self, enemy_chess, pos, chess_list):
        # 首先判断，pos 和当前棋子是否在同一行或同一列
        # 然后判断，两个棋子之间有几个棋子
        if self.rect.left - 10 < enemy_chess.rect.left < self.rect.left + 50:
            # 说明在同一列
            count = 0
            for each in chess_list:
                if self.rect.left - 10 < each.rect.left < self.rect.left + 50 \
                        and min(self.rect.center[1], enemy_chess.rect.center[1]) < \
                        each.rect.center[1] < max(self.rect.center[1], enemy_chess.rect.center[1]):
                    count += 1
            if count == 1:
                return True
        elif self.rect.top - 10 < enemy_chess.rect.top < self.rect.top + 50:
            # 说明在同一行
            count = 0
            for each in chess_list:
                if self.rect.top - 10 < each.rect.top < self.rect.top + 50 and \
                        min(self.rect.center[0], enemy_chess.rect.center[0]) < \
                        each.rect.center[0] < max(self.rect.center[0], enemy_chess.rect.center[0]):
                    count += 1
            if count == 1:
                return True
        return False


# ----------------------------------------------------------------------------------------5555 卒
class ZuChess:
    def __init__(self, rect):
        self.r_image = pygame.image.load('../image/red_bing.png')
        self.b_image = pygame.image.load('../image/black_zu.png')
        self.position = x, y = 86, 66
        self.state = HIDDEN_STATE
        self.type = ZU_TYPE
        self.role = RED_ROLE
        self.rect = self.b_image.get_rect()

    def getImage(self, role):
        if self.state == HIDDEN_STATE:
            return bg_image
        elif self.state == DEAD_STATE:
            return -1
        else:
            if role == RED_ROLE:
                return self.r_image
            elif role == BLACK_ROLE:
                return self.b_image
            else:
                print('传入参数有误，无法判断是红方还是黑方！')
                return -1

    def move(self, pos):
        return can_move_one_step(self, pos)

    # 将 可以吃 其它所有
    # 是否可吃需要满足两个条件
    # 1、是否满足该子的行走规律
    # 2、是否满足该子的吃子规律
    def eat(self, enemy_chess, pos, chess_list):
        if can_eat(self.type, enemy_chess.type):
            if self.move(pos):
                self.rect.left = enemy_chess.rect.left
                self.rect.top = enemy_chess.rect.top
                enemy_chess.state = DEAD_STATE
                enemy_chess.rect.left = -100
                enemy_chess.rect.top = -100
                return True
            else:
                print('点击位置不在范围内，无法吃子')
        return False

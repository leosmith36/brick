import pygame

def collides_bottom(ball, block):
    return (
        ball.rect.left - ball.vec.x <= block.rect.right and 
        ball.rect.right - ball.vec.x >= block.rect.left and
        ball.rect.top - ball.vec.y < block.rect.bottom and 
        ball.rect.top - ball.vec.y > block.rect.top and
        ball.rect.bottom - ball.vec.y > block.rect.bottom and
        ball.vec.y > 0
    )

def collides_top(ball, block):
    return (
        ball.rect.left - ball.vec.x <= block.rect.right and 
        ball.rect.right - ball.vec.x >= block.rect.left and
        ball.rect.bottom - ball.vec.y > block.rect.top and 
        ball.rect.bottom - ball.vec.y < block.rect.bottom and
        ball.rect.top - ball.vec.y < block.rect.top and
        ball.vec.y < 0
    )

def collides_left(ball, block):
    return (
        ball.rect.bottom - ball.vec.y >= block.rect.top and
        ball.rect.top - ball.vec.y <= block.rect.bottom and
        ball.rect.left - ball.vec.x < block.rect.right and
        ball.rect.left - ball.vec.x > block.rect.left and
        ball.rect.right - ball.vec.x > block.rect.right and
        ball.vec.x > 0
    )

def collides_right(ball, block):
    return (
        ball.rect.bottom - ball.vec.y >= block.rect.top and
        ball.rect.top - ball.vec.y <= block.rect.bottom and
        ball.rect.right - ball.vec.x > block.rect.left and
        ball.rect.right - ball.vec.x < block.rect.right and
        ball.rect.left - ball.vec.x  < block.rect.left and
        ball.vec.x < 0
    )

def clamp(value, min, max):
    if value > max:
        return max
    elif value < min:
        return min
    else:
        return value

import pygame.event

import main as Main
from Movement import MovementHandler as movement


class ShootingHandler():
    LEFT_BULLETS, RIGHT_BULLETS = [], []
    BULLET_HEIGHT, BULLET_WIDTH = 8, 14
    SHOOT_RATE = 4
    SHOOT_SPEED = 20

    def handleBullets(self, left_bullets, right_bullets, left_spaceship, right_spaceship):
        for bullet in left_bullets:
            bullet.x += self.SHOOT_SPEED
            if right_spaceship.colliderect(bullet):
                Main.game.event.post(Main.game.event.Event(Main.gameClass.RIGHT_HIT))
                left_bullets.remove(bullet)
            if bullet.x > Main.gameClass.WIDTH:
                left_bullets.remove(bullet)
        for bullet in right_bullets:
            bullet.x -= self.SHOOT_SPEED
            if left_spaceship.colliderect(bullet):
                Main.game.event.post(Main.game.event.Event(Main.gameClass.LEFT_HIT))
                right_bullets.remove(bullet)
            if bullet.x < 0:
                right_bullets.remove(bullet)

    def shooting(self, event):
        
        if event.key == Main.game.K_SPACE and len(self.RIGHT_BULLETS) < self.SHOOT_RATE:
            bullet = Main.game.Rect(movement.right_space_rect.x, movement.right_space_rect.y + Main.gameClass.SCALE[1] // 2 - self.BULLET_HEIGHT // 2, self.BULLET_WIDTH, self.BULLET_HEIGHT)
            self.RIGHT_BULLETS.append(bullet)
        elif event.key == Main.game.K_e and len(self.LEFT_BULLETS) < self.SHOOT_RATE:
            bullet = Main.game.Rect(movement.left_space_rect.x + Main.gameClass.SCALE[0], movement.left_space_rect.y + Main.gameClass.SCALE[1] // 2 - self.BULLET_HEIGHT // 2, self.BULLET_WIDTH, self.BULLET_HEIGHT)
            self.LEFT_BULLETS.append(bullet)
        self.handleBullets(self.LEFT_BULLETS, self.RIGHT_BULLETS, movement.left_space_rect, movement.right_space_rect)

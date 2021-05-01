import pygame.event

import main as Main


class ShootingHandler():
    LEFT_BULLETS, RIGHT_BULLETS = [], []
    BULLET_HEIGHT, BULLET_WIDTH = 6, 12

    def handleBullets(self, left_bullets, right_bullets, left_spaceship, right_spaceship):
        for bullet in left_bullets:
            bullet.x += Main.gameClass.SHOOT_SPEED
            if right_spaceship.colliderect(bullet):
                Main.game.event.post(Main.game.event.Event(Main.gameClass.RIGHT_HIT))
                left_bullets.remove(bullet)
        for bullet in right_bullets:
            bullet.x -= Main.gameClass.SHOOT_SPEED
            if left_spaceship.colliderect(bullet):
                Main.game.event.post(Main.game.event.Event(Main.gameClass.LEFT_HIT))
                right_bullets.remove(bullet)

    def shooting(self, event):
        if event.key == Main.game.K_SPACE:
            bullet = Main.game.Rect(Main.gameClass.movement.right_space.x, Main.gameClass.movement.right_space.y + Main.gameClass.SCALE[1] / 2 - Main.gameClass.BULLET_HEIGHT / 2, Main.gameClass.BULLET_WIDTH, Main.gameClass.BULLET_HEIGHT)
            self.RIGHT_BULLETS.append(bullet)
        elif event.key == Main.game.K_e:
            bullet = Main.game.Rect(Main.gameClass.movement.left_space.x + Main.gameClass.SCALE[0], Main.gameClass.movement.left_space.y + Main.gameClass.SCALE[1] / 2 - Main.gameClass.BULLET_HEIGHT / 2, Main.gameClass.BULLET_WIDTH, Main.gameClass.BULLET_HEIGHT)
            self.LEFT_BULLETS.append(bullet)

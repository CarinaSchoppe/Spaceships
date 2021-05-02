import main as Main
from Movement import MovementHandler as movement
import random



class ShootingHandler():
    LEFT_BULLETS, RIGHT_BULLETS = [], []
    BULLET_HEIGHT, BULLET_WIDTH = 8, 15
    SHOOT_RATE = 3
    SHOOT_SPEED = 12
    HEALTH = 13
    LEFT_HEALTH, RIGHT_HEALTH = HEALTH, HEALTH
    LEFT_HIT, RIGHT_HIT = Main.game.USEREVENT + 1, Main.game.USEREVENT + 2
    SOUNDS = [Main.gameClass.BULLET_HIT_SOUND_A, Main.gameClass.BULLET_HIT_SOUND_B, Main.gameClass.BULLET_HIT_SOUND_C]

    def handleBullets(self, left_bullets, right_bullets, left_spaceship, right_spaceship, left_health, right_health):
        for bullet in left_bullets:
            bullet.x += self.SHOOT_SPEED
            if right_spaceship.colliderect(bullet):
                sound = random.choice(self.SOUNDS)
                sound.play()
                Main.game.event.post(Main.game.event.Event(self.RIGHT_HIT))
                left_bullets.remove(bullet)
            if bullet.x > Main.gameClass.WIDTH:
                left_bullets.remove(bullet)
        for bullet in right_bullets:
            bullet.x -= self.SHOOT_SPEED
            if left_spaceship.colliderect(bullet):
                sound = random.choice(self.SOUNDS)
                sound.play()
                Main.game.event.post(Main.game.event.Event(self.LEFT_HIT))
                right_bullets.remove(bullet)
            if bullet.x < 0:
                right_bullets.remove(bullet)

    def shooting(self, event):
        if event.type == Main.game.KEYDOWN:
            if event.key == Main.game.K_SPACE and len(self.RIGHT_BULLETS) < self.SHOOT_RATE:
                Main.gameClass.BULLET_FIRE_SOUND.play()
                bullet = Main.game.Rect(movement.right_space_rect.x, movement.right_space_rect.y + Main.gameClass.SCALE[1] //
                                        2 - self.BULLET_HEIGHT // 2, self.BULLET_WIDTH, self.BULLET_HEIGHT)
                self.RIGHT_BULLETS.append(bullet)
            elif event.key == Main.game.K_e and len(self.LEFT_BULLETS) < self.SHOOT_RATE:
                Main.gameClass.BULLET_FIRE_SOUND.play()
                bullet = Main.game.Rect(movement.left_space_rect.x + Main.gameClass.SCALE[0], movement.left_space_rect.y + Main.gameClass.SCALE[1] //
                                        2 - self.BULLET_HEIGHT // 2, self.BULLET_WIDTH, self.BULLET_HEIGHT)
                self.LEFT_BULLETS.append(bullet)
        elif event.type == self.LEFT_HIT:
            self.LEFT_HEALTH -= 1
        elif event.type == self.RIGHT_HIT:
            self.RIGHT_HEALTH -= 1

    @staticmethod
    def displayWinner(text):
        draw_text = Main.gameClass.WINNER_FONT.render(text, 1, Main.gameClass.WHITE)
        Main.gameClass.WINDOW.blit(draw_text, (Main.gameClass.WIDTH // 2 - draw_text.get_width() //
                                               2, Main.gameClass.HEIGHT // 2 - draw_text.get_height() // 2))
        Main.game.display.update()
        Main.game.time.delay(1000 * Main.gameClass.DELAY)

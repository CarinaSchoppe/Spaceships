import pygame as game
import os

game.font.init()
game.mixer.init()

if __name__ == '__main__':
    from Movement import MovementHandler
    from Shooting import ShootingHandler


class GameClass:
    if __name__ == '__main__':
        shooting = ShootingHandler()
        movement = MovementHandler()

    pythonGame = game
    WIDTH, HEIGHT, VEL, FPS = 1280, 720, 6, 60
    WINDOW = game.display.set_mode((WIDTH, HEIGHT))
    HEALTH_FONT, WINNER_FONT = game.font.SysFont('comicsans', 45), game.font.SysFont('comicsans', 90)
    BORDER_WIDTH, BORDER_HEIGHT, BORDER_THICKNESS = WIDTH / 2 - 5, HEIGHT, 10
    BORDER, SCALE = game.Rect(BORDER_WIDTH, 0, BORDER_THICKNESS, BORDER_HEIGHT), (70, 85)
    LEFT_SPACESHIP_IMAGE = game.transform.scale(game.image.load(os.path.join('Assets', 'spaceship.png')), SCALE)
    LEFT_SPACESHIP = game.transform.rotate(LEFT_SPACESHIP_IMAGE, 180)
    RIGHT_SPACESHIP = game.transform.scale(game.image.load(os.path.join('Assets', 'spaceship.png')), SCALE)
    CHARACTER_HEIGHT, DISTANCE_TEXT, WINNER_TEXT = 55, 10, ""
    BULLET_HIT_SOUND, BULLET_FIRE_SOUND = game.mixer.Sound(os.path.join('Assets', 'Peng.mp3')), game.mixer.Sound(os.path.join('Assets', 'shot_sound.mp3'))
    RED, GREEN, WHITE, BLACK = (255, 0, 0), (0, 255, 0), (255, 255, 255), (0, 0, 0)
    BACKGROUND, DELAY, RUN = game.transform.scale(game.image.load(os.path.join('Assets', 'background.png')), (WIDTH, HEIGHT)), 5, True

    def updateScreen(self, left_spaceship, right_spaceship, left_bullets, right_bullets):
        self.WINDOW.blit(self.BACKGROUND, (0, 0))
        left_health_text = self.HEALTH_FONT.render("Health: " + str(self.shooting.LEFT_HEALTH), 1, self.WHITE)
        right_health_text = self.HEALTH_FONT.render("Health: " + str(self.shooting.RIGHT_HEALTH), 1, self.WHITE)
        self.WINDOW.blit(self.movement.LEFT_SPACESHIP, (left_spaceship.x, left_spaceship.y))
        self.WINDOW.blit(self.movement.RIGHT_SPACESHIP, (right_spaceship.x, right_spaceship.y))
        game.draw.rect(self.WINDOW, self.BLACK, self.BORDER)
        self.WINDOW.blit(left_health_text, (self.DISTANCE_TEXT, self.DISTANCE_TEXT))
        self.WINDOW.blit(right_health_text, (self.WIDTH - right_health_text.get_width() - self.DISTANCE_TEXT, self.DISTANCE_TEXT))
        for bullets in left_bullets:
            game.draw.rect(self.WINDOW, self.GREEN, bullets)
        for bullets in right_bullets:
            game.draw.rect(self.WINDOW, self.RED, bullets)
        game.display.update()

    def checkWin(self):
        if self.shooting.LEFT_HEALTH <= 0:
            self.WINNER_TEXT = "RIGHT wins!"
            ShootingHandler.displayWinner(self.WINNER_TEXT)
            self.RUN = False
        if self.shooting.RIGHT_HEALTH <= 0:
            self.WINNER_TEXT = "LEFT wins!"
            ShootingHandler.displayWinner(self.WINNER_TEXT)
            self.RUN = False

    def startGame(self):
        clock = game.time.Clock()
        while self.RUN:
            clock.tick(GameClass.FPS)
            self.checkWin()
            self.shooting.handleBullets(self.shooting.LEFT_BULLETS, self.shooting.RIGHT_BULLETS, self.movement.left_space_rect,
                                        self.movement.right_space_rect, self.shooting.LEFT_HEALTH, self.shooting.RIGHT_HEALTH)
            for event in game.event.get():
                if event.type == game.QUIT:  # EVENT That user quits the game
                    self.RUN = False
                    game.quit()
                self.shooting.shooting(event)
                # BULLETS

            self.movement.move_Left(game.key.get_pressed())
            self.movement.move_Right(game.key.get_pressed())
            self.updateScreen(self.movement.left_space_rect, self.movement.right_space_rect, self.shooting.LEFT_BULLETS, self.shooting.RIGHT_BULLETS)

        # END THE GAME TO CLOSE
        game.quit()


gameClass = GameClass()

if __name__ == '__main__':
    gameClass.startGame()

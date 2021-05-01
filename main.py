import pygame as game
import os

if __name__ == '__main__':
    from Movement import MovementHandler
    from Shooting import ShootingHandler


class GameClass:
    if __name__ == '__main__':
        shooting = ShootingHandler()
        movement = MovementHandler()

    pythonGame = game
    WIDTH, HEIGHT, VEL, FPS = 1000, 600, 4, 60
    WINDOW = game.display.set_mode((WIDTH, HEIGHT))
    WHITE, SCALE, BLACK = (123, 245, 45), (55, 65), (0, 0, 0)
    BORDER_WIDTH, BORDER_HEIGHT, BORDER_THICKNESS = WIDTH / 2 - 5, HEIGHT, 10
    BORDER = game.Rect(BORDER_WIDTH, 0, BORDER_THICKNESS, BORDER_HEIGHT)
    LEFT_HIT, RIGHT_HIT = game.USEREVENT + 1, game.USEREVENT + 2
    LEFT_SPACESHIP_IMAGE = game.transform.scale(game.image.load(os.path.join('Assets', 'spaceship.png')), SCALE)
    LEFT_SPACESHIP = game.transform.rotate(LEFT_SPACESHIP_IMAGE, 180)
    RIGHT_SPACESHIP = game.transform.scale(game.image.load(os.path.join('Assets', 'spaceship.png')), SCALE)
    CHARACTER_HEIGHT = 50
    RED, BLUE = (255,0,0), (0,0,255)
    BACKGROUND = game.transform.scale(game.image.load(os.path.join('Assets', 'background.png')), (WIDTH, HEIGHT))

    def updateScreen(self, left_spaceship, right_spaceship, left_bullets, right_bullets):
        self.WINDOW.blit(self.BACKGROUND, (0,0))
        self.WINDOW.blit(self.movement.LEFT_SPACESHIP, (left_spaceship.x, left_spaceship.y))
        self.WINDOW.blit(self.movement.RIGHT_SPACESHIP, (right_spaceship.x, right_spaceship.y))
        game.draw.rect(self.WINDOW, self.BLACK, self.BORDER)

        for bullets in left_bullets:
            game.draw.rect(self.WINDOW, self.BLUE, bullets)
        for bullets in right_bullets:
            game.draw.rect(self.WINDOW, self.RED, bullets)
        game.display.update()

    def startGame(self):
        run = True
        clock = game.time.Clock()

        while run:
            clock.tick(GameClass.FPS)
            for event in game.event.get():
                if event.type == game.QUIT:  # EVENT That user quits the game
                    run = False
                if event.type == game.KEYDOWN:
                    self.shooting.shooting(event)
                    # BULLETS

            self.shooting.handleBullets(self.shooting.LEFT_BULLETS, self.shooting.RIGHT_BULLETS, self.movement.left_space_rect, self.movement.right_space_rect)
            self.movement.move_Left(game.key.get_pressed())
            self.movement.move_Right(game.key.get_pressed())
            self.updateScreen(self.movement.left_space_rect, self.movement.right_space_rect, self.shooting.LEFT_BULLETS, self.shooting.RIGHT_BULLETS)

        # END THE GAME TO CLOSE
        game.quit()


gameClass = GameClass()

if __name__ == '__main__':
    gameClass.startGame()

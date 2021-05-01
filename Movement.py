import main


class MovementHandler:
    game = main.gameClass.pythonGame
    gameClass = main.GameClass
    leftspace_left = False
    leftspace_right = True
    leftspace_up = False
    leftspace_down = False

    rightspace_left = True
    rightspace_right = False
    rightspace_up = False
    rightspace_down = False

    LEFT_SPACESHIP = gameClass.LEFT_SPACESHIP
    RIGHT_SPACESHIP = gameClass.RIGHT_SPACESHIP
    left_space_rect = game.Rect(100, 300, gameClass.SCALE[0], gameClass.SCALE[1])
    right_space_rect = game.Rect(800, 300, gameClass.SCALE[0], gameClass.SCALE[1])

    def move_Right(self, keys_pressed):
        if keys_pressed[self.game.K_UP] and self.right_space_rect.y - main.gameClass.VEL + 5 > 0:
            self.right_space_rect.y -= self.gameClass.VEL
            if self.rightspace_right:
                self.RIGHT_SPACESHIP = self.game.transform.rotate(self.RIGHT_SPACESHIP, 90)
            elif self.rightspace_left:
                self.RIGHT_SPACESHIP = self.game.transform.rotate(self.RIGHT_SPACESHIP, 270)
            elif self.rightspace_down:
                self.RIGHT_SPACESHIP = self.game.transform.rotate(self.RIGHT_SPACESHIP, 180)

            self.rightspace_up = True
            self.rightspace_down = False
            self.rightspace_left = False
            self.rightspace_right = False

            # MOVEMENT FOR ONE KEY!

        if keys_pressed[self.game.K_DOWN] and self.right_space_rect.y + main.gameClass.VEL + \
                main.gameClass.CHARACTER_HEIGHT < main.gameClass.HEIGHT:
            self.right_space_rect.y += self.gameClass.VEL
            if self.rightspace_right:
                self.RIGHT_SPACESHIP = self.game.transform.rotate(self.RIGHT_SPACESHIP, 270)
            elif self.rightspace_left:
                self.RIGHT_SPACESHIP = self.game.transform.rotate(self.RIGHT_SPACESHIP, 90)
            elif self.rightspace_up:
                self.RIGHT_SPACESHIP = self.game.transform.rotate(self.RIGHT_SPACESHIP, 180)
            self.rightspace_up = False
            self.rightspace_down = True
            self.rightspace_left = False
            self.rightspace_right = False

        if keys_pressed[self.game.K_LEFT] and self.right_space_rect.x - main.gameClass.VEL > \
                main.gameClass.BORDER_WIDTH + main.gameClass.BORDER_THICKNESS / 2:
            self.right_space_rect.x -= self.gameClass.VEL
            if self.rightspace_right:
                self.RIGHT_SPACESHIP = self.game.transform.rotate(self.RIGHT_SPACESHIP, 180)
            elif self.rightspace_up:
                self.RIGHT_SPACESHIP = self.game.transform.rotate(self.RIGHT_SPACESHIP, 90)
            elif self.rightspace_down:
                self.RIGHT_SPACESHIP = self.game.transform.rotate(self.RIGHT_SPACESHIP, 270)
            self.rightspace_up = False
            self.rightspace_down = False
            self.rightspace_left = True
            self.rightspace_right = False

            # MOVEMENT FOR ONE KEY!

        if keys_pressed[self.game.K_RIGHT] and self.right_space_rect.x + main.gameClass.VEL + 5 + \
                main.gameClass.CHARACTER_HEIGHT < main.gameClass.WIDTH:
            self.right_space_rect.x += self.gameClass.VEL
            if self.rightspace_down:
                self.RIGHT_SPACESHIP = self.game.transform.rotate(self.RIGHT_SPACESHIP, 90)
            elif self.rightspace_left:
                self.RIGHT_SPACESHIP = self.game.transform.rotate(self.RIGHT_SPACESHIP, 180)
            elif self.rightspace_up:
                self.RIGHT_SPACESHIP = self.game.transform.rotate(self.RIGHT_SPACESHIP, 270)
            self.rightspace_up = False
            self.rightspace_down = False
            self.rightspace_left = False
            self.rightspace_right = True

    def move_Left(self, keys_pressed):
        if keys_pressed[self.game.K_w] and self.left_space_rect.y - main.gameClass.VEL + 5 > 0:
            self.left_space_rect.y -= self.gameClass.VEL
            if self.leftspace_right:
                self.LEFT_SPACESHIP = self.game.transform.rotate(self.LEFT_SPACESHIP, 90)
            elif self.leftspace_left:
                self.LEFT_SPACESHIP = self.game.transform.rotate(self.LEFT_SPACESHIP, 270)
            elif self.leftspace_down:
                self.LEFT_SPACESHIP = self.game.transform.rotate(self.LEFT_SPACESHIP, 180)
            elif self.leftspace_up:
                pass
            self.leftspace_up = True
            self.leftspace_down = False
            self.leftspace_left = False
            self.leftspace_right = False

            # MOVEMENT FOR ONE KEY!

        if keys_pressed[self.game.K_s] and self.left_space_rect.y + main.gameClass.VEL + main.gameClass.CHARACTER_HEIGHT < main.gameClass.HEIGHT:
            self.left_space_rect.y += self.gameClass.VEL
            if self.leftspace_right:
                self.LEFT_SPACESHIP = self.game.transform.rotate(self.LEFT_SPACESHIP, 270)
            elif self.leftspace_left:
                self.LEFT_SPACESHIP = self.game.transform.rotate(self.LEFT_SPACESHIP, 90)
            elif self.leftspace_up:
                self.LEFT_SPACESHIP = self.game.transform.rotate(self.LEFT_SPACESHIP, 180)
            elif self.leftspace_down:
                pass
            self.leftspace_up = False
            self.leftspace_down = True
            self.leftspace_left = False
            self.leftspace_right = False

        if keys_pressed[self.game.K_a] and self.left_space_rect.x - main.gameClass.VEL + 5 > 0:
            self.left_space_rect.x -= self.gameClass.VEL
            if self.leftspace_right:
                self.LEFT_SPACESHIP = self.game.transform.rotate(self.LEFT_SPACESHIP, 180)
            elif self.leftspace_up:
                self.LEFT_SPACESHIP = self.game.transform.rotate(self.LEFT_SPACESHIP, 90)
            elif self.leftspace_down:
                self.LEFT_SPACESHIP = self.game.transform.rotate(self.LEFT_SPACESHIP, 270)
            self.leftspace_up = False
            self.leftspace_down = False
            self.leftspace_left = True
            self.leftspace_right = False

            # MOVEMENT FOR ONE KEY!

        if keys_pressed[self.game.K_d] and self.left_space_rect.x + main.gameClass.VEL + main.gameClass.CHARACTER_HEIGHT \
                < main.gameClass.BORDER_WIDTH:
            self.left_space_rect.x += self.gameClass.VEL
            if self.leftspace_down:
                self.LEFT_SPACESHIP = self.game.transform.rotate(self.LEFT_SPACESHIP, 90)
            elif self.leftspace_left:
                self.LEFT_SPACESHIP = self.game.transform.rotate(self.LEFT_SPACESHIP, 180)
            elif self.leftspace_up:
                self.LEFT_SPACESHIP = self.game.transform.rotate(self.LEFT_SPACESHIP, 270)
            self.leftspace_up = False
            self.leftspace_down = False
            self.leftspace_left = False
            self.leftspace_right = True

            # PFEILTASTEN

class Game:
    def __init__(self):
        self.character = None
        self.obstacles = []

    def set_character(self, character):
        self.character = character

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def play(self):
        if self.character is None:
            print("Персонаж не задан. Невозможно начать игру.")
            return

        print("Игра началась за этого персонажа:")
        self.character.info()

        print("Расстановка препятствий:")
        for obstacle in self.obstacles:
            obstacle.info()


class Character:
    def __init__(self):
        self.name = None
        self.health = 0

    def set_name(self, name):
        self.name = name

    def set_health(self, health):
        self.health = health

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Здоровье: {self.health}")


class Obstacle:
    def __init__(self):
        self.name = None
        self.difficulty = 0

    def set_name(self, name):
        self.name = name

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def info(self):
        print(f"Название: {self.name}")
        print(f"Сложность: {self.difficulty}")


class GameBuilder:
    def __init__(self):
        self.game = Game()

    def build_character(self, name, health):
        character = Character()
        character.set_name(name)
        character.set_health(health)
        self.game.set_character(character)

    def build_obstacle(self, name, difficulty):
        obstacle = Obstacle()
        obstacle.set_name(name)
        obstacle.set_difficulty(difficulty)
        self.game.add_obstacle(obstacle)

    def get_game(self):
        return self.game


if __name__ == '__main__':
    builder = GameBuilder()
    builder.build_character("Player", 100)
    builder.build_obstacle("Medium obstacle", 5)
    builder.build_obstacle("High obstacle", 8)
    game = builder.get_game()
    game.play()

# 1) Класс-переменная как “общее число созданных объектов”
class Student:
    total_students = 0  # class variable (общая)

    def __init__(self, name: str):
        self.name = name  # instance variable (у каждого своя)
        Student.total_students += 1


# 2) Class variable как “настройка по умолчанию”
class AppConfig:
    language = "ru"  # общий язык для приложения

    def __init__(self, theme: str):
        self.theme = theme


# 3) Переопределение class variable через класс
class Game:
    max_players = 4

    def __init__(self, title: str):
        self.title = title


# 4) Осторожно: изменяемые class variables (покажем правильный подход)
class Team:
    # ПЛОХО делать общий список игроков как class variable, потому что он будет общий для всех команд.
    # Поэтому сделаем правильный вариант: список на уровне экземпляра.
    def __init__(self, name: str):
        self.name = name
        self.players: list[str] = []

    def add_player(self, player: str) -> None:
        self.players.append(player)


if __name__ == "__main__":
    s1 = Student("Dana")
    s2 = Student("Ali")
    print("Example 1:", Student.total_students, s1.name, s2.name)

    config = AppConfig(theme="dark")
    print("Example 2:", AppConfig.language, config.theme)
    AppConfig.language = "en"
    print("Example 2:", AppConfig.language)

    game = Game("Chess")
    print("Example 3:", Game.max_players, game.title)
    Game.max_players = 2
    print("Example 3:", Game.max_players)

    team_a = Team("A")
    team_b = Team("B")
    team_a.add_player("Neo")
    team_b.add_player("Trinity")
    print("Example 4:", team_a.players, team_b.players)

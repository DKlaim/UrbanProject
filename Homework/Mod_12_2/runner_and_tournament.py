class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.speed = speed
        self.distance = 0

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


# runner_1 = Runner('Усэйн', 10)
# runner_2 = Runner('Андрей', 15)
# runner_3 = Runner('Ник', 20)
#
# tournament = Tournament(90, runner_1, runner_2, runner_3)
# result = tournament.start()
#
# for place, participant in result.items():
#     print(place, participant)

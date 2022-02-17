class Training:

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight


def read_package(workout_type: str, data: list):
    """Прочитать данные полученные от датчиков."""
    dictitionary = {'SWM': 'Swimming', 'RUN': 'Running', 'WLK': 'Walking'}
    return (dictitionary[workout_type], (*data))




packages = [
    ('SWM', [720, 1, 80, 25, 40]),
    ('RUN', [15000, 1, 75]),
    ('WLK', [9000, 1, 75, 180]),
]
for workout_type, data in packages:
    training = read_package(workout_type, data)
    print(training)    

print(packages)

class ExercisePlan:
    id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = __class__.id
        __class__.id += 1

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, duration=hours*60)

    @staticmethod
    def get_next_id():
        return __class__.id

    def __repr__(self):
        return f'Plan <{self.id}> with duration {self.duration} minutes'

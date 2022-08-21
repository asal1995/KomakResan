from enum import Enum


class StateChoice(Enum):
    CHECK = 'check'
    DEFECT = 'defect'
    COMPLETE = 'complete'

    @classmethod
    def choices(cls):
        # print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)
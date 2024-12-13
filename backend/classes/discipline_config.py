from dataclasses import dataclass


@dataclass
class DisciplineConfig:
    contol_form: str
    name: str
    semester: int
    mark: int | str
    study_hours: int
    credits_number: int | float


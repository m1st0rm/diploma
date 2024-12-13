from dataclasses import dataclass


@dataclass
class DisciplineConfig:
    contol_type_form: str
    name: str
    priority: int
    mark: int | str
    study_hours: int
    credits_number: int | float


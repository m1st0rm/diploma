from dataclasses import dataclass


@dataclass
class DisciplineConfig:
    contol_form: str
    name: str
    semester: int
    mark: int | str
    study_hours: int
    credits_number: int | float
    categoty: str

    def __repr__(self) -> str:
        return f"""
        Discipline name: {self.name}\n
        Contol form: {self.contol_form}\n
        Semester: {self.semester}\n
        Mark: {self.mark}\n
        Study hours: {self.study_hours}\n
        Credits number: {self.credits_number}\n
        Categoty: {self.categoty}\n
        """

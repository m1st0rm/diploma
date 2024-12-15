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
        Discipline name: {self.name}
        Contol form: {self.contol_form}
        Semester: {self.semester}
        Mark: {self.mark}
        Study hours: {self.study_hours}
        Credits number: {self.credits_number}
        Categoty: {self.categoty}
        """

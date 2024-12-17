"""
Module defining the DisciplineConfig class for storing discipline-specific configurations.

This class represents the structure of discipline data, including its name, semester,
mark, study hours, credits, and other related attributes.

Classes:
- DisciplineConfig: A dataclass for managing discipline configurations.

"""

from dataclasses import dataclass


@dataclass
class DisciplineConfig:
    """
    A class representing the configuration of a discipline.

    Attributes:
        contol_form: The form of control for the discipline (e.g., exam, test, project).
        name: The name of the discipline.
        semester: The semester number in which the discipline was studied.
        mark: The mark or grade for the discipline. Can be an integer, string, or list of mixed values.
        study_hours: The total number of study hours assigned to the discipline.
        credits_number: The number of credits associated with the discipline (can be integer or float).
        categoty: The category of the discipline.
    """
    contol_form: str
    name: str
    semester: int
    mark: int | str | list[int | str]
    study_hours: int
    credits_number: int | float
    categoty: str

    def __repr__(self) -> str:
        """
        Returns a formatted string representation of the discipline configuration.

        :return: A formatted string with all discipline details.
        :rtype: str
        """
        return f"""
        Discipline name: {self.name}
        Contol form: {self.contol_form}
        Semester: {self.semester}
        Mark: {self.mark}
        Study hours: {self.study_hours}
        Credits number: {self.credits_number}
        Categoty: {self.categoty}
        """

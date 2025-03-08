"""
Module defining the StudentConfig class for managing student-specific configurations.

This class represents the structure of a student's data, including their full name,
disciplines divided by category (regular, course work, course project, practice), and the diploma theme.

Classes:
- StudentConfig: A dataclass for storing student information and discipline details.
"""

from dataclasses import dataclass


@dataclass
class StudentConfig:
    """
    A class representing the configuration of a student.

    Attributes:
        full_name: The full name of the student.
        regular_disciplines: A list of regular disciplines as tuples (name, hours/credits, mark).
        course_work_disciplines: A list of course work disciplines as tuples (name, hours/credits, mark).
        course_project_disciplines: A list of course project disciplines as tuples (name, hours/credits, mark).
        practice_disciplines: A list of practice disciplines as tuples (name, hours/credits, mark).
        diploma_theme: The theme or title of the student's diploma project.
    """

    full_name: str
    regular_disciplines: list[tuple[str, str, str]]
    course_work_disciplines: list[tuple[str, str, str]]
    course_project_disciplines: list[tuple[str, str, str]]
    practice_disciplines: list[tuple[str, str, str]]
    diploma_theme: str

    def __repr__(self):
        """
        Returns a formatted string representation of the student's configuration.

        :return: A formatted string containing all student details.
        :rtype: str
        """
        return f"""
        Student's Full Name: {self.full_name}
        Regular Disciplines: {self.regular_disciplines}
        Course Work Disciplines: {self.course_work_disciplines}
        Course Project Disciplines: {self.course_project_disciplines}
        Practice Disciplines: {self.practice_disciplines}
        Diploma Theme: {self.diploma_theme}
        """

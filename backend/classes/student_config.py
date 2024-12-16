from dataclasses import dataclass


@dataclass
class StudentConfig:
    full_name: str
    regular_disciplines: list[tuple[str, str, str]]
    course_work_disciplines: list[tuple[str, str, str]]
    course_project_disciplines: list[tuple[str, str, str]]
    practice_disciplines: list[tuple[str, str, str]]
    diploma_theme: str

    def __repr__(self):
        return f"""
        Student's Full Name: {self.full_name}
        Regular Disciplines: {self.regular_disciplines}
        Course Work Disciplines: {self.course_work_disciplines}
        Course Project Disciplines: {self.course_project_disciplines}
        Practice Disciplines: {self.practice_disciplines}
        Diploma Theme: {self.diploma_theme}
        """
from backend.classes.discipline_config import DisciplineConfig

STUDENTS_STATS_RAW_TYPE = list[dict[str, dict[str, str | int]]]
STUDENTS_STATS_WITH_DISCIPLINE_CONFIGS = dict[str, list[DisciplineConfig]]

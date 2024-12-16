from dataclasses import dataclass


@dataclass
class CommonConfig:
    start_date_day: str
    start_date_month: str
    start_date_year: str
    end_date_day: str
    end_date_month: str
    end_date_year: str
    specialty_code: str
    specialty_name: str
    specialty_area_code: str
    specialty_area_name: str
    statement_date_day: str
    statement_date_month: str
    statement_date_year: str

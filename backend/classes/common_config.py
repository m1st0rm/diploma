"""
Module containing the CommonConfig class for storing shared configuration details.

This class is used to store date ranges, specialty details, and statement generation information,
which are common across multiple processes for building Word documents or generating reports.

Classes:
- CommonConfig: A dataclass for storing shared configuration details such as dates, specialty names, and codes.
"""

from dataclasses import dataclass


@dataclass
class CommonConfig:
    """
    A class representing shared configuration details for document generation.

    Attributes:
       start_date_day: The starting day of the study period.
       start_date_month: The starting month of the study period.
       start_date_year: The starting year of the study period.
       end_date_day: The ending day of the study period.
       end_date_month: The ending month of the study period.
       end_date_year: The ending year of the study period.
       speciality_code: The code of the student's specialty.
       speciality_name: The full name of the student's specialty.
       speciality_area_code: The code of the specialty area or direction.
       speciality_area_name: The full name of the specialty area or direction.
       statement_date_day: The day of the statement generation.
       statement_date_month: The month of the statement generation.
       statement_date_year: The year of the statement generation.
    """
    start_date_day: str
    start_date_month: str
    start_date_year: str
    end_date_day: str
    end_date_month: str
    end_date_year: str
    speciality_code: str
    speciality_name: str
    speciality_area_code: str
    speciality_area_name: str
    statement_date_day: str
    statement_date_month: str
    statement_date_year: str

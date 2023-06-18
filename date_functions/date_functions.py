'date_functions.py'

from datetime import datetime

class CustomDate(datetime):
    """
    Represents a custom date class derived from datetime.

    Attributes:
        year (int): The year component of the date.
        month (int): The month component of the date.
        day (int): The day component of the date.
    """

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def formatted_date(self) -> str:
        """
        Formats the date as a string in the format '%a %d/%m'.

        Returns:
            str: The formatted date string.
        """
        return self.strftime('%a %d/%m')

    def duration(self) -> int:
        """
        Calculates the age based on the date.

        Returns:
            int: The duration in days.
        """
        today = datetime.now().date()
        return (today - self.date()).days

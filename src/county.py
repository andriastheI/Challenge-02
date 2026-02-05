"""
Filename: county.py
Author: Andrias Zelele
Date: 2026-01-27
Description:
    Defines the County class, which represents a Montana county with
    a county name, county seat (city), and license plate prefix.
    The class provides getter and setter methods for each attribute
    and a string representation for easy display.
"""
class County:
    """
    County
    ------
    Represents a Montana county with a name, county seat (city),
    and license plate prefix.
    """

    def __init__(self, name, city, prefix):
        """
        Initializes a County object.

        :param name: Name of the county
        :param city: County seat (city)
        :param prefix: License plate prefix
        """
        self.name = name
        self.city = city
        self.prefix = prefix

    def set_name(self, name):
        """
        Sets the county name.

        :param name: New county name
        """
        self.name = name

    def get_name(self):
        """
        Returns the county name.

        :return: County name
        """
        return self.name

    def set_city(self, city):
        """
        Sets the county seat (city).

        :param city: New county seat name
        """
        self.city = city

    def get_city(self):
        """
        Returns the county seat (city).

        :return: County seat name
        """
        return self.city

    def set_prefix(self, prefix):
        """
        Sets the license plate prefix.

        :param prefix: New license plate prefix
        """
        self.prefix = prefix

    def get_prefix(self):
        """
        Returns the license plate prefix.

        :return: License plate prefix
        """
        return self.prefix

    def __str__(self):
        """
        Returns a string representation of the County object.

        :return: Formatted string containing county data
        """
        return f"{self.name}, {self.city}, {self.prefix}"

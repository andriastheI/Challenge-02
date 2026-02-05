from county import County

"""
Filename: challenge02.py
Author: Andrias Zelele
Date: 2026-01-27
Description:
    A console-based Python program that loads Montana county data from a CSV file
    and allows users to search for a county and/or county seat using a license
    plate prefix. The program provides a menu-driven interface with input
    validation and demonstrates basic file I/O and object-oriented programming.
"""


class Challenge02:
    """
    Challenge02
    -----------
    A console-based program that allows users to search Montana counties
    using a license plate prefix. The program can display the county name,
    county seat (city), or both based on user selection.
    """

    # Path to the CSV file containing Montana county data
    STORIES_FILE = "doc/MontanaCounties.csv"

    def __init__(self):
        """
        Initializes the Challenge02 object.
        Creates an empty list to store County objects.
        """
        self.county_arr = []

    def load_data(self, file_path):
        """
        Loads county data from a CSV file and stores it as County objects.

        Each row in the CSV file is expected to contain:
        county name, county seat (city), and license plate prefix.
        """
        try:
            # Open the CSV file for reading
            with open(file_path, 'r', encoding='utf-8') as file:
                # Skip the header line
                next(file, None)

                # Read each remaining line in the file
                for line in file:
                    # Remove whitespace and split the line by commas
                    single_line = line.strip().split(",")

                    # Ensure the line contains exactly three values
                    if len(single_line) == 3:
                        name, city, prefix = single_line
                        # Create a County object and add it to the list
                        self.county_arr.append(County(name.strip(), city.strip(), prefix.strip()))

        # Handle missing file error
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        # Handle any other unexpected errors
        except Exception as e:
            print(f"An error occurred: {e}")

    def intro(self):
        """
        Displays the program menu and prompts the user to choose an option.

        Returns:
            int: The user's selected menu option.
        """
        print("*******************************************************************************************************")
        print("******************************** WELCOME TO THE CHALLENGE 02 ******************************************")
        print("*******************************************************************************************************")
        print("Where you can search and find your County and license Plate Prefix based on your County Seat(city)!!!")
        print("First, Which option would you like to use?(choose a number from 1-4)")
        print(" 1. Display County name")
        print(" 2. Display license Plate Prefix")
        print(" 3. Display both County and license Plate Prefix")
        print(" 4. Quit Program")

        # Continuously prompt the user until a valid menu option is entered
        while True:
            ask_user = input("")
            if ask_user.strip() == "1":
                request = 1
                break
            elif ask_user.strip() == "2":
                request = 2
                break
            elif ask_user.strip() == "3":
                request = 3
                break
            elif ask_user.strip() == "4":
                request = 4
                break
            else:
                print("Please enter a number from 1-4!!!")

        return request

    def run_program(self):
        """
        Runs the main program loop.
        Handles menu selection and user interaction until the program exits.
        """
        # Load county data from the CSV file
        self.load_data(Challenge02.STORIES_FILE)

        check_in = True
        while check_in:
            # Display the menu and get user selection
            double_check = self.intro()

            # Exit the program if the user chooses option 4
            if double_check == 4:
                print("Thank you for not using this program!")
                check_in = False
                break

            # Option 1: Display county name
            elif double_check == 1:
                while True:
                    ask_user_city = input("Please enter your County Seat(city)('Back' to to go back): ")

                    # Search for the county using the city name
                    if self.search_county_by_city(ask_user_city.strip().title()) is not None:
                        print(
                            f" County Seat(city) : {ask_user_city} \n"
                            f" County name : {self.search_county_by_city(ask_user_city.strip().title()).get_name()} "
                        )
                    # Allow the user to return to the main menu
                    elif ask_user_city.strip().title() == "Back":
                        print("Going back ...")
                        break
                    else:
                        print(f" County Seat(city) : {ask_user_city} has no County in this Data")

            # Option 2: Display license plate prefix
            elif double_check == 2:
                while True:
                    ask_user_city = input("Please enter your County Seat(city)('Back' to to go back): ")

                    # Search for the county using the city name
                    if self.search_county_by_city(ask_user_city.strip().title()) is not None:
                        print(
                            f" County Seat(city) : {ask_user_city} \n"
                            f" license Plate Prefix : {self.search_county_by_city(ask_user_city.strip().title()).get_prefix()} "
                        )
                    # Allow the user to return to the main menu
                    elif ask_user_city.strip().title() == "Back":
                        print("Going back ...")
                        break
                    else:
                        print(f" County Seat(city) : {ask_user_city} has no license Plate Prefix in this Data")

            # Option 3: Display both county name and license plate prefix
            elif double_check == 3:
                while True:
                    ask_user_city = input("Please enter your County Seat(city)('Back' to to go back): ")

                    # Search for the county using the city name
                    if self.search_county_by_city(ask_user_city.strip().title()) is not None:
                        print(
                            f" County Seat(city) : {ask_user_city} \n"
                            f" County name : {self.search_county_by_city(ask_user_city.strip().title()).get_name()} \n"
                            f" license Plate Prefix : {self.search_county_by_city(ask_user_city.strip().title()).get_prefix()} "
                        )
                    # Allow the user to return to the main menu
                    elif ask_user_city.strip().title() == "Back":
                        print("Going back ...")
                        break
                    else:
                        print(f" County Seat(city) : {ask_user_city} has no license Plate Prefix or County in this Data")

    def search_county_by_city(self, city):
        """
        Searches for a county using the county seat (city).

        Args:
            city (str): The county seat name.

        Returns:
            County or None: The matching County object if found.
        """
        for county in self.county_arr:
            if county.city == city:
                return county
        return None

    def search_county_by_prefix(self, prefix):
        """
        Searches for a county using the license plate prefix.

        Args:
            prefix (str): The license plate prefix.

        Returns:
            County or None: The matching County object if found.
        """
        for county in self.county_arr:
            if county.prefix == prefix:
                return county
        return None


# Program entry point
if __name__ == '__main__':
    challenge01 = Challenge02()
    challenge01.run_program()

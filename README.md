# Challenge02 – Montana County Lookup

A **console-based Python application** that allows users to search Montana counties
using a **county seat (city)**. Users can choose to display the **county name**,
**license plate prefix**, or **both** through a simple menu-driven interface.

This project demonstrates:
- Object-Oriented Programming (OOP)
- File I/O with CSV files
- Input validation
- Menu-based program flow

---

## Project Structure

```
├── src/
│   ├── challenge02.py        # Main program logic and user interface
│   └── county.py             # County class definition
├── doc/
│   └── MontanaCounties.csv   # CSV file containing county data
└── README.md                 # Project documentation
```
---

## How the Program Works

1. The program loads Montana county data from a CSV file.
2. The user is presented with a menu of options:
   - Display county name
   - Display license plate prefix
   - Display both county name and license plate prefix
   - Quit the program
3. The user enters a **county seat (city)**.
4. The program searches the data and displays the requested information.

---

## How to Run

### Requirements
- Python **3.10 or higher**

### Steps

1. Clone or download the project files.
2. Ensure `MontanaCounties.csv` is located inside the `doc/` folder.
3. Navigate to the `src/` directory.
4. Run the program from the terminal:

```
python src/challenge_02.py
```

---

## Sample Output

WELCOME TO THE CHALLENGE 02
1. Display County name
2. Display License Plate Prefix
3. Display both County and License Plate Prefix
4. Quit Program

Please enter your County Seat (city):

---

## Classes

### County
Represents a Montana county with:
- County name
- County seat (city)
- License plate prefix

### Challenge02
Handles:
- Loading data from the CSV file
- User interaction and menu system
- Searching counties by county seat (city)

---

## Author

Andrias Zelele  
Computer Science Student

---

## Notes

- License plate prefixes range from **1–56**
- Input validation prevents invalid menu selections
- Designed for academic and educational use

---

## Purpose

This project is intended for **academic and educational purposes only**.
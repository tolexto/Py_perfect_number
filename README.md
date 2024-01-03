# Perfect Number Checker Application
---
made by Tuna MEYDAN a.k.a. tolexto
## Overview
---
This Python application is designed to find perfect numbers. A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself. The Perfect Number Checker allows users to input a range and identifies all perfect numbers within that range.

## Features & Modes
---
- **Perfect Number Identification:** The application calculates, is the number you give a perfect number or not. To use this mode, press **A** and **enter** in the bash when you ran the app.
- **Range Input:** Users can specify the range within which they want to find perfect numbers from 1 to desired number range. To use this mode, press **B** and **enter** in the bash when you ran the app.
- **User-Friendly Interface:** The application provides a simple and intuitive command-line interface for user interaction.

## Getting Started
---
1. **Prerequisites:**
   - Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/tolexto/Py_perfect_number.git
3. **Navigate to the Project Directory:**
   ```bash
   cd Py_perfect_number
4. **Run the Application:**
   ```bash
   python perfect_number_finder.py
   
## Usage
---
1. **Choose a Mode:**
    - Choose a mode for;
        - **a** mode, only if the number you are given is a perfect number or not,
        - **b** mode, all perfect numbers up to the number you give,
        will be checked.
2. **Input Range:**
   - When prompted, enter the range within which you want to find perfect numbers. For example, you can input "100" to find perfect numbers between 1 and 100.
3. **View Results:**
    - The application will display all the perfect numbers found within the specified range.
4. **Repeat or Exit:**-
    - You can choose to find perfect numbers in another range or exit the application.
    
## Example
---
    $ python Perfect_number.py
    a or b:

    Tip: c for exit :)
    a
    insert num: 6
    Number: 6       Divider: 1      Remainder: 0    Success!
    Number: 6       Divider: 2      Remainder: 0    Success!
    Number: 6       Divider: 3      Remainder: 0    Success!
    Number: 6       Divider: 4      Remainder: 2    Not Success!
    Number: 6       Divider: 5      Remainder: 1    Not Success!
    exact divisors  [1, 2, 3]
    6 = 6 Perfect Number!
    Let's Try Again!


    a or b:

    Tip: c for exit :)

## Contributing
---
If you would like to contribute to the development of this Perfect Number Finder application, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear and concise messages.
4. Push your changes to your fork.
5. Submit a pull request, explaining the changes you made.

## License
---
This Perfect Number Finder application is open-source software licensed under the MIT License. Feel free to use, modify, and distribute it as per the terms of the license.



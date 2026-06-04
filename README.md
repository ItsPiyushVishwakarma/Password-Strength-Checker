# Password Strength Checker

A simple Python-based Password Strength Checker that evaluates the strength of a password based on common security requirements.

## Features

* Checks password length
* Checks for uppercase letters
* Checks for lowercase letters
* Checks for numbers
* Checks for special characters
* Generates a password strength score (0–100%)
* Displays a visual strength bar
* Shows missing security requirements
* Categorizes passwords as Weak, Medium, or Strong

## Technologies Used

* Python 3

## How It Works

The program analyzes the entered password and awards points for:

* Minimum 8 characters
* At least one uppercase letter
* At least one lowercase letter
* At least one number
* At least one special character

Each requirement contributes to the overall strength score.

## Example Output

### Weak Password

Input:

piyush

Output:

Password Strength: Weak Password

[████----------------] 40%

Missing Requirements:

* Uppercase letter
* Number
* Special Character

### Medium Password

Input:

Piyush123

Output:

Password Strength: Medium Password

[████████████████----] 80%

Missing Requirements:

* Special Character

### Strong Password

Input:

Piyush@123

Output:

Password Strength: Strong Password

[████████████████████] 100%

## Project Structure

Password-Strength-Checker/

├── Password_strength_checker.py

├── README.md

└── screenshots/

```
├── Running_Code.png

└── Output.png
```

## Learning Outcomes

Through this project, I learned:

* Python functions
* Conditional statements
* Loops
* String methods
* Lists
* Return values
* Basic cybersecurity password policies
* Building practical security tools with Python

## Author

Piyush Vishwakarma

Cybersecurity Student | Python Learner | Aspiring SOC Analyst

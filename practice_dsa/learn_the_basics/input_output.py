"""
This module explains the basic input/output operations in Python.
Practice link: https://practice.geeksforgeeks.org/problems/search-query-auto-complete/0?category%5B%5D=Strings&category%5B%5D=Strings&problemStatus=unsolved&difficulty%5B%5D=2&page=1&query=category%5B%5DStringsproblemStatusunsolveddifficulty%5B%5D2page1category%5B%5DStr
Following: https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/
"""

def output_format():
    year = 2024
    date = 19
    month = "February"

    # Using f-string
    print(f"The date is {date} {month} {year}")

    # Using format method
    Yes = 42_574_567
    No = 2_173_567

    percentage = (Yes / (Yes + No)) * 100
    print("Yes: {0} No: {1} Percentage: {2:.2f}%".format(Yes, No, percentage))
    # .2f is used to print only 2 decimal places


def main():
    output_format()

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Living presidents

@author: Breno Jamal
@date: 03/12/2024
"""

from collections import defaultdict


def alive_presidents(filename: str, year: int) -> list[str]:
    presidents = set() # Store living presidents names
    with open(filename, 'r', encoding='utf8') as file: # Read the file with president data
        for line in file:
            words=line.strip().split() # Split the line into words
            if words[-2].isdigit() and int(words[-2])<= year <= int(words[-1]): # Check if the president was alive
                presidents.add(" ".join(words[:-2]))
            elif  not(words[-2].isdigit()) and int(words[-1])<= year : 
                presidents.add(" ".join(words[:-1])) # Check if the president was alive in that date and no death
    return sorted(list(presidents),key=lambda x: (x.split()[-1], x.split()[:-1])) # Sort presidents by last name, then first name

def main():
    """Main function"""
    for filename, year, expected in [
        (
            "presidents.txt",
            1776,
            [
                "John Adams",
                "John Quincy Adams",
                "William Henry Harrison",
                "Andrew Jackson",
                "Thomas Jefferson",
                "James Madison",
                "James Monroe",
                "George Washington",
            ],
        ),
        (
            "presidents.txt",
            1800,
            [
                "John Adams",
                "John Quincy Adams",
                "James Buchanan",
                "Martin Van Buren",
                "Millard Fillmore",
                "William Henry Harrison",
                "Andrew Jackson",
                "Thomas Jefferson",
                "James Madison",
                "James Monroe",
                "James K. Polk",
                "Zachary Taylor",
                "John Tyler",
            ],
        ),
        (
            "presidents.txt",
            1822,
            [
                "John Adams",
                "John Quincy Adams",
                "James Buchanan",
                "Martin Van Buren",
                "Millard Fillmore",
                "Ulysses S. Grant",
                "William Henry Harrison",
                "Rutherford B. Hayes",
                "Andrew Jackson",
                "Thomas Jefferson",
                "Andrew Johnson",
                "Abraham Lincoln",
                "James Madison",
                "James Monroe",
                "Franklin Pierce",
                "James K. Polk",
                "Zachary Taylor",
                "John Tyler",
            ],
        ),
        (
            "presidents.txt",
            1865,
            [
                "Chester A. Arthur",
                "James Buchanan",
                "Grover Cleveland",
                "Millard Fillmore",
                "James A. Garfield",
                "Ulysses S. Grant",
                "Warren G. Harding",
                "Benjamin Harrison",
                "Rutherford B. Hayes",
                "Andrew Johnson",
                "Abraham Lincoln",
                "William McKinley",
                "Franklin Pierce",
                "Theodore Roosevelt",
                "William Howard Taft",
                "Woodrow Wilson",
            ],
        ),
        (
            "presidents.txt",
            1913,
            [
                "Calvin Coolidge",
                "Dwight D. Eisenhower",
                "Gerald Ford",
                "Warren G. Harding",
                "Herbert Hoover",
                "Lyndon B. Johnson",
                "Richard Nixon",
                "Ronald Reagan",
                "Franklin D. Roosevelt",
                "Theodore Roosevelt",
                "William Howard Taft",
                "Harry S. Truman",
                "Woodrow Wilson",
            ],
        ),
        (
            "presidents.txt",
            1946,
            [
                "Joe Biden",
                "George H. W. Bush",
                "George W. Bush",
                "Jimmy Carter",
                "Bill Clinton",
                "Dwight D. Eisenhower",
                "Gerald Ford",
                "Herbert Hoover",
                "Lyndon B. Johnson",
                "John F. Kennedy",
                "Richard Nixon",
                "Ronald Reagan",
                "Harry S. Truman",
                "Donald Trump",
            ],
        ),
        (
            "presidents.txt",
            2000,
            [
                "Joe Biden",
                "George H. W. Bush",
                "George W. Bush",
                "Jimmy Carter",
                "Bill Clinton",
                "Gerald Ford",
                "Barack Obama",
                "Ronald Reagan",
                "Donald Trump",
            ],
        ),
        (
            "presidents.txt",
            2022,
            [
                "Joe Biden",
                "George W. Bush",
                "Jimmy Carter",
                "Bill Clinton",
                "Barack Obama",
                "Donald Trump",
            ],
        ),
    ]:
        try:
            result = alive_presidents(filename, year)
            assert (
                result == expected
            ), f"{expected} were alive in {year}, but {result} was returned instead"
        except AssertionError as a_err:
            print(a_err)

    for year in [1776, 1800, 1822, 1865, 1913, 1946, 2000, 2022]:
        result = alive_presidents("presidents.txt", year)
        print(f"{len(result)} presidents were alive in {year}")


if __name__ == "__main__":
    main()

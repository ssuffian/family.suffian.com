#!/usr/bin/env python3
"""
Calculate age in quarters since birth date and update the JSON file.
"""
import json
import sys
from datetime import date
from pathlib import Path

BIRTH_DATE = date(2024, 3, 26)
JSON_FILE = Path(__file__).parent.parent / "data" / "ages.json"


def calculate_age_in_quarters(birth_date: date, today: date) -> str:
    """Calculate age in quarters and return as formatted string."""
    # Calculate difference in days
    days_diff = (today - birth_date).days
    
    # Calculate years
    years = days_diff / 365.25
    
    # Round to nearest quarter
    quarters = round(years * 4)
    age_decimal = quarters / 4
    
    # Format as string (e.g., "1", "1 1/4", "1 1/2", "1 3/4")
    whole = int(age_decimal)
    decimal = age_decimal - whole
    
    if decimal == 0:
        age_str = str(whole)
    elif decimal == 0.25:
        age_str = "1/4" if whole == 0 else f"{whole} 1/4"
    elif decimal == 0.5:
        age_str = "1/2" if whole == 0 else f"{whole} 1/2"
    elif decimal == 0.75:
        age_str = "3/4" if whole == 0 else f"{whole} 3/4"
    else:
        age_str = str(age_decimal)
    
    return age_str


def main():
    """Main function to update the age JSON file."""
    today = date.today()
    age_str = calculate_age_in_quarters(BIRTH_DATE, today)
    
    # Update JSON file
    data = {"approximateAge": age_str}
    JSON_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    
    print(f"Updated age to: {age_str} years")
    print(f"Age in decimal: {calculate_age_in_quarters(BIRTH_DATE, today)}")
    
    # Output for GitHub Actions
    if len(sys.argv) > 1 and sys.argv[1] == "--output":
        print(f"::set-output name=age_str::{age_str}")
    
    return age_str


if __name__ == "__main__":
    main()


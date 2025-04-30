# W06 Project: Life Expectancy Data Analysis
# Author: Blessing Glory Tsikey

# Features:
#Load and read the life-expectancy.csv file.
#Iterate through the dataset line by line.
#Find the overall minimum life expectancy value (with country and year).
#Find the overall maximum life expectancy value (with country and year).
#Prompt the user to enter a year of interest, and calculates the minimum and maximum life expectancy for that year.Prompt the user to enter a country of interest.

#Added Features
# For the entered country:
# Calculate the average life expectancy.
# Determine the maximum life expectancy.
# Determine the minimum life expectancy.

file_path = r"C:\Users\user\Downloads\life-expectancy.csv"

min_life = float('inf')
max_life = float('-inf')
min_country = ""
max_country = ""
min_year = ""
max_year = ""

year_of_interest = input("Enter the year of interest: ")

year_life_values = []
year_min_life = float('inf')
year_max_life = float('-inf')
year_min_country = ""
year_max_country = ""

# Creativity feature - ask user for country
country_of_interest = input("Enter the country of interest: ").capitalize()

country_life_values = []
country_min = float('inf')
country_max = float('-inf')

with open(file_path, "r") as file:
    next(file)
    for line in file:
        parts = line.strip().split(",")
        country = parts[0]
        code = parts[1]
        year = parts[2]
        life_exp = parts[3]

        if life_exp == "":
            continue

        life_exp = float(life_exp)

        if life_exp < min_life:
            min_life = life_exp
            min_country = country
            min_year = year

        if life_exp > max_life:
            max_life = life_exp
            max_country = country
            max_year = year

        if year == year_of_interest:
            year_life_values.append(life_exp)

            if life_exp < year_min_life:
                year_min_life = life_exp
                year_min_country = country

            if life_exp > year_max_life:
                year_max_life = life_exp
                year_max_country = country

        if country.lower() == country_of_interest.lower():
            country_life_values.append(life_exp)
            if life_exp < country_min:
                country_min = life_exp
            if life_exp > country_max:
                country_max = life_exp

print()
print(f"The overall max life expectancy is: {max_life} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_life} from {min_country} in {min_year}")
print()

if year_life_values:
    average_life = sum(year_life_values) / len(year_life_values)
    print(f"For the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {average_life:.2f}")
    print(f"The max life expectancy was in {year_max_country} with {year_max_life}")
    print(f"The min life expectancy was in {year_min_country} with {year_min_life}")
else:
    print(f"No data found for the year {year_of_interest}.")

print()
if country_life_values:
    country_avg = sum(country_life_values) / len(country_life_values)
    print(f"For the country {country_of_interest.capitalize()}:")
    print(f"The average life expectancy was {country_avg:.2f}")
    print(f"The maximum life expectancy was {country_max}")
    print(f"The minimum life expectancy was {country_min}")
else:
    print(f"No data found for the country {country_of_interest}.")

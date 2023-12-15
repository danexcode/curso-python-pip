import matplotlib.pyplot as plt

import read_csv as csv
import charts

data = csv.read_csv("./data.csv")


def find_country(country):
    for country_data in data:
        if country_data["Country/Territory"] == country:
            return country_data
    raise Exception("Country not found")


def extract_country_data(country):
    country_data = find_country(country)

    population_by_year = {
        "1970": country_data["1970 Population"],
        "1980": country_data["1980 Population"],
        "1990": country_data["1990 Population"],
        "2000": country_data["2000 Population"],
        "2010": country_data["2010 Population"],
        "2015": country_data["2015 Population"],
        "2020": country_data["2020 Population"],
        "2022": country_data["2022 Population"],
    }

    labels = list(population_by_year.keys())
    values = list(population_by_year.values())

    return labels, values


if __name__ == "__main__":
    try:
        country = input('Ingresa el pais => ')
        labels, values = extract_country_data(country)
        charts.generate_bar_chart(country, labels, values)
    except Exception as error:
        print(error)

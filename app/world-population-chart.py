import read_csv as csv
import charts as chart


def world_population_chart():
    data = csv.read_csv("./data.csv")
    data = list(filter(lambda country: country["Continent"] == "South America", data))

    labels = [country["Country/Territory"] for country in data]
    values = [country["World Population Percentage"] for country in data]

    chart.generate_pie_chart('world', labels, values)


if __name__ == "__main__":
    world_population_chart()

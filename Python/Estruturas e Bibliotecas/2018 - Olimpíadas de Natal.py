"""
Autor: Pierre Vieira
Data da submissão: 15/02/2022 23:49:47
"""


class Medals:
    def __init__(self):
        self.gold = self.silver = self.bronze = 0

    def up_gold(self):
        self.gold += 1

    def up_silver(self):
        self.silver += 1

    def up_bronze(self):
        self.bronze += 1

    def __eq__(self, other):
        return self.gold == self.silver == self.bronze

    def __str__(self):
        return f'{self.gold} {self.silver} {self.bronze}'

    def __repr__(self):
        return self.__str__()


class Country:
    def __init__(self, name: str):
        self.medals = Medals()
        self.name = name

    def __lt__(self, other: "Country"):
        if self.medals.gold != other.medals.gold:
            return self.medals.gold < other.medals.gold
        if self.medals.silver != other.medals.silver:
            return self.medals.silver < other.medals.silver
        if self.medals.bronze != other.medals.bronze:
            return self.medals.bronze < other.medals.bronze
        return self.name > other.name

    def __gt__(self, other: "Country"):
        if self.medals.gold != other.medals.gold:
            return self.medals.gold > other.medals.gold
        if self.medals.silver != other.medals.silver:
            return self.medals.silver > other.medals.silver
        if self.medals.bronze != other.medals.bronze:
            return self.medals.bronze > other.medals.bronze
        return self.name < other.name

    def __eq__(self, other: "Country"):
        return self.name == other.name

    def __str__(self):
        return f'{self.name} {str(self.medals)}'

    def __repr__(self):
        return self.__str__()


class Tournament:
    def __init__(self):
        self.countries: list[Country] = []

    def add_country(self, country: Country):
        if country in self.countries:
            index_country = self.countries.index(country)
            stored_country = self.countries[index_country]
            stored_country.medals.gold += country.medals.gold
            stored_country.medals.silver += country.medals.silver
            stored_country.medals.bronze += country.medals.bronze
            self.countries[index_country] = stored_country
        else:
            self.countries.append(country)

    def output(self):
        sorted_countries = sorted(self.countries, reverse=True)
        print('Quadro de Medalhas')
        for country in sorted_countries:
            print(str(country))


def main():
    tournament = Tournament()
    while True:
        try:
            input()
            country_gold_name = input()
            country_silver_name = input()
            country_bronze_name = input()
            country_gold = Country(country_gold_name)
            country_gold.medals.up_gold()
            country_silver = Country(country_silver_name)
            country_silver.medals.up_silver()
            country_bronze = Country(country_bronze_name)
            country_bronze.medals.up_bronze()
            tournament.add_country(country_gold)
            tournament.add_country(country_silver)
            tournament.add_country(country_bronze)
        except EOFError:
            break
    tournament.output()


if __name__ == '__main__':
    main()

import click
from done.services import analytictools


@click.group()
def cli():
    """Analyse your Habits"""
    pass


@cli.command()
def returnHabits():
    """returns all habits and all information"""
    print("This is a place holder for return returnAllHabits")
    analytictools.returnAllHabits()


@cli.command()
@click.argument("name")
def returnLongestStreak(name: str):
    print("This is a place holder for return returnLongestStreak")
    print(name)


@cli.command()
@click.argument("name")
def returnGivenStreak(name: str):
    print("This is a place holder for return returnGivenStreak")
    print(name)


@cli.command()
@click.argument("periodicity")
def returnHabitSamePeridocity(periodicity: int):
    print("This is a place holder for return returnHabitSamePeridocity")
    print(periodicity)
    print(type(periodicity))

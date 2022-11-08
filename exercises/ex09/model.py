"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730609760" 


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, object: Point) -> float:
        """Returns the distance between two cells."""
        return sqrt((self.x - object.x)**2 + (self.y - object.y)**2)


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Runs on every "tic" of the clock."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def contract_disease(self) -> None:
        """Gives cell infected variable."""
        self.sickness = constants.INFECTED

    def immunize(self) -> None:
        """Gives recovered cell immunized variable."""
        self.sickness = constants.IMMUNE

    def is_vulnerable(self) -> bool:
        """Tests if a cell can still get sick."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Tests if a cell is sick."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
    
    def is_immune(self) -> bool:
        """Tests if a cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "red"
        elif self.is_immune():
            return "pink"
        return "gray"

    def contact_with(self, object: Cell) -> None:
        """Passes sickness between touching cells."""
        if self.is_vulnerable() and object.is_infected():
            self.contract_disease()
        if self.is_infected() and object.is_vulnerable():
            object.contract_disease()


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_cells: int, immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        if infected_cells >= cells or infected_cells <= 0:
            raise ValueError("Some cells must begin as infected or vulnerable.")
        if immune_cells >= cells or immune_cells < 0:
            raise ValueError("Some cells must begin as infected or vulnerable.")
        if infected_cells + immune_cells >= cells:
            raise ValueError("Inappriate amount of infected and/or immune cells.")
        self.population = []
        for _ in range(cells - (infected_cells + immune_cells)):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            cell.is_vulnerable()
            self.population.append(cell)
        for _ in range(infected_cells):
            start_location_infected: Point = self.random_location()
            start_direction_infected: Point = self.random_direction(speed)
            infected_cell: Cell = Cell(start_location_infected, start_direction_infected)
            infected_cell.contract_disease()
            infected_cell.is_infected()
            self.population.append(infected_cell)
        for _ in range(immune_cells):
            start_location_immune: Point = self.random_location()
            start_direction_immune: Point = self.random_direction(speed)
            immune_cell: Cell = Cell(start_location_immune, start_direction_immune)
            immune_cell.immunize()
            immune_cell.is_immune()
            self.population.append(immune_cell)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.color()
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Checks if any two cells are touching."""
        i: int = 0
        b: int
        while i < len(self.population):
            b = i + 1
            while b < len(self.population):
                if self.population[i].location.distance(self.population[b].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[b])
                b += 1
            i += 1
                    
    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        i: int = 0
        while i < len(self.population):
            if self.population[i].is_infected():
                return False
            i += 1
        return True
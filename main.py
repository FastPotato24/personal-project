import rich
from rich import print
from rich.layout import Layout
from rich.panel import Panel
import numpy as np


class Board:
    def __init__(self, size: tuple[int, int]):
        self.grid = np.asarray([[None for _ in range(size[0])]
                               for _ in range(size[1])])

        # Initiate Card Layout
        self.layout = Layout(name="Window")
        self.layout.split_column(
            Layout(name="Spacer", size=2),
            Layout(name="Board"),
            Layout(name="UI")
        )
        self.layout["Board"].split_column(
            Layout(name="y0"),
            Layout(name="y1")
        )
        for y in range(len(self.grid)):
            if y >= 2:
                self.layout["Board"].add_split(
                    Layout(name=f"y{y}")
                )
            for x in range(len(self.grid[y])):
                if x == 0:
                    self.layout[f"y{y}"].split_row(
                        Layout(name=f"(0,{y})"),
                        Layout(name=f"(1,{y})")
                    )
                elif x >= 2:
                    self.layout[f"y{y}"].add_split(
                        Layout(name=f"({x},{y})")
                    )

    def render(self):
        for y, column in enumerate(self.grid):
            for x, card in enumerate(column):
                self.layout[f"({x},{y})"].update(
                    renderable=card.panel(
                        self) if card is not None else Panel(" ")
                )
        print(self.layout)


class Card:
    def __init__(self, name: str, stats: tuple[int | None, int | None]):
        self.name = name
        self.power = stats[0]
        self.health = stats[1]

    def panel(self, board) -> Panel:
        console = rich.get_console()
        width = console.width
        space = (width - 6*len(board.grid[0]))//len(board.grid[0]) - 4
        return Panel(" ", title=self.name, subtitle=f"{self.power} {'─'*space} {self.health} ")


class Encounter:
    def __init__(self, board: Board, totem: str | None = None):
        self.turns = 0
        self.currentBoard = board
        self.totem = totem
        self.bottomRow = self.currentBoard.grid[len(self.currentBoard.grid)-1]

    def endTurn(self):
        for card in self.bottomRow:
            pass  # TODO: Cards act here


test = Board((4, 3))
test.grid[0, 1] = Card("Stoat", (1, 1))
test.render()

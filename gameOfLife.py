from itertools import product


class GameOfLife:
    _cells = set()

    def __init__(self):
        self._cells = set()

    def set_alive(self, x, y):
        self._cells.add((x, y))

    def set_dead(self, x, y):
        if (x, y) in self._cells:
            self._cells.remove((x, y))

    def is_alive(self, x, y):
        return (x, y) in self._cells

    def tick(self):
        next_generation_cells = set()
        checked_cells = set()
        for cell_x, cell_y in self._cells:
            for x, y in product(range(cell_x - 1, cell_x + 2), range(cell_y - 1, cell_y + 2)):
                if (x, y) not in checked_cells:
                    checked_cells.add((x, y))
                    if self.tick_cell(x, y):
                        next_generation_cells.add((x, y))

        self._cells = next_generation_cells

    def tick_cell(self, x, y):
        neighbours = set([(neighbour_x, neighbour_y)
                          for neighbour_x, neighbour_y
                          in product(range(x - 1, x + 2),
                                     range(y - 1, y + 2))])
        neighbours.remove((x, y))

        live_neighbours = len(self._cells & neighbours)

        if self.is_alive(x, y):
            return 2 <= live_neighbours <= 3
        else:
            return live_neighbours == 3

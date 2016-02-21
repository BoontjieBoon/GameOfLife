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
        # set that contains new generation
        next_generation_cells = set()
        # set to keep track of cell have already
        # been checked for the next generation
        checked_cells = set()

        for cell_x, cell_y in self._cells:
            # check all cell's neighbours for the next
            # generation because they might become alive
            for x, y in product(range(cell_x - 1, cell_x + 2), range(cell_y - 1, cell_y + 2)):
                # skip already checked cells to save on processing
                if (x, y) not in checked_cells:
                    checked_cells.add((x, y))
                    # add cell to next generation if it lives
                    if self.tick_cell(x, y):
                        next_generation_cells.add((x, y))

        self._cells = next_generation_cells

    def tick_cell(self, x, y):
        # create set with neighbour positions
        neighbours = set([(neighbour_x, neighbour_y)
                          for neighbour_x, neighbour_y
                          in product(range(x - 1, x + 2),
                                     range(y - 1, y + 2))])
        # remove cell itself
        neighbours.remove((x, y))

        # and-ing the _cells and neighbours sets
        # gives us a set of live neighbour cells
        live_neighbours = len(self._cells & neighbours)

        if self.is_alive(x, y):
            # cell should only keep living with 2 or 3 neighbours
            return 2 <= live_neighbours <= 3
        else:
            # cell should only become alive with exactly 3 neighbours
            return live_neighbours == 3

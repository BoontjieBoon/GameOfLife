from itertools import product


class GameOfLife:
    _cells = set()
    _view_width = 5
    _view_height = 5

    @property
    def width(self):
        return len(self._cells[0])

    @property
    def height(self):
        return len(self._cells)

    def __init__(self):
        self._cells = set()
        pass

    def __repr__(self):
        world_string = ['.' * self._view_width] * self._view_height
        for x, y in self.cell_iter():
            if self.is_alive(x, y):
                world_string[x - 1] = world_string[x - 1][:y - 1] + '*' + world_string[x - 1][y:]
        return '\n'.join(world_string) + '\n\n'

    def set_alive(self, x_coord, y_coord):
        self._cells.add((x_coord, y_coord))

    def set_dead(self, x_coord, y_coord):
        if (x_coord, y_coord) in self._cells:
            self._cells.remove((x_coord, y_coord))

    def is_alive(self, x_coord, y_coord):
        return (x_coord, y_coord) in self._cells

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

    def tick_cell(self, x_coord, y_coord):
        neighbours = set([(x, y)
                         for x, y in product(range(x_coord - 1, x_coord + 2),
                                             range(y_coord - 1, y_coord + 2))])
        neighbours.remove((x_coord, y_coord))

        live_neighbours = len(self._cells & neighbours)

        if self.is_alive(x_coord, y_coord):
            return 2 <= live_neighbours <= 3
        else:
            return live_neighbours == 3

        return False

    def cell_iter(self):
        for x, y in product(range(self._view_width), range(self._view_height)):
            yield x + 1, y + 1

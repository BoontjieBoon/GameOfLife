from itertools import product


class GameOfLife:
    _cells = []

    @property
    def width(self):
        return len(self._cells[0])

    @property
    def height(self):
        return len(self._cells)

    def __init__(self):
        pass

    def __repr__(self):
        world_string = ['.' * self.width] * self.height
        for x, y in self.cell_iter():
            if self.is_alive(x, y):
                world_string[x - 1] = world_string[x - 1][:y - 1] + '*' + world_string[x - 1][y:]
        return '\n'.join(world_string) + '\n\n'

    def set_alive(self, x_coord, y_coord):
        self.set_cell(x_coord, y_coord, True)

    def set_dead(self, x_coord, y_coord):
        self.set_cell(x_coord, y_coord, False)

    def set_cell(self, x_coord, y_coord, alive):
        if x_coord <= 0 or y_coord <= 0:
            raise OutOfBoundsError
        else:
            try:
                self._cells[x_coord - 1][y_coord - 1] = alive
            except IndexError:
                raise OutOfBoundsError

    def is_alive(self, x_coord, y_coord):
        try:
            return self._cells[x_coord - 1][y_coord - 1]
        except IndexError:
            return False

    def tick(self):
        next_gen_cells = GameOfLife._empty_world(self.width, self.height)
        for x, y in self.cell_iter():
            next_gen_cells[x - 1][y - 1] = self.tick_cell(x, y)
        self._cells = next_gen_cells

    def tick_cell(self, x_coord, y_coord):
        live_neighbours = 0
        for x, y in product(range(x_coord - 1, x_coord + 2), range(y_coord - 1, y_coord + 2)):
            if x != x_coord or y != y_coord:
                if self.is_alive(x, y):
                    live_neighbours += 1
                    if live_neighbours > 3:
                        break

        if self.is_alive(x_coord, y_coord):
            return 2 <= live_neighbours <= 3
        else:
            return live_neighbours == 3

        return False

    def cell_iter(self):
        for x, y in product(range(self.width), range(self.height)):
            yield x + 1, y + 1

    @staticmethod
    def _empty_world(width, height):
        return [[False] * width for i in range(height)]


class OutOfBoundsError(Exception):
    def __init__(self):
        pass

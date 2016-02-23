import unittest
from gameOfLife import GameOfLife


class TestClass(unittest.TestCase):
    def test_set_cell_state(self):
        game = GameOfLife()
        game.set_alive(1, 1)
        self.assertTrue(game.is_alive(1, 1), "Cell should be alive")
        game.set_dead(1, 1)
        self.assertFalse(game.is_alive(1, 1), "Cell should be dead")
        game.set_alive(1000, 1000)
        self.assertTrue(game.is_alive(1000, 1000), "Cell should be alive")
        game.set_dead(1000, 1000)
        self.assertFalse(game.is_alive(1000, 1000), "Cell should be dead")

    def test_set_parameters_are_integers(self):
        game = GameOfLife()
        self.assertRaises(TypeError, game.set_alive, 0.5, 1)
        self.assertRaises(TypeError, game.set_alive, 1, 0.5)
        self.assertRaises(TypeError, game.is_alive, 0.5, 1)
        self.assertRaises(TypeError, game.is_alive, 1, 0.5)
        self.assertRaises(TypeError, game.set_dead, 0.5, 1)
        self.assertRaises(TypeError, game.set_dead, 1, 0.5)

    def test_cell_dies_with_no_neighbours(self):
        game = GameOfLife()
        game.set_alive(3, 3)
        self.assertTrue(game.is_alive(3, 3), "Cell should be alive before the tick")
        game.tick()
        self.assertFalse(game.is_alive(3, 3), "Cell should die with no neighbours")

    def test_cell_dies_with_one_neighbour(self):
        game = GameOfLife()
        game.set_alive(3, 3)
        game.set_alive(4, 4)
        self.assertTrue(game.is_alive(3, 3), "Cell should be alive before the tick")
        game.tick()
        self.assertFalse(game.is_alive(3, 3), "Cell should die with one neighbour")

    def test_cell_lives_with_two_neighbours(self):
        game = GameOfLife()
        game.set_alive(3, 3)
        game.set_alive(4, 4)
        game.set_alive(2, 3)
        self.assertTrue(game.is_alive(3, 3), "Cell should be alive before the tick")
        game.tick()
        self.assertTrue(game.is_alive(3, 3), "Cell should survive with two neighbours")

    def test_cell_lives_with_three_neighbours(self):
        game = GameOfLife()
        game.set_alive(3, 3)
        game.set_alive(4, 4)
        game.set_alive(2, 3)
        game.set_alive(4, 3)
        self.assertTrue(game.is_alive(3, 3), "Cell should be alive before the tick")
        game.tick()
        self.assertTrue(game.is_alive(3, 3), "Cell should survive with three neighbours")

    def test_cell_dies_with_more_than_three_neighbours(self):
        game = GameOfLife()
        game.set_alive(3, 3)
        game.set_alive(4, 4)
        game.set_alive(2, 3)
        game.set_alive(4, 3)
        game.set_alive(3, 4)
        self.assertTrue(game.is_alive(3, 3), "Cell should be alive before the tick")
        game.tick()
        self.assertFalse(game.is_alive(3, 3), "Cell should die with four or more neighbours")

    def test_cell_becomes_alive_with_three_neighbours(self):
        game = GameOfLife()
        game.set_alive(4, 4)
        game.set_alive(2, 3)
        game.set_alive(4, 3)
        self.assertFalse(game.is_alive(3, 3), "Cell should be dead before the tick")
        game.tick()
        self.assertTrue(game.is_alive(3, 3), "Cell should become alive with three neighbours")

    def test_cell_stays_dead_with_two_neighbours(self):
        game = GameOfLife()
        game.set_alive(4, 4)
        game.set_alive(2, 3)
        self.assertFalse(game.is_alive(3, 3), "Cell should be dead before the tick")
        game.tick()
        self.assertFalse(game.is_alive(3, 3), "Cell should not become alive with two neighbours")

    def test_cell_stays_dead_with_four_neighbours(self):
        game = GameOfLife()
        game.set_alive(4, 4)
        game.set_alive(2, 3)
        game.set_alive(4, 3)
        game.set_alive(3, 4)
        self.assertFalse(game.is_alive(3, 3), "Cell should be dead before the tick")
        game.tick()
        self.assertFalse(game.is_alive(3, 3), "Cell should not become alive with four neighbours")

    # Any live cell with fewer than two live neighbours dies, as if caused by under-population.
    # Any live cell with two or three live neighbours lives on to the next generation.
    # Any live cell with more than three live neighbours dies, as if by over-population.
    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

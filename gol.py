from pprint import pprint

class Game(object):
    def __init__(self):
        """Currently initializes and looks something like this array:
           [[0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]]

        In the future, it would be nice to take in a starting set of positions.
        """

        self.live_cells = set([(1, 2), (2, 2), (3, 2)])

    def print_grid(self):
        """Pretty prints the current game state as as a 2D array, with live
        cells represented by value 1 vs dead cells with value 0."""
        # figure out how large the grid should be
        # generate the array and print
        # FIXME currently only prints a 5 by 5 grid

        grid = [[0 for cell in xrange(5)] for row in xrange(5)]

        for i, j in self.live_cells:
            grid[i][j] = 1

        pprint(grid)


    def regenerate(self):
        """Evaluates the game grid to yield next generation of live cells."""
        # FIXME adjust the grid to account for any negatives coordinate values
            # seems optional here, could just handle in printing the grid

        new_live_cells = set()

        for coords in self.live_cells | self.get_dead_candidates():
            if self.evaluate(coords):
                new_live_cells.add(coords)

        self.live_cells = new_live_cells

    def evaluate(self, coords):
        """Evaluates a cell to determine alive-ness for next generation.
        Returns True or False.

        The rules:
            For currently live cells:
                if live_neighbors < 2:
                    cell becomes dead
                if 2 <= live_neighbors <= 3:
                    cell becomes alive
                if live_neighbors > 3:
                    cell becomes dead
            For currently dead cells:
                if live_neighbors == 3:
                    cell becomes alive
        """

        if coords in self.live_cells:
            return 2 <= self.get_live_neighbors(coords) <= 3

        else:
            return self.get_live_neighbors(coords)== 3

    def get_live_neighbors(self, coords):
        """For a given cell, returns the number of live neighbors."""

        live_neighbors = 0

        for neighbor in self.get_possible_neighbors(coords):
            if neighbor in self.live_cells:
                live_neighbors += 1

        return live_neighbors

    def get_possible_neighbors(self, coords):
        """Returns the coordinates of a given cell's neighbors."""

        possible_neighbors = set()
        possible_rows = [coords[0] + i for i in xrange(-1, 2)]
        possible_columns = [coords[1] + i for i in xrange(-1, 2)]

        for i in possible_rows:
            for j in possible_columns:
                if (i, j) != coords:
                    possible_neighbors.add((i, j))

        return possible_neighbors

    def get_dead_candidates(self):
        """Returns the coordinates of dead cells that are next to live cells."""

        candidates = set()

        for coords in self.live_cells:
            for neighbor in self.get_possible_neighbors(coords):
                candidates.add(neighbor)

        return candidates - self.live_cells


if __name__ == "__main__":
    game = Game()
    print "Generation 1"
    game.print_grid()

    for g in xrange(2, 6):
        game.regenerate()

        print
        print "Generation", g
        game.print_grid()

from frontend.Cell import Cell, CellState


class Grid:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.cells = []
        for row in range(rows):
            row_cells = []
            for col in range(cols):
                row_cells.append(Cell(row, col, cell_size, CellState.AVAILABLE))
            self.cells.append(row_cells)

    def draw(self, screen):
        for row in self.cells:
            for cell in row:
                cell.draw(screen)

    def get_cell_at_pos(self, x, y):
        col = x // self.cell_size
        row = y // self.cell_size
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.cells[row][col]
        return None

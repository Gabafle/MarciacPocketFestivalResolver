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

    def can_place_element(self, row, col, element):
        """Vérifie si l'élément peut être placé à partir de (row, col)."""
        w = getattr(element, "width", 1)
        h = getattr(element, "height", 1)
        for dr in range(h):
            for dc in range(w):
                r, c = row + dr, col + dc
                if r >= self.rows or c >= self.cols:
                    return False
                if self.cells[r][c].state != CellState.AVAILABLE:
                    return False
        return True

    def place_element(self, row, col, element):
        """Place l'élément sur toutes les cases qu'il occupe."""
        if not self.can_place_element(row, col, element):
            return False
        w = getattr(element, "width", 1)
        h = getattr(element, "height", 1)
        for dr in range(h):
            for dc in range(w):
                r, c = row + dr, col + dc
                is_top_left = dr == 0 and dc == 0
                self.cells[r][c].occupy(element, is_top_left=is_top_left)
        return True

    def remove_element(self, element):
        """Libère toutes les cases occupées par l'élément."""
        for row in self.cells:
            for cell in row:
                if cell.occupant is element:
                    cell.set_available()

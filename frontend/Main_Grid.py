import pygame

from backend.structure.Chair import Chair
from frontend.Cell import CellState
from frontend.Grid import Grid


def main():
    pygame.init()

    rows, cols = 12, 12
    cell_size = 50
    width, height = cols * cell_size, rows * cell_size
    blocked_cells = [
        [0, 0],
        [0, 1],
        [0, 2],
        [0, 9],
        [0, 10],
        [0, 11],
        [1, 0],
        [1, 1],
        [1, 10],
        [1, 11],
        [2, 0],
        [2, 11],
        [9, 0],
        [9, 11],
        [10, 0],
        [10, 1],
        [10, 10],
        [10, 11],
        [11, 0],
        [11, 1],
        [11, 2],
        [11, 9],
        [11, 10],
        [11, 11],
    ]

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("12x12 Grid System")

    grid = Grid(rows, cols, cell_size)

    for cell in blocked_cells:
        grid.cells[cell[0]][cell[1]].block_cell()

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                cell = grid.get_cell_at_pos(x, y)
                if cell:
                    if cell.state == CellState.AVAILABLE:
                        cell.occupy(Chair())

        screen.fill((255, 255, 255))
        grid.draw(screen)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()

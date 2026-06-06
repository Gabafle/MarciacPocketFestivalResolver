import pygame
from backend.DefaultParty import DefaultParty
from backend.scoring.ScoreEngine import ScoreEngine
from frontend.Button import Button
from frontend.Grid import Grid
from frontend.ScorePanel import ScorePanel

# Palette
BLUE = (52, 120, 219)
BG_COLOR = (22, 26, 38)
GRID_OFFSET_X = 50
GRID_OFFSET_Y = 50
HINT_COLOR = (255, 220, 80)
PREVIEW_VALID = (100, 220, 100, 130)
PREVIEW_INVALID = (220, 80, 80, 130)


def draw_placement_preview(screen, grid, element, mx, my, offset_x, offset_y):
    """Aperçu translucide du bloc sous le curseur."""
    ax = mx - offset_x
    ay = my - offset_y
    cell = grid.get_cell_at_pos(ax, ay)
    if cell is None:
        return
    w = getattr(element, "width", 1)
    h = getattr(element, "height", 1)
    can = grid.can_place_element(cell.row, cell.col, element)
    color = PREVIEW_VALID if can else PREVIEW_INVALID
    surf = pygame.Surface((w * grid.cell_size, h * grid.cell_size), pygame.SRCALPHA)
    surf.fill(color)
    screen.blit(
        surf,
        (
            offset_x + cell.col * grid.cell_size,
            offset_y + cell.row * grid.cell_size,
        ),
    )


def main():
    pygame.init()

    rows, cols = 12, 12
    cell_size = 50
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

    grid_pixel_w = cols * cell_size
    grid_pixel_h = rows * cell_size

    # Layout : grille à gauche | boutons au centre | score à droite
    btn_panel_w = 320
    score_panel_w = 300
    margin = 20

    total_w = (
        GRID_OFFSET_X
        + grid_pixel_w
        + margin
        + btn_panel_w
        + margin
        + score_panel_w
        + margin
    )
    total_h = GRID_OFFSET_Y + grid_pixel_h + 250
    screen = pygame.display.set_mode((total_w, total_h))
    pygame.display.set_caption("Party Planner – Grid System")

    # Grille
    grid = Grid(rows, cols, cell_size)
    for cell in blocked_cells:
        grid.cells[cell[0]][cell[1]].block_cell()

    # Surface dédiée à la grille (pour gérer l'offset proprement)
    grid_surface = pygame.Surface((grid_pixel_w, grid_pixel_h))

    # Éléments
    party = DefaultParty().create()

    # Boutons
    btn_x = GRID_OFFSET_X + grid_pixel_w + margin
    buttons = []
    for i, element in enumerate(party.elements):
        label = f"{type(element).__name__}  {element.width}×{element.height}  [{element.score}pts]"
        buttons.append(
            Button(btn_x, GRID_OFFSET_Y + i * 42, btn_panel_w, 38, label, BLUE)
        )

    # Score
    score_x = btn_x + btn_panel_w + margin
    score_panel = ScorePanel(score_x, GRID_OFFSET_Y, score_panel_w, grid_pixel_h)
    engine = ScoreEngine(grid)

    selected_element = None
    font_hint = pygame.font.SysFont("Consolas", 13)
    running = True
    clock = pygame.time.Clock()

    while running:
        mx, my = pygame.mouse.get_pos()
        # Coordonnées relatives à la grille
        gx, gy = mx - GRID_OFFSET_X, my - GRID_OFFSET_Y

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                selected_element = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_button = False
                for i, button in enumerate(buttons):
                    if button.rect.collidepoint(mx, my):
                        selected_element = party.elements[i]
                        clicked_button = True
                        break

                if not clicked_button and selected_element:
                    cell = grid.get_cell_at_pos(gx, gy)
                    if cell:
                        placed = grid.place_element(
                            cell.row, cell.col, selected_element
                        )
                        if placed:
                            idx = party.elements.index(selected_element)
                            buttons.pop(idx)
                            party.elements.pop(idx)
                            selected_element = None

        # Recalcul du score à chaque frame
        score_data = engine.compute()
        score_panel.update(score_data)

        # Dessin
        screen.fill(BG_COLOR)

        # Grille sur sa surface dédiée
        grid_surface.fill(BG_COLOR)
        # Rediriger le draw de la grille vers grid_surface
        _orig_blit = screen.blit
        for row in grid.cells:
            for cell in row:
                # Dessiner sur grid_surface en recalculant la position
                import pygame as _pg

                from frontend.Cell import CellState as CS

                if cell.state == CS.BLOCKED:
                    c = (80, 85, 100)
                elif cell.state == CS.AVAILABLE:
                    c = (35, 42, 58)
                else:
                    c = cell._get_occupant_color()
                rx = cell.col * cell_size
                ry = cell.row * cell_size
                _pg.draw.rect(grid_surface, c, (rx, ry, cell_size, cell_size))
                _pg.draw.rect(
                    grid_surface, (55, 65, 90), (rx, ry, cell_size, cell_size), 1
                )

                # Nom de l'élément sur la cellule maître
                if cell.state == CS.OCCUPIED and cell.is_top_left and cell.occupant:
                    ew = getattr(cell.occupant, "width", 1)
                    eh = getattr(cell.occupant, "height", 1)
                    bw = ew * cell_size
                    bh = eh * cell_size
                    class_name = type(cell.occupant).__name__
                    fs = max(9, min(15, cell_size // 3))
                    fnt = _pg.font.SysFont("Consolas", fs, bold=True)
                    txt = fnt.render(class_name, True, (255, 255, 255))
                    grid_surface.blit(
                        txt,
                        (
                            rx + (bw - txt.get_width()) // 2,
                            ry + (bh - txt.get_height()) // 2,
                        ),
                    )

        screen.blit(grid_surface, (GRID_OFFSET_X, GRID_OFFSET_Y))

        # Aperçu placement
        if selected_element:
            draw_placement_preview(
                screen, grid, selected_element, mx, my, GRID_OFFSET_X, GRID_OFFSET_Y
            )

        # Boutons
        for button in buttons:
            button.draw(screen)

        # Score panel
        score_panel.draw(screen)

        # Hint bas de grille
        if selected_element:
            hint = font_hint.render(
                f"Placement : {type(selected_element).__name__} "
                f"({selected_element.width}×{selected_element.height}) | ESC pour annuler",
                True,
                HINT_COLOR,
            )
            screen.blit(hint, (GRID_OFFSET_X, GRID_OFFSET_Y + grid_pixel_h + 12))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

import pygame
from backend.DefaultParty import DefaultParty
from backend.buildeur.BuildeurParty import BuildeurParty
from backend.scoring.ScoreEngine import ScoreEngine
from backend.structure.Bodyguard import Bodyguard
from backend.structure.Chair import Chair
from backend.structure.Speaker import Speaker
from backend.structure.Stand import Stand
from backend.structure.Tent import Tent
from backend.structure.Toilet import Toilet
from backend.structure.Vending_machine import Vending_machine
from backend.structure.Water_fountain import Water_fountain
from frontend.Button import Button
from frontend.Grid import Grid
from frontend.ScorePanel import ScorePanel
import pygame as _pg

from frontend.Cell import CellState as CS

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


def make_element_buttons(btn_x, base_y, btn_panel_w, elements):
    buttons = []
    sorted_elements = sorted(elements, key=lambda element: type(element).__name__)
    for i, element in enumerate(sorted_elements):
        label = f"{type(element).__name__}  {element.width}×{element.height}  [{element.score}pts]"
        buttons.append(Button(btn_x, base_y + i * 42, btn_panel_w, 38, label, BLUE))
    return buttons


def clamp(value, lower, upper):
    return max(lower, min(upper, value))


def draw_builder_panel(
    screen,
    score_x,
    builder_panel_y,
    builder_panel_w,
    builder_counts,
    builder_total,
    builder_list_count,
    validation_message,
    validation_color,
    font_hint,
):
    panel_rect = pygame.Rect(score_x, builder_panel_y, builder_panel_w, 240)
    pygame.draw.rect(screen, (18, 22, 33), panel_rect, border_radius=10)
    pygame.draw.rect(screen, (80, 90, 110), panel_rect, 2, border_radius=10)

    title = font_hint.render(
        "Party Builder : ajustez les éléments puis validez", True, (255, 230, 120)
    )
    screen.blit(title, (panel_rect.x + 12, panel_rect.y + 12))

    info = font_hint.render(
        f"Total sélectionné au builder : {builder_total} / 20", True, (180, 220, 255)
    )
    screen.blit(info, (panel_rect.x + 12, panel_rect.y + 34))

    info_current = font_hint.render(
        f"Liste actuelle : {builder_list_count} éléments", True, (180, 220, 255)
    )
    screen.blit(info_current, (panel_rect.x + 12, panel_rect.y + 54))

    row_y = panel_rect.y + 80
    row_height = 20
    for name, count in builder_counts.items():
        label = font_hint.render(f"{name}", True, (220, 220, 220))
        screen.blit(label, (panel_rect.x + 12, row_y))
        count_surf = font_hint.render(str(count), True, (255, 255, 255))
        screen.blit(count_surf, (panel_rect.x + 172, row_y))
        row_y += row_height

    if validation_message:
        status_surf = font_hint.render(validation_message, True, validation_color)
        screen.blit(status_surf, (panel_rect.x + 12, panel_rect.y + 210))

    return panel_rect


def get_builder_entry_types():
    return [
        ("Bodyguard", Bodyguard, "changeBodyguard"),
        ("Chair", Chair, "changeChair"),
        ("Speaker", Speaker, "changeSpeaker"),
        ("Stand", Stand, "changeStand"),
        ("Tent", Tent, "changeTent"),
        ("Toilet", Toilet, "changeToilet"),
        ("Vending_machine", Vending_machine, "changeVendingMachine"),
        ("Water_fountain", Water_fountain, "changeWaterFontain"),
    ]


def update_builder_counts(builder_counts, name, delta):
    for label, cls, _ in get_builder_entry_types():
        if label == name:
            current = builder_counts[name]
            builder_counts[name] = clamp(current + delta, cls().min, cls().max)
            return


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

    btn_panel_w = 320
    score_panel_w = 300
    margin = 5

    total_w = (
        GRID_OFFSET_X
        + grid_pixel_w
        + margin
        + btn_panel_w
        + margin
        + score_panel_w
        + margin
    )
    builder_panel_h = 300
    total_h = GRID_OFFSET_Y + grid_pixel_h + builder_panel_h + margin
    screen = pygame.display.set_mode((total_w, total_h))
    pygame.display.set_caption("Party Planner – Grid System")

    grid = Grid(rows, cols, cell_size)
    for cell in blocked_cells:
        grid.cells[cell[0]][cell[1]].block_cell()

    grid_surface = pygame.Surface((grid_pixel_w, grid_pixel_h))

    party = DefaultParty().create()
    party.elements = sorted(party.elements, key=lambda element: type(element).__name__)

    # Boutons de sélection des éléments disponibles
    btn_x = GRID_OFFSET_X + grid_pixel_w + margin
    buttons = make_element_buttons(btn_x, GRID_OFFSET_Y, btn_panel_w, party.elements)

    # Score
    score_x = btn_x + btn_panel_w + margin
    score_panel = ScorePanel(score_x, GRID_OFFSET_Y, score_panel_w, grid_pixel_h - 300)

    builder_panel_y = GRID_OFFSET_Y - 200 + grid_pixel_h + 20 + margin
    builder_counts = {
        label: party.elements.count(cls())
        for label, cls, _ in get_builder_entry_types()
    }
    fixed_elements = 2
    builder_total = sum(builder_counts.values()) + fixed_elements
    builder_list_count = len(party.elements)
    builder_buttons = []
    button_width = 16
    button_height = 15
    control_x = score_x + 12
    plus_x = score_x + 220
    row_y = builder_panel_y + 60
    row_height = 20
    for label, cls, _ in get_builder_entry_types():
        minus_button = Button(
            control_x + 190, row_y + 15, button_width, button_height, "-", BLUE
        )
        plus_button = Button(plus_x, row_y + 15, button_width, button_height, "+", BLUE)
        builder_buttons.append((minus_button, label, -1))
        builder_buttons.append((plus_button, label, +1))
        row_y += row_height
    validate_button = Button(
        score_x + 12,
        builder_panel_y + 280,
        score_panel_w - 24,
        44,
        "VALIDER LA LISTE",
        BLUE,
    )
    validation_message = ""
    validation_color = (255, 90, 90)
    engine = ScoreEngine(grid)

    selected_element = None
    font_hint = pygame.font.SysFont("Consolas", 13)
    running = True
    clock = pygame.time.Clock()

    while running:
        mx, my = pygame.mouse.get_pos()
        gx, gy = mx - GRID_OFFSET_X, my - GRID_OFFSET_Y

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                selected_element = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_button = False
                for button, name, delta in builder_buttons:
                    if button.rect.collidepoint(mx, my):
                        update_builder_counts(builder_counts, name, delta)
                        builder_total = sum(builder_counts.values()) + fixed_elements
                        validation_message = ""
                        clicked_button = True
                        break

                if not clicked_button and validate_button.rect.collidepoint(mx, my):
                    builder_total = sum(builder_counts.values()) + fixed_elements
                    if builder_total != 20:
                        validation_message = f"Erreur : {builder_total} éléments au total, il faut exactement 20 éléments (Scene+Ramp fixes)."
                        validation_color = (255, 90, 90)
                    else:
                        builder = BuildeurParty(DefaultParty().create())

                        for label, _, method_name in get_builder_entry_types():
                            getattr(builder, method_name)(builder_counts[label])

                        party = builder.build()

                        # Réinitialisation du plateau
                        grid = Grid(rows, cols, cell_size)

                        for cell in blocked_cells:
                            grid.cells[cell[0]][cell[1]].block_cell()

                        engine = ScoreEngine(grid)

                        party.elements = sorted(
                            party.elements, key=lambda element: type(element).__name__
                        )

                        buttons = make_element_buttons(
                            btn_x, GRID_OFFSET_Y + 10, btn_panel_w, party.elements
                        )

                        selected_element = None
                        builder_list_count = len(party.elements)

                        validation_message = "Liste validée et plateau réinitialisé."
                        validation_color = (120, 230, 120)
                    clicked_button = True

                if not clicked_button:
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

        # Builder panel
        draw_builder_panel(
            screen,
            score_x,
            builder_panel_y,
            score_panel_w,
            builder_counts,
            builder_total,
            builder_list_count,
            validation_message,
            validation_color,
            font_hint,
        )
        for button, _, _ in builder_buttons:
            button.draw(screen)
        validate_button.draw(screen)

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

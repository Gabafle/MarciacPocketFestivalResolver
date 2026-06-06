import pygame


class ScorePanel:
    """
    Panneau d'affichage du score affiché en bas à droite de la fenêtre.
    """

    # Couleurs
    BG_COLOR = (20, 24, 35)
    BORDER_COLOR = (70, 80, 110)
    TITLE_COLOR = (255, 220, 50)
    BASE_COLOR = (150, 200, 255)
    BONUS_COLOR = (80, 220, 120)
    MALUS_COLOR = (255, 90, 90)
    TOTAL_COLOR = (255, 255, 255)
    RULE_POS_COLOR = (100, 230, 140)
    RULE_NEG_COLOR = (255, 110, 110)
    SEPARATOR_COLOR = (60, 70, 95)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.font_title = pygame.font.SysFont("Consolas", 17, bold=True)
        self.font_normal = pygame.font.SysFont("Consolas", 13)
        self.font_total = pygame.font.SysFont("Consolas", 22, bold=True)
        self.score_data = {"total": 0, "base": 0, "bonus": 0, "details": []}

    def update(self, score_data):
        self.score_data = score_data

    def draw(self, screen):
        # Fond + bordure
        pygame.draw.rect(screen, self.BG_COLOR, self.rect, border_radius=8)
        pygame.draw.rect(screen, self.BORDER_COLOR, self.rect, 2, border_radius=8)

        pad = 12
        x = self.rect.x + pad
        y = self.rect.y + pad
        w = self.rect.width - 2 * pad

        title = self.font_title.render("◈  SCORE", True, self.TITLE_COLOR)
        screen.blit(title, (x, y))
        y += title.get_height() + 6
        self._hline(screen, x, y, w)
        y += 8

        base_surf = self.font_normal.render(
            f"Score de base   : {self.score_data['base']:>+6}", True, self.BASE_COLOR
        )
        screen.blit(base_surf, (x, y))
        y += base_surf.get_height() + 4

        bonus = self.score_data["bonus"]
        bonus_color = self.BONUS_COLOR if bonus >= 0 else self.MALUS_COLOR
        bonus_surf = self.font_normal.render(
            f"Bonus/Malus     : {bonus:>+6}", True, bonus_color
        )
        screen.blit(bonus_surf, (x, y))
        y += bonus_surf.get_height() + 6

        self._hline(screen, x, y, w)
        y += 8

        total = self.score_data["total"]
        total_color = self.TOTAL_COLOR
        if total >= 300:
            total_color = (255, 215, 0)  # Or
        elif total >= 150:
            total_color = (180, 240, 180)  # Vert clair
        elif total < 0:
            total_color = self.MALUS_COLOR

        total_surf = self.font_total.render(f"TOTAL  :  {total:>+6}", True, total_color)
        screen.blit(total_surf, (x, y))
        y += total_surf.get_height() + 8

        self._hline(screen, x, y, w)
        y += 8

        # ── Détails des règles actives ─────────────────────────
        header = self.font_normal.render("Règles actives :", True, (180, 180, 220))
        screen.blit(header, (x, y))
        y += header.get_height() + 4

        details = self.score_data.get("details", [])
        if not details:
            none_surf = self.font_normal.render("  — aucune —", True, (100, 100, 130))
            screen.blit(none_surf, (x, y))
        else:
            # Compter les doublons pour afficher ×N
            from collections import Counter

            counts = Counter(details)
            for desc, count in counts.items():
                # Détecter si la règle est positive ou négative
                is_positive = "+" in desc
                color = self.RULE_POS_COLOR if is_positive else self.RULE_NEG_COLOR
                line = f"  {'×'+str(count)+' ' if count>1 else '   '}{desc.strip()}"
                surf = self.font_normal.render(line, True, color)
                # Clip si le texte dépasse
                if y + surf.get_height() > self.rect.bottom - pad:
                    break
                screen.blit(surf, (x, y))
                y += surf.get_height() + 2

    def _hline(self, screen, x, y, w):
        pygame.draw.line(screen, self.SEPARATOR_COLOR, (x, y), (x + w, y), 1)

import pygame
from notes import HIT_Y, LANE_X, NOTE_W

class UI:
    def __init__(self, w=800, h=600):
        pygame.init()
        self.screen = pygame.display.set_mode((w,h))
        pygame.display.set_caption("Real Guitar Hero")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 18)
        self.big  = pygame.font.SysFont("Arial", 28)

    def draw_frame(self, notes, score, combo, last_status, expected):
        self.screen.fill((20,22,28))
        pygame.draw.rect(self.screen, (40,45,55), pygame.Rect(LANE_X-4, 0, NOTE_W+8, 600), border_radius=8)
        pygame.draw.line(self.screen, (230,230,230), (LANE_X, HIT_Y+NOTE_W//8), (LANE_X+NOTE_W, HIT_Y+NOTE_W//8), 3)
        for n in notes:
            n.draw(self.screen, self.font)
        hud = self.big.render(f"Score {score}  Combo {combo}", True, (240,240,240))
        self.screen.blit(hud, (20, 20))
        stat = self.font.render(last_status, True, (220,220,220))
        self.screen.blit(stat, (20, 60))
        exp  = self.font.render(f"Play: {expected}", True, (200,200,255))
        self.screen.blit(exp, (20, 84))
        pygame.display.flip()


import pygame

HIT_Y = 520
LANE_X = 320
NOTE_W, NOTE_H = 160, 28

class Note:
    def __init__(self, chord, spawn_time, speed=240):
        self.chord = chord
        self.x = LANE_X
        self.y = -NOTE_H
        self.spawn_time = spawn_time
        self.speed = speed
        self.active = True
        self.hit = False
        self.judged = False

    def update(self, dt):
        if not self.active:
            return
        self.y += self.speed * dt
        if self.y > 700:
            self.active = False

    def draw(self, screen, font):
        color = (60,130,255) if not self.hit else (120,200,120)
        pygame.draw.rect(screen, color, pygame.Rect(self.x, int(self.y), NOTE_W, NOTE_H), border_radius=6)
        label = font.render(self.chord, True, (10,10,10))
        screen.blit(label, (self.x+NOTE_W//2 - label.get_width()//2, int(self.y)+4))

    def in_hit_window(self, window=20):
        return abs(self.y - HIT_Y) <= window


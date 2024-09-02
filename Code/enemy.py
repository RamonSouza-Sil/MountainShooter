#!/usr/bin/python
# -*- coding: utf-8 -*-
from Code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY, WIN_HEIGHT
from Code.enemyShot import EnemyShot
from Code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # velocidade do Enemy

        if self.name == 'Enemy3':
            self.rect.centery += ENTITY_SPEED[self.name]
            print("descendo")
            if self.rect.centery >= WIN_HEIGHT:
                self.rect.centery -= ENTITY_SPEED[self.name] * 2
                print("Subindo")
            if self.rect.centery <= WIN_HEIGHT:
                self.rect.centery += ENTITY_SPEED[self.name]
                return

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

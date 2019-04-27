# -*- coding: utf-8 -*-

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position, speed, main_image):
        """Crea una clase que determina el personaje y le asigna los sprites
        con sus respectivos movimientos"""
        self.sheet = pygame.image.load(main_image) #La imagen con todos los sprites
        self.sheet.set_clip(pygame.Rect(0, 0, 64, 64))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.speed = speed
        """Aquí se seleccionan los sprites con cada una de las direcciones de
        movimiento que adoptará el personaje"""
        self.up_sprites = { 0: (0, 0, 64, 64), 1: (64, 0, 64, 64), 2: (128, 0, 64, 64), 3: (192, 0, 64, 64), 4:(256, 0, 64, 64), 5: (320, 0, 64, 64), 6: (384, 0, 64, 64), 7: (448, 0, 64, 64), 8: (512, 0, 64, 64)}
        self.left_sprites = { 0: (0, 64, 64, 64), 1: (64, 64, 64, 64), 2: (128, 64, 64, 64), 3:(192, 64, 64, 64), 4:(256, 64, 64, 64), 5:(320, 64, 64, 64), 6:(384, 64, 64, 64), 7:(448, 64, 64, 64), 8:(512, 64, 64, 64) }
        self.down_sprites = { 0: (0, 128, 64, 64), 1: (64, 128, 64, 64), 2: (128, 128, 64, 64), 3:(192, 128, 64, 64), 4:(256, 128, 64, 64), 5:(320, 128, 64, 64), 6:(384, 128, 64, 64), 7:(448, 128, 64, 64), 8:(512, 128, 64, 64)}
        self.right_sprites = { 0: (0, 192, 64, 64), 1: (64, 192, 64, 64), 2: (128, 192, 64, 64), 3:(192, 192, 64, 64), 4:(256, 192, 64, 64), 5:(320, 192, 64, 64), 6:(384, 192, 64, 64), 7:(448, 192, 64, 64), 8:(512, 192, 64, 64) }

    def get_frame(self, frame_set):
        """Selecciona el cuadro en la animación del personaje"""
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        """De la imagen con todos los sprites, actualiza constantemente los
        cuadros según las coordenadas dadas en "clipped_rect".  """
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        """Actualiza los sprites en función de la direccion hacia la cual se
        dirige el personaje"""
        if direction == 'left':
            self.clip(self.left_sprites)
            self.rect.x -= self.speed
        if direction == 'right':
            self.clip(self.right_sprites)
            self.rect.x += self.speed
        if direction == 'up':
            self.clip(self.up_sprites)
            self.rect.y -= self.speed
        if direction == 'down':
            self.clip(self.down_sprites)
            self.rect.y += self.speed

        if direction == 'stand_left':
            self.clip(self.left_sprites[0])
        if direction == 'stand_right':
            self.clip(self.right_sprites[0])
        if direction == 'stand_up':
            self.clip(self.up_sprites[0])
        if direction == 'stand_down':
            self.clip(self.down_sprites[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):

        if event.type == pygame.QUIT:
            """Evalua si se presionó el boton de cerrar el juego, de ser así, se
            terminará la ejecución del mismo"""
            game_over = True

        if event.type == pygame.KEYDOWN:
            """Evalua si se presionan las teclas de movimiento, de ser así,el
            personaje se mueve hacia la dirección indicada"""
            if event.key == pygame.K_a:
                self.update('left')
            if event.key == pygame.K_d:
                self.update('right')
            if event.key == pygame.K_w:
                self.update('up')
            if event.key == pygame.K_s:
                self.update('down')

        if event.type == pygame.KEYUP:
            """Evalua si se levanta alguna tecla de movimiento, de ser así,
            sobrepone la imagen "Stand" para indicar la última dirección hacia la
            cual se movió el personaje"""
            if event.key == pygame.K_a:
                self.update('stand_left')
            if event.key == pygame.K_d:
                self.update('stand_right')
            if event.key == pygame.K_w:
                self.update('stand_up')
            if event.key == pygame.K_s:
                self.update('stand_down')
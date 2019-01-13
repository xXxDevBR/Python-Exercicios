import pygame

pygame.init()
pygame.mixer_music.load('/home/joaolusca/Música/bi.mp3')
pygame.mixer_music.play()
pygame.event.wait()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-19 20:01:05
# @Author  : Sundae Chen (sundaechn@gmail.com)
# @Link    : http://sundae.applinzi.com/home


import time
import pygame


def ShowLine(x0, y0, x1, y1):
    pygame.draw.line(screen, pygame.Color(
        255, 255, 255), (x0, y0), (x1, y1), fill)
    return


def ShowRec(x0, y0, x1, y1):
    pygame.draw.rect(screen, pygame.Color(
        255, 255, 255), (x0, y0, x1, y1), fill)
    return


def ShowCir(x0, y0, d0):
    pygame.draw.circle(screen, pygame.Color(255, 255, 255), (x0, y0), d0, fill)
    return


def ShowNum(mynum, x0, y0, size):
    font = pygame.font.Font('digital-7_mono.ttf', size, bold=1)
    textSuface = font.render(mynum, 1, pygame.Color(255, 255, 255))
    screen.blit(textSuface, (x0, y0))
    return


def ShowStr(mystring, x0, y0, size):
    font = pygame.font.Font('jiheti.ttf', size, bold=1)
    textSuface = font.render(mystring, 1, pygame.Color(255, 255, 255))
    screen.blit(textSuface, (x0, y0))
    return

width = 480
height = 320
fill = 1

pygame.init()
pygame.display.set_caption('Raspberry Pi')
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
# screen=pygame.display.set_mode((width,height),pygame.RESIZABLE)
screen.fill(pygame.Color(255, 255, 255))

Fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill(pygame.Color(0, 0, 0))
    # ShowRec(4,4,472,312)
    words = u"让我再看你一眼    星空和黑夜"
    ShowCir(240, 100, 60)
    mylocaltime = time.localtime()
    myclock = time.strftime("%H:%M:%S", mylocaltime)  # 13:15:03 2017-04-21
    ShowNum(myclock, 195, 90, 24)
    ShowStr(words, 80, 220, 24)
    pygame.display.update()

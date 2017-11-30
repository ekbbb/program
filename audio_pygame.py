#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame.mixer
import time

# mixer モジュールの初期化
pygame.mixer.init()
#音楽ファイルの読み込み
pygame.mixer.music.load("crrect_answer3.mp3")
#pygame.mixer.music.play(-1)

time.sleep(60)
# 再生の終了
pygame.mixer.music.stop()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎮 Azal - لعبة المحمدية الواعرة والمضحكة
لعبة مغربية شعبية كوميدية على موبايل والكومبيوتر
Made with ❤️ in Morocco 🇲🇦
"""

import pygame
import random
import sys
from config import *
from sound_manager import SoundManager

# تهيئة pygame
pygame.init()

# تهيئة مدير الأصوات
sound_manager = SoundManager()

# إع��اد الشاشة
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎮 Azal - لعبة المحمدية الواعرة 😂")
clock = pygame.time.Clock()

# متغيرات اللاعب
player_x = WIDTH // 2
player_y = HEIGHT - 80
player_width = 40
player_height = 40
player_speed = PLAYER_SPEED
player_jump = False
player_jump_speed = 0

# متغيرات اللعبة
score = 0
money = 0
level = 1
game_over = False
game_paused = False

# قائمة الموانع (الثقوب)
holes = []
hole_spawn_timer = 0
current_hole_spawn_rate = HOLE_SPAWN_RATE

# متغيرات العدو (الشرطي)
enemy_x = random.randint(0, WIDTH - 40)
enemy_y = -40
enemy_speed = ENEMY_SPEED
enemy_spawn_timer = 0
current_enemy_spawn_rate = ENEMY_SPAWN_RATE
enemy_spotted = False

# نصوص كوميدية
funny_text_display = ""
funny_timer = 0

# المتغيرات الإضافية
combo = 0
high_score = 0
sound_enabled = True

# دالة لرسم النص
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# دالة لرسم اللاعب
def draw_player():
    # جسم اللاعب (مربع أصفر)
    pygame.draw.rect(screen, YELLOW, (player_x, player_y, player_width, player_height))
    # عيون اللاعب
    pygame.draw.circle(screen, BLACK, (int(player_x + 12), int(player_y + 8)), 3)
    pygame.draw.circle(screen, BLACK, (int(player_x + 28), int(player_y + 8)), 3)
    # فم (ضحكة)
    pygame.draw.arc(screen, BLACK, (int(player_x + 10), int(player_y + 15), 20, 15), 0, 3.14, 2)

# دالة لرسم العدو (الشرطي)
def draw_enemy():
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, 40, 40))
    # عيون العدو
    pygame.draw.circle(screen, BLACK, (int(enemy_x + 12), int(enemy_y + 8)), 3)
    pygame.draw.circle(screen, BLACK, (int(enemy_x + 28), int(enemy_y + 8)), 3)
    # شعر الشرطي
    pygame.draw.rect(screen, DARK_GRAY, (int(enemy_x), int(enemy_y - 5), 40, 5))

# دالة لرسم الثقوب
def draw_holes():
    for hole in holes:
        pygame.draw.rect(screen, BROWN, hole)
        pygame.draw.rect(screen, BLACK, hole, 2)
        # خطوط داخل الثقب
        pygame.draw.line(screen, BLACK, (int(hole[0] + 5), int(hole[1] + 10)), 
                        (int(hole[0] + 25), int(hole[1] + 20)), 1)

# دالة لرسم الخلفية
def draw_background():
    screen.fill(WHITE)
    # رسم الشارع (خطوط الطريق)
    pygame.draw.line(screen, DARK_GRAY, (WIDTH//4, 0), (WIDTH//4, HEIGHT), 3)
    pygame.draw.line(screen, DARK_GRAY, (3*WIDTH//4, 0), (3*WIDTH//4, HEIGHT), 3)
    # خطوط بيضاء في الوسط
    for y in range(0, HEIGHT, 30):
        pygame.draw.line(screen, WHITE, (WIDTH//2 - 1, y), (WIDTH//2 + 1, y + 20), 2)

# دالة لرسم النقط والمعلومات
def draw_ui():
    font_small = pygame.font.Font(None, 28)
    font_large = pygame.font.Font(None, 36)
    
    # النقط
    score_text = f"Score: {score}"
    draw_text(score_text, font_large, BLACK, 10, 10)
    
    # الفلوس
    money_text = f"Money: {money} 💰"
    draw_text(money_text, font_large, GREEN, 10, 50)
    
    # المستوى
    level_text = f"Level: {level}"
    draw_text(level_text, font_large, BLUE, 10, 90)
    
    # أفضل نقطة
    high_score_text = f"High: {high_score}"
    draw_text(high_score_text, font_small, ORANGE, WIDTH - 140, 10)
    
    # حالة الصوت
    sound_status = "🔊 ON" if sound_enabled else "🔇 OFF"
    draw_text(sound_status, font_small, BLACK, WIDTH - 90, HEIGHT - 30)

# دالة لرسم النصوص الكوميدية
def draw_funny_text():
    if funny_timer > 0:
        font = pygame.font.Font(None, 48)
        funny_surface = font.render(funny_text_display, True, RED)
        rect = funny_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        # خلفية للنص
        pygame.draw.rect(screen, WHITE, rect.inflate(10, 10))
        pygame.draw.rect(screen, RED, rect.inflate(10, 10), 2)
        screen.blit(funny_surface, rect)

# دالة لرسم شاشة Game Over
def draw_game_over():
    font_large = pygame.font.Font(None, 72)
    font_medium = pygame.font.Font(None, 48)
    font_small = pygame.font.Font(None, 36)
    
    # خلفية شبه شفافة
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(200)
    overlay.fill(BLACK)
    screen.blit(overlay, (0, 0))
    
    # نص Game Over
    game_over_text = font_large.render("Game Over!", True, RED)
    screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//3))
    
    # النقط النهائية
    final_score_text = font_medium.render(f"Score: {score}", True, YELLOW)
    screen.blit(final_score_text, (WIDTH//2 - final_score_text.get_width()//2, HEIGHT//2 - 50))
    
    # الفلوس النهائية
    final_money_text = font_medium.render(f"Money: {money} 💰", True, GREEN)
    screen.blit(final_money_text, (WIDTH//2 - final_money_text.get_width()//2, HEIGHT//2 + 20))
    
    # تعليمات للبدء من جديد
    restart_text = font_small.render("Press SPACE to restart", True, WHITE)
    screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT - 100))

# دالة لتحديث المستوى
def update_level():
    global level, current_hole_spawn_rate, current_enemy_spawn_rate, enemy_speed
    
    old_level = level
    if score >= level * 100:
        level = min(level + 1, 5)
        if level > old_level:
            sound_manager.play_level_up()
            funny_text_display = f"مستوى جديد! Level {level} 🌟"
        level_config = LEVELS[level]
        current_hole_spawn_rate = level_config['hole_rate']
        current_enemy_spawn_rate = level_config['enemy_rate']
        enemy_speed = level_config['enemy_speed']

# دالة لإعادة تعيين اللعبة
def reset_game():
    global player_x, player_y, score, money, level, game_over
    global holes, hole_spawn_timer, enemy_x, enemy_y, enemy_spawn_timer
    global current_hole_spawn_rate, current_enemy_spawn_rate, enemy_speed
    global funny_text_display, funny_timer, combo, high_score, enemy_spotted
    
    if score > high_score:
        high_score = score
    
    player_x = WIDTH // 2
    player_y = HEIGHT - 80
    score = 0
    money = 0
    level = 1
    game_over = False
    holes = []
    hole_spawn_timer = 0
    enemy_x = random.randint(0, WIDTH - 40)
    enemy_y = -40
    enemy_spawn_timer = 0
    current_hole_spawn_rate = HOLE_SPAWN_RATE
    current_enemy_spawn_rate = ENEMY_SPAWN_RATE
    enemy_speed = ENEMY_SPEED
    funny_text_display = ""
    funny_timer = 0
    combo = 0
    enemy_spotted = False

# الحلقة الرئيسية
running = True

while running:
    clock.tick(FPS)
    
    # معالجة الأحداث
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_over:
                    reset_game()
                elif not game_paused and not player_jump:
                    player_jump = True
                    player_jump_speed = 15
                    sound_manager.play_jump()
            if event.key == pygame.K_p:
                game_paused = not game_paused
            if event.key == pygame.K_m:
                sound_enabled = sound_manager.toggle_sound()
    
    # إذا كانت اللعبة متوقفة أو انتهت، لا نحدّث شيء
    if game_over or game_paused:
        draw_background()
        draw_holes()
        draw_enemy()
        draw_player()
        draw_ui()
        draw_funny_text()
        if game_over:
            draw_game_over()
        pygame.display.flip()
        continue
    
    # التحكم بحركة اللاعب
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    
    # القفز
    if player_jump:
        player_y -= player_jump_speed
        player_jump_speed -= 0.5
        if player_y >= HEIGHT - 80:
            player_y = HEIGHT - 80
            player_jump = False
            player_jump_speed = 0
    
    # ظهور الثقوب
    hole_spawn_timer += 1
    if hole_spawn_timer > current_hole_spawn_rate:
        hole_x = random.randint(0, WIDTH - 30)
        holes.append([hole_x, -30, 30, 30])
        hole_spawn_timer = 0
    
    # تحريك الثقوب
    for hole in holes[:]:
        hole[1] += HOLE_SPEED
        if hole[1] > HEIGHT:
            holes.remove(hole)
            score += POINTS_HOLE_DODGE
            combo += 1
            money = int(score * MONEY_MULTIPLIER)
            sound_manager.play_dodge()
            funny_text_display = random.choice(FUNNY_TEXTS)
            funny_timer = 30
            update_level()
    
    # ظهور العدو (الشرطي)
    enemy_spawn_timer += 1
    if enemy_spawn_timer > current_enemy_spawn_rate:
        enemy_x = random.randint(0, WIDTH - 40)
        enemy_y = -40
        enemy_spawn_timer = 0
        enemy_spotted = False
    
    # تحريك العدو وإصدار صوت عند ظهوره
    if enemy_y > 0 and not enemy_spotted:
        sound_manager.play_enemy_spotted()
        enemy_spotted = True
    
    enemy_y += enemy_speed
    
    # كشف الاصطدام بالثقوب
    for hole in holes:
        if (player_x < hole[0] + hole[2] and 
            player_x + player_width > hole[0] and
            player_y < hole[1] + hole[3] and
            player_y + player_height > hole[1]):
            score = max(0, score - 10)
            combo = 0
            sound_manager.play_hit()
            funny_text_display = "سقطت في الثقب! 🕳️"
            funny_timer = 50
            player_y = HEIGHT - 80
            if score < 0:
                game_over = True
                sound_manager.play_game_over()
                if score > high_score:
                    high_score = score
    
    # كشف الاصطدام بالعدو (الشرطي)
    if (player_x < enemy_x + 40 and 
        player_x + player_width > enemy_x and
        player_y < enemy_y + 40 and
        player_y + player_height > enemy_y):
        funny_text_display = "الشرطي اتفسخ ضحك! 😂"
        funny_timer = 50
        score += POINTS_ENEMY_DODGE
        combo += 1
        sound_manager.play_laugh()
        sound_manager.play_money_earned()
        money = int(score * MONEY_MULTIPLIER)
        enemy_y = -100
        enemy_spotted = False
        update_level()
    
    # إذا خرج الشرطي من الشاشة، لا نحسبه
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_spotted = False
    
    # رسم كل شيء
    draw_background()
    draw_holes()
    draw_enemy()
    draw_player()
    draw_ui()
    draw_funny_text()
    
    pygame.display.flip()

pygame.quit()
sys.exit()

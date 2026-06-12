"""
🔊 نظام الأصوات والموسيقى ديال اللعبة
"""

import pygame
import os

class SoundManager:
    def __init__(self):
        """تهيئة مدير الأصوات"""
        pygame.mixer.init()
        self.sounds = {}
        self.music_volume = 0.5
        self.sound_volume = 0.7
        self.sound_enabled = True
        self.music_enabled = True
        
        # تحميل الأصوات
        self.load_sounds()
    
    def load_sounds(self):
        """تحميل كل الأصوات (إذا كانت موجودة)"""
        try:
            # أصوات مزيفة (سنضيفها بعدين)
            pass
        except Exception as e:
            print(f"خطأ في تحميل الأصوات: {e}")
    
    def play_jump(self):
        """صوت القفز"""
        if not self.sound_enabled:
            return
        try:
            # تشغيل صوت القفز
            jump_sound = pygame.mixer.Sound(buffer=self.generate_beep(440, 0.1))
            jump_sound.set_volume(self.sound_volume)
            jump_sound.play()
        except:
            pass
    
    def play_dodge(self):
        """صوت التجنب (تجنب الثقب أو الشرطي)"""
        if not self.sound_enabled:
            return
        try:
            # صوت تجنب بنجاح
            dodge_sound = pygame.mixer.Sound(buffer=self.generate_beep(880, 0.2))
            dodge_sound.set_volume(self.sound_volume)
            dodge_sound.play()
        except:
            pass
    
    def play_hit(self):
        """صوت الاصطدام (السقوط في ثقب)"""
        if not self.sound_enabled:
            return
        try:
            # صوت الاصطدام
            hit_sound = pygame.mixer.Sound(buffer=self.generate_beep(200, 0.3))
            hit_sound.set_volume(self.sound_volume)
            hit_sound.play()
        except:
            pass
    
    def play_laugh(self):
        """صوت الضحك الكوميدي 😂"""
        if not self.sound_enabled:
            return
        try:
            # سلسلة من الأصوات العالية للضحك
            laugh_sound = pygame.mixer.Sound(buffer=self.generate_beep(700, 0.5))
            laugh_sound.set_volume(self.sound_volume)
            laugh_sound.play()
        except:
            pass
    
    def play_level_up(self):
        """صوت رفع المستوى"""
        if not self.sound_enabled:
            return
        try:
            # سلسلة أصوات صاعدة
            for freq in [440, 550, 660, 880]:
                try:
                    beep = pygame.mixer.Sound(buffer=self.generate_beep(freq, 0.1))
                    beep.set_volume(self.sound_volume)
                    beep.play()
                except:
                    pass
        except:
            pass
    
    def play_game_over(self):
        """صوت انتهاء اللعبة"""
        if not self.sound_enabled:
            return
        try:
            # سلسلة أصوات هابطة
            for freq in [880, 660, 550, 440]:
                try:
                    beep = pygame.mixer.Sound(buffer=self.generate_beep(freq, 0.15))
                    beep.set_volume(self.sound_volume)
                    beep.play()
                except:
                    pass
        except:
            pass
    
    def play_money_earned(self):
        """صوت كسب فلوس"""
        if not self.sound_enabled:
            return
        try:
            # صوت نقود (تصفيق خفيف)
            money_sound = pygame.mixer.Sound(buffer=self.generate_beep(520, 0.2))
            money_sound.set_volume(self.sound_volume)
            money_sound.play()
        except:
            pass
    
    def play_enemy_spotted(self):
        """صوت رؤية الشرطي"""
        if not self.sound_enabled:
            return
        try:
            # صوت تحذير
            alert_sound = pygame.mixer.Sound(buffer=self.generate_beep(1000, 0.3))
            alert_sound.set_volume(self.sound_volume)
            alert_sound.play()
        except:
            pass
    
    @staticmethod
    def generate_beep(frequency, duration):
        """إنشاء صوت بيب بسيط"""
        import math
        sample_rate = 22050
        num_samples = int(duration * sample_rate)
        
        # إنشاء موجة جيبية
        frames = []
        for i in range(num_samples):
            sample = int(32767.0 * 0.3 * math.sin(2.0 * math.pi * frequency * i / sample_rate))
            frames.append(sample & 0xffff)
        
        # تحويل إلى bytes
        import array
        arr = array.array('h', frames)
        return arr.tobytes()
    
    def toggle_sound(self):
        """تشغيل/إيقاف الأصوات"""
        self.sound_enabled = not self.sound_enabled
        return self.sound_enabled
    
    def toggle_music(self):
        """تشغيل/إيقاف الموسيقى"""
        self.music_enabled = not self.music_enabled
        return self.music_enabled
    
    def set_sound_volume(self, volume):
        """تعديل مستوى صوت المؤثرات الصوتية (0-1)"""
        self.sound_volume = max(0, min(1, volume))
    
    def set_music_volume(self, volume):
        """تعديل مستوى صوت الموسيقى (0-1)"""
        self.music_volume = max(0, min(1, volume))

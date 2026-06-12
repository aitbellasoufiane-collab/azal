# إعدادات اللعبة

# الشاشة
WIDTH = 400
HEIGHT = 600
FPS = 60

# الألوان
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
DARK_GRAY = (50, 50, 50)

# سرعات
PLAYER_SPEED = 6
ENEMY_SPEED = 2
HOLE_SPEED = 4

# الإعدادات
HOLE_SPAWN_RATE = 40
ENEMY_SPAWN_RATE = 120

# النصوص الكوميدية
FUNNY_TEXTS = [
    "واااش كاين!",
    "يا الله شنو هاد!",
    "معليش يا جاج!",
    "دير بالك من الثقب!",
    "هههههه 😂",
    "الباره شفتك!",
    "واخ يا سيدي!",
    "سقطت برك! 🕳️",
    "الشرطي اتفسخ ضحك! 😂",
    "ديرولي الهاري!",
    "كنت كنتلفت!",
    "شنو ��اد الطريق!",
]

# نقط الربح
POINTS_HOLE_DODGE = 10
POINTS_ENEMY_DODGE = 20
POINTS_LEVEL_COMPLETE = 50
MONEY_MULTIPLIER = 0.01

# المستويات
LEVELS = {
    1: {'hole_rate': 40, 'enemy_speed': 2, 'enemy_rate': 120},
    2: {'hole_rate': 30, 'enemy_speed': 3, 'enemy_rate': 100},
    3: {'hole_rate': 25, 'enemy_speed': 4, 'enemy_rate': 80},
    4: {'hole_rate': 20, 'enemy_speed': 5, 'enemy_rate': 60},
    5: {'hole_rate': 15, 'enemy_speed': 6, 'enemy_rate': 50},
}

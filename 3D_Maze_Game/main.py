import pygame
import math
import sys
import random

# Ekran boyutları
WIDTH = 1920
HEIGHT = 1080

# Oyuncu özellikleri
PLAYER_HEIGHT = 30
PLAYER_SPEED = 0.05
PLAYER_ROT_SPEED = 0.005
PLAYER_SIZE = 10
PLAYER_FOV = math.pi / 3

# Labirent haritası
world_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Pygame başlatma
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Muzik Oynatıcı
pygame.mixer.init()
music_path = "abc.mp3"
pygame.mixer.music.load(music_path)
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

# Oyuncu başlangıç pozisyonu ve bakış açısı
player_x = 1.5
player_y = 1.5
player_angle = 1.55

# Yıldız Oluşturma
stars = []
for _ in range(100):
    star_x = random.randint(0, WIDTH)
    star_y = random.randint(0, HEIGHT // 2)
    stars.append((star_x, star_y))

# Oyun durumu menü olarak başlar
game_state = "menu"

# Oyun Döngüsü
while True:

    for event in pygame.event.get():
        #Oyunu kapatma
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Oyun durumu menü ise
        if game_state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # "New Game" seçeneğine tıklanırsa
                if new_game_rect.collidepoint(mouse_pos):
                    game_state = "game"

                # "Quit" seçeneğine tıklanırsa
                if quit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

    # ESC ile oyunu kapatma
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    # Game durumunda oyunun akış hali
    elif game_state == "game":
        # Mouse ile oyuncunun kafa hareketi
        mouse_dx, mouse_dy = pygame.mouse.get_rel()
        player_angle += mouse_dx * PLAYER_ROT_SPEED

        # Mouse merkeze sabitler ve gizler
        center_x = WIDTH // 2
        center_y = HEIGHT // 2
        # Mouse merkeze sabitler ve gizler
        pygame.mouse.set_visible(False)
        pygame.mouse.set_pos(center_x, center_y)

        # Oyuncunun koşma hareketi
        if keys[pygame.K_LSHIFT]:
            PLAYER_SPEED = 0.09
        else:
            PLAYER_SPEED = 0.05

        # Oyuncunun yürüme hareketi
        if keys[pygame.K_w]:
            new_player_x = player_x + math.sin(player_angle) * PLAYER_SPEED
            new_player_y = player_y + math.cos(player_angle) * PLAYER_SPEED
            # Oyuncunun harita sınırları içinde hareketi
            if (new_player_x < 10) & (new_player_y < 10):
                if world_map[int(new_player_x)][int(player_y)] == 0:
                    player_x = new_player_x
                if world_map[int(player_x)][int(new_player_y)] == 0:
                    player_y = new_player_y

        if keys[pygame.K_s]:
            new_player_x = player_x - math.sin(player_angle) * PLAYER_SPEED
            new_player_y = player_y - math.cos(player_angle) * PLAYER_SPEED
            # Oyuncunun harita sınırları içinde hareketi
            if (new_player_x < 10) & (new_player_y < 10):
                if world_map[int(new_player_x)][int(player_y)] == 0:
                    player_x = new_player_x
                if world_map[int(player_x)][int(new_player_y)] == 0:
                    player_y = new_player_y

        if keys[pygame.K_d]:
            new_player_x = player_x + math.cos(player_angle) * PLAYER_SPEED
            new_player_y = player_y - math.sin(player_angle) * PLAYER_SPEED
            # Oyuncunun harita sınırları içinde hareketi
            if (new_player_x < 10) & (new_player_y < 10):
                if world_map[int(new_player_x)][int(player_y)] == 0:
                    player_x = new_player_x
                if world_map[int(player_x)][int(new_player_y)] == 0:
                    player_y = new_player_y

        if keys[pygame.K_a]:
            new_player_x = player_x - math.cos(player_angle) * PLAYER_SPEED
            new_player_y = player_y + math.sin(player_angle) * PLAYER_SPEED
            # Oyuncunun harita sınırları içinde hareketi
            if (new_player_x < 10) & (new_player_y < 10):
                if world_map[int(new_player_x)][int(player_y)] == 0:
                    player_x = new_player_x
                if world_map[int(player_x)][int(new_player_y)] == 0:
                    player_y = new_player_y

        # Oyunun bitiş noktası ve menüye dönüş
        if (player_x >= 9) | (player_y >= 9):
            # Mouse görünür olur
            pygame.mouse.set_visible(True)
            game_state = "menu"
            player_x = 1.5
            player_y = 1.5
            player_angle = 1.55

    # Oyun durumuna göre çıkış
    elif game_state == "quit":
        pygame.quit()
        sys.exit()

    if game_state == "game":

        # Zemin rengi
        floor_color = (60, 60, 60)

        # Gökyüzü çizimi
        screen.fill((0, 51, 102))

        # Zeminin çizimi
        pygame.draw.rect(screen, floor_color, (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

        # Beyaz noktaların çizimi
        for star in stars:
            pygame.draw.circle(screen, (255, 255, 255), star, 1)

        for x in range(WIDTH):
            ray_angle = (player_angle - PLAYER_FOV / 2) + (x / WIDTH) * PLAYER_FOV
            distance_to_wall = 0
            hit_wall = False
            wall_x = 0
            wall_y = 0

            while not hit_wall and distance_to_wall < 20:
                distance_to_wall += 0.06
                test_x = int(player_x + math.sin(ray_angle) * distance_to_wall)
                test_y = int(player_y + math.cos(ray_angle) * distance_to_wall)
                # Çarpışma kontrolü
                if test_x < 0 or test_x >= len(world_map) or test_y < 0 or test_y >= len(world_map[0]):
                    hit_wall = True
                    distance_to_wall = 10
                elif world_map[test_x][test_y] == 1:
                    hit_wall = True
                    wall_x = test_x
                    wall_y = test_y

            # Duvar çizimi
            if hit_wall:
                wall_distance = distance_to_wall
                wall_height = int(HEIGHT / wall_distance)

                # Gölgelendirme
                shading = max(0, 255 - distance_to_wall * 40)
                wall_color = (shading, shading, shading)

                ceiling = HEIGHT // 2 - wall_height // 2  # Tavan yüksekliği
                floor = HEIGHT - ceiling  # Zemin yüksekliği

                wall_column = pygame.Surface((1, floor - ceiling))
                wall_column.fill(wall_color)
                screen.blit(wall_column, (x, ceiling))

    # Menü durumuna göre ekran çizimi
    elif game_state == "menu":

        # Ana menü metni çizimi
        font = pygame.font.Font(None, 36)
        text = font.render("Labirent Oyunu", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        screen.blit(text, text_rect)

        # "New Game" seçeneği çizimi
        new_game_text = font.render("New Game", True, (255, 255, 255))
        new_game_rect = new_game_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(new_game_text, new_game_rect)

        # "Quit" seçeneği çizimi
        quit_text = font.render("Quit", True, (255, 255, 255))
        quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        screen.blit(quit_text, quit_rect)

    # 60 fps görüntü yenileme
    pygame.display.flip()
    clock.tick(60)

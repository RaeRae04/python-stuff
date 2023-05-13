import pygame
import time
import os

# Initialize
pygame.init()

# Current Directory
current_dir = os.path.dirname(__file__)
print(current_dir)
image_dir = os.path.join(current_dir, "images")
print(image_dir)

# Set screen dimensions and caption
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

# Load image files
background_image = pygame.image.load(os.path.join(image_dir, "scene1.jpg"))
character_image = pygame.image.load(os.path.join(image_dir, "icon.png"))

# Define button dimensions and positions
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50
BUTTON_MARGIN = 20
play_button_pos = (SCREEN_WIDTH//2 - BUTTON_WIDTH//2, SCREEN_HEIGHT//2 - BUTTON_HEIGHT//2 - BUTTON_HEIGHT - BUTTON_MARGIN)
settings_button_pos = (SCREEN_WIDTH//2 - BUTTON_WIDTH//2, SCREEN_HEIGHT//2 - BUTTON_HEIGHT//2)
credits_button_pos = (SCREEN_WIDTH//2 - BUTTON_WIDTH//2, SCREEN_HEIGHT//2 - BUTTON_HEIGHT//2 + BUTTON_HEIGHT + BUTTON_MARGIN)

def main_menu():
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    game_loop()

        # Draw buttons and labels
        screen.blit(play_button_img, play_button_pos)
        screen.blit(settings_button_img, settings_button_pos)
        screen.blit(credits_button_img, credits_button_pos)

        # Update the display
        pygame.display.update()

def game_loop():
    # Set starting character position and timer
    character_pos = (0, -100)
    character_timer = 0

    # Run the game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Start the character timer when the user clicks the play button
                if play_button_rect.collidepoint(event.pos):
                    character_timer = pygame.time.get_ticks() + 5000

        # Draw the scene
        screen.blit(background_image, (0, 0))
        if pygame.time.get_ticks() > character_timer:
            screen.blit(character_image, character_pos)
            character_pos = (200, 200) # change this to whatever position you want

        # Update the display
        pygame.display.update()

    pygame.quit()

# Define the button rectangles
play_button_rect = pygame.Rect(play_button_pos[0], play_button_pos[1], BUTTON_WIDTH, BUTTON_HEIGHT)
settings_button_rect = pygame.Rect(settings_button_pos[0], settings_button_pos[1], BUTTON_WIDTH, BUTTON_HEIGHT)
credits_button_rect = pygame.Rect(credits_button_pos[0], credits_button_pos[1], BUTTON_WIDTH, BUTTON_HEIGHT)

# Load button images
play_button_img = pygame.image.load("play_button.png")
settings_button_img = pygame.image.load("settings_button.png")
credits_button_img = pygame.image.load("credits_button.png")

# Start the main menu loop
main_menu()

import pygame

# Initialize Pygame
pygame.init()

# Set screen width and height
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window title
pygame.display.set_caption("My Game")

# Define button sizes and colors
button_width = 200
button_height = 50
button_color = (255, 0, 255)
button_active_color = (200, 0, 200)

# Create play button rectangle
play_button_rect = pygame.Rect((screen_width/2 - button_width/2), (screen_height/2 - button_height/2 - 100), button_width, button_height)

# Create settings button rectangle
settings_button_rect = pygame.Rect((screen_width/2 - button_width/2), (screen_height/2 - button_height/2), button_width, button_height)

# Create credits button rectangle
credits_button_rect = pygame.Rect((screen_width/2 - button_width/2), (screen_height/2 - button_height/2 + 100), button_width, button_height)

# Set font and font size for button labels
font_size = 24
font = pygame.font.Font(None, font_size)

try:
	# Game loop
	running = True
	print("Game is running")
	while running:
		# Handle events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			# Handle mouse click event on button surfaces
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if play_button_rect.collidepoint(event.pos):
						print("Play button clicked")
					elif settings_button_rect.collidepoint(event.pos):
						print("Settings button clicked")
					elif credits_button_rect.collidepoint(event.pos):
						print("Credits button clicked")

		# Draw buttons to screen
		pygame.draw.rect(screen, button_color, play_button_rect)
		pygame.draw.rect(screen, button_color, settings_button_rect)
		pygame.draw.rect(screen, button_color, credits_button_rect)

		# Add button labels to screen
		play_button_text = font.render("Play", True, (255, 255, 255))
		screen.blit(play_button_text, (play_button_rect.x + button_width/2 - play_button_text.get_width()/2, play_button_rect.y + button_height/2 - play_button_text.get_height()/2))

		settings_button_text = font.render("Settings", True, (255, 255, 255))
		screen.blit(settings_button_text, (settings_button_rect.x + button_width/2 - settings_button_text.get_width()/2, settings_button_rect.y + button_height/2 - settings_button_text.get_height()/2))

		credits_button_text = font.render("Credits", True, (255, 255, 255))
		screen.blit(credits_button_text, (credits_button_rect.x + button_width/2 - credits_button_text.get_width()/2, credits_button_rect.y + button_height/2 - credits_button_text.get_height()/2))

		# Update display
		pygame.display.flip()

# Handle error
except Exception as e:
	# Handle exception by closing game window and displaying error message.
	pygame.quit()
	print(f"An error occurred: {e}")

# Quit Pygame
pygame.quit(); print("Game successfully closed.")

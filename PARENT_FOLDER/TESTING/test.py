import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the window
win = pygame.display.set_mode((200, 50))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the rectangle
rect = pygame.Rect(0, 0, 200, 50)

# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Get the current time
    current_time = time.strftime("%H:%M:%S")

    # Render the text
    text = font.render(current_time, True, (255, 255, 255))

    # Clear the screen
    win.fill((0, 0, 0))

    # Draw the rectangle
    pygame.draw.rect(win, (255, 123, 0), rect)

    # Draw the text
    win.blit(text, (rect.x + rect.width // 2 - text.get_width() // 2,
                    rect.y + rect.height // 2 - text.get_height() // 2))

    # Update the screen
    pygame.display.update()

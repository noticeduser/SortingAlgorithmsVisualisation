"""
import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

colour = (255, 0, 0)

print(pygame.image.load("ICON.png"))

user_input_font = pygame.font.SysFont("ComicSans", 50)
text = ""



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode
    
    screen.fill("black")
    textbox_surface = user_input_font.render(text, True, "WHITE")
    textbox_rect = textbox_surface.get_rect(center = (250, 250))
    screen.blit(textbox_surface, textbox_rect)
    
    pygame.display.update()

"""

import pygame
import sys
import clipboard

pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Clipboard Input')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Check for Enter key press to retrieve clipboard content
                clipboard_content = clipboard.paste()
                if clipboard_content:
                    print("Clipboard contents:", clipboard_content)
                else:
                    print("Clipboard is empty or doesn't contain text.")
    
    pygame.display.flip()

pygame.quit()
sys.exit()


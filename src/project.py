import pygame
from pygame.locals import RESIZABLE
import random
import os

class Screen():
    def __init__(self, width=1920, height=1000):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height), RESIZABLE)
        self.run = True
        self.background_color = (0, 0, 0)  # Background color at start
        self.color_change_interval = 500  # Color change in ms
        self.last_color_change_time = pygame.time.get_ticks()

         # Create a list for images
        self.images = []
        animation_folder = os.path.join(os.path.dirname(__file__), 'animation')
        for filename in os.listdir(animation_folder):
            if filename.endswith(('.png')):
                image_path = os.path.join(animation_folder, filename)
                image = pygame.image.load(image_path).convert_alpha()  # Make background of image transparent so you can see the color changes
                self.images.append(image)
        self.current_image_index = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            elif event.type == pygame.VIDEORESIZE:
                self.handle_resize(event.size)

    def handle_resize(self, size):
        width, height = size
        pygame.display.set_mode((width, height), RESIZABLE)

    def update_background_color(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_color_change_time > self.color_change_interval:
            self.background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.last_color_change_time = current_time

    def update_image(self):
        # create animation through image cycling
        self.current_image_index = (self.current_image_index + 1) % len(self.images)

    def run_game(self):
        clock = pygame.time.Clock()

        while self.run:
            self.handle_events()
            self.update_background_color()
            self.update_image()

            self.screen.fill(self.background_color)

            # Draw image on the screen
            current_image = self.images[self.current_image_index]
            image_rect = current_image.get_rect(center=self.screen.get_rect().center)
            self.screen.blit(current_image, image_rect)

            pygame.display.flip()
            clock.tick(12)  # Adjust the frame rate if necessary

        pygame.quit()

def main():
    pygame.init()
    pygame.display.set_caption("Resizable Box with Image Sequence")
    screen = Screen()
    screen.run_game()

if __name__ == "__main__":
    main()
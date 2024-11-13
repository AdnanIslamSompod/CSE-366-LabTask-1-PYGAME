import pygame
from agent import Agent
from environment import Environment

# Initialize Pygame
pygame.init()

# Set up the environment
WIDTH, HEIGHT = 600, 500
environment = Environment(WIDTH, HEIGHT)

# Create the agent
agent = Agent(x=WIDTH // 2, y=HEIGHT // 2, speed=2, environment=environment)

# Set up the Pygame window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Agent-Environment Simulation")

# Set up font for displaying coordinates
font = pygame.font.Font(None, 36)

# Define the position and dimensions of the fixed rectangle to center it
fixed_rect_width = 50  # Width of the fixed rectangle
fixed_rect_height = 30  # Height of the fixed rectangle
fixed_rect_x = (WIDTH // 2) - (fixed_rect_width // 2)  # Center horizontally
fixed_rect_y = (HEIGHT // 2) - (fixed_rect_height // 2)  # Center vertically
fixed_rect_color = (0, 128, 255)  # Color of the rectangle (blue in this case)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        agent.move("up")
    if keys[pygame.K_DOWN]:
        agent.move("down")
    if keys[pygame.K_LEFT]:
        agent.move("left")
    if keys[pygame.K_RIGHT]:
        agent.move("right")

    # Fill the screen with a yellow background color
    window.fill((255, 255, 0))  # Yellow background

    # Draw the centered fixed rectangle
    pygame.draw.rect(window, fixed_rect_color, pygame.Rect(fixed_rect_x, fixed_rect_y, fixed_rect_width, fixed_rect_height))

    # Draw the agent as a rectangle
    rect_width, rect_height = 30, 20  # Dimensions of the rectangle representing the agent
    pygame.draw.rect(window, (255, 100, 100), pygame.Rect(agent.x, agent.y, rect_width, rect_height))

    # Display the agent's position
    position_text = font.render(f"Position: ({agent.x}, {agent.y})", True, (0, 0, 0))
    text_rect = position_text.get_rect(center=(WIDTH // 2, position_text.get_height() // 2))
    window.blit(position_text, text_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()

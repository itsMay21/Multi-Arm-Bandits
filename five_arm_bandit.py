import pygame
import random
import time
import csv

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (236, 181, 85)

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Five-Armed Bandit Task Game")

# Define font
font = pygame.font.Font(None, 36)

class BanditArm:
    def __init__(self, probability, reward_range):
        self.probability = probability
        self.reward_range = reward_range

    def pull(self):
        if random.random() < self.probability:
            return random.uniform(*self.reward_range)
        else:
            return 0

# Create bandit arms
bandit_arms = [
    BanditArm(probability=1.0, reward_range=(10, 40)),
    BanditArm(probability=1.0, reward_range=(20, 60)),
    BanditArm(probability=1.0, reward_range=(30, 80)),
    BanditArm(probability=1.0, reward_range=(15, 95)),
    BanditArm(probability=1.0, reward_range=(25, 65))
]

# Initialize game variables
score = 0
time_limit = 0  # Placeholder for time limit
current_time = time_limit
selected_arm = None
rounds = 0
total_rounds = 0
emotions = list(range(-5, 6))  # Updated emotions scale
player_name = ""
player_emotion = 0  # Updated to integer
trial_data = []

# Function to display information and start the game
def show_info_screen():
    screen.fill((255, 253, 208))
    info_text = font.render("Five-Armed Bandit Task Game", True, BLACK)
    screen.blit(info_text, (200, 100))
    pygame.display.flip()

def create_slider():
    global player_emotion  # Declare player_emotion as global to access it
    slider_rect = pygame.Rect(250, 250, 300, 20)
    slider_handle = pygame.Rect(250 + (player_emotion + 5) * 30, 245, 20, 30)  # Adjust for -5 to 5 scale
    pygame.draw.rect(screen, BLACK, slider_rect)
    pygame.draw.rect(screen, (185, 146, 79), slider_handle)
    pygame.display.flip()

    slider_active = True
    while slider_active:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if slider_handle.collidepoint(event.pos):
                    slider_active = False  # Exit the loop when slider is clicked
            elif event.type == pygame.MOUSEMOTION and slider_active:
                mouse_x, _ = event.pos
                mouse_x = max(250, min(mouse_x, 550))  # Limit slider movement within the bar
                player_emotion = (mouse_x - 250) // 30 - 5  # Adjust to -5 to 5 scale
                slider_handle.x = 250 + (player_emotion + 5) * 30  # Adjust for -5 to 5 scale
                pygame.draw.rect(screen, WHITE, slider_rect)  # Clear previous slider position
                pygame.draw.rect(screen, BLACK, slider_rect)  # Redraw slider bar
                pygame.draw.rect(screen, (185, 146, 79), slider_handle)  # Redraw slider handle
                pygame.display.flip()

    # Clear the screen after selecting emotion
    screen.fill((255, 253, 208))
    pygame.display.flip()


def get_player_info():
    global player_name, player_emotion
    screen.fill((255, 253, 208))
    name_text = font.render("Enter Your Name:", True, BLACK)
    screen.blit(name_text, (200, 200))
    pygame.display.flip()

    input_active = True
    player_name = ""
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode

        screen.fill((255, 253, 208))
        name_text = font.render("Enter Your Name:", True, BLACK)
        screen.blit(name_text, (200, 200))
        pygame.draw.rect(screen, (185, 146, 79), (200, 250, 400, 40))
        pygame.draw.rect(screen, BLACK, (200, 250, 400, 40), 2)
        name_input = font.render(player_name, True, BLACK)
        screen.blit(name_input, (210, 260))
        pygame.display.flip()

    screen.fill((255, 253, 208))
    emotion_text = font.render("Select Your Emotional State (-5 to 5):", True, BLACK)
    screen.blit(emotion_text, (150, 200))
    pygame.display.flip()

    create_slider()

def get_game_settings():
    global time_limit, total_rounds
    screen.fill((255, 253, 208))
    time_text = font.render("Enter Time Limit per trial (in 100's of milliseconds):", True, BLACK)
    screen.blit(time_text, (150, 200))
    pygame.display.flip()

    input_active = True
    time_input = ""
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        time_limit = int(time_input)
                        input_active = False
                    except ValueError:
                        pass
                elif event.key == pygame.K_BACKSPACE:
                    time_input = time_input[:-1]
                else:
                    time_input += event.unicode

        screen.fill((255, 253, 208))
        time_text = font.render("Enter Time Limit per trial (in 100's of milliseconds):", True, BLACK)
        screen.blit(time_text, (150, 200))
        pygame.draw.rect(screen, (185, 146, 79), (150, 250, 200, 40))
        pygame.draw.rect(screen, BLACK, (150, 250, 200, 40), 2)
        time_input_render = font.render(time_input, True, BLACK)
        screen.blit(time_input_render, (160, 260))
        pygame.display.flip()

    screen.fill((255, 253, 208))
    rounds_text = font.render("Enter Number of Trials:", True, BLACK)
    screen.blit(rounds_text, (250, 200))
    pygame.display.flip()

    input_active = True
    rounds_input = ""
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        total_rounds = int(rounds_input)
                        input_active = False
                    except ValueError:
                        pass
                elif event.key == pygame.K_BACKSPACE:
                    rounds_input = rounds_input[:-1]
                else:
                    rounds_input += event.unicode

        screen.fill((255, 253, 208))
        rounds_text = font.render("Enter Number of Trials:", True, BLACK)
        screen.blit(rounds_text, (250, 200))
        pygame.draw.rect(screen, (185, 146, 79), (250, 250, 200, 40))
        pygame.draw.rect(screen, BLACK, (250, 250, 200, 40), 2)
        rounds_input_render = font.render(rounds_input, True, BLACK)
        screen.blit(rounds_input_render, (260, 260))
        pygame.display.flip()

def run_game():
    global score, current_time, selected_arm, rounds, trial_data
    score = 0
    rounds = 0
    trial_data.clear()

    while rounds < total_rounds:
        run_round()

def run_round():
    global score, current_time, selected_arm, rounds, trial_data
    current_time = time_limit
    selected_arm = None
    arm_selected = False  # Flag to track if an arm has been selected in this round
    round_score = 0  # Variable to track the score earned in this round

    while current_time > 0:
        pygame.time.Clock().tick(30)  # Limit to 30 frames per second

        screen.fill((255, 253, 208))

        # Draw bandit arms
        for i, arm in enumerate(bandit_arms):
            arm_button = pygame.Rect(i * SCREEN_WIDTH // len(bandit_arms), 100, SCREEN_WIDTH // len(bandit_arms), 200)
            if selected_arm == i:  # Change color to red for selected arm
                pygame.draw.rect(screen, (255, 164, 4), arm_button)
            else:
                pygame.draw.rect(screen, BLUE, arm_button)
            arm_text = font.render(chr(ord('A') + i), True, WHITE)
            screen.blit(arm_text, (arm_button.x + 20, 150))

        # Display score and time
        round_score_text = font.render(f"Round Score: {round_score}", True, BLACK)
        screen.blit(round_score_text, (20, 50))
        # total_score_text = font.render(f"Total Score: {score}", True, BLACK)  # Add total score display
        # screen.blit(total_score_text, (20, 20))  # Adjust position as needed
        time_text = font.render(f"Time: {current_time}", True, BLACK)
        screen.blit(time_text, (SCREEN_WIDTH - 150, 20))

        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not arm_selected:
                # Check if any arm is clicked
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i, arm in enumerate(bandit_arms):
                    arm_button = pygame.Rect(i * SCREEN_WIDTH // len(bandit_arms), 100, SCREEN_WIDTH // len(bandit_arms), 200)
                    if arm_button.collidepoint(mouse_x, mouse_y):
                        selected_arm = i
                        reward = arm.pull()
                        round_score += reward  # Accumulate the score for this round
                        trial_data.append([rounds + 1, current_time, i, reward])  # Save data for this arm selection
                        arm_selected = True  # Mark arm as selected for this round
                        break
            elif event.type == pygame.KEYDOWN and not arm_selected:
                # Check for key presses
                if event.key == pygame.K_q:
                    selected_arm = 0  # Arm A
                elif event.key == pygame.K_w:
                    selected_arm = 1  # Arm B
                elif event.key == pygame.K_e:
                    selected_arm = 2  # Arm C
                elif event.key == pygame.K_r:
                    selected_arm = 3  # Arm D
                elif event.key == pygame.K_t:
                    selected_arm = 4  # Arm E

                if selected_arm is not None:
                    reward = bandit_arms[selected_arm].pull()
                    round_score += reward  # Accumulate the score for this round
                    trial_data.append([rounds + 1, current_time, selected_arm, reward])  # Save data for this arm selection
                    arm_selected = True  # Mark arm as selected for this round

        current_time = max(0, current_time - 1)

    # Check if an arm was selected after the trial time ends
    if not arm_selected:
        trial_data.append([rounds + 1, "NOT SELECTED"])  # Record "NOT SELECTED"

    score += round_score  # Add the round score to the total score
    rounds += 1
    data.extend(trial_data)
    trial_data.clear()



def save_data():
    with open('bandit_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Participant Name', 'Emotion'])
        writer.writerow([player_name, player_emotion])  # Save integer emotion value
        writer.writerow(['Round', 'SelectedArm', 'Reward','Response Time' 'TotalScore'])
        total_score = 0  # Calculate total score
        round_number = 1  # Initialize round number
        for round_data in data:
            if len(round_data) == 4:  # Check if round_data has correct structure
                response_time, selected_arm, reward = round_data[1:]  # Ignore response time
                round_score = reward if reward != "NOT SELECTED" else 0
                total_score += round_score
                writer.writerow([round_number, chr(ord('A') + selected_arm), reward,response_time*100, total_score])
                round_number += 1

def main():
    show_info_screen()
    get_player_info()
    get_game_settings()
    run_game()
    save_data()

if __name__ == '__main__':
    data = []  # Global variable to store trial data
    main()


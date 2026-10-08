# Mandie Mason - Final Project - BioShock Game

import random
import time

import cv2
import pygame
from pygame import mixer

# Declarations
START_ITALIC = "\033[3m"  # words after this tag are italic. this tag begins bolding.
END_ITALIC = "\033[0m"  # words before this are italic. this tag ends the bold.
multiple_newlines = "\n" * 4
LOGO_WIDTH = 120


def a_burning_memory():  # Function that plays the intro song infinitely at 30% volume
    mixer.music.load("assets/audio/ABurningMemory.mp3")
    mixer.music.set_volume(.3)
    mixer.music.play(loops=-1)


def beyond_the_sea():  # Function that plays the intro song infinitely at 30% volume
    mixer.music.load("assets/audio/BeyondTheSea.mp3")
    mixer.music.set_volume(.1)
    mixer.music.play(loops=1)


def rain():  # Function that plays rain infinitely at 20% volume
    rain = mixer.Sound("assets/audio/rain.mp3")
    rain.set_volume(.2)
    rain.play(loops=-1)  # =-1 makes the loop play infinitely


def playVideo():  # funciton for playing the video
    capture = cv2.VideoCapture("assets/video/EnteringRapture.mp4")  # capture variable with video name

    mixer.init()
    mixer.music.load("assets/audio/BeyondTheSea.mp3")
    mixer.music.set_volume(.1)
    mixer.music.play(loops=-1)

    while True:
        ret, frame = capture.read()  # read video frame by frame
        if not ret:
            break
        cv2.imshow("assets/video/Entering Rapture Cutscene", frame)
        cv2.waitKey(15)

    capture.release()
    cv2.destroyAllWindows()


def hacking():
    # screen, bar, and checkpoints variables
    win_x = 736
    win_y = 414
    checkpoints = 3
    timer_duration = 10
    bar_speed = 3
    bar_width = 150
    bar_height = 10
    dot_radius = 8

    black = (0, 0, 0)  # screen color
    white = (255, 255, 255)  # bar color
    red = (255, 0, 0)  # text and checkpoints color

    pygame.init()  # inits pygame
    mixer.init()

    alarm = mixer.Sound("assets/audio/alarm.mp3")
    alarm.set_volume(.1)
    alarm.play(loops=1)

    screen = pygame.display.set_mode((win_x, win_y))  # sets up the screen with size variables
    pygame.display.set_caption("Hacking Game")  # sets the window caption to 'Hacking Game'
    background_image = pygame.image.load("assets/images/hacking.jpeg")  # sets the background to an image from the disk

    bar_position = [win_x // 2, win_y // 2]  # bar's position
    dot_x = random.randint(dot_radius, win_x - dot_radius)  # x value of the checkpoint
    dot_y = bar_position[1]  # y value of the checkpoint (same as y value for bar)
    score = 0  # init the beginning score

    start_time = time.time()  # starts the games timer

    running = True  # flag that lets program know to run game

    def show_score():  # function that displays the score
        font = pygame.font.SysFont("arial", 24)  # init the font and size
        score_text = "Checkpoints: " + str(score)  # variable to store the checkpoint score
        score_surface = font.render(score_text, True, red)  # renders the score on a display surface
        screen.blit(score_surface, (10, 10))  # draws it into the program to be shown

    def game_over():  # the function that handles when the game is over
        screen.fill(black)  # sets the screen black
        font = pygame.font.SysFont("comic sans", 40)  # init the font and size
        if score >= checkpoints:  # if the score is greater than or equal to the checkpoint amount
            message = "HACK SUCCESSFUL!"  # the message to show is 'HACK SUCCESSFUL'
            color = white  # in the color white
        else:  # anything else,
            message = "HACK FAILED!"  # display the message 'HACK FAILED'
            color = red  # in the color red

        text_surface = font.render(message, True, color)  # renders the final message on a display surface
        screen.blit(text_surface, (win_x // 4, win_y // 2 - 20))  # displays the final message centered on the screen
        pygame.display.flip()  # updates the screen
        pygame.time.wait(3000)  # waits 3 seconds before closing

    while running:  # while running is True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if the user quits
                pygame.quit()  # the game quits
                return  # and returns to the program
            if event.type == pygame.KEYDOWN:  # when the program detects a button press
                if event.key == pygame.K_SPACE:  # if the buttpm is the spacebar
                    if bar_position[1] <= dot_y <= bar_position[
                        1] + bar_height:  # i tried different combinations like == but it kept breaking my program
                        score += 1  # add to the score
                        dot_x = random.randint(dot_radius, win_x - dot_radius)  # place another dot in a random x coord
                        dot_y = bar_position[1]  # place the dot in the same y level as the bar
                        if score >= checkpoints:  # if the score equals or surpasses the checkpoint variable
                            running = False  # end the game

        bar_position[0] += bar_speed  # move the bar at the selected speed
        if bar_position[0] > win_x - bar_width or bar_position[0] < 0:  # if the bar hits the edge of the screen
            bar_speed = -bar_speed  # go backwards

        screen.blit(background_image, (0, 0))  # import the background image
        pygame.draw.rect(screen, white, (bar_position[0], bar_position[1], bar_width, bar_height))  # draw the bar
        pygame.draw.circle(screen, red, (dot_x, dot_y), dot_radius)  # draw the checkpoint
        show_score()  # run the show score function

        current_time = time.time()  # get the current time
        elapsed_time = current_time - start_time  # find elapsed time by subtracting the start time from the timers duration
        remaining_time = timer_duration - elapsed_time  # the remaining time is the time elapsed from the duration
        remaining_time = max(0, remaining_time)  # max makes sure it doesnt go below 0
        timer_text = "Time Left: " + str(
            remaining_time)  # stores the text for the timer countdown and converts the remain time to a string

        font = pygame.font.SysFont("arial", 24)  # sets the font
        timer_surface = font.render(timer_text, True, red)  # stores the display the timer text
        screen.blit(timer_surface, (win_x - 128, 10))  # displays the timer dispay surface at given coordinates

        if remaining_time <= 0:  # if the timer hits 0
            running = False  # the game ends

        pygame.display.flip()  # update the screen

    game_over()  # after running = false, call game over function
    pygame.quit()  # then end the game

def wait_for_user_input():
    input("")


bioshockLogo = {
    1: "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣄⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    2: "⠀⣀⣀⣀⣠⣤⣤⣤⠴⠶⠶⡖⡖⠚⠿⠛⠛⣙⣋⣛⣋⣋⣋⣍⣥⣡⣭⢤⣌⣍⡭⣭⣬⡵⢦⠴⣦⠴⣦⣦⣤⣤⣦⣴⣦⣶⣶⣮⣶⣴⣤⣤⣤⣤⣬⣩⣍⣭⣭⣡⣭⣬⣭⣩⣉⣛⣉⣉⣛⡲⠶⠶⠒⠶⠲⣦⡤⡤⣤⣄⣀⣀⣀⡀⠀",
    3: "⢸⡟⢋⣉⣤⣤⣤⣤⣶⣾⡲⣏⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣶⣳⣒⣮⣿⣿⣿⣿⣿⣷⣟⣴⣿⣿⣿⣧⣟⣿⣼⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⡾⣝⣯⣓⣞⣴⣿⣿⣿⣿⣿⣿⣿⣿⣻⣽⣿⣿⡷⣾⣷⣶⣭⣥⣯⣽⣛⡶",
    4: "⢸⡇⢸⣿⣿⡟⢛⠛⠛⢻⠻⢿⣿⣿⣿⠟⢻⣿⣿⣿⡿⠟⠛⠉⠋⣛⠻⢿⣟⣿⣿⣿⣿⠛⡛⠻⠿⣿⣿⡛⢻⣷⣻⢾⣿⡟⢻⣿⣿⣿⣿⡿⢟⠛⢉⠛⠻⢿⣯⣒⣯⣿⣿⣿⠿⠛⠿⠛⠛⠿⢿⣿⣹⣿⠛⢻⣿⣿⡿⠟⣻⣿⣿⣿⠴",
    5: "⢸⡇⢸⣿⣿⡇⠀⣿⣾⣿⣶⡀⢻⣿⣿⢠⢾⣿⣿⠏⠀⣠⣶⡿⢿⣿⣦⡀⠻⣿⣿⡇⠠⣿⣿⣧⣶⣿⣿⠁⠰⣿⣿⣿⣿⡅⢸⣿⣿⡿⠃⣠⣾⣿⣻⣷⣦⡀⠉⢻⣿⣿⡿⠉⢠⣴⣿⣾⣿⢦⣄⣩⢿⣿⠆⢹⣿⠟⠁⣰⣿⣿⣿⣿⠟",
    6: "⢸⣿⢹⣿⣿⡇⠰⠿⠿⢿⡛⣀⣾⣿⣿ ⢸⣿⡏⠀⣾⣿⣿⣿⣿⣿⣿⣿⡤⢹⣿⣷⣀⠙⢻⣿⣿⣿⣿⡀⠘⠛⠛⠟⠛⠃⢸⣿⣿⠄⣴⣿⣿⣿⣿⣽⣿⣿⡆⠈⣿⡿⠀⣰⣿⣿⣯⣿⢻⣛⣽⡗⣺⣿⠆⢸⠁⢠⣜⠿⣿⣿⣾⣿⢺",
    7: "⢸⡿⢸⣿⣿⡇⠀⣶⣴⣶⣿⣏⠻⣿⣿⠀⢸⣿⡇⠘⣿⣿⣿⣿⣿⣿⣿⣿⠏⢹⣿⣿⣿⣷⣤⠘⢻⣿⣿⠄⢠⣦⣶⣴⣦⡄⠰⣿⣿⠖⢻⣿⣿⣿⣿⣾⣿⣿⡇⠀⣿⣯⠀⢻⣯⣿⣜⣺⣵⣿⣾⣟⢼⣿⠀⢰⣄⠈⢿⣿⣯⣷⣹⣿⣠",
    8: "⢸⡇⣽⣿⣿⡇⠀⣿⣿⣿⣿⡿⠀⣸⣿⠀⢸⣿⣿⡀⠙⢿⣿⣿⣿⣿⡿⠋⠀⣼⣿⡿⢿⣿⣿⡗⠀ ⢻⣿⡀⠰⣿⣿⣿⣿⣿⠄⢘⣿⣿⣄⠈⠻⣿⣿⣿⣿⣿⠟⠀⣰⣛⣿⠀⠻⣿⣿⣿⣿⣿⣿⠿⢿⣿⠀⢸⣿⣦⠀⠹⣧⣿⣽⣿⢫",
    9: "⢸⣷⢻⣿⣿⡇⠀⢉⠉⣉⣅⣀⣠⣿⣿⢀⢸⣿⣿⣿⣤⣀⠈⠉⠉⠁⢀⣠⣾⣿⣿⣧⣀⠉⠉⠁⣠⣿⣿⡀⢈⣿⣝⣿⣿⠂⠘⣾⣿⣿⣶⣄⠀⠉⠉⠉⠀⣠⣔⣻⣶⢿⣿⠦⣀⠀⠙⠋⠀⣀⣴⣿⣿⡿⠀⠸⣾⣿⣧⡀⠘⢿⣿⣿⢸",
    10: "⢸⡿⣾⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣼⣿⣿⡿⣿⢿⣿⣿⣟⣿⣶⣿⡟⢯⡝⣿⣼⡿⣾⣿⣿⠿⣷⣶⣾⣿⣿⣿⣿⣿⢿⣟⣵⣿⡻⣽⣿⢿⣿⣿⢠",
    11: "⢸⡇⢿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠡⣈⣿⣿⣗⣯⢿⣿⠿⠿⢿⣿⣿⣿⣿⣿⡗⠋⢛⢿⣿⣿⢽⣿⣿⣯⣿⣿⡿⠠⡀⢸⣷⣾⣿⣽⣿⣿⣽⢶⣻⡟⢁⡺⣭⠦⣍⠐⠌⠹⡿⣿⠭⢓⣿⡾⣿⣛⣾⣝⣳⢎⣿⣋⣾⣿⢰",
    12: "⢸⣧⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠧⡌⢦⡉⢳⢿⣇⠛⢺⣿⠈⢚⣵⡙⣿⣿⡿⢿⣧⠀⠊⢺⣿⣿⢾⣿⣿⣿⣿⡟⣠⢠⣼⠛⢻⣿⣿⡿⠟⡻⢫⢧⡟⠀⢸⢀⡇⢄⡀⡎⠿⠀⢻⣯⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢸",
    13: "⠀⠉⠓⠢⠁⢨⢭⡉⠙⣛⠻⠛⠻⠿⡿⠿⣥⣿⣶⣠⣸⣞⣹⣦⣼⣿⠃⠂⢾⣡⣿⣿⠐⠇⡩⠐⠀⢸⡏⣿⡽⢺⣿⠙⣿⡇⢰⣟⢸⢠⣹⣿⡟⠀⠀⢀⠸⡟⢇⣤⣿⣈⡇⠸⢁⣧⣼⣿⣿⡿⠿⢿⠿⠛⠛⠛⢋⡉⠉⢉⣄⠀⠠⠀⠊",
    14: "⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠀⠁⠉⠉⠙⠒⠒⠂⠠⠌⡉⢉⣙⠛⠛⠛⠶⠤⠬⢷⣿⣿⣀⣀⣱⣭⣁⣽⣗⣿⣗⢹⣿⠀⣹⡇⢀⠘⢸⠐⢻⣿⣧⣂⣨⢥⡤⠿⠿⠿⠛⠛⠛⢋⣉⠉⠡⠤⠀⠄⠒⠀⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
}

backstory = {
    1: ["[Press Enter to proceed...]",
        "You wake up to the sound of rain lightly tapping on your tent roof.",  # Backstory Snip Part 1
        "Opening your tent's zipper door, you stick your hand outside to feel the cool pellets of water stinging your skin.",
        "Much like the rain pooling outside in the dents of the road, your eyes begin to fill with tears. ",
        "Trying to hold them in you fail, and a tear slowly falls down your cheek as you think about the last year of your life.",
        "\n"],

    2: [START_ITALIC + "After your parents left rather suddenly, you were left to figure things out on your own. ",
        # Memory
        "Unable to keep the house due to bills and upkeep, you had no choice but to leave. ",
        "After wandering the streets for days, you were brought in by a 'gang' in your town, whom raised you through your teenage and young adult years.",
        "They fed you and gave you a roof over your head. They're basically your family now and you love them as if they were blood.",
        "\n" + END_ITALIC],

    3: ["Coming out of your memory, you close your tent and get dressed.",  # Backstory Snip Part 2
        "It's been months since you've been able to find work.",
        "The group is starting to struggle for money and more fights are breaking out between everyone.",
        "You feel stuck, everyday you constantly wonder where your family went and why you haven't heard anything from them.",
        "That morning you decide to go back to the family's home to see if you can find any hints of their whereabouts.",
        "Without mentioning your plans to anyone, you head out. Umbrella in hand, walking down the road to your old home.",
        "\n\n"
        "You walk up to the front door and twist the doorknob. As you walk in, memories flood your mind like a dam bursting.",
        "Conversations you overheard about your medical conditions and your family's finances being the most prominent in your memories.",
        "All of the furniture is untouched and covered in dust. You wonder why they left without taking anything.",
        "On the kitchen counter, you see a letter tucked under a vase.",
        "Picking it up, you recognize the seal to be from the government. You open the letter and scan the words line-by-line.",
        "\n\n"],

    4: [START_ITALIC + "Dear Gilman Family,\n\n",  # Government Letter
        "      We are pleased to inform you of a unique and unprecedented opportunity.",
        "You have been selected to participate in an exclusive event known as 'Rapture.'",
        "This program is designed to offer an enriching experience in prepare for the possible war on our nation.",
        "We invite you to join us at Rapture on November 5th, 1946. Further details will be provided in due time.",
        "Please keep an eye out for a message from Andrew Ryan of Ryan Industries.",
        "\n",
        "Sincerely,",
        "\n",
        "Governor George E. Lopez ",
        "\n\n" + END_ITALIC],

    5: [
        "You weren't able to read some of the letter as something had been spilt on it and the ink muddled together, but you understood what you needed to.",
        "On the counter you see another letter, this time from Andrew Ryan.",  # Backstory snip part 3
        "Assuming this is the follow-up the government-issued letter mentioned, you open it up and begin reading.",
        "Inside the letter, an address is listed and further instructions about how to get inside the compound.",
        "The excitement of getting closer to reuniting with your siblings fills your head, and you throw the letters in your bag and run out the door.",
        "\n",
        "Later that night, you finally find the facility to get into rapture.",
        "To your surprise the only thing guarding the door to the elevator is a security camera.",
        "You walk up to the door, and examine the keypad. The buttons are coated in dust, but there are faint prints on certain buttons.",
        "\n\nSuddenly, a loud alarm starts blaring and the security camera begins flashing red.",
        "'Nonononono,' You panic. Scurrying over to the camera, you try to pull the wires out to turn off the alarm.\n\n"],

    6: ["As fast as it came on, the alarm turns off as you rip the wires out.",  # Backstory snip part 4
        "You exhale a long breath, thankful the ringing stopped.\n",
        "As you walk back over to the keypad and you hear dinging.\n",
        "'An elevator?' You wonder.\n",
        "\n",
        "Just then, the compound doors open, and presented to you is a large elevator with a lever in the back.\n",
        "Looking around for anyone else around, you take a slow step onto the elevator.\n",
        "The doors close as you pull the lever. With a shake, you slowly start to descend.\n"]
}

outro = [
    "The elevator dings and the doors open. You stand in the doorway, taking in your environment, seeing propaganda signs hung around you.",
    "Above your head, glass ceilings shield you from the pressure of the Atlantic Ocean bearing down on-top of you.",
    "\n",
    "A large sign above the elevator reads 'Bathysphere Station.' Seeing this sign caused more memories to flood you.",
    "Conversations between your parents you overheard about them discussing the Bathysphere leaves you more determined than ever.",
    "\n",
    "You start to walk down the hallway in front of you. Knowing that you're closer than ever to your family.",
    "Just then, a shadow crosses the wall in front of you, and distant laughs echo the halls.",
    "'I'm in for more than I could ever think, huh...' You quietly say to yourself. This is only your beginning.",
]


def main_game():
    mixer.init()
    a_burning_memory()
    rain()

    print(multiple_newlines)

    for key in backstory.keys():
        for line in backstory[key]:
            if line == "\n":
                print(line)
            else:
                print(line, end="")
                wait_for_user_input()

            # Check for the specific line and call hacking() for key 5
        if key == 5:
            for line in backstory[key]:
                if line == "\n\nSuddenly, a loud alarm starts blaring and the security camera begins flashing red.":
                    hacking()
    playVideo()

    print(multiple_newlines)
    beyond_the_sea()

    for line in outro:
        if line == "\n":
            print(line)
        else:
            print(line, end="")
            wait_for_user_input()

    print(multiple_newlines)
    for line in bioshockLogo.values():  # for every value in the dictionary
        print(line.center(LOGO_WIDTH))  # print it


main_game()

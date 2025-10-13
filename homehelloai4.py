import random
from colorama import Fore
def get_ai_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def determine_winner(player, ai):
    if player == ai:
        return 'tie'
    elif (player == 'rock' and ai == 'scissors') or \
         (player == 'scissors' and ai == 'paper') or \
         (player == 'paper' and ai == 'rock'):
        return 'win'
    else:
        return 'lose'
def play_game():
    print(f"{Fore.GREEN} Welcome to Rock, Paper, Scissors!")
    print(f"{Fore.GREEN} Type 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit.\n")
    score = {'win': 0, 'lose': 0, 'tie': 0}
    while True:
        player = input("Your move: ").strip().lower()
        if player == 'exit':
            print("\nFinal Score:")
            print(f"{Fore.CYAN} Wins: {score['win']}, Losses: {score['lose']}, Ties: {score['tie']}")
            print(f"{Fore.YELLOW} Thanks for playing!")
            break
        if player not in ['rock', 'paper', 'scissors']:
            print(f"{Fore.RED} Invalid input. Please type 'rock', 'paper', or 'scissors'.\n")
            continue
        ai = get_ai_choice()
        print(f"AI chose: {ai}")
        result = determine_winner(player, ai)
        if result == 'win':
            print(f"{Fore.GREEN} You win!\n")
        elif result == 'lose':
            print(f"{Fore.RED} You lose!\n")
        else:
            print(f"{Fore.YELLOW} It's a tie!\n")
        score[result] += 1
play_game()

# Hacerle un refactor al juego
import random

def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    if not user_option in options:
      message_decorator('Esa opcion no es valida', '\\')
      return None, None

    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        message_draw(user_option, computer_option)
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            message_win(user_option, computer_option)
            user_wins += 1
        else:
            message_lose(user_option, computer_option)
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            message_win(user_option, computer_option)
            user_wins += 1
        else:
            message_lose(user_option, computer_option)
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            message_win(user_option, computer_option)
            user_wins += 1
        else:
            message_lose(user_option, computer_option)
            computer_wins += 1
    return user_wins, computer_wins

def message_decorator(message, decorator):
    message_len = len(message)
    print(f'\n{decorator * message_len}\n{message}\n{decorator * message_len}')

def game_status(user_wins, computer_wins):
    print(f'user_wins: {user_wins}')
    print(f'computer_wins: {computer_wins}')

def message_draw(user_option, computer_option):
    message = f'{user_option} empata con {computer_option}'
    message_decorator(message, decorator='#')

def message_win(user_option, computer_option):
    message = f'{user_option} gana con {computer_option}'
    message_decorator(message, decorator='+')

def message_lose(user_option, computer_option):
    message = f'{user_option} pierde con {computer_option}'
    message_decorator(message, decorator='-')

def check_winner(user_wins, computer_wins):
    if computer_wins == 2:
        message_decorator('El ganador definitivo es la computadora', '^*')
        return True
    elif user_wins == 2:
        message_decorator('El ganador definitivo es el usuario', '<')
        return True
    
def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        game_round = f'ROUND {rounds}' 
        message_decorator(game_round, '*')

        game_status(user_wins, computer_wins)
        
        user_option, computer_option = choose_options()
        
        if user_option == None and computer_option == None:
            continue
        
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

        if check_winner(user_wins, computer_wins):
            return
        
        rounds += 1

run_game()
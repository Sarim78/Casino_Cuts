import time

time.sleep(0.5)
heist = input('What type of casino heist you doing: ')

time.sleep(0.6)
Players = float(input('How much members are in your casino heist: '))

if Players == 2:
    two_money = input('How much did you just rob: ')
    two_lester = input('How much does lester take: ')
    two_person = input('What is a first person cut: ')
    two_human = input('What is a second person cut: ')

    left_over = float(two_money) - float(two_lester)
    print(f'Your money after lester takes it {float(left_over)}!\n')

    cut_1 = int(two_person) / 100 * int(left_over)
    print(f'Player 1 will get {float(cut_1)}!\n')

    cut_2 = int(two_human) / 100 * int(left_over)
    print(f'Player 2 will get {float(cut_2)}!\n')

    print(f'Player 1 will get {cut_1}, Player 2 will get {cut_2}!\n')

    print(f'I hope your {heist} went well:)')

elif Players == 3:
    three_money = input('How much did you just rob: ')
    three_lester = input('How much does lester take: ')
    three_person = input('What is a first person cut: ')
    three_human = input('What is a second person cut: ')
    three_random = input('What is a third person cut: ')

    left_over_three = float(three_money) - float(three_lester)
    print(f'Your money after lester takes it {float(left_over_three)}!')

    cut_3 = int(three_person) / 100 * int(left_over_three)
    print(f'Player 1 will get {float(cut_3)}!\n')

    cut_4 = int(three_human) / 100 * int(left_over_three)
    print(f'Player 2 will get {float(cut_4)}!\n')

    cut_5 = int(three_human) / 100 * int(left_over_three)
    print(f'Player 3 will get {float(cut_5)}!\n')

    print(f'Player 1 will get {cut_3}, Player 2 will get {cut_4}, Player 3 will get {cut_5}!\n')

    print(f'I hope your {heist} went well:)')

elif Players == 4:
    four_money = input('How much did you just rob: ')
    four_lester = input('How much does lester take: ')
    four_person = input('What is a first person cut: ')
    four_human = input('What is a second person cut: ')
    four_random = input('What is a third person cut: ')
    four_animal = input('What is a fourth person cut: ')

    left_over_four = float(four_money) - float(four_lester)
    print(f'Your money after lester takes it {float(left_over_four)}!')

    cut_6 = int(four_person) / 100 * int(left_over_four)
    print(f'Player 1 will get {float(cut_6)}!\n')

    cut_7 = int(four_human) / 100 * int(left_over_four)
    print(f'Player 2 will get {float(cut_7)}!\n')

    cut_8 = int(four_random) / 100 * int(left_over_four)
    print(f'Player 3 will get {float(cut_8)}!\n')

    cut_9 = int(four_animal) / 100 * int(left_over_four)
    print(f'Player 4 will get {float(cut_9)}!\n')

    print(f'Player 1 will get {cut_6}, Player 2 will get {cut_7}, Player 3 will get {cut_8}, \n'
          f'Player 4 will get {cut_9}!')

    print(f'I hope your {heist} went well:)')

else:
    print('Sorry, Casino heist only can go up to 4 players!')
    exit()

import random
import time

def play_game():
	is_correct = False

	print ('What range of numbers would you like to play with?')
	print ('Low number?')
	low_number_str = raw_input()
	if low_number_str == 'restart':
		return 'restart'

	print ('High number?')
	high_number_str = raw_input()
	if high_number_str == 'restart':
		return 'restart'

	low_number = float(low_number_str)
	high_number = float(high_number_str)
 
	before_decimal = random.randint (low_number, high_number)
 	after_decimal = random.randint (low_number, high_number)
 	
 	answer_str = '{}.{}'.format(before_decimal, after_decimal)
	answer = float(answer_str)

	print('Guess a number from {} to {}'.format(low_number, high_number))

	num_guesses = 0
	start_time = time.time()

	while not is_correct:
		user_guess = raw_input()
		if user_guess == 'restart':
				return 'restart'
		num_guesses = num_guesses + 1
		if float(user_guess) == answer:
			end_time = time.time()
			time_took = end_time - start_time
			print ('You are correct! The answer was {}. You took {} guesses and {} seconds'.format(
				answer,  num_guesses, time_took))
			break
		elif float(user_guess) < answer:
			print ('Your answer was too low. Try Again')
		else:
			print ('Your answer was too high. Try Again')

end_state = 'restart'

while end_state == 'restart':
	end_state = play_game()
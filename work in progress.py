  if (guesses_0 != guesses):
            letter = guesses_0[i].lower()
        else:
            if (i != 0):
                viable, current_guess = generate_viable_dictionary(viable,current_guess[0])
                print (current_guess)
                for j in current_guess:
                    if j not in guesses:
                        letter = j
                        guesses = guesses + letter
                        print(guesses)
                        break
            elif (i == 0):
                letter = current_guess[0]
                guesses = guesses + letter
                print (guesses)
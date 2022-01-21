import os
import json
import time
import requests

class quiz_game:

    def api_trivia(self):
        api_url = 'https://opentdb.com/api.php?amount=5&difficulty=easy&type=boolean'
        response = requests.get(api_url)
        questions = json.loads(response.text)
        
        return questions['results']

    def true_or_false(self,i):
        print('1: True')
        print('2: False\n')

        wait_to_user = True
        while wait_to_user:
            print('Make your selection: ')
            answer = int(input())

            if answer == 1:
                answer = 'True'
                wait_to_user = False
            if answer == 2:
                answer = 'False'
                wait_to_user = False                
        
        if answer == i['correct_answer']:
            print('Correct!')
            time.sleep(.9)
            return True
        else:
            print('You have failed!')
            time.sleep(.9)
            return False
    def score(self,score):
        os.system('cls')
        print(f"Score: {score}")

    def play_game(self):
        trivia_data = self.api_trivia()
        score = 0
        
        for i in trivia_data:
            os.system('cls')
            print(f"Category: {i['category']}")
            print(f"Difficulty: {i['difficulty']}\n")
            print(f"Question:\n{i['question']}\n") 
            question = self.true_or_false(i)

            if question:
                score += 1
        
        self.score(score)
            
app = quiz_game()
app.play_game()
        




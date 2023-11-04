from copy import deepcopy
import matplotlib.pyplot as plt


class healthQuiz:

    def __init__(self):
        self._questions = [
            "1: Do you see a gold, pollen-like substance on your betta when you shine a light on them?",
            "2: Does your betta have white spots on it?",
            "3. Does your betta seem lethargic or more inactive than usual?",
            "4. Does your betta seem to have a swollen abdomen?",
            "5. Does your betta seem to have trouble swimming?",
            "6. Do your betta's eyes seem to be popping out?",
            "7. Do your betta's fins seems to look weathered?",
            "8. Does your betta have clamped fins?",
            "9. Take a look at your betta's head. Do you see something similar to a hole in the area?",
            "10. Is your betta trying to scratch against surfaces?",
            "11. Does your betta refuse to eat?",
            "12. Does your betta seem to have trouble breathing. Do you see it gasping?",
            "13. Do you see cottony patches on your betta?",
            "14: Are your betta's scales flaking off?",
            "15: Is your betta 'pineconing' aka puffing out like a pufferfish?",
            "16: Does you betta appear to be floating at the top of the tank or on the bettas side?",
            "17. Does your betta's feces appear to be pale and stringy?"

        ]

        self._options = ("1. Yes", "2. No", "3. Previous Question", "4. Restart Quiz")

        self._scores = {"Velvet": 0,
                        "Ich": 0,
                        "Popeye": 0,
                        "Fin Rot": 0,
                        "Columnaris": 0,
                        "Hole in \nthe Head": 0,
                        "Dropsy": 0,
                        "Swim Bladder \nDisorder": 0,
                        "Constipation": 0}
        self._record = {}
        self._answers = {1: ["Velvet"],
                         2: ["Ich"],
                         3: ["Velvet", "Ich", "Popeye", "Hole in \nthe Head", "Dropsy", "Constipation"],
                         4: ["Swim Bladder \nDisorder", "Constipation"],
                         5: ["Swim Bladder \nDisorder", "Constipation"],
                         6: ["Popeye"],
                         7: ["Fin Rot", "Velvet", "Columnaris"],
                         8: ["Velvet", "Ich"],
                         9: ["Hole in \nthe Head"],
                         10: ["Velvet", "Ich", "Columnaris"],
                         11: ["Ich", "Velvet", "Popeye", "Hole in \nthe Head", "Dropsy", "Constipation"],
                         12: ["Ich", "Velvet", "Columnaris", "Dropsy"],
                         13: ["Columnaris"],
                         14: ["Columnaris", "Velvet"],
                         15: ["Dropsy"],
                         16: ["Swim Bladder \nDisorder"],
                         17: ["Constipation"]}

    def introduction(self):
        intro = "Hello and welcome to the Betta Health Quiz!" \
                "\nThis quiz was made to help you further see what the " \
                "\npossible illnesses are of you betta. It must be stated that" \
                "\nthis is a student-created program, and should not take" \
                "\nprecedence over the opinions of a medical professional." \
                "\nIf you feel you have a good idea of what your betta's" \
                "\nillness might be, feel free to skip the quiz as needed." \
                "\nAlso, if you feel you answered a question wrong, you can" \
                "\nalways go back a question, or restart the quiz entirely!" \
                "\nTake your time to read the questions thoroughly and I " \
                "\nwish your betta a speedy recovery!" \
                "\n- Blake Jennings"
        print(intro)

    def questions(self):
        self._record[-1] = deepcopy(self._scores)
        question_num = 0
        while question_num < len(self._questions):
            print("--------------------------------")
            print(self._questions[question_num])
            for option in self._options:
                print(option)
            ans = input("Please type 1, 2, 3, or 4 and then enter: ")
            if ans == "1":
                for item in self._answers[question_num + 1]:
                    self._scores[item] += 1
                self._record[question_num] = deepcopy(self._scores)
                question_num += 1
            elif ans == "3":
                if question_num >= 1:
                    self._scores = deepcopy(self._record[question_num - 2])
                else:
                    self._scores = deepcopy(self._record[-1])
                question_num -= 1
            elif ans == "2":
                self._record[question_num] = deepcopy(self._scores)
                question_num += 1
            elif ans == "4":
                self._scores = deepcopy(self._record[-1])
                question_num = 0
            print(self._scores.values())
        plt.bar(*zip(*self._scores.items()))
        plt.show()


quiz = healthQuiz()
quiz.introduction()
quiz.questions()

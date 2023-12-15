import webbrowser
from copy import deepcopy
import matplotlib.pyplot as plt
import operator
from Disease_info import *
import zmq
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk

socket = zmq.Context().socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5500")


class BettaHealth:

    def __init__(self):
        self._diseases = ["Velvet",
                          "Ich",
                          "Popeye",
                          "Fin Rot",
                          "Columnaris",
                          "Hole in the Head",
                          "Dropsy",
                          "Swim Bladder Disorder",
                          "Constipation"]

        self._quiz = healthQuiz()
        self._links = []
        self._home_button = None
        self._quiz_button = None
        self._disease_buttons = []
        self._button_page = None
        self._velvet_img = tk.Label(master=root, image=ImageTk.PhotoImage(Image.open("Velvet.png")))

    def start_program(self):
        """
        Initializes tkinter buttons for home page and diseases.
        """
        # initialize disease buttons
        for item in self._diseases:
            button = ttk.Button(
                root,
                command=lambda i=item: [self.clear_buttons(), self.disease_page(i)]
            )
            self._disease_buttons.append(button)

        # initialize home screen button
        self._home_button = ttk.Button(
            root,
            command=lambda: [self.clear_buttons(), self.home_page()]
        )
        # initialize quiz button
        self._quiz_button = ttk.Button(
            root,
            command=lambda: [self.clear_buttons(), self._quiz.startup()]
        )

        # initialize disease list button
        self._button_page = ttk.Button(
            root,
            command=lambda: [self.clear_buttons(), self.button_page()]
        )

    def clear_buttons(self):
        """
        Clears the buttons and links when changing pages in tkinter.
        """
        img_label.config(image=img)
        if self._home_button:
            self._home_button.pack_forget()
        if self._quiz_button:
            self._quiz_button.pack_forget()
        for button in self._disease_buttons:
            button.pack_forget()
        if self._button_page:
            self._button_page.pack_forget()
        for link in self._links:
            link.pack_forget()

    def home_page(self):
        """
        Displays opening page of BettaHealth.
        """
        if not self._home_button:
            self.start_program()
        intro = "Hello and welcome to BettaHealth! BettaHealth is a program designed to help you better understand " \
                "the health of your betta fish. It is recommended that first time users of this program take the " \
                "BettaHealth Symptoms Quiz to better understand what potential illness their betta might have. If you " \
                "feel you know what your betta might have, however, you can skip the quiz and immediately go to the " \
                "list of common betta illnesses to find out more about each one and some treatment options. \nThis " \
                "program is dedicated to my betta fish, GG!"
        qs_label.configure(text=intro)
        self._quiz_button.pack(pady=5)
        self._quiz_button.configure(text="Take Quiz", state="normal")
        self._button_page.pack(pady=5)
        self._button_page.config(text="Skip Quiz", state="normal")

    def button_page(self):
        """
        Page of Disease Buttons which go to individual disease page if clicked.
        """
        if not self._home_button:
            self.start_program()
        intro = "Here is a list of the nine most common betta illnesses. Each gives a small description of the " \
                "disease and some treatment options to consider purchasing."
        qs_label.config(text=intro)
        for i, button in enumerate(self._disease_buttons):
            button.pack(pady=5)
            button.config(text=self._diseases[i], state="normal")
        self._home_button.pack(pady=5)
        self._home_button.config(text="Home", state="normal")

    def disease_page(self, disease_name):
        """
        Individual disease page with info on disease.
        """
        change_image(disease_name)
        info = info_dict[disease_name]
        result = f'{disease_name}\n\n{info} \nHere are some items that could help with treatment:'
        qs_label.config(text=result)
        links = self._quiz.request_links(disease_name)
        for ind, item in enumerate(links[1]):
            link = ttk.Label(root, text=links[0][ind], cursor="hand1", font=["Helvetica", 20, 'underline'])
            link.pack()
            self._links.append(link)
            link.bind("<Button-1>", lambda e, url=item: webbrowser.open_new(url))
        self._button_page.pack(pady=5)
        self._button_page.config(text="Disease List", state="normal")
        self._home_button.pack(pady=5)
        self._home_button.config(text="Home", state="normal")


class healthQuiz:

    def __init__(self):
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

        self._questions = questions
        self._record = {-1: deepcopy(self._scores)}
        self._answers = answers
        self.choice_btns = []
        self._buttons = False
        self._links = []
        self._chart_button = None
        self._disease_list_button = None
        self._home_button = None
        self._quiz_button = None
        self._current_question = 0

    def startup(self):
        """
        Initializes tkinter buttons for quiz.
        """
        self._chart_button = ttk.Button(
            root,
            command=lambda: [self.show_chart()]
        )
        self._home_button = ttk.Button(
            root,
            command=lambda: [self.clear_buttons(), BettaHealth().home_page()]
        )
        self._quiz_button = ttk.Button(
            root,
            command=lambda: [self.clear_buttons(), self.questions()]
        )
        self._disease_list_button = ttk.Button(
            root,
            command=lambda: [self.clear_buttons(), BettaHealth().button_page()]
        )
        for i in range(4):
            button = ttk.Button(
                root,
                command=lambda i=i: [self.clear_buttons(), self.check_answer(i), self.next_question()]
            )
            self.choice_btns.append(button)

        self.introduction()

    def clear_buttons(self):
        """
        Clears the buttons and links when changing pages in tkinter.
        """
        change_image(img)
        if self._quiz_button:
            self._quiz_button.pack_forget()
        if self._home_button:
            self._home_button.pack_forget()
        if self._chart_button:
            self._chart_button.pack_forget()
        if self._disease_list_button:
            self._disease_list_button.pack_forget()
        for button in self.choice_btns:
            button.pack_forget()
        for item in self._links:
            item.pack_forget()

    def introduction(self):
        """
        Introduces the quiz and its guidelines.
        """
        intro = "Hello and welcome to the Betta Health Quiz! " \
                "This quiz was made to help you further see what the " \
                "possible illnesses are of you betta. It must be stated that " \
                "this is a student-created program, and should not take " \
                "precedence over the opinions of a medical professional." \
                "If you feel you have a good idea of what your betta's " \
                "illness might be, feel free to skip the quiz as needed. " \
                "Also, if you feel you answered a question wrong, you can " \
                "always go back a question, or restart the quiz entirely! " \
                "Take your time to read the questions thoroughly and I " \
                "wish your betta a speedy recovery!\n" \
                "\n- Blake Jennings"

        qs_label.config(text=intro)
        self._quiz_button.pack(pady=5)
        self._quiz_button.config(text="Start Quiz", state="normal")
        self._home_button.pack(pady=5)
        self._home_button.config(text="Home", state="normal")

    def questions(self):
        """
        Displays the questions for the health quiz.
        """
        for item in self.choice_btns:
            item.pack(pady=5)
        if self._current_question == 0:
            self.choice_btns[2].pack_forget()
        question = self._questions[self._current_question]
        qs_label.config(text=question["question"])
        choices = question["choices"]

        for i in range(4):
            self.choice_btns[i].config(text=choices[i], state="normal")  # Reset button state
        self._buttons = True
        self._home_button.pack(pady=5)
        self._home_button.config(text="Home", state="normal")

    def check_answer(self, choice):
        """
        Evaluates the answer given in each question of the health quiz.
        """
        selected_choice = self.choice_btns[choice].cget("text")

        if selected_choice == "Yes":
            for item in self._answers[self._current_question + 1]:
                self._scores[item] += 1
            self._record[self._current_question] = deepcopy(self._scores)

        elif selected_choice == "No":
            self._record[self._current_question] = deepcopy(self._scores)

        elif selected_choice == "Previous Question":
            if self._current_question >= 1:
                self._scores = deepcopy(self._record[self._current_question - 2])
            else:
                self._scores = deepcopy(self._record[-1])
            if self._current_question >= 1:
                self._current_question -= 2
            else:
                self._current_question -= 1

        elif selected_choice == "Restart Quiz":
            self.clear_buttons()
            self._scores = deepcopy(self._record[-1])
            self._current_question = -1

        print(self._scores.values())

    def next_question(self):
        """
        Moves to the next question. Displays the results of the quiz if on final question.
        """
        self._current_question += 1

        if self._current_question < len(self._questions):
            self.questions()
        else:
            self.results()

    def show_chart(self):
        """
        Displays the quiz results chart, which shows the
        individual scores of each disease based on answers.
        """
        plt.bar(*zip(*self._scores.items()))
        plt.show()

    def results(self):
        """
        Displays the results of the quiz, with options to show the
        results chart as well as links to purchasable items to
        potentially aid in betta recovery.
        """
        for button in self.choice_btns:
            button.pack_forget()
        max_result = max(self._scores.items(), key=operator.itemgetter(1))[0]
        info = info_dict[max_result]
        change_image(max_result)
        result = f'Your betta most likely has {max_result}. \n{info} Check out your results chart to see what other ' \
                 f'illness your betta could have. \nFor {max_result}, here are some items that could help with ' \
                 f'treatment:'
        qs_label.config(text=result)
        links = self.request_links(max_result)
        for ind, item in enumerate(links[1]):
            link = ttk.Label(root, text=links[0][ind], cursor="hand1", font=["Helvetica", 20, 'underline'])
            link.pack()
            self._links.append(link)
            link.bind("<Button-1>", lambda e, url=item: webbrowser.open_new(url))
        self._buttons = False
        self._chart_button.pack(pady=5)
        self._chart_button.config(text="My Results Chart", state="normal")
        self._disease_list_button.pack(pady=5)
        self._disease_list_button.configure(text="See Other Diseases", state="normal")
        self.choice_btns[3].pack()
        self._home_button.pack(pady=5)
        self._home_button.config(text="Home", state="normal")

    def request_links(self, disease):
        """
        Microservice to request and receive amazon links
        to medications based on disease name.
        """
        socket.send_string(disease)
        try:
            treatment_links = socket.recv_pyobj()
            return treatment_links
        except zmq.ZMQError as e:
            print(f"An error occurred: {e}")


def change_image(name):
    """
    Displays example image based on disease.
    """
    if name == "Velvet":
        img_label.config(image=velvet)
    elif name == "Ich":
        img_label.config(image=ich)
    elif name == "Popeye":
        img_label.config(image=popeye)
    elif name == "Fin Rot":
        img_label.config(image=finrot)
    elif name == "Columnaris":
        img_label.config(image=columnaris)
    elif name == "Hole in the Head":
        img_label.config(image=hole)
    elif name == "Dropsy":
        img_label.config(image=dropsy)
    elif name == "Swim Bladder Disorder":
        img_label.config(image=bladder)
    elif name == "Constipation":
        img_label.config(image=constipation)
    else:
        img_label.config(image=img)


root = tk.Tk()
root.title("BettaHealth")
root.geometry("600x800")
style = Style()
style.configure("TLabel", font=("Arial Bold", 18))
style.configure("TButton", font=("Arial Bold", 16), width=50, borderwidth=0)

velvet = ImageTk.PhotoImage(Image.open("Velvet.png"))
ich = ImageTk.PhotoImage(Image.open("Ich.png"))
popeye = ImageTk.PhotoImage(Image.open("Popeye.png"))
finrot = ImageTk.PhotoImage(Image.open("fin-rot.png"))
columnaris = ImageTk.PhotoImage(Image.open("Columnaris.png"))
hole = ImageTk.PhotoImage(Image.open("hole.png"))
dropsy = ImageTk.PhotoImage(Image.open("dropsy.png"))
bladder = ImageTk.PhotoImage(Image.open("bladder.png"))
constipation = ImageTk.PhotoImage(Image.open("constipation.png"))
img = ImageTk.PhotoImage(Image.open("bettatest.png"))

img_label = tk.Label(master=root, image=img)
qs_label = tk.Label(
    master=root,
    anchor="center",
    wraplength=550,
    font=("Arial Bold", 20)
)
img_label.pack()
qs_label.pack(pady=10)

app = BettaHealth()
app.home_page()
root.mainloop()

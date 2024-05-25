import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

class DepressionTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Depression Test")
        self.root.geometry("700x720")
        self.input_page = InputPage(self.root, self)
        self.question_page = QuestionPage(self.root, self)
        self.result_page = ResultPage(self.root, self)
        self.current_page = self.input_page
        self.input_page.frame.pack()

    def reset(self):
        self.input_page.reset()
        self.question_page.reset()
        self.result_page.reset()
        self.input_page.frame.pack()
        self.current_page = self.input_page

class InputPage:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.name = tk.StringVar()
        self.age = tk.IntVar()
        self.frame = tk.Frame(self.master, bg="#EF9595")
        self.create_widgets()

    def create_widgets(self):
        image = Image.open("depression_test_image.jpg")
        image = image.resize((1000, 500), resample=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(self.frame, image=photo)
        label.image = photo
        label.pack()

        tk.Label(self.frame, text="Name:", bg="#f8f7f2", fg="#0A0000").pack(pady=10)
        tk.Entry(self.frame, textvariable=self.name, bg="#f8f7f2", fg="#0A0000").pack(pady=10)

        tk.Label(self.frame, text="Age:", bg="#f8f7f2", fg="#0A0000").pack(pady=10)
        tk.Entry(self.frame, textvariable=self.age, bg="#f8f7f2", fg="#0A0000").pack(pady=10)

        tk.Button(self.frame, text="Next", command=self.next_page, bg="#f8f7f2", fg="#0A0000").pack(pady=10)

    def reset(self):
        self.name.set("")
        self.age.set(0)
        self.frame.pack()

    def next_page(self):
        self.frame.pack_forget()
        self.app.question_page.frame.pack()
        self.app.current_page = self.app.question_page

class QuestionPage:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.questions = [
            {"question": "Sadness",
            "options": [{"option": "I do not feel sad", "weight": 0},
                        {"option": "I feel sad very often", "weight": 1},
                        {"option": "I am sad all the time", "weight": 2},
                        {"option": "I am so sad or so unhappy that I can't stand it", "weight": 3}]},
            {"question": "Pessimism",
            "options": [{"option": "I am not discouraged about my future", "weight": 0},
                        {"option": "I feel more discouraged about my future than I used to", "weight": 1},
                        {"option": "I do not expect things to work out for me", "weight": 2},
                        {"option": "I feel that my future is hopeless and will only get worse", "weight": 3}]},
            {"question": "Past Failures",
            "options": [{"option": "I do not feel like a failure", "weight": 0},
                        {"option": "I have failed more than I should have", "weight": 1},
                        {"option": "When I think about my past, I see a lot of failures", "weight": 2},
                        {"option": "I feel like I have completely failed in life", "weight": 3}]},
            {"question": "Loss of Pleasure",
            "options": [{"option": "I get as much pleasure as I ever did from the things I enjoy", "weight": 0},
                        {"option": "I don't enjoy things as much as I used to", "weight": 1},
                        {"option": "I get very little pleasure from the things I used to enjoy", "weight": 2},
                        {"option": "I can't get any pleasure from the things I used to enjoy", "weight": 3}]},
            {"question": "Guilty Feelings",
            "options": [{"option": "I don't feel particularly guilty", "weight": 0},
                        {"option": "I feel guilty about many things I have done or should have done", "weight": 1},
                        {"option": "I feel guilty most of the time", "weight": 2},
                        {"option": "I feel guilty all the time", "weight": 3}]},
            {"question": "Feeling of Being Punished",
            "options": [{"option": "I don't feel punished", "weight": 0},
                        {"option": "I feel like I might be punished", "weight": 1},
                        {"option": "I expect to be punished", "weight": 2},
                        {"option": "I feel like I am being punished", "weight": 3}]},
            {"question": "Negative Feelings About Self",
            "options": [{"option": "I feel the same about myself as ever", "weight": 0},
                        {"option": "I have lost confidence in myself", "weight": 1},
                        {"option": "I am disappointed in myself", "weight": 2},
                        {"option": "I dislike myself", "weight": 3}]},
            {"question": "Self-Criticism",
            "options": [{"option": "I don't criticize or blame myself more than usual", "weight": 0},
                        {"option": "I am more critical of myself than I used to be", "weight": 1},
                        {"option": "I blame myself for everything", "weight": 2},
                        {"option": "I blame myself for everything bad that happens", "weight": 3}]},
            {"question": "Suicidal Thoughts or Wishes",
            "options": [{"option": "I don't have any thoughts of killing myself", "weight": 0},
                        {"option": "I have thoughts of killing myself, but I would not carry them out", "weight": 1},
                        {"option": "I would like to kill myself", "weight": 2},
                        {"option": "I would kill myself if I had the chance", "weight": 3}]},
            {"question": "Crying",
            "options": [{"option": "I don't cry any more than I used to", "weight": 0},
                        {"option": "I cry more than I used to", "weight": 1},
                        {"option": "I cry over every little thing", "weight": 2},
                        {"option": "I feel like crying but I can't", "weight": 3}]},
            {"question": "Agitation",
            "options": [{"option": "I am no more restless or wound up than usual", "weight": 0},
                        {"option": "I feel more restless or wound up than usual", "weight": 1},
                        {"option": "I am so restless or agitated that it's hard to stay still", "weight": 2},
                        {"option": "I am so restless or agitated that I have to keep moving or doing something", "weight": 3}]},
            {"question": "Loss of Interest",
            "options": [{"option": "I have not lost interest in other people or activities", "weight": 0},
                        {"option": "I am less interested in other people or things than before", "weight": 1},
                        {"option": "I have lost most of my interest in other people or things", "weight": 2},
                        {"option": "It's hard to get interested in anything", "weight": 3}]},
            {"question": "Indecisiveness",
            "options": [{"option": "I make decisions as well as ever", "weight": 0},
                        {"option": "I find it more difficult to make decisions than usual", "weight": 1},
                        {"option": "I have much greater difficulty in making decisions than I used to", "weight": 2},
                        {"option": "I have trouble making any decisions", "weight": 3}]},
            {"question": "Worthlessness",
            "options": [{"option": "I feel that I am as worthwhile and useful as I have ever been", "weight": 0},
                        {"option": "I don't feel as worthwhile and useful as I used to", "weight": 1},
                        {"option": "I feel less worthwhile than others", "weight": 2},
                        {"option": "I feel utterly worthless", "weight": 3}]},
            {"question": "Loss of Energy",
            "options": [{"option": "I have as much energy as ever", "weight": 0},
                        {"option": "I have less energy than I used to have", "weight": 1},
                        {"option": "I don't have enough energy to do very much", "weight": 2},
                        {"option": "I don't have enough energy to do anything", "weight": 3}]},
            {"question": "Changes in Sleeping Pattern",
            "options": [{"option": "I have not experienced any change in my sleeping pattern", "weight": 0},
                        {"option": "I sleep a little more than usual", "weight": 1},
                        {"option": "I sleep a little less than usual", "weight": 1},
                        {"option": "I sleep much more than usual", "weight": 2},
                        {"option": "I sleep much less than usual", "weight": 2},
                        {"option": "I sleep most of the day", "weight": 3},
                        {"option": "I wake up one or two hours earlier and can't get back to sleep", "weight": 3}]},
            {"question": "Irritability",
            "options": [{"option": "I am no more irritable than usual", "weight": 0},
                        {"option": "I am more irritable than usual", "weight": 1},
                        {"option": "I am much more irritable than usual", "weight": 2},
                        {"option": "I am irritable all the time", "weight": 3}]},
            {"question": "Changes in Appetite",
            "options": [{"option": "My appetite is no different than usual", "weight": 0},
                        {"option": "I have a slightly smaller appetite than usual", "weight": 1},
                        {"option": "I have a slightly greater appetite than usual", "weight": 1},
                        {"option": "I have a much smaller appetite than usual", "weight": 2},
                        {"option": "I have a much greater appetite than usual", "weight": 2},
                        {"option": "I have no appetite at all", "weight": 3},
                        {"option": "I crave food all the time", "weight": 3}]},
            {"question": "Difficulty Concentrating",
            "options": [{"option": "I can concentrate as well as ever", "weight": 0},
                        {"option": "I can't concentrate as well as usual", "weight": 1},
                        {"option": "It's hard to keep my mind on anything for very long", "weight": 2},
                        {"option": "I find it impossible to concentrate on anything", "weight": 3}]},
            {"question": "Tiredness or Fatigue",
            "options": [{"option": "I am no more tired or fatigued than usual", "weight": 0},
                        {"option": "I get tired or fatigued more easily than usual", "weight": 1},
                        {"option": "I am too tired or fatigued to do a lot of the things I used to do", "weight": 2},
                        {"option": "I am too tired or fatigued to do most of the things I used to do", "weight": 3}]}
        ]
        self.answers = []
        self.question_index = 0
        self.frame = tk.Frame(self.master, bg="#EF9595")
        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.frame, text="", wraplength=1500, bg="#EF9595")
        self.question_label.pack(pady=10)

        self.answer = tk.IntVar()

        self.options_frame = tk.Frame(self.frame, bg="#EF9595")
        self.options_frame.pack(pady=10)

        self.back_button = tk.Button(self.frame, text="Back", command=self.prev_question, bg="#f8f7f2")
        self.next_button = tk.Button(self.frame, text="Next", command=self.next_question, bg="#f8f7f2")
        self.result_button = tk.Button(self.frame, text="Result", command=lambda: self.show_result(self.answers), bg="#f8f7f2")

        self.back_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.next_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.result_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.show_question()

    def reset(self):
        self.question_index = 0
        self.answers = []
        self.show_question()
        self.frame.pack()

    def show_question(self):
        self.question_label.config(text=self.questions[self.question_index]["question"])
        self.options_frame.destroy()
        self.options_frame = tk.Frame(self.frame, bg="#f8f7f2")
        self.options_frame.pack(pady=10)

        for i, option in enumerate(self.questions[self.question_index]["options"]):
            tk.Radiobutton(self.options_frame, text=option["option"], variable=self.answer, value=option["weight"]).pack(anchor=tk.W, padx=10, pady=10)

        self.back_button.config(state="normal" if self.question_index > 0 else "disabled")
        self.result_button.config(state="normal" if self.question_index == len(self.questions) - 1 else "disabled")

    def next_question(self):
        self.answers.append(self.answer.get())
        self.answer.set(0)
        self.question_index += 1
        self.show_question()

    def prev_question(self):
        self.question_index -= 1
        self.answer.set(self.answers[self.question_index])
        self.show_question()

    def show_result(self, answers):
        self.frame.pack_forget()
        self.app.result_page.frame.pack()
        self.app.result_page.show(answers)
        self.app.current_page = self.app.result_page

class ResultPage:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master, bg="#EF9595")
        self.create_widgets()

    def create_widgets(self):
        image = Image.open("depression_test_image.jpg")
        image = image.resize((1000, 500), resample=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.frame, image=photo)
        label.image = photo
        label.pack()

        self.score = 0
        self.diagnosis_label = tk.Label(self.frame, text="", wraplength=1500, bg="#f8f7f2")
        self.diagnosis_label.pack(pady=10)

        self.finish_button = tk.Button(self.frame, text="Finish", command=self.show_input, bg="#f8f7f2")
        self.finish_button.pack(pady=10)

    def reset(self):
        self.score = 0
        self.diagnosis_label.config(text="")
        self.frame.pack_forget()

    def show(self, answers):
        self.frame.pack()
        self.score = sum(answer for answer in answers)
        if self.score < 5:
            self.diagnosis_label.config(text="Your diagnosis: Low Risk. You might not be suffering from depression. Please consult a professional for further assistance.")
        elif self.score < 10:
            self.diagnosis_label.config(text="Your diagnosis: Moderate Risk. You might be suffering from depression. Please consult a professional for further assistance.")
        else:
            self.diagnosis_label.config(text="Your diagnosis: High Risk. You are likely suffering from depression. Please consult a professional for further assistance.")

    def show_input(self):
        self.frame.pack_forget()
        self.app.input_page.frame.pack()
        self.app.current_page = self.app.input_page

def main():
    root = tk.Tk()
    app = DepressionTestApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

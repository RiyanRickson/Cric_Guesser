import wx
import random
import ref

# ================= GLOBAL VARIABLES =================
role_choice = ""
country_choice = ""
answer = ""
hint = []
wrong_guesses = 0
guessed_letters = set()

# FULL LIFE AT 6 → DECREASES ON WRONG GUESSES
life_art = {
    6: [" O ", "/|\\", "/ \\"],   # FULL
    5: [" O ", "/|\\", "/  "],
    4: [" O ", "/|\\", "   "],
    3: [" O ", "/| ", "   "],
    2: [" O ", " | ", "   "],
    1: [" O ", "   ", "   "],
    0: ["   ", "   ", "   "]    # DEAD
}

# FUNCTIONS 
def choose_role(event):
    global role_choice
    role_choice = event.GetEventObject().GetLabel()[0]
    status.SetLabel(f"Role selected")

def choose_country(event):
    global country_choice
    country_choice = event.GetEventObject().GetLabel()[0]
    status.SetLabel(f"Country selected")

def start_game(event):
    global answer, hint, wrong_guesses, guessed_letters

    if not role_choice or not country_choice:
        msg.SetLabel("Select role and country first")
        return

    code = role_choice + country_choice
    answer = random.choice(ref.cric[code]).lower()

    hint = ["_" if c != " " else " " for c in answer]
    hint[0] = answer[0]

    wrong_guesses = 0
    guessed_letters.clear()

    update_ui("Game started")

def guess_letter(event):
    global wrong_guesses

    if not answer:
        msg.SetLabel("Start a game first")
        return

    g = guess.GetValue().lower()
    guess.SetValue("")

    if len(g) != 1 or not g.isalpha():
        update_ui("Enter ONE letter only")
        return

    if g in guessed_letters:
        update_ui("Already guessed")
        return

    guessed_letters.add(g)
    correct = False

    if g in answer:
        correct = True
        for i in range(len(answer)):
            if answer[i] == g:
                hint[i] = g
    else:
        wrong_guesses += 1   

    if "_" not in hint:
        update_ui("YOU WIN!")
    elif wrong_guesses >= 6:
        update_ui(f"YOU LOSE! Answer: {answer}")
    else:
        update_ui("Correct guess" if correct else "Wrong guess")

def play_again(event):
    global role_choice, country_choice
    global answer, hint, wrong_guesses, guessed_letters

    role_choice = ""
    country_choice = ""
    answer = ""
    hint = []
    wrong_guesses = 0
    guessed_letters.clear()

    status.SetLabel("Select role and country")
    msg.SetLabel("Game reset. Choose again.")
    word_label.SetLabel("")
    guess.SetValue("")
    life_label.SetLabel("\n".join(life_art[6]))  

def update_ui(message):
    lives_left = max(0, 6 - wrong_guesses)

    life_label.SetLabel("\n".join(life_art[lives_left]))
    word_label.SetLabel(" ".join(hint))
    msg.SetLabel(message)

# basic wx frame
app = wx.App()
frame = wx.Frame(None, title="Guess The Cricketer", size=(520, 620))
panel = wx.Panel(frame)

panel.SetBackgroundColour(wx.Colour(173, 216, 230))

main_vbox = wx.BoxSizer(wx.VERTICAL)

# role selection
main_vbox.Add(wx.StaticText(panel, label="Choose Role"), 0, wx.ALL, 5)
role_box = wx.BoxSizer(wx.HORIZONTAL)

for label in ["1 Batsman", "2 All-Rounder", "3 Bowler", "4 Women"]:
    btn = wx.Button(panel, label=label)
    btn.Bind(wx.EVT_BUTTON, choose_role)
    role_box.Add(btn, 1, wx.ALL, 2)

main_vbox.Add(role_box, 0, wx.EXPAND)

# country selection
main_vbox.Add(wx.StaticText(panel, label="Choose Country"), 0, wx.ALL, 5)
country_box = wx.BoxSizer(wx.HORIZONTAL)

for label in ["1 India", "2 Australia", "3 England", "4 NZ", "5 SA", "6 WI"]:
    btn = wx.Button(panel, label=label)
    btn.Bind(wx.EVT_BUTTON, choose_country)
    country_box.Add(btn, 1, wx.ALL, 2)

main_vbox.Add(country_box, 0, wx.EXPAND)

# choice
status = wx.StaticText(panel, label="Select role and country")
main_vbox.Add(status, 0, wx.ALL, 5)

# start button
start_btn = wx.Button(panel, label="Start Game")
start_btn.Bind(wx.EVT_BUTTON, start_game)
main_vbox.Add(start_btn, 0, wx.ALL | wx.CENTER, 5)

# life display
life_label = wx.StaticText(panel, label="", style=wx.ALIGN_LEFT)
life_label.SetMinSize((120, 60))
life_label.SetFont(wx.Font(14, wx.FONTFAMILY_TELETYPE,
                           wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
life_label.SetLabel("\n".join(life_art[6]))  

word_label = wx.StaticText(panel, label="", style=wx.ALIGN_LEFT)
word_label.SetMinSize((400, 40))
word_label.SetFont(wx.Font(16, wx.FONTFAMILY_TELETYPE,
                           wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

msg = wx.StaticText(panel, label="")

main_vbox.Add(life_label, 0, wx.LEFT | wx.TOP, 20)
main_vbox.Add(word_label, 0, wx.LEFT | wx.TOP, 20)
main_vbox.Add(msg, 0, wx.ALL, 10)

# user input one letter at a time
guess = wx.TextCtrl(panel)
main_vbox.Add(guess, 0, wx.EXPAND | wx.ALL, 5)

guess_btn = wx.Button(panel, label="Guess Letter")
guess_btn.Bind(wx.EVT_BUTTON, guess_letter)
main_vbox.Add(guess_btn, 0, wx.ALL | wx.CENTER, 5)

# play again button (resets entire game)
play_again_btn = wx.Button(panel, label="Play Again")
play_again_btn.Bind(wx.EVT_BUTTON, play_again)
main_vbox.Add(play_again_btn, 0, wx.ALL | wx.CENTER, 5)

panel.SetSizer(main_vbox)
frame.Show()
app.MainLoop()

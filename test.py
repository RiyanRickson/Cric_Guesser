import wx
import random
import REF
def cric_game(choice):
    # ---------------- GLOBAL VARIABLES ----------------
    answer = ""
    hint = []
    wrong = 6
    guessed = set()

    life_art = {
        6: ["   ", "   ", "   "],
        5: [" 👽 ", "   ", "   "],
        4: [" 👽 ", " | ", "   "],
        3: [" 👽 ", "/| ", "   "],
        2: [" 👽 ", "/|\\", "   "],
        1: [" 👽 ", "/|\\", "/  "],
        0: [" 👽 ", "/|\\", "/ \\"]
    }

    # ---------------- FUNCTIONS ----------------
    def update_display():
        life_label.SetLabel("\n".join(life_art[wrong]))
        hint_label.SetLabel(" ".join(hint))

    def start_game(event):
        global answer, hint, wrong, guessed,choice 
        words = REF.cric[choice]

        answer = random.choice(words).lower()
        hint = ["_" if c != " " else " " for c in answer]
        hint[0] = answer[0]

        wrong = 6
        guessed = set()

        update_display()
        msg.SetLabel("Game Started!")

    def guess_letter(event):
        global wrong

        if not answer:
            return

        g = guess_input.GetValue().lower()
        guess_input.Clear()

        if len(g) != 1 or not g.isalpha():
            msg.SetLabel("Invalid input")
            return

        if g in guessed:
            msg.SetLabel("Already guessed")
            return

        guessed.add(g)

        if g in answer:
            for i in range(len(answer)):
                if answer[i] == g:
                    hint[i] = g
        else:
            wrong -= 1

        update_display()

        if "_" not in hint:
            msg.SetLabel("🎉 YOU WIN!")
        elif wrong == 0:
            msg.SetLabel(f"❌ YOU LOSE! Answer: {answer}")

    # ---------------- wxPython APP ----------------

    vbox = wx.BoxSizer(wx.VERTICAL)

    start_btn = wx.Button(panel, label="Start Game")
    start_btn.Bind(wx.EVT_BUTTON, start_game)
    vbox.Add(start_btn, 0, wx.ALL | wx.CENTER, 10)

    life_label = wx.StaticText(panel, label="")
    vbox.Add(life_label, 0, wx.ALL | wx.CENTER, 10)

    hint_label = wx.StaticText(panel, label="")
    hint_label.SetFont(wx.Font(12, wx.FONTFAMILY_TELETYPE,
                            wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
    vbox.Add(hint_label, 0, wx.ALL | wx.CENTER, 10)

    guess_input = wx.TextCtrl(panel)
    vbox.Add(guess_input, 0, wx.ALL | wx.EXPAND, 10)

    guess_btn = wx.Button(panel, label="Guess Letter")
    guess_btn.Bind(wx.EVT_BUTTON, guess_letter)
    vbox.Add(guess_btn, 0, wx.ALL | wx.CENTER, 10)

    msg = wx.StaticText(panel, label="")
    vbox.Add(msg, 0, wx.ALL | wx.CENTER, 10)

    panel.SetSizer(vbox)


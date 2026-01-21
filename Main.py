import REF
import test
import random
import wx
app=wx.App()
frame=wx.Frame(None,title="Guess the Cricketer",size=(700,700))

# panel 1
p1=wx.Panel(frame,style=wx.SIMPLE_BORDER)
p1.SetBackgroundColour("light blue")

txt=wx.StaticText(p1,label="WELCOME TO GUESS THE CRICKETER🏏\nRULES:\nYou will have 6 chances to guess the correct name.Your life will be displayed by the graphic",pos=(0,0))
txt1=wx.StaticText(p1,label="CHOOSE PLAYER ROLE ",pos=(250,50))
txt1.SetFont(wx.Font(16,wx.FONTFAMILY_SWISS,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD))

#main buttons
ba=wx.Button(p1,label="BATSMEN",pos=(300,100),size=(100,20))
bo=wx.Button(p1,label="BOWLERS",pos=(300,200),size=(100,20))
al=wx.Button(p1,label="ALL ROUNDERS",pos=(300,300),size=(100,20))
wo=wx.Button(p1,label="WOMEN",pos=(300,300),size=(100,20))



#2nd panel function
def make_p2():
    p2=wx.Panel(frame,style=wx.SIMPLE_BORDER,size=(700,700))
    p2.SetBackgroundColour("light blue")
    p1.Hide()

    #3rd panel (main game) function
    def make_p3():
        p3=wx.Panel(frame,style=wx.SIMPLE_BORDER,size=(700,700))
        p3.SetBackgroundColour("light purple")
        p2.Hide()
        def cric_game(choice):
            #game variables
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
            def update_display():
                life=wx.StaticText(p3,label="\n".join(life_art[wrong]))
                hint=wx.StaticText(p3,label=" ".join(hint))
            def start_game(event):
                global answer, hint, wrong, guessed,choice 
                words = REF.cric[choice]  #getting dataset

                answer = random.choice(words).lower()  #getting name 
                hint = ["_" if c != " " else " " for c in answer]  #displaying spaces if any
                hint[0] = answer[0] #displaying 1st letter

                wrong = 6
                guessed = set()

                update_display()
            start_btn = wx.Button(p3, label="Start Game")
            start_btn.Bind(wx.EVT_BUTTON, start_game)

            def guess_letter(event):
                global wrong 
                letter=''
                l=wx.TextCtrl(p3,pos=(100,200),size=(10,10))
                b=wx.Button(p3,label="SAVE",pos=(100,210))

                def on_c(event):
                    global letter
                    letter+=l.GetValue()
                b.Bind(wx.EVT_BUTTON,on_c)
                




            guess_btn = wx.Button(p3, label="Guess Letter")
            guess_btn.Bind(wx.EVT_BUTTON, guess_letter)











        global choice
        cric_game(choice)

    txt2=wx.StaticText(p2,label="CHOOSE PLAYER COUNTRY ",pos=(250,10))
    txt2.SetFont(wx.Font(16,wx.FONTFAMILY_SWISS,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD))
    ind=wx.Button(p2,label="INDIA",pos=(300,100),size=(100,20))
    aus=wx.Button(p2,label="AUSTRALIA",pos=(300,200),size=(100,20))
    eng=wx.Button(p2,label="ENGLAND",pos=(300,300),size=(100,20))
    nz=wx.Button(p2,label="NEW ZEALAND",pos=(300,400),size=(100,20))
    sa=wx.Button(p2,label="SOUTH AFRICA",pos=(300,500),size=(100,20))
    wi=wx.Button(p2,label="WEST INDIES",pos=(300,600),size=(100,20))

    #p2 events 
    def c_ind(event):
        global choice
        choice+='1'
        make_p3()
    def c_aus(event):
        global choice
        choice+='2'
    def c_eng(event):
        global choice
        choice+='3'
    def c_nz(event):
        global choice
        choice+='4'
    def c_sa(event):
        global choice
        choice+='5'
    def c_wi(event):
        global choice
        choice+='6'

    #p2 event binding
    ind.Bind(wx.EVT_BUTTON,c_ind)
    aus.Bind(wx.EVT_BUTTON,c_aus)
    eng.Bind(wx.EVT_BUTTON,c_eng)
    nz.Bind(wx.EVT_BUTTON,c_nz)
    sa.Bind(wx.EVT_BUTTON,c_sa)
    wi.Bind(wx.EVT_BUTTON,c_wi)

choice=''
#panel1  button events
def c_ba(event):
    global choice
    choice+='1'
    make_p2()

def c_bo(event):
    global choice
    choice+='2'
    make_p2()


def c_al(event):
    global choice
    choice+='3'
    make_p2()


def c_wo(event):
    global choice
    make_p2()
    choice+='4'

#panel 1 event binding
ba.Bind(wx.EVT_BUTTON,c_ba)
bo.Bind(wx.EVT_BUTTON,c_bo)
al.Bind(wx.EVT_BUTTON,c_al)
wo.Bind(wx.EVT_BUTTON,c_wo)








frame.Show()
app.MainLoop()
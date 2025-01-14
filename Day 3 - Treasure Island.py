import time

gewonnen = False
falsch_Eingabe = False

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Willkommen zur Schatzsuche.")
print("Deine Aufgabe ist es, einen Schatz zu finden.")

entscheidung1_Kreuzung = input("\nDu befindest dich an einer Weggabelung.\nMöchtest du den "
                               "linken oder rechten Weg entlanggehen? (l/r) ").lower()
if entscheidung1_Kreuzung == "l" or entscheidung1_Kreuzung == "links":
    entscheidung2_Wasser = input("\nNach etwa 5 Minuten Fußmarsch, kommst du an einen Fluss."
                                 "\nDu kannst das andere Ufer sehen, das Wasser fließt nur "
                                 "langsam. Etwas links von dir ist ein kleiner Steg, aber "
                                 "derzeit ohne Boot.\nMöchtest du auf die andere Seite "
                                 "schwimmen (s) oder lieber warten, ob ein Boot "
                                 "vorbeikommt (w)? ").lower()
    if entscheidung2_Wasser == "w" or entscheidung2_Wasser == "warten" or entscheidung2_Wasser == "boot":
        entscheidung3_Tuer = input("\nDu musstest zwar etwas warten, aber tatsächlich kamen "
                                   "zwei Fischer in einem Boot vorbei.\nDu konntest ihnen "
                                   "verständlich machen, dass du ans andere Ufer möchtest."
                                   "\nIm Austausch für deinen Gürtel haben sie dich auf die "
                                   "andere Flussseite gebracht.\nDu findest einen Weg, der am "
                                   "Ufer beginnt und folgst ihm.\n\nDu erreichst eine Lichtung, "
                                   "an deren anderem Ende sich eine große Felswand befindet."
                                   "\nIn dieser Wand gibt es drei Türen.\nWelche willst du "
                                   "wählen? Die rote (r), die blaue (b) oder die "
                                   "gelbe (g)? ").lower()
        if entscheidung3_Tuer == "r" or entscheidung3_Tuer == "rot":
            print("\nRot ist eigentlich eine Warnfarbe. Aber wer mitten im Nirgendwo auf ein "
                  "Boot wartet und damit auch noch Recht hat, \nhat wohl heute einen Glückstag. "
                  "Und Rot ist deine Lieblingsfarbe.\nDu wählst diese Tür und kommst in einen "
                  "Gang. Weiter hinten siehst du Licht.\nDie Tür fällt hinter dir zu, aber du "
                  "bist schon weitergegangen und möchtest die Lichtquelle finden.\nLeider ist "
                  "die Lichtquelle ein Feuer, dass den gesamten weiteren Gang füllt.\nDu hast "
                  "nur noch die Wahl zwischen verbrennen oder ersticken, denn der Sauerstoff "
                  "ist endlich.")
            time.sleep(18)
        elif entscheidung3_Tuer == "g" or entscheidung3_Tuer == "gelb":
            gewonnen = True
            print("\nGelb wie Gold - also Schatz. Eine bessere Analogie fällt dir nicht ein."
                  "\nHinter der Tür ist eine kleine Höhle ohne weitere Gänge.\nDas durch die "
                  "Tür fallende Licht genügt, um zu erkennen, dass sich an der rechten Wand "
                  "etwas kistenartiges befindet.\nDu läufst hin und ziehst und schiebst dieses "
                  "Ding näher an die Tür.\nEs ist tatsächlich eine Schatztruhe! Das Holz ist "
                  "gut erhalten, aber das Schloss ist sehr rostig.\nMit einem kräftigen Tritt "
                  "kannst du es lösen und die Schatztruhe öffnen.\nHerzlichen Glückwunsch!")
            time.sleep(15)
        elif entscheidung3_Tuer == "b" or entscheidung3_Tuer == "blau":
            print("\nBlau hat etwas friedliches an sich. Diese Tür ist bestimmt sicher.\nMit "
                  "diesen Gedanken öffnest du die Tür und folgst dem kleinen Gang dahinter."
                  "\nEs ist relativ dunkel, aber du erkennst grob den Weg.\nDer Gang ist sehr "
                  "breit und du bist unsicher, ob es nicht an den Seiten Ausbuchtungen oder "
                  "weitere Gänge gibt.\nNach einigen Metern hörst du vor dir ein Scharren und "
                  "Schnauben - irgendwie unmenschlich.\nDu willst umdrehen, aber hinter dir "
                  "leuchten plötzlich Augenpaare auf.\nDeine letzten Augenblicke versuchst du, "
                  "die Wesen, die dich von allen Seiten umzingelt haben, zu erkennen.\nAber vor "
                  "lauter Zähnen und Klauen gelingt dir das nicht.")
            time.sleep(20)
        else:
            falsch_Eingabe = True
    elif entscheidung2_Wasser == "s" or entscheidung2_Wasser == "schwimmen":
        print("\nDu steigst ins Wasser, dass sogar überraschend warm ist. Du beginnst zu "
              "schwimmen und hast schon über die Hälfte geschafft, als etwas dein Bein streift."
              "\nDu denkst, es wäre ein Fisch, aber dieses Etwas ist noch da und schlängelt "
              "sich um deinen Fuß.\nDu versuchst, schneller zu schwimmen und dich "
              "freizustrampeln, aber es ist zu spät. Das Etwas hat deinen Fuß und dein Bein "
              "fest umschlungen.\nEs beginnt zu ziehen und es ist stärker als du. Es zieht "
              "dich immer tiefer und du kannst nicht mehr atmen, geschweige denn dich befreien.")
        time.sleep(15)
    else:
        falsch_Eingabe = True
elif entscheidung1_Kreuzung == "r" or entscheidung1_Kreuzung == "rechts":
    print("\nDer Weg schlängelt sich durch Gebüsch und wird immer schmaler. Du stolperst über e"
          "ine Wurzel und übersiehst das dahinterliegende Loch.\nDu fällst hinein und dein "
          "Fußknöchel schmerzt höllisch. Zudem ist das Loch mehrere Meter tief. Du wirst "
          "hier nicht mehr rauskommen.")
    time.sleep(10)
else:
    falsch_Eingabe = True

#time.sleep ist nicht Bestandteil des Kurses, soll aber helfen, den Text zu lesen,
# bevor er durch die ASCII-Art weggescrollt wird.

if falsch_Eingabe == True:
    print("\nDu versuchst, mit einer fehlerhaften Eingabe dieses Spiel zu überlisten.\n"
          "Das solltest du nicht tun. Das war leider ein Fehler.")
    time.sleep(4)

if gewonnen == True:
    print('''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'|U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-|U|.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
    ''')
else:
    print('''
        ██               ██
      ████▄   ▄▄▄▄▄▄▄   ▄████
         ▀▀█▄█████████▄█▀▀
           █████████████
           ██▀▀▀███▀▀▀██
           ██   ███   ██
           █████▀▄▀█████
            ███████████
        ▄▄▄██  █▀█▀█  ██▄▄▄
        ▀▀██           ██▀▀
          ▀▀           ▀▀
    ''')

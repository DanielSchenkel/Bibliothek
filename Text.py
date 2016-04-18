# Dies ist ein tolles Spiel
geheimnis = 50
versuch = 0
zaehler = 0

while versuch != geheimnis:
    versuch = int(input("Raten Sie: "))
    if versuch < geheimnis/2:
            print("Viel zu klein!")

    elif versuch < geheimnis:
            print("Leider zu klein!")

    elif versuch > geheimnis * 1.5:
        print("Viel zu groß!")

    elif versuch > geheimnis:
        print("Leider zu groß!")

    else:
        print("Gut gemacht!")

    if zaehler > 9:
        break


    zaehler = zaehler + 1

if zaehler < 5:
    print("Du bist ein echtes Naturtalent! Du hast es in", zaehler, "Versuchen geschafft!")
elif zaehler >= 5 and zaehler < 10:
    print("Eine starke Leistung! Das waren nur", zaehler, "Versuche!")
else:
    print("Eine ganz schwache Leistung. Dieses Mal hast Du es leider nicht geschafft. Deine 10 Versuche sind um.")

print("Die Sonne scheint!")
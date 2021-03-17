import json
from random import randint

f = json.load(open("Data/mydata.json", "r", encoding="utf-8"))


def VerbeType(verbe):
    if verbe.find('#') == -1:
        return 0
    else:
        return int(verbe[verbe.find('#')+1:])


def conjugeur(verbe, temps, prs):
    t = VerbeType(verbe)
    if verbe.find('#') != -1:
        verbe = verbe[:verbe.find('#')]
    racine = ""
    terminaisons = []
    formes = []
    if t == 1:  # 1 : (modèle: chanter)
        racine = verbe[:-2]
        terminaisons = [
            ["ais", "ais", "ait", "ions", "iez", "aient"],
            ["e", "es", "e", "ons", "ez", "ent"],
            ["erai", "eras", "era", "erons", "erez", "eront"],
            ["é", "ant"]
        ]
    elif t == 2:  # 2 : (modèle: finir)
        racine = verbe[:-4]
        terminaisons = [
            ["issais", "issais", "issait", "issions", "issiez", "issaient"],
            ["is", "is", "it", "issons", "issez", "issent"],
            ["irai", "iras", "ira", "irons", "irez", "iront"],
            ["i", "issant"]
        ]
    elif t == 3:  # 3 : (modèle: sentir)
        racine = verbe[:-3]
        terminaisons = [
            ["tais", "tais", "tait", "tions", "tiez", "taient"],
            ["s", "s", "t", "tons", "tez", "tent"],
            ["tirai", "tiras", "tira", "tirons", "tirez", "tiront"],
            ["ti", "tant"]
        ]
    elif t == 4:  # 4 : (modèle: vendre/répondre)
        racine = verbe[:-2]
        terminaisons = [
            ["ais", "ais", "ait", "ions", "iez", "aient"],
            ["s", "s", "", "ons", "ez", "ent"],
            ["rai", "ras", "ra", "rons", "rez", "ront"],
            ["u", "ant"]
        ]
    elif t == 5:  # 5 : (modèle: paraître)
        racine = verbe[:-5]
        terminaisons = [
            ["aissais", "aissais", "aissait", "aissions", "aissiez", "aissaient"],
            ["ais", "ais", "aît", "aissons", "aissez", "aissent"],
            ["aîtrai", "aîtras", "aîtra", "aîtrons", "aîtrez", "aîtront"],
            ["u", "aissant"]
        ]
    elif t == 6:  # 6 : (modèle: construire)
        racine = verbe[:-2]
        terminaisons = [
            ["sais", "sais", "sait", "sions", "siez", "saient"],
            ["s", "s", "t", "sons", "sez", "sent"],
            ["rai", "ras", "ra", "rons", "rez", "ront"],
            ["t", "sant"]
        ]
    elif t == 7:  # 7 : (modèle: peindre/joindre/craindre)
        racine = verbe[:-4]
        terminaisons = [
            ["gnais", "gnais", "gnait", "gnions", "gniez", "gnaient"],
            ["ns", "ns", "nt", "gnons", "gnez", "gnent"],
            ["ndrai", "ndras", "ndra", "ndrons", "ndrez", "ndront"],
            ["nt", "gnant"]
        ]
    elif t == 8:  # 8 : (modèle: tenir)
        racine = verbe[: -4]
        terminaisons = [
            ["enais", "enais", "enait", "enions", "eniez", "enaient"],
            ["iens", "iens", "ient", "enons", "enez", "iennent"],
            ["iendrai", "iendras", "iendra", "iendrons", "iendrez", "iendront"],
            ["enu", "enant"]
        ]
    elif t == 9:  # 9 : (modèle: placer)
        racine = verbe[: -3]
        terminaisons = [
            ["çais", "çais", "çait", "cions", "ciez", "çaient"],
            ["ce", "ces", "ce", "çons", "cez", "cent"],
            ["cerai", "ceras", "cera", "cerons", "cerez", "ceront"],
            ["cé", "çant"]
        ]
    elif t == 10:  # 10 : (modèle: manger)
        racine = verbe[: -2]
        terminaisons = [
            ["eais", "eais", "eait", "ions", "iez", "eaient"],
            ["e", "es", "e", "eons", "ez", "ent"],
            ["erai", "eras", "era", "erons", "erez", "eront"],
            ["é", "eant"]
        ]
    elif t == 11:  # 11 : (modèle: récupérer/accéder)
        racine = verbe[:-5]
        terminaisons = [
            ["é_ais", "é_ais", "é_ait", "é_ions", "é_iez", "é_aient"],
            ["è_e", "è_es", "è_e", "é_ons", "é_ez", "è_ent"],
            ["é_erai", "é_eras", "é_era", "é_erons", "é_erez", "é_eront"],
            ["é_é", "é_ant"]
        ]
        tmp = racine+terminaisons[temps][prs]
        return tmp.replace("_", verbe[-3:-2])
    elif t == 12:  # 12 : (modèle: mener/lever/peser)
        racine = verbe[:-4]
        terminaisons = [
            ["e_ais", "e_ais", "e_ait", "e_ions", "e_iez", "e_aient"],
            ["è_e", "è_es", "è_e", "e_ons", "e_ez", "è_ent"],
            ["è_erai", "è_eras", "è_era", "è_erons", "è_erez", "è_eront"],
            ["e_é", "e_ant"]
        ]
        tmp = racine+terminaisons[temps][prs]
        return tmp.replace("_", verbe[-3:-2])
    elif t == 13:  # 13 : (modèle: prendre)
        racine = verbe[: -5]
        terminaisons = [
            ["enais", "enais", "enait", "enions", "eniez", "enaient"],
            ["ends", "ends", "end", "enons", "enez", "ennent"],
            ["endrai", "endras", "endra", "endrons", "endrez", "endront"],
            ["is", "enant"]
        ]
    elif t == 14:  # 14 : (modèle: mettre)
        racine = verbe[: -5]
        terminaisons = [
            ["ettais", "ettais", "ettait", "ettions", "ettiez", "ettaient"],
            ["ets", "ets", "et", "ettons", "ettez", "ettent"],
            ["ettrai", "ettras", "ettra", "ettrons", "ettrez", "ettront"],
            ["is", "ettant"]
        ]
    elif t == 15:  # 15 : (modèle: essuyer/employer)
        racine = verbe[: -3]
        terminaisons = [
            ["yais", "yais", "yait", "yions", "yiez", "yaient"],
            ["ie", "ies", "ie", "yons", "yez", "ient"],
            ["ierai", "ieras", "iera", "ierons", "ierez", "ieront"],
            ["yé", "yant"]
        ]
    elif t == 16:  # 16 : (modèle: ouvrir)
        racine = verbe[: -3]
        terminaisons = [
            ["rais", "rais", "rait", "rions", "riez", "raient"],
            ["re", "res", "re", "rons", "rez", "rent"],
            ["rirai", "riras", "rira", "rirons", "rirez", "riront"],
            ["ert", "rant"]
        ]
    elif t == 17:  # 17 : (modèle: battre)
        racine = verbe[: -3]
        terminaisons = [
            ["tais", "tais", "tait", "tions", "tiez", "taient"],
            ["s", "s", "", "tons", "tez", "tent"],
            ["trai", "tras", "tra", "trons", "trez", "tront"],
            ["tu", "tant"]
        ]
    elif t == 18:  # 18 : (modèle: écrire)
        racine = verbe[: -2]
        terminaisons = [
            ["vais", "vais", "vait", "vions", "viez", "vaient"],
            ["s", "s", "t", "vons", "vez", "vent"],
            ["rai", "ras", "ra", "rons", "rez", "ront"],
            ["t", "vant"]
        ]
    elif t == 19:  # 19 : (modèle: servir)
        racine = verbe[: -3]
        terminaisons = [
            ["vais", "vais", "vait", "vions", "viez", "vaient"],
            ["s", "s", "t", "vons", "vez", "vent"],
            ["virai", "viras", "vira", "virons", "virez", "viront"],
            ["vi", "vant"]
        ]
    elif t == 20:  # 20 : (modèle: percevoir)
        racine = verbe[: -6]
        terminaisons = [
            ["cevais", "cevais", "cevait", "cevions", "ceviez", "cevaient"],
            ["çois", "çois", "çoit", "cevons", "cevez", "çoivent"],
            ["cevrai", "cevras", "cevra", "cevrons", "cevrez", "cevront"],
            ["çu", "cevant"]
        ]
    elif t == 21:  # 21 : (modèle: jeter)
        racine = verbe[: -2]
        terminaisons = [
            ["ais", "ais", "ait", "ions", "iez", "aient"],
            ["te", "tes", "te", "ons", "ez", "tent"],
            ["terai", "teras", "tera", "terons", "terez", "teront"],
            ["é", "ant"]
        ]
    elif t == 22:  # 22 : (modèle: vivre)
        racine = verbe[: -4]
        terminaisons = [
            ["ivais", "ivais", "ivait", "ivions", "iviez", "ivaient"],
            ["is", "is", "it", "ivons", "ivez", "ivent"],
            ["ivrai", "ivras", "ivra", "ivrons", "ivrez", "ivront"],
            ["écu", "vant"]
        ]
    elif t == 23:  # 23 : (modèle: appeler)
        racine = verbe[: -2]
        terminaisons = [
            ["ais", "ais", "ait", "ions", "iez", "aient"],
            ["le", "les", "le", "ons", "ez", "lent"],
            ["lerai", "leras", "lera", "lerons", "lerez", "leront"],
            ["é", "ant"]
        ]
    elif verbe == "être":
        formes = [
            ["étais", "étais", "était", "étions", "étiez", "étaient"],
            ["suis", "es", "est", "sommes", "êtes", "sont"],
            ["serai", "seras", "sera", "serons", "serez", "seront"],
            ["été", "étant"]
        ]
    elif verbe == "avoir":
        formes = [
            ["avais", "avais", "avait", "avions", "aviez", "avaient"],
            ["ai", "as", "a", "avons", "avez", "ont"],
            ["aurai", "auras", "aura", "aurons", "aurez", "auront"],
            ["eu", "ayant"]
        ]
    elif verbe == "aller":
        formes = [
            ["allais", "allais", "allait", "allions", "alliez", "allaient"],
            ["vais", "vas", "va", "allons", "allez", "vont"],
            ["irai", "iras", "ira", "irons", "irez", "iront"],
            ["allé", "allant"]
        ]
    elif verbe == "devoir":
        formes = [
            ["devais", "devais", "devait", "devions", "deviez", "devaient"],
            ["dois", "dois", "doit", "devons", "devez", "doivent"],
            ["devrai", "devras", "devra", "devrons", "devrez", "devront"],
            ["du", "devant"]
        ]

    elif verbe == "voir":
        formes = [
            ["voyais", "voyais", "voyait", "voyions", "voyiez", "voyaient"],
            ["vois", "vois", "voit", "voyons", "voyez", "voient"],
            ["verrai", "verras", "verra", "verrons", "verrez", "verront"],
            ["vu", "voyant"]
        ]

    elif verbe == "savoir":
        formes = [
            ["savais", "savais", "savait", "savions", "saviez", "savaient"],
            ["sais", "sais", "sait", "savons", "savez", "savent"],
            ["saurai", "sauras", "saura", "saurons", "saurez", "sauront"],
            ["su", "sachant"]
        ]
    elif verbe == "pouvoir":
        formes = [
            ["pouvais", "pouvais", "pouvait", "pouvions", "pouviez", "pouvaient"],
            ["peux", "peux", "peut", "pouvons", "pouvez", "peuvent"],
            ["pourrai", "pourras", "pourra", "pourrons", "pourrez", "pourront"],
            ["pu", "pouvant"]
        ]
    elif verbe == "résoudre":
        formes = [
            ["résolvais", "résolvais", "résolvait",
                "résolvions", "résolviez", "résolvaient"],
            ["résous", "résous", "résout", "résolvons", "résolvez", "résolvent"],
            ["résoudrai", "résoudras", "résoudra",
                "résoudrons", "résoudrez", "résoudront"],
            ["résolu", "résolvant"]
        ]
    elif verbe == "mordre":
        formes = [
            ["mordais", "mordais", "mordait", "mordions", "mordiez", "mordaient"],
            ["mords", "mords", "mord", "mordons", "mordez", "mordent"],
            ["mordrai", "mordras", "mordra", "mordrons", "mordrez", "mordront"],
            ["mordu", "mordant"]
        ]
    elif verbe == "envoyer":
        formes = [
            ["envoyais", "envoyais", "envoyait",
                "envoyions", "envoyiez", "envoyaient"],
            ["envoie", "envoies", "envoie", "envoyons", "envoyez", "envoient"],
            ["enverrai", "enverras", "enverra",
                "enverrons", "enverrez", "enverront"],
            ["envoyé", "envoyant"]
        ]
    elif verbe == "faire":
        formes = [
            ["faisais", "faisais", "faisait", "faisions", "faisiez", "faisaient"],
            ["fais", "fais", "fait", "faisons", "faites", "font"],
            ["ferai", "feras", "fera", "ferons", "ferez", "feront"],
            ["fait", "faisant"]
        ]
    elif verbe == "vouloir":
        formes = [
            ["voulais", "voulais", "voulait", "voulions", "vouliez", "voulaient"],
            ["veux", "veux", "veut", "voulons", "voulez", "veulent"],
            ["voudrai", "voudras", "voudra", "voudrons", "voudrez", "voudront"],
            ["voulu", "voulant"]
        ]
    elif verbe == "croire":
        formes = [
            ["croyais", "croyais", "croyait", "croyions", "croyiez", "croyaient"],
            ["crois", "crois", "croit", "croyons", "croyez", "croient"],
            ["croirai", "croiras", "croira", "croirons", "croirez", "croiront"],
            ["cru", "croyant"]
        ]
    elif verbe == "rire":
        formes = [
            ["riais", "riais", "riait", "riions", "riiez", "riaient"],
            ["ris", "ris", "rit", "rions", "riez", "rient"],
            ["rirai", "riras", "rira", "rirons", "rirez", "riront"],
            ["ri", "riant"]
        ]
    elif verbe == "lire":
        formes = [
            ["lisais", "lisais", "lisait", "lisions", "lisiez", "lisaient"],
            ["lis", "lis", "lit", "lisons", "lisez", "lisent"],
            ["lirai", "liras", "lira", "lirons", "lirez", "liront"],
            ["lu", "lisant"]
        ]
    elif verbe == "dire":
        formes = [
            ["disais", "disais", "disait", "disions", "disiez", "disaient"],
            ["dis", "dis", "dit", "disons", "dites", "disent"],
            ["dirai", "diras", "dira", "dirons", "direz", "diront"],
            ["dit", "disant"]
        ]
    elif verbe == "interdire":
        formes = [
            ["interdisais", "interdisais", "interdisait",
                "interdisions", "interdisiez", "interdisaient"],
            ["interdis", "interdis", "interdit",
                "interdisons", "interdisez", "interdisent"],
            ["interdirai", "interdiras", "interdira",
                "interdirons", "interdirez", "interdiront"],
            ["interdit", "interdisant"]
        ]
    elif verbe == "suivre":
        formes = [
            ["suivais", "suivais", "suivait", "suivions", "suiviez", "suivaient"],
            ["suis", "suis", "suit", "suivons", "suivez", "suivent"],
            ["suivrai", "suivras", "suivra", "suivrons", "suivrez", "suivront"],
            ["suivi", "suivant"]
        ]
    elif verbe == "perdre":
        formes = [
            ["perdais", "perdais", "perdait", "perdions", "perdiez", "perdaient"],
            ["perds", "perds", "perd", "perdons", "perdez", "perdent"],
            ["perdrai", "perdras", "perdra", "perdrons", "perdrez", "perdront"],
            ["perdu", "perdant"]
        ]
    elif verbe == "dormir":
        formes = [
            ["dormais", "dormais", "dormait", "dormions", "dormiez", "dormaient"],
            ["dors", "dors", "dort", "dormons", "dormez", "dorment"],
            ["dormirai", "dormiras", "dormira",
                "dormirons", "dormirez", "dormiront"],
            ["dormi", "dormant"]
        ]
    elif verbe == "courir":
        formes = [
            ["courais", "courais", "courait", "courions", "couriez", "couraient"],
            ["cours", "cours", "court", "courons", "courez", "courent"],
            ["courrai", "courras", "courra", "courrons", "courrez", "courront"],
            ["couru", "courant"]
        ]
    elif verbe == "recourir":
        formes = [
            ["recourais", "recourais", "recourait",
                "recourions", "recouriez", "recouraient"],
            ["recours", "recours", "recourt", "recourons", "recourez", "recourent"],
            ["recourrai", "recourras", "recourra",
                "recourrons", "recourrez", "recourront"],
            ["recouru", "recourant"]
        ]
    elif verbe == "mourir":
        formes = [
            ["mourais", "mourais", "mourait", "mourions", "mouriez", "mouraient"],
            ["meurs", "meurs", "meurt", "mourons", "mourez", "meurent"],
            ["mourrai", "mourras", "mourra", "mourrons", "mourrez", "mourront"],
            ["mort", "mourant"]
        ]
    elif verbe == "plaire":
        formes = [
            ["plaisais", "plaisais", "plaisait",
                "plaisions", "plaisiez", "plaisaient"],
            ["plais", "plais", "plaît", "plaisons", "plaisez", "plaisent"],
            ["plairai", "plairas", "plaira", "plairons", "plairez", "plairont"],
            ["plu", "plaisant"]
        ]
    elif verbe == "nuire":
        formes = [
            ["nuisais", "nuisais", "nuisait", "nuisions", "nuisiez", "nuisaient"],
            ["nuis", "nuis", "nuit", "nuisons", "nuisez", "nuisent"],
            ["nuirai", "nuiras", "nuira", "nuirons", "nuirez", "nuiront"],
            ["nui", "nuisant"]
        ]
    elif verbe == "fuir":
        formes = [
            ["fuyais", "fuyais", "fuyait", "fuyions", "fuyiez", "fuyaient"],
            ["fuis", "fuis", "fuit", "fuyons", "fuyez", "fuient"],
            ["fuirai", "fuiras", "fuira", "fuirons", "fuirez", "fuiront"],
            ["fui", "fuyant"]
        ]
    elif verbe == "enfuir":
        formes = [
            ["enfuyais", "enfuyais", "enfuyait",
                "enfuyions", "enfuyiez", "enfuyaient"],
            ["enfuis", "enfuis", "enfuit", "enfuyons", "enfuyez", "enfuient"],
            ["enfuirai", "enfuiras", "enfuira",
                "enfuirons", "enfuirez", "enfuiront"],
            ["enfui", "enfuyant"]
        ]
    elif verbe == "fair":
        formes = [
            ["faissais", "faissais", "faissait",
                "faissions", "faissiez", "faissaient"],
            ["fais", "fais", "fait", "faissons", "faissez", "faissent"],
            ["fairai", "fairas", "faira", "fairons", "fairez", "fairont"],
            ["fai", "faissant"]
        ]
    if t != 0:
        return racine+terminaisons[temps][prs]
    else:
        # print("DB : "+verbe+","+str(temps)+","+str(prs))
        return formes[temps][prs]


def listStructure():
    listing = []
    # 3 cas : [CT, VG, GN] ou [CL, VG, GN] ou [GN]
    choice = randint(0, 0)
    if choice == 0:
        listing.append("GN")
    # 1 cas par verbe modal possible (ou absence de modal)(+ 3 pour les éventuels AP)(total : 7)
    choice = randint(0, 0)
    if choice == 0:
        listing.append("")
    # 1 cas par verbe principal possible (44 actuellement)
    choice = randint(0, 5)
    if choice == 0:
        listing.append("VT")
        listing.append("GN")
    elif choice == 1:
        listing.append("VT")
        listing.append("CO")
    elif choice == 2:
        listing.append("VT")
        listing.append("AP")
        listing.append("GN")
    elif choice == 3:
        listing.append("VT")
        listing.append("AP")
        listing.append("CO")
    elif choice == 4:
        listing.append("VTL")
        listing.append("CL")
    elif choice == 5:
        listing.append("VTL")
        listing.append("AP")
        listing.append("CL")
    return listing


def removeF(word):
    if word.find('_') != -1:
        return word[:-2]
    else:
        return word


def personneFinder(word):
    if word.find('@') != 0:
        return int(word[word.find('@')+1])
    else:
        return word


def generateur():
    structure = listStructure()
    sentence = ""
    prs = 2
    for i in structure:
        if i == "GN":
            if randint(0, 1):
                max = 0
                max = randint(0, len(f["sujet"]["GN"]["NP"]))
                rdnGN = removeF(f["sujet"]["GN"]["NP"][max-1])

            else:
                max = randint(0, len(f["sujet"]["GN"]["classique"])-1)
                rdnGN = removeF(f["sujet"]["GN"]["classique"][max])
                prs = personneFinder(f["sujet"]["GN"]["classique"][max])-1
                if rdnGN[-1] == '_':
                    rdnGN = rdnGN[:-3]
                else:
                    rdnGN = rdnGN[:-2]
            sentence += rdnGN+" "
        elif i == "VT":
            max = 0
            max = randint(0, len(f["verbe"]["transitif"])-1)
            rdnVerbe = f["verbe"]["transitif"][max]
            verbe = conjugeur(rdnVerbe, randint(0, 2), prs)
            prs = 2
            sentence += verbe+" "
        elif i == "CO":
            max = randint(0, len(f["complements"]["objDir"])-1)
            co = f["complements"]["objDir"][max]
            sentence += co+" "
        elif i == "AP":
            max = randint(0, len(f["adverbes"]["postpose"])-1)
            ap = f["adverbes"]["postpose"][max]
            sentence += ap+" "
        elif i == "VTL":
            part2 = ""
            part1 = ""
            max = randint(0, len(f["verbe"]["avecPreposition"]["lieu"])-1)
            rdnVerbe = f["verbe"]["avecPreposition"]["lieu"][max]
            if rdnVerbe == "s'enfuir":
                rdnVerbe = "fuir"
                part1 = "s'en"
            else:
                if rdnVerbe.find('{') != -1:
                    part2 = rdnVerbe[rdnVerbe.find('{')+1:-1]+" "
                    rdnVerbe = rdnVerbe[:rdnVerbe.find('{')]
                if rdnVerbe[:2] == "se":
                    rdnVerbe = rdnVerbe[3:]
                    part1 = "se "
                elif rdnVerbe[:2] == "s":
                    rdnVerbe = rdnVerbe[2:]
                    part1 = "s'"
            verbe = conjugeur(rdnVerbe, randint(0, 2), prs)
            prs = 2
            sentence += part1+verbe+" "+part2
        elif i == "CL":
            max = randint(0, len(f["complements"]["lieu"])-1)
            lieu = f["complements"]["lieu"][max]
            while lieu.find('$') != -1:
                max = 0
                max = randint(0, len(f["sujet"]["GN"]["NP"]))
                rdnGN = removeF(f["sujet"]["GN"]["NP"][max-1])+" "
                lieu = lieu.replace("$", rdnGN)

            sentence += lieu+" "

    return sentence[:-1]

def exportToFile(x):
    myfile = open("Data/exemple.txt","a",encoding="utf-8")
    for i in range(0, x):
        myfile.write(generateur()+"\n")
    myfile.close()



# print(len(f["sujet"]["GN"]["NP"]))
# print("Tu "+conjugeur("chanter#1", 2, 1))
# for i in range(0, 10):
#     print(generateur())

exportToFile(100000)
print("DONE !")

import json
from random import *

f = json.load(open("Data/mydata.json", "r", encoding="utf-8"))


def VerbeType(verbe):
    if verbe.find('#') == -1:
        return 0
    else:
        return int(verbe[verbe.find('#')+1:])


def conjugeur(verbe, temps, prs):
    t = VerbeType(verbe)
    verbe = verbe[:verbe.find('#')]
    racine = ""
    terminaisons = []
    if t == 1:  # 1 : (modèle: chanter)
        racine = verbe[:-2]
        terminaisons = [
        ["ais", "ais", "ait", "ions", "iez", "aient"],
        ["e", "es", "e", "ons", "ez", "ent"],
        ["erai", "eras", "era", "erons", "erez", "eront"],
        ["é", "ant"]
        ]
    elif t == 2:  # 2 : (modèle: finir)
        racine = verbe[:-3]
        terminaisons = [
        ["issais", "issais", "issait", "issions", "issiez", "issaient"],
        ["is", "is", "it", "issons", "issez", "issent"],
        ["irai", "iras", "ira", "irons", "irez", "iront"],
        ["i", "issant"]
        ]
    elif t == 3:  # 3 : (modèle: sentir)
        racine = verbe[:-2]
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
    # if t==11: #11 : (modèle: récupérer/accéder)
    #     var posEaigu = verbe.lastIndexOf("é");
    #     racine = verbe[:-2]= verbe.replace(/^(.*)é([^é]*)er#11$/, "$2");
    #     terminaisons = [
    #     ["é_ais", "é_ais", "é_ait", "é_ions", "é_iez", "é_aient"],
    #     ["è_e", "è_es", "è_e", "é_ons", "é_ez", "è_ent"],
    #     ["é_erai", "é_eras", "é_era", "é_erons", "é_erez", "é_eront"],
    #     ["é_é", "é_ant"]
    #     ]
    # if t==12: #12 : (modèle: mener/lever/peser)
    #     var posEfaible = verbe.lastIndexOf("e");
    #     posEfaible = verbe.substr(0, posEfaible).lastIndexOf("e");
    #     racine = verbe[:-2]r = verbe.replace(/^(.*)e([^e]*)er#12$/, "$2");
    #     terminaisons = [
    #     ["e_ais", "e_ais", "e_ait", "e_ions", "e_iez", "e_aient"],
    #     ["è_e", "è_es", "è_e", "e_ons", "e_ez", "è_ent"],
    #     ["è_erai", "è_eras", "è_era", "è_erons", "è_erez", "è_eront"],
    #     ["e_é", "e_ant"]
    #     ]
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
    else:
        # print("ERROR "+str(t))
        return verbe

    return racine+terminaisons[temps][prs]

def listStructure():
    listing = []
    #3 cas : [CT, VG, GN] ou [CL, VG, GN] ou [GN]
    choice = randint(0,0)
    if choice==0:
        listing.append("GN")
    #1 cas par verbe modal possible (ou absence de modal)(+ 3 pour les éventuels AP)(total : 7)
    choice = randint(0,0)
    if choice==0:
        listing.append("")
    #1 cas par verbe principal possible (44 actuellement)
    choice = randint(0,0)
    if choice==0:
        listing.append("VT")
        listing.append("GN")
    return listing

def generateur():
    structure = listStructure()
    sentence = ""
    for i in structure:
        if i=="GN":
            rdnGN = f["sujet"]["GN"]["NP"][randint(0,len(f["sujet"]["GN"]["NP"]))]
            sentence += rdnGN+" "
        elif i=="VT":
            rdnVerbe = f["verbe"]["transitif"][randint(0, len(f["verbe"]["transitif"]))]
            verbe = conjugeur(rdnVerbe, randint(0,2), 2)
            sentence += verbe+" "
    return sentence[:-1]


print(len(f["sujet"]["GN"]["NP"]))
print("Tu "+conjugeur("chanter#1", 2, 1))
for i in range(0,12):
    print(generateur())

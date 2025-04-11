import requests
import argparse
import sys

host = "https://api.runelite.net/runelite-1.10.38.1/chat/"
runelite_auth = ""

parser=argparse.ArgumentParser()

parser.add_argument('--rsn', help='Enter in the in game rsn of the user you want to modify kc/pb for.')
parser.add_argument('--boss', help='Enter in the boss name that you want to modify the kc/pb for.')
parser.add_argument('--kc', help='Enter in the kc you want to set.')
parser.add_argument('--pb', help='Enter in the pb in seconds you want to set.')

args=parser.parse_args()


def new_line_print(input):
    print("\n" + input)


def set_kc(rsn, boss, kc):
    headers = {
        "RUNELITE-AUTH": runelite_auth
    }
    params = {
        "name": rsn,
        "boss": boss,
        "kc": kc
    }
    response = requests.post(host + "kc", headers=headers, params=params)
    if response.status_code != 200:
        print("Error occurred setting killcount. Error: " + response.text)


def get_kc(rsn, boss, kc):
    headers = {
        "RUNELITE-AUTH": runelite_auth
    }
    params = {
        "name": rsn,
        "boss": boss,
        "kc": kc
    }
    response = requests.get(host + "kc", headers=headers, params=params)
    if response.status_code != 200:
        print("Error occurred setting killcount. Error: " + response.text)
    else:
        print(response.json())


def set_pb(rsn, boss, pb):
    headers = {
        "RUNELITE-AUTH": runelite_auth
    }
    params = {
        "name": rsn,
        "boss": boss,
        "pb": pb
    }
    response = requests.post(host + "pb", headers=headers, params=params)
    if response.status_code != 200:
        print("Error occurred setting pb. Error: " + response.text)


if args.rsn is None:
    new_line_print("Error occurred due to rsn argument missing.")
    exit()
elif args.boss is None:
    new_line_print("Error occurred due to boss argument missing.")
    exit()
elif args.kc is None and args.pb is None:
    new_line_print("Error occurred due to neither a kc or pb argument was provided.")
    exit()


boss_abbreviation_dict = dict()
boss_abbreviation_dict["corp"] = "Corporeal Beast"
boss_abbreviation_dict["jad"] = "TzTok-Jad"
boss_abbreviation_dict["tzhaar fight cave"] = "TzTok-Jad"
boss_abbreviation_dict["kq"] = "Kalphite Queen"
boss_abbreviation_dict["chaos ele"] = "Chaos Elemental"
boss_abbreviation_dict["dusk"] = "Grotesque Guardians"
boss_abbreviation_dict["dawn"] = "Grotesque Guardians"
boss_abbreviation_dict["gargs"] = "Grotesque Guardians"
boss_abbreviation_dict["ggs"] = "Grotesque Guardians"
boss_abbreviation_dict["gg"] = "Grotesque Guardians"
boss_abbreviation_dict["crazy arch"] = "Crazy Archaeologist"
boss_abbreviation_dict["deranged arch"] = "Deranged Archaeologist"
boss_abbreviation_dict["mole"] = "Giant Mole"
boss_abbreviation_dict["vetion"] = "Vet'ion"
boss_abbreviation_dict["vene"] = "Venenatis"
boss_abbreviation_dict["kbd"] = "King Black Dragon"
boss_abbreviation_dict["vork"] = "Vorkath"
boss_abbreviation_dict["sire"] = "Abyssal Sire"
boss_abbreviation_dict["smoke devil"] = "Thermonuclear Smoke Devil"
boss_abbreviation_dict["thermy"] = "Thermonuclear Smoke Devil"
boss_abbreviation_dict["cerb"] = "Cerberus"
boss_abbreviation_dict["zuk"] = "TzKal-Zuk"
boss_abbreviation_dict["inferno"] = "TzKal-Zuk"
boss_abbreviation_dict["hydra"] = "Alchemical Hydra"
boss_abbreviation_dict["sara"] = "Commander Zilyana"
boss_abbreviation_dict["saradomin"] = "Commander Zilyana"
boss_abbreviation_dict["zilyana"] = "Commander Zilyana"
boss_abbreviation_dict["zily"] = "Commander Zilyana"
boss_abbreviation_dict["zammy"] = "K'ril Tsutsaroth"
boss_abbreviation_dict["zamorak"] = "K'ril Tsutsaroth"
boss_abbreviation_dict["kril"] = "K'ril Tsutsaroth"
boss_abbreviation_dict["kril trutsaroth"] = "K'ril Tsutsaroth"
boss_abbreviation_dict["arma"] = "Kree'arra"
boss_abbreviation_dict["kree"] = "Kree'arra"
boss_abbreviation_dict["kreearra"] = "Kree'arra"
boss_abbreviation_dict["armadyl"] = "Kree'arra"
boss_abbreviation_dict["bando"] = "General Graardor"
boss_abbreviation_dict["bandos"] = "General Graardor"
boss_abbreviation_dict["graardor"] = "General Graardor"
boss_abbreviation_dict["supreme"] = "Dagannoth Supreme"
boss_abbreviation_dict["rex"] = "Dagannoth Rex"
boss_abbreviation_dict["prime"] = "Dagannoth Prime"
boss_abbreviation_dict["wt"] = "Wintertodt"
boss_abbreviation_dict["barrows"] = "Barrows Chests"
boss_abbreviation_dict["herbi"] = "Herbiboar"
boss_abbreviation_dict["cox"] = "Chambers of Xeric"
boss_abbreviation_dict["xeric"] = "Chambers of Xeric"
boss_abbreviation_dict["chambers"] = "Chambers of Xeric"
boss_abbreviation_dict["olm"] = "Chambers of Xeric"
boss_abbreviation_dict["raids"] = "Chambers of Xeric"
boss_abbreviation_dict["cox cm"] = "Chambers of Xeric Challenge Mode"
boss_abbreviation_dict["xeric cm"] = "Chambers of Xeric Challenge Mode"
boss_abbreviation_dict["chambers cm"] = "Chambers of Xeric Challenge Mode"
boss_abbreviation_dict["olm cm"] = "Chambers of Xeric Challenge Mode"
boss_abbreviation_dict["raids cm"] = "Chambers of Xeric Challenge Mode"
boss_abbreviation_dict["chambers of xeric - challenge mode"] = "Chambers of Xeric Challenge Mode"
boss_abbreviation_dict["tob"] = "Theatre of Blood"
boss_abbreviation_dict["theatre"] = "Theatre of Blood"
boss_abbreviation_dict["verzik"] = "Theatre of Blood"
boss_abbreviation_dict["verzik vitur"] = "Theatre of Blood"
boss_abbreviation_dict["raids 2"] = "Theatre of Blood"
boss_abbreviation_dict["theatre of blood: story mode"] = "Theatre of Blood Entry Mode"
boss_abbreviation_dict["tob sm"] = "Theatre of Blood Entry Mode"
boss_abbreviation_dict["tob story mode"] = "Theatre of Blood Entry Mode"
boss_abbreviation_dict["tob story"] = "Theatre of Blood Entry Mode"
boss_abbreviation_dict["Theatre of Blood: Entry Mode"] = "Theatre of Blood Entry Mode"
boss_abbreviation_dict["tob em"] = "Theatre of Blood Entry Mode"
boss_abbreviation_dict["tob entry mode"] = "Theatre of Blood Entry Mode"
boss_abbreviation_dict["tob entry"] = "Theatre of Blood Entry Mode"
boss_abbreviation_dict["theatre of blood: hard mode"] = "Theatre of Blood Hard Mode"
boss_abbreviation_dict["tob cm"] = "Theatre of Blood Hard Mode"
boss_abbreviation_dict["tob hm"] = "Theatre of Blood Hard Mode"
boss_abbreviation_dict["tob hard mode"] = "Theatre of Blood Hard Mode"
boss_abbreviation_dict["tob hard"] = "Theatre of Blood Hard Mode"
boss_abbreviation_dict["prif"] = "Prifddinas Agility Course"
boss_abbreviation_dict["prifddinas"] = "Prifddinas Agility Course"
boss_abbreviation_dict["gaunt"] = "Gauntlet"
boss_abbreviation_dict["gauntlet"] = "Gauntlet"
boss_abbreviation_dict["the gauntlet"] = "Gauntlet"
boss_abbreviation_dict["cgaunt"] = "Corrupted Gauntlet"
boss_abbreviation_dict["cgauntlet"] = "Corrupted Gauntlet"
boss_abbreviation_dict["the corrupted gauntlet"] = "Corrupted Gauntlet"
boss_abbreviation_dict["cg"] = "Corrupted Gauntlet"
boss_abbreviation_dict["nm"] = "Nightmare"
boss_abbreviation_dict["tnm"] = "Nightmare"
boss_abbreviation_dict["nmare"] = "Nightmare"
boss_abbreviation_dict["the nightmare"] = "Nightmare"
boss_abbreviation_dict["pnm"] = "Phosani's Nightmare"
boss_abbreviation_dict["phosani"] = "Phosani's Nightmare"
boss_abbreviation_dict["phosanis"] = "Phosani's Nightmare"
boss_abbreviation_dict["phosani nm"] = "Phosani's Nightmare"
boss_abbreviation_dict["phosani nightmare"] = "Phosani's Nightmare"
boss_abbreviation_dict["phosanis nightmare"] = "Phosani's Nightmare"
boss_abbreviation_dict["hs"] = "Hallowed Sepulchre"
boss_abbreviation_dict["sepulchre"] = "Hallowed Sepulchre"
boss_abbreviation_dict["ghc"] = "Hallowed Sepulchre"
boss_abbreviation_dict["hs1"] = "Hallowed Sepulchre Floor 1"
boss_abbreviation_dict["hs 1"] = "Hallowed Sepulchre Floor 1"
boss_abbreviation_dict["hs2"] = "Hallowed Sepulchre Floor 2"
boss_abbreviation_dict["hs 2"] = "Hallowed Sepulchre Floor 2"
boss_abbreviation_dict["hs3"] = "Hallowed Sepulchre Floor 3"
boss_abbreviation_dict["hs 3"] = "Hallowed Sepulchre Floor 3"
boss_abbreviation_dict["hs4"] = "Hallowed Sepulchre Floor 4"
boss_abbreviation_dict["hs 4"] = "Hallowed Sepulchre Floor 4"
boss_abbreviation_dict["hs5"] = "Hallowed Sepulchre Floor 5"
boss_abbreviation_dict["hs 5"] = "Hallowed Sepulchre Floor 5"
boss_abbreviation_dict["aa"] = "Ape Atoll Agility"
boss_abbreviation_dict["ape atoll"] = "Ape Atoll Agility"
boss_abbreviation_dict["draynor"] = "Draynor Village Rooftop"
boss_abbreviation_dict["draynor agility"] = "Draynor Village Rooftop"
boss_abbreviation_dict["al kharid"] = "Al-Kharid Rooftop"
boss_abbreviation_dict["al kharid agility"] = "Al-Kharid Rooftop"
boss_abbreviation_dict["al-kharid"] = "Al-Kharid Rooftop"
boss_abbreviation_dict["al-kharid agility"] = "Al-Kharid Rooftop"
boss_abbreviation_dict["alkharid"] = "Al-Kharid Rooftop"
boss_abbreviation_dict["alkharid agility"] = "Al-Kharid Rooftop"
boss_abbreviation_dict["varrock"] = "Varrock Rooftop"
boss_abbreviation_dict["varrock agility"] = "Varrock Rooftop"
boss_abbreviation_dict["canifis"] = "Canifis Rooftop"
boss_abbreviation_dict["canifis agility"] = "Canifis Rooftop"
boss_abbreviation_dict["fally"] = "Falador Rooftop"
boss_abbreviation_dict["fally agility"] = "Falador Rooftop"
boss_abbreviation_dict["falador"] = "Falador Rooftop"
boss_abbreviation_dict["falador agility"] = "Falador Rooftop"
boss_abbreviation_dict["seers"] = "Seers' Village Rooftop"
boss_abbreviation_dict["seers agility"] = "Seers' Village Rooftop"
boss_abbreviation_dict["seers village"] = "Seers' Village Rooftop"
boss_abbreviation_dict["seers village agility"] = "Seers' Village Rooftop"
boss_abbreviation_dict["seers'"] = "Seers' Village Rooftop"
boss_abbreviation_dict["seers' agility"] = "Seers' Village Rooftop"
boss_abbreviation_dict["seers' village"] = "Seers' Village Rooftop"
boss_abbreviation_dict["seers' village agility"] = "Seers' Village Rooftop"
boss_abbreviation_dict["seer's"] = "Seers' Village Rooftop"
boss_abbreviation_dict["seer's agility"] = "Seers' Village Rooftop"
boss_abbreviation_dict["seer's village"] = "Seers' Village Rooftop"
boss_abbreviation_dict["seer's village agility"] = "Seers' Village Rooftop"
boss_abbreviation_dict["pollnivneach"] = "Pollnivneach Rooftop"
boss_abbreviation_dict["pollnivneach agility"] = "Pollnivneach Rooftop"
boss_abbreviation_dict["rellekka"] = "Rellekka Rooftop"
boss_abbreviation_dict["rellekka agility"] = "Rellekka Rooftop"
boss_abbreviation_dict["ardy"] = "Ardougne Rooftop"
boss_abbreviation_dict["ardy agility"] = "Ardougne Rooftop"
boss_abbreviation_dict["ardy rooftop"] = "Ardougne Rooftop"
boss_abbreviation_dict["ardougne"] = "Ardougne Rooftop"
boss_abbreviation_dict["ardougne agility"] = "Ardougne Rooftop"
boss_abbreviation_dict["ap"] = "Agility Pyramid"
boss_abbreviation_dict["pyramid"] = "Agility Pyramid"
boss_abbreviation_dict["barb"] = "Barbarian Outpost"
boss_abbreviation_dict["barb outpost"] = "Barbarian Outpost"
boss_abbreviation_dict["brimhaven"] = "Agility Arena"
boss_abbreviation_dict["brimhaven agility"] = "Agility Arena"
boss_abbreviation_dict["dorg"] = "Dorgesh-Kaan Agility"
boss_abbreviation_dict["dorgesh kaan"] = "Dorgesh-Kaan Agility"
boss_abbreviation_dict["dorgesh-kaan"] = "Dorgesh-Kaan Agility"
boss_abbreviation_dict["gnome stronghold"] = "Gnome Stronghold Agility"
boss_abbreviation_dict["penguin"] = "Penguin Agility"
boss_abbreviation_dict["werewolf"] = "Werewolf Agility"
boss_abbreviation_dict["skullball"] = "Werewolf Skullball"
boss_abbreviation_dict["wildy"] = "Wilderness Agility"
boss_abbreviation_dict["wildy agility"] = "Wilderness Agility"
boss_abbreviation_dict["jad 1"] = "TzHaar-Ket-Rak's First Challenge"
boss_abbreviation_dict["jad 2"] = "TzHaar-Ket-Rak's Second Challenge"
boss_abbreviation_dict["jad 3"] = "TzHaar-Ket-Rak's Third Challenge"
boss_abbreviation_dict["jad 4"] = "TzHaar-Ket-Rak's Fourth Challenge"
boss_abbreviation_dict["jad 5"] = "TzHaar-Ket-Rak's Fifth Challenge"
boss_abbreviation_dict["jad 6"] = "TzHaar-Ket-Rak's Sixth Challenge"

actual_boss_name = args.boss.title()
if args.boss in boss_abbreviation_dict:
    actual_boss_name = boss_abbreviation_dict[args.boss]

if args.kc is not None and args.pb is not None:
    new_line_print("Setting %s killcount to %s and personal best to %s seconds for rsn '%s'." % (actual_boss_name, args.kc, args.pb, args.rsn))
    set_kc(args.rsn, actual_boss_name, args.kc)
    set_pb(args.rsn, actual_boss_name, args.pb)
elif args.kc is None and args.pb is not None:
    new_line_print("Setting %s personal best to %s seconds for rsn '%s'." % (actual_boss_name, args.pb, args.rsn))
    set_pb(args.rsn, actual_boss_name, args.pb)
elif args.kc is not None and args.pb is None:
    new_line_print("Setting %s killcount to %s for rsn '%s'." % (actual_boss_name, args.kc, args.rsn))
    set_kc(args.rsn, actual_boss_name, args.kc)
    get_kc(args.rsn, actual_boss_name, args.kc)


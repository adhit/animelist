from mal import AnimeSearch

def fetch_urls(names_list):
    print('test0')
    print(names_list)
    urls_list = map(
        lambda name: AnimeSearch(name).results[0].url,
        names_list
    )
    print(list(urls_list))

names_list = [
    "86 Eighty-Six",
    "A Sister's All You Need",
    "Afro Samurai",
    "Akagi ",
    "Alice in Borderland",
    "Angel Beats",
    "AnoHana",
    "Assassination Classroom",
    "Baccano",
    "Bakuman",
    "Baslik",
    "Battle Royale",
    "Beastars",
    "Beelzebub",
    "Berserk",
    "Black Clover",
    "Black Lagoon",
    "Bleach",
    "Blue Spring ride",
    "BNA",
    "BOFURI: I Don't Want to Get Hurt, so I'll Max Out My Defense.",
    "Bokurano",
    "Btooom!",
    "Bungo Stray Dogs",
    "Cage of Eden",
    "Captain Tsubasa",
    "Cardcaptor Sakura",
    "Case Closed / Detective Conan",
    "Chainsaw Man",
    "Clannad",
    "Claymore",
    "Code Geass",
    "Cowboy Bebop",
    "Death Note",
    "Death Parade",
    "Digimon, first season / OG",
    "Don't Toy with Me, Miss Nagatoro",
    "Doubt",
    "Dragon Ball Super",
    "Dragon Ball Z",
    "Dr. Stone",
    "Elfen Lied",
    "Eyeshield 21",
    "Flame of Recca",
    "FLCL",
    "Fruit Basket",
    "Full Metal Alchemist",
    "Full Metal Alchemist: Brotherhood",
    "Durarara!!",
    "Gantz",
    "Golden Time",
    "Grand Blue Dreaming",
    "Great Teacher Onizuka",
    "Gurren Lagann",
    "Haikyuu",
    "Hajime no Ippo",
    "Hellsing Ultimate",
    "High School of the Dead",
    "High School DxD",
    "Hunter X Hunter",
    "Idaten Deities Know Only Peace",
    "Inuyasha",
    "Jojo's Bizarre Adventure",
    "Jujutsu Kaisen",
    "Jujutsu Kaisen 0",
    "Kaiji",
    "Kami Sama no Iutoori / As The God Wills",
    "Kenichi: The Mightiest Disciple",
    "Kimetsu no Yaiba / Demon Slayer",
    "Law of Ueki",
    "Liar Game",
    "Little Busters",
    "Made in Abyss",
    "Masamunes-kun's Revenge",
    "Mirrai Niiki // Future Diary",
    "Mob Psycho 100",
    "Mobile Fighter G Gundam",
    "Mobile Suit Gundam 00",
    "Mobile Suit Gundam SEED",
    "Mobile Suit Gundam SEED: Destiny",
    "Mobile Suit Gundam Wing",
    "Monster",
    "Mushoku Tensei",
    "My Hero Academia",
    "Nana",
    "Naruto",
    "Negima! Magister Negi Magi",
    "Neon Genesis Evangelion",
    "Night Head 2041",
    "No Game No Life",
    "My Dress-Up Darling",
    "One Outs",
    "One Piece",
    "One Punch Man",
    "Orient",
    "Parasyte",
    "Prison School",
    "Puella Magi Madoka Magica",
    "Re: Zero",
    "Record of Ragnarok",
    "Rurouni Kenshin",
    "Sabikui Bisco",
    "Saint Seiya",
    "Samurai Champloo",
    "Say I love you",
    "School Days",
    "Serial Experiments Lain ",
    "Shenmue The Animation",
    "Shingeki No Kyojin / Attack on Titan",
    "Steins;Gate ",
    "Super Dragon Ball Heroes",
    "The Case Study of Vanitas",
    "The Faraway Paladin",
    "The Fruit of Evolution",
    "The Promised Neverland",
    "The Rose of Versailles",
    "The Strongest Sage with the Weakest Crest",
    "The World's Finest Assassin Gets Reincarnated in Another World as an Aristocrat",
    "Tiger & Bunny",
    "Tokyo Ghoul",
    "Tokyo Revenger",
    "Toradora",
    "Toriko",
    "When They Cry",
    "Wolf Rain",
    "Your Lie in April",
    "Yu Yu Hakusho",
    "YuGiOh",
    "Yurri on Ice"
]
fetch_urls(names_list)

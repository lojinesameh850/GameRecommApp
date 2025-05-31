game_images = {
    "the_witcher_3": "https://upload.wikimedia.org/wikipedia/en/0/0c/Witcher_3_cover_art.jpg",
    "minecraft": "https://upload.wikimedia.org/wikipedia/en/5/51/Minecraft_cover.png",
    "call_of_duty": "https://upload.wikimedia.org/wikipedia/en/8/8d/Call_of_Duty_Modern_Warfare_2_cover.jpg",
    "stardew_valley": "https://upload.wikimedia.org/wikipedia/en/f/fd/Stardew_Valley_Cover_Art.png",
    "dark_souls": "https://upload.wikimedia.org/wikipedia/en/5/5e/Dark_Souls_cover_art.jpg",
    "animal_crossing": "https://upload.wikimedia.org/wikipedia/en/1/1f/Animal_Crossing_New_Horizons.jpg",
    "fifa_2024": "https://upload.wikimedia.org/wikipedia/en/5/53/FIFA_24_cover_art.jpg",
    "cyberpunk_2077": "https://upload.wikimedia.org/wikipedia/en/9/9f/Cyberpunk_2077_box_art.jpg",
    "among_us": "https://upload.wikimedia.org/wikipedia/en/9/9a/Among_Us_cover_art.jpg",
    "fortnite": "https://upload.wikimedia.org/wikipedia/en/thumb/6/6b/Fortnite_logo.svg/2560px-Fortnite_logo.svg.png",
    "candy_crush": "https://upload.wikimedia.org/wikipedia/en/5/54/Candy_Crush_Saga_cover.png",
    "super_mario_bros": "https://upload.wikimedia.org/wikipedia/en/5/5d/Super_Mario_Bros._box.png",
    "resident_evil_4": "https://upload.wikimedia.org/wikipedia/en/f/fb/Resident_Evil_4_Box_Art.jpg",
    "portal_2": "https://upload.wikimedia.org/wikipedia/en/f/f9/Portal2cover.jpg",
    "celeste": "https://upload.wikimedia.org/wikipedia/en/b/b5/Celeste_logo.png",
    "terraria": "https://upload.wikimedia.org/wikipedia/en/9/92/Terraria_cover.png",
    "half-life_2": "https://upload.wikimedia.org/wikipedia/en/2/25/Half-Life_2_cover.jpg",
    "ark_survival_evolved": "https://upload.wikimedia.org/wikipedia/en/0/05/ARK_Survival_Evolved_cover_art.jpg",
    "marvel_rivals": "https://static.wikia.nocookie.net/marvelrivals/images/1/1b/Marvel_Rivals_logo.png",
    "spelunky": "https://upload.wikimedia.org/wikipedia/en/f/f9/Spelunky_cover.jpg",
    "tetris": "https://upload.wikimedia.org/wikipedia/en/7/7d/Tetris_logo.svg",
    "league_of_legends": "https://upload.wikimedia.org/wikipedia/en/7/7f/League_of_Legends_cover_art.jpg",
    "journey": "https://upload.wikimedia.org/wikipedia/en/7/7b/Journey_cover_art.jpg",
    "hades": "https://upload.wikimedia.org/wikipedia/en/0/0f/Hades_cover_art.jpg",
    "rocket_league": "https://upload.wikimedia.org/wikipedia/en/7/7b/Rocket_League_cover_art.jpg",
    "dead_by_daylight": "https://upload.wikimedia.org/wikipedia/en/f/f7/Dead_by_Daylight_cover_art.jpg",
    "firewatch": "https://upload.wikimedia.org/wikipedia/en/f/f0/Firewatch_cover_art.jpg",
    "hollow_knight": "https://upload.wikimedia.org/wikipedia/en/3/34/Hollow_Knight_cover_art.jpg",
    "clash_of_clans": "https://upload.wikimedia.org/wikipedia/en/5/5a/Clash_of_Clans_logo.png",
    "god_of_war": "https://upload.wikimedia.org/wikipedia/en/a/a7/God_of_War_4_cover.jpg",
    "it_takes_two": "https://upload.wikimedia.org/wikipedia/en/3/31/It_Takes_Two_cover_art.jpg",
    "valorant": "https://upload.wikimedia.org/wikipedia/en/0/07/Valorant_cover_art.jpg",
    "slay_the_spire": "https://upload.wikimedia.org/wikipedia/en/6/6b/Slay_the_Spire_cover_art.png",
    "roblox": "https://upload.wikimedia.org/wikipedia/en/e/e7/Roblox_Logo_2022.svg",
    "baldurs_gate_3": "https://upload.wikimedia.org/wikipedia/en/0/0f/Baldur%27s_Gate_III_cover_art.jpg",
    "little_nightmares": "https://upload.wikimedia.org/wikipedia/en/7/7a/Little_Nightmares_cover_art.jpg",
    "the_legend_of_zelda": "https://upload.wikimedia.org/wikipedia/en/a/a3/The_Legend_of_Zelda_Breath_of_the_Wild.jpg"
}

import os
import requests

os.makedirs("images", exist_ok=True)

HEADERS = {
    "User-Agent": "MyGameImageDownloader/1.0 (https://github.com/badrgello; badrgalal21@gmail.com)"
}

def download_images():
    for game_name, url in game_images.items():
        ext = url.split('.')[-1].split('?')[0]  # remove URL params if any
        filename = f"images/{game_name}.{ext}"
        if not os.path.exists(filename):
            print(f"Downloading {game_name}...")
            try:
                r = requests.get(url, headers=HEADERS)
                r.raise_for_status()
                with open(filename, 'wb') as f:
                    f.write(r.content)
                print(f"Saved to {filename}")
            except Exception as e:
                print(f"Failed to download {game_name}: {e}")
        else:
            print(f"{filename} already exists, skipping.")

if __name__ == "__main__":
    download_images()

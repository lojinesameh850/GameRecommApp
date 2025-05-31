import subprocess
import tempfile
import os
import re

def result(answers):
    """
    Process user answers and get game recommendations from Prolog
    """
    # Extract variables from answers dictionary
    age = answers['age']                    # ['child','teen','adult']
    genre = answers['genre']                # ['rpg','shooter','puzzle','platformer','sports','horror','adventure']
    platform = answers['platform']         # ['pc','console','mobile']
    session_length = answers['session_length']  # ['short','medium','long']
    game_mode = answers['game_mode']        # ['multiplayer','singleplayer']
    violence = answers['violence']          # ['yes','no']
    graphics = answers['graphics']          # ['realistic','stylized','retro']
    story = answers['story']               # ['low','medium','high']
    budget = answers['budget']             # ['free','cheap','pricey']
    online = answers['online']             # ['yes','no']
    skill = answers['skill']               # ['beginner','intermediate','expert']
    
    # Create Prolog query
    prolog_query = f"""
    % Player profile facts
    player_age('{age}').
    player_genre('{genre}').
    player_platform('{platform}').
    player_session_length('{session_length}').
    player_game_mode('{game_mode}').
    player_violence('{violence}').
    player_graphics('{graphics}').
    player_story('{story}').
    player_budget('{budget}').
    player_online('{online}').
    player_skill('{skill}').
    
    % Query all games for recommendations
    ?- findall(Game, (game(Game), suitable_for_player(Game)), RecommendedGames),
       write('Recommended Games: '), write(RecommendedGames), nl,
       findall(Game, (game(Game), \\+ suitable_for_player(Game)), NotRecommended),
       write('Not Recommended: '), write(NotRecommended), nl.
    """
    
    return query_prolog_games(prolog_query)

def parse_prolog_output(stdout: str):
    recommended = []
    not_recommended = []

    # Use regex to extract game names
    recommended_match = re.search(r"Recommended Games:\s*\[(.*?)\]", stdout)
    not_recommended_match = re.search(r"Not Recommended:\s*\[(.*?)\]", stdout)

    if recommended_match:
        recommended = [game.strip() for game in recommended_match.group(1).split(',') if game.strip()]

    if not_recommended_match:
        not_recommended = [game.strip() for game in not_recommended_match.group(1).split(',') if game.strip()]

    return recommended, not_recommended

def query_prolog_games(query):
    """
    Execute Prolog query and return results
    """
    # Create temporary Prolog file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.pl', delete=False) as temp_file:
        # Write the game database and rules
        temp_file.write(get_prolog_game_database())
        temp_file.write("\n\n")
        temp_file.write(query)
        temp_file_path = temp_file.name
    
    try:
        # Execute SWI-Prolog
        result = subprocess.run(
            ['swipl', '-q', '-t', 'halt', '-s', temp_file_path],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        recommended, not_recommended = parse_prolog_output(result.stdout)

        return {
            'success': result.returncode == 0,
            # 'output': result.stdout,
            'recommended': recommended,
            'not_recommended': not_recommended,
            'error': result.stderr
        }
    
    except subprocess.TimeoutExpired:
        return {'success': False, 'error': 'Query timeout'}
    except FileNotFoundError:
        return {'success': False, 'error': 'SWI-Prolog not found. Please install SWI-Prolog.'}
    finally:
        # Clean up temporary file
        if os.path.exists(temp_file_path):
            os.unlink(temp_file_path)

def get_prolog_game_database():
    """
    Return the Prolog game database with rules
    """
    return """
% Game definitions with attributes
game('The Witcher 3').
game('Minecraft').
game('Call of Duty').
game('Stardew Valley').
game('Dark Souls').
game('Animal Crossing').
game('FIFA 2024').
game('Cyberpunk 2077').
game('Among Us').
game('Fortnite').
game('Candy Crush').
game('Super Mario Bros').
game('Resident Evil 4').
game('Portal 2').
game('Celeste').

game('Terraria').
game('Half-Life 2').
game('ARK: Survival Evolved').
game('Marvel Rivals').
game('Spelunky').
game('Tetris').
game('League of Legends').
game('Journey').
game('Hades').
game('Rocket League').
game('Dead by Daylight').
game('Firewatch').
game('Hollow Knight').
game('Clash of Clans').
game('God of War').
game('It Takes Two').
game('Valorant').
game('Slay the Spire').
game('Roblox').
game('Baldur\'s Gate 3').
game('Little Nightmares').
game('The Legend of Zelda').

% Game attributes - updated to match your categories
game_genre('The Witcher 3', 'rpg').
game_genre('Minecraft', 'adventure').
game_genre('Call of Duty', 'shooter').
game_genre('Stardew Valley', 'adventure').
game_genre('Dark Souls', 'rpg').
game_genre('Animal Crossing', 'adventure').
game_genre('FIFA 2024', 'sports').
game_genre('Cyberpunk 2077', 'rpg').
game_genre('Among Us', 'puzzle').
game_genre('Fortnite', 'shooter').
game_genre('Candy Crush', 'puzzle').
game_genre('Super Mario Bros', 'platformer').
game_genre('Resident Evil 4', 'horror').
game_genre('Portal 2', 'puzzle').
game_genre('Celeste', 'platformer').

game_genre('Half-Life 2', 'shooter').
game_genre('Half-Life 2', 'adventure').
game_genre('Terraria', 'adventure').
game_genre('Terraria', 'platformer').
game_genre('ARK: Survival Evolved', 'adventure').
game_genre('Marvel Rivals', 'shooter').
game_genre('Spelunky', 'platformer').
game_genre('Spelunky', 'adventure').
game_genre('Tetris', 'puzzle').
game_genre('League of Legends', 'rpg').
game_genre('Journey', 'adventure').
game_genre('Hades', 'rpg').
game_genre('Rocket League', 'sports').
game_genre('Dead by Daylight', 'horror').
game_genre('Firewatch', 'adventure').
game_genre('Hollow Knight', 'platformer').
game_genre('Clash of Clans', 'strategy'). % i dont think Strategy exists
game_genre('God of War', 'rpg').
game_genre('God of War', 'adventure').
game_genre('It Takes Two', 'platformer').
game_genre('Valorant', 'shooter').
game_genre('Slay the Spire', 'puzzle').
game_genre('Slay the Spire', 'adventure').
game_genre('Roblox', 'platformer').
game_genre('Baldur\'s Gate 3', 'rpg').
game_genre('Little Nightmares', 'horror').
game_genre('The Legend of Zelda', 'adventure').
game_genre('The Legend of Zelda', 'platformer').


% Game Platform: pc, console, mobile

game_platform('The Witcher 3', 'pc').
game_platform('The Witcher 3', 'console').
game_platform('Minecraft', 'pc').
game_platform('Minecraft', 'mobile').
game_platform('Minecraft', 'console').
game_platform('Call of Duty', 'pc').
game_platform('Call of Duty', 'console').
game_platform('Call of Duty', 'mobile').
game_platform('Stardew Valley', 'pc').
game_platform('Stardew Valley', 'mobile').
game_platform('Dark Souls', 'pc').
game_platform('Dark Souls', 'console').
game_platform('Animal Crossing', 'console').
game_platform('FIFA 2024', 'pc').
game_platform('FIFA 2024', 'console').
game_platform('Cyberpunk 2077', 'pc').
game_platform('Cyberpunk 2077', 'console').
game_platform('Among Us', 'pc').
game_platform('Among Us', 'mobile').
game_platform('Fortnite', 'pc').
game_platform('Fortnite', 'console').
game_platform('Fortnite', 'mobile').
game_platform('Candy Crush', 'mobile').
game_platform('Super Mario Bros', 'console').
game_platform('Resident Evil 4', 'pc').
game_platform('Resident Evil 4', 'console').
game_platform('Portal 2', 'pc').
game_platform('Celeste', 'pc').
game_platform('Celeste', 'console').
game_platform('Half-Life 2', 'pc').
game_platform('Half-Life 2', 'console').
game_platform('Half-Life 2', 'mobile').
game_platform('Terraria', 'pc').
game_platform('Terraria', 'console').
game_platform('Terraria', 'mobile').
game_platform('ARK: Survival Evolved', 'pc').
game_platform('ARK: Survival Evolved', 'console').
game_platform('ARK: Survival Evolved', 'mobile').
game_platform('Marvel Rivals', 'pc').
game_platform('Marvel Rivals', 'console').
game_platform('Spelunky', 'pc').
game_platform('Spelunky', 'console').
game_platform('Tetris', 'pc').
game_platform('Tetris', 'console').
game_platform('Tetris', 'mobile').
game_platform('League of Legends', 'pc').
game_platform('Journey', 'pc').
game_platform('Journey', 'console').
game_platform('Hades', 'pc').
game_platform('Rocket League', 'pc').
game_platform('Rocket League', 'console').
game_platform('Dead by Daylight', 'pc').
game_platform('Dead by Daylight', 'console').
game_platform('Firewatch', 'pc').
game_platform('Firewatch', 'console').
game_platform('Hollow Knight', 'pc').
game_platform('Hollow Knight', 'console').
game_platform('Hollow Knight', 'mobile').
game_platform('Clash of Clans', 'mobile').
game_platform('God of War', 'pc').
game_platform('God of War', 'console').
game_platform('It Takes Two', 'pc').
game_platform('It Takes Two', 'console').
game_platform('Valorant', 'pc').
game_platform('Slay the Spire', 'pc').
game_platform('Roblox', 'pc').
game_platform('Roblox', 'console').
game_platform('Baldur\'s Gate 3', 'pc').
game_platform('Baldur\'s Gate 3', 'console').
game_platform('Little Nightmares', 'pc').
game_platform('Little Nightmares', 'console').
game_platform('The Legend of Zelda', 'pc').
game_platform('The Legend of Zelda', 'console').


% Age categories: child, teen, adult
game_age_category('The Witcher 3', 'adult').
game_age_category('Minecraft', 'child').
game_age_category('Call of Duty', 'adult').
game_age_category('Stardew Valley', 'child').
game_age_category('Dark Souls', 'teen').
game_age_category('Animal Crossing', 'child').
game_age_category('FIFA 2024', 'child').
game_age_category('Cyberpunk 2077', 'adult').
game_age_category('Among Us', 'child').
game_age_category('Fortnite', 'teen').
game_age_category('Candy Crush', 'child').
game_age_category('Super Mario Bros', 'child').
game_age_category('Resident Evil 4', 'adult').
game_age_category('Portal 2', 'teen').
game_age_category('Celeste', 'teen').
game_age_category('Half-Life 2', 'teen').
game_age_category('Half-Life 2', 'adult').
game_age_category('Terraria', 'child').
game_age_category('Terraria', 'teen').
game_age_category('Terraria', 'adult').
game_age_category('ARK: Survival Evolved', 'teen').
game_age_category('ARK: Survival Evolved', 'adult').
game_age_category('Marvel Rivals', 'teen').
game_age_category('Marvel Rivals', 'adult').
game_age_category('Spelunky', 'teen').
game_age_category('Spelunky', 'adult').
game_age_category('Tetris', 'child').
game_age_category('League of Legends', 'teen').
game_age_category('Journey', 'adult').
game_age_category('Hades', 'adult').
game_age_category('Rocket League', 'teen').
game_age_category('Dead by Daylight', 'adult').
game_age_category('Firewatch', 'adult').
game_age_category('Hollow Knight', 'teen').
game_age_category('Clash of Clans', 'child').
game_age_category('God of War', 'teen').
game_age_category('God of War', 'adult').
game_age_category('It Takes Two', 'adult').
game_age_category('Valorant', 'teen').
game_age_category('Slay the Spire', 'adult').
game_age_category('Roblox', 'child').
game_age_category('Baldur\'s Gate 3', 'adult').
game_age_category('Little Nightmares', 'teen').
game_age_category('The Legend of Zelda', 'teen').


% Game mode: multiplayer, singleplayer
game_mode('The Witcher 3', 'singleplayer').
game_mode('Minecraft', 'multiplayer').
game_mode('Minecraft', 'singleplayer').
game_mode('Call of Duty', 'multiplayer').
game_mode('Call of Duty', 'singleplayer').
game_mode('Stardew Valley', 'singleplayer').
game_mode('Stardew Valley', 'multiplayer').
game_mode('Dark Souls', 'singleplayer').
game_mode('Animal Crossing', 'singleplayer').
game_mode('FIFA 2024', 'multiplayer').
game_mode('FIFA 2024', 'singleplayer').
game_mode('Cyberpunk 2077', 'singleplayer').
game_mode('Among Us', 'multiplayer').
game_mode('Fortnite', 'multiplayer').
game_mode('Candy Crush', 'singleplayer').
game_mode('Super Mario Bros', 'singleplayer').
game_mode('Resident Evil 4', 'singleplayer').
game_mode('Portal 2', 'singleplayer').
game_mode('Portal 2', 'multiplayer').
game_mode('Celeste', 'singleplayer').
game_mode('Half-Life 2', 'singleplayer').
game_mode('Terraria', 'singleplayer').
game_mode('Terraria', 'multiplayer').
game_mode('ARK: Survival Evolved', 'singleplayer').
game_mode('ARK: Survival Evolved', 'multiplayer').
game_mode('Marvel Rivals', 'multiplayer').
game_mode('Spelunky', 'singleplayer').
game_mode('Tetris', 'singleplayer').
game_mode('League of Legends', 'multiplayer').
game_mode('Journey', 'singleplayer').
game_mode('Journey', 'multiplayer').
game_mode('Hades', 'singleplayer').
game_mode('Rocket League', 'multiplayer').
game_mode('Dead by Daylight', 'multiplayer').
game_mode('Firewatch', 'singleplayer').
game_mode('Hollow Knight', 'singleplayer').
game_mode('Clash of Clans', 'multiplayer').
game_mode('God of War', 'singleplayer').
game_mode('It Takes Two', 'multiplayer').
game_mode('Valorant', 'multiplayer').
game_mode('Slay the Spire', 'singleplayer').
game_mode('Roblox', 'multiplayer').
game_mode('Baldur\'s Gate 3', 'singleplayer').
game_mode('Baldur\'s Gate 3', 'multiplayer').
game_mode('Little Nightmares', 'singleplayer').
game_mode('The Legend of Zelda', 'singleplayer').


% Violence: yes, no
game_violence('The Witcher 3', 'yes').
game_violence('Minecraft', 'no').
game_violence('Call of Duty', 'yes').
game_violence('Stardew Valley', 'no').
game_violence('Dark Souls', 'yes').
game_violence('Animal Crossing', 'no').
game_violence('FIFA 2024', 'no').
game_violence('Cyberpunk 2077', 'yes').
game_violence('Among Us', 'no').
game_violence('Fortnite', 'yes').
game_violence('Candy Crush', 'no').
game_violence('Super Mario Bros', 'no').
game_violence('Resident Evil 4', 'yes').
game_violence('Portal 2', 'no').
game_violence('Celeste', 'no').
game_violence('Half-Life 2', 'yes').
game_violence('Terraria', 'no').
game_violence('ARK: Survival Evolved', 'yes').
game_violence('Marvel Rivals', 'no').
game_violence('Spelunky', 'no').
game_violence('Tetris', 'no').
game_violence('League of Legends', 'no').
game_violence('Journey', 'no').
game_violence('Hades', 'yes').
game_violence('Rocket League', 'no').
game_violence('Dead by Daylight', 'yes').
game_violence('Firewatch', 'no').
game_violence('Hollow Knight', 'yes').
game_violence('Clash of Clans', 'no').
game_violence('God of War', 'yes').
game_violence('It Takes Two', 'no').
game_violence('Valorant', 'yes').
game_violence('Slay the Spire', 'no').
game_violence('Roblox', 'no').
game_violence('Baldur\'s Gate 3', 'yes').
game_violence('Little Nightmares', 'yes').
game_violence('The Legend of Zelda', 'no').


% Graphics: realistic, stylized, retro
game_graphics('The Witcher 3', 'realistic').
game_graphics('Minecraft', 'stylized').
game_graphics('Call of Duty', 'realistic').
game_graphics('Stardew Valley', 'retro').
game_graphics('Dark Souls', 'realistic').
game_graphics('Animal Crossing', 'stylized').
game_graphics('FIFA 2024', 'realistic').
game_graphics('Cyberpunk 2077', 'realistic').
game_graphics('Among Us', 'stylized').
game_graphics('Fortnite', 'stylized').
game_graphics('Candy Crush', 'stylized').
game_graphics('Super Mario Bros', 'retro').
game_graphics('Resident Evil 4', 'realistic').
game_graphics('Portal 2', 'stylized').
game_graphics('Celeste', 'retro').
game_graphics('Half-Life 2', 'realistic').
game_graphics('Terraria', 'retro').
game_graphics('ARK: Survival Evolved', 'realistic').
game_graphics('Marvel Rivals', 'stylized').
game_graphics('Spelunky', 'retro').
game_graphics('Tetris', 'retro').
game_graphics('League of Legends', 'stylized').
game_graphics('Journey', 'stylized').
game_graphics('Hades', 'stylized').
game_graphics('Rocket League', 'stylized').
game_graphics('Dead by Daylight', 'realistic').
game_graphics('Firewatch', 'realistic').
game_graphics('Hollow Knight', 'stylized').
game_graphics('Clash of Clans', 'stylized').
game_graphics('God of War', 'realistic').
game_graphics('It Takes Two', 'stylized').
game_graphics('Valorant', 'stylized').
game_graphics('Slay the Spire', 'stylized').
game_graphics('Roblox', 'stylized').
game_graphics('Baldur\'s Gate 3', 'realistic').
game_graphics('Little Nightmares', 'stylized').
game_graphics('The Legend of Zelda', 'stylized').


% Story importance: low, medium, high
game_story('The Witcher 3', 'high').
game_story('Minecraft', 'low').
game_story('Call of Duty', 'medium').
game_story('Stardew Valley', 'medium').
game_story('Dark Souls', 'high').
game_story('Animal Crossing', 'low').
game_story('FIFA 2024', 'low').
game_story('Cyberpunk 2077', 'high').
game_story('Among Us', 'low').
game_story('Fortnite', 'low').
game_story('Candy Crush', 'low').
game_story('Super Mario Bros', 'low').
game_story('Resident Evil 4', 'high').
game_story('Portal 2', 'medium').
game_story('Celeste', 'medium').
game_story('Half-Life 2', 'high').
game_story('Terraria', 'low').
game_story('ARK: Survival Evolved', 'medium').
game_story('Marvel Rivals', 'low').
game_story('Spelunky', 'low').
game_story('Tetris', 'low').
game_story('League of Legends', 'low').
game_story('Journey', 'high').
game_story('Hades', 'medium').
game_story('Rocket League', 'low').
game_story('Dead by Daylight', 'low').
game_story('Firewatch', 'high').
game_story('Hollow Knight', 'high').
game_story('Clash of Clans', 'low').
game_story('God of War', 'high').
game_story('It Takes Two', 'high').
game_story('Valorant', 'low').
game_story('Slay the Spire', 'medium').
game_story('Roblox', 'low').
game_story('Baldur\'s Gate 3', 'high').
game_story('Little Nightmares', 'high').
game_story('The Legend of Zelda', 'high').


% Budget: free, cheap, pricey
game_budget('The Witcher 3', 'cheap').
game_budget('Minecraft', 'cheap').
game_budget('Call of Duty', 'pricey').
game_budget('Stardew Valley', 'cheap').
game_budget('Dark Souls', 'cheap').
game_budget('Animal Crossing', 'pricey').
game_budget('FIFA 2024', 'pricey').
game_budget('Cyberpunk 2077', 'pricey').
game_budget('Among Us', 'cheap').
game_budget('Fortnite', 'free').
game_budget('Candy Crush', 'free').
game_budget('Super Mario Bros', 'cheap').
game_budget('Resident Evil 4', 'cheap').
game_budget('Portal 2', 'cheap').
game_budget('Celeste', 'cheap').
game_budget('Half-Life 2', 'cheap').
game_budget('Terraria', 'cheap').
game_budget('ARK: Survival Evolved', 'pricey').
game_budget('Marvel Rivals', 'free').
game_budget('Spelunky', 'cheap').
game_budget('Tetris', 'free').
game_budget('League of Legends', 'free').
game_budget('Journey', 'cheap').
game_budget('Hades', 'cheap').
game_budget('Rocket League', 'free').
game_budget('Dead by Daylight', 'pricey').
game_budget('Firewatch', 'cheap').
game_budget('Hollow Knight', 'cheap').
game_budget('Clash of Clans', 'free').
game_budget('God of War', 'pricey').
game_budget('It Takes Two', 'pricey').
game_budget('Valorant', 'free').
game_budget('Slay the Spire', 'cheap').
game_budget('Roblox', 'free').
game_budget('Baldur\'s Gate 3', 'pricey').
game_budget('Little Nightmares', 'cheap').
game_budget('The Legend of Zelda', 'pricey').


% Online: yes, no
game_online('The Witcher 3', 'no').
game_online('Minecraft', 'yes').
game_online('Call of Duty', 'yes').
game_online('Stardew Valley', 'yes').
game_online('Dark Souls', 'no').
game_online('Animal Crossing', 'yes').
game_online('FIFA 2024', 'yes').
game_online('Cyberpunk 2077', 'no').
game_online('Among Us', 'yes').
game_online('Fortnite', 'yes').
game_online('Candy Crush', 'no').
game_online('Super Mario Bros', 'no').
game_online('Resident Evil 4', 'no').
game_online('Portal 2', 'no').
game_online('Celeste', 'no').
game_online('Half-Life 2', 'no').
game_online('Terraria', 'no').
game_online('ARK: Survival Evolved', 'no').
game_online('ARK: Survival Evolved', 'yes').
game_online('Marvel Rivals', 'yes').
game_online('Spelunky', 'no').
game_online('Tetris', 'no').
game_online('League of Legends', 'yes').
game_online('Journey', 'no').
game_online('Hades', 'no').
game_online('Rocket League', 'yes').
game_online('Rocket League', 'no').
game_online('Dead by Daylight', 'yes').
game_online('Firewatch', 'no').
game_online('Hollow Knight', 'no').
game_online('Clash of Clans', 'yes').
game_online('God of War', 'no').
game_online('It Takes Two', 'yes').
game_online('Valorant', 'yes').
game_online('Slay the Spire', 'no').
game_online('Roblox', 'yes').
game_online('Baldur\'s Gate 3', 'yes').
game_online('Little Nightmares', 'no').
game_online('The Legend of Zelda', 'no').


% Skill level: beginner, intermediate, expert
game_skill('The Witcher 3', 'intermediate').
game_skill('Minecraft', 'beginner').
game_skill('Call of Duty', 'intermediate').
game_skill('Stardew Valley', 'beginner').
game_skill('Dark Souls', 'expert').
game_skill('Animal Crossing', 'beginner').
game_skill('FIFA 2024', 'intermediate').
game_skill('Cyberpunk 2077', 'intermediate').
game_skill('Among Us', 'beginner').
game_skill('Fortnite', 'intermediate').
game_skill('Candy Crush', 'beginner').
game_skill('Super Mario Bros', 'intermediate').
game_skill('Resident Evil 4', 'intermediate').
game_skill('Portal 2', 'intermediate').
game_skill('Celeste', 'expert').
game_skill('Half-Life 2', 'beginner').
game_skill('Half-Life 2', 'intermediate').
game_skill('Terraria', 'beginner').
game_skill('Terraria', 'intermediate').
game_skill('Terraria', 'expert').
game_skill('ARK: Survival Evolved', 'intermediate').
game_skill('ARK: Survival Evolved', 'expert').
game_skill('Marvel Rivals', 'intermediate').
game_skill('Marvel Rivals', 'expert').
game_skill('Spelunky', 'intermediate').
game_skill('Spelunky', 'expert').
game_skill('Tetris', 'beginner').
game_skill('League of Legends', 'expert').
game_skill('Journey', 'beginner').
game_skill('Hades', 'expert').
game_skill('Rocket League', 'intermediate').
game_skill('Dead by Daylight', 'expert').
game_skill('Firewatch', 'beginner').
game_skill('Hollow Knight', 'expert').
game_skill('Clash of Clans', 'beginner').
game_skill('God of War', 'expert').
game_skill('God of War', 'intermediate').
game_skill('It Takes Two', 'intermediate').
game_skill('Valorant', 'intermediate').
game_skill('Slay the Spire', 'expert').
game_skill('Roblox', 'beginner').
game_skill('Baldur\'s Gate 3', 'expert').
game_skill('Little Nightmares', 'intermediate').
game_skill('The Legend of Zelda', 'intermediate').


% Session length: short, medium, long
game_session_length('The Witcher 3', 'long').
game_session_length('Minecraft', 'medium').
game_session_length('Call of Duty', 'medium').
game_session_length('Stardew Valley', 'medium').
game_session_length('Dark Souls', 'long').
game_session_length('Animal Crossing', 'short').
game_session_length('FIFA 2024', 'short').
game_session_length('Cyberpunk 2077', 'long').
game_session_length('Among Us', 'short').
game_session_length('Fortnite', 'medium').
game_session_length('Candy Crush', 'short').
game_session_length('Super Mario Bros', 'medium').
game_session_length('Resident Evil 4', 'long').
game_session_length('Portal 2', 'medium').
game_session_length('Celeste', 'medium').
game_session_length('Half-Life 2', 'medium').
game_session_length('Terraria', 'short').
game_session_length('Terraria', 'medium').
game_session_length('Terraria', 'long').
game_session_length('ARK: Survival Evolved', 'medium').
game_session_length('ARK: Survival Evolved', 'long').
game_session_length('Marvel Rivals', 'short').
game_session_length('Marvel Rivals', 'medium').
game_session_length('Spelunky', 'short').
game_session_length('Tetris', 'short').
game_session_length('League of Legends', 'long').
game_session_length('Journey', 'short').
game_session_length('Hades', 'medium').
game_session_length('Rocket League', 'medium').
game_session_length('Dead by Daylight', 'medium').
game_session_length('Firewatch', 'short').
game_session_length('Hollow Knight', 'medium').
game_session_length('Clash of Clans', 'short').
game_session_length('God of War', 'long').
game_session_length('God of War', 'medium').
game_session_length('It Takes Two', 'medium').
game_session_length('Valorant', 'medium').
game_session_length('Slay the Spire', 'short').
game_session_length('Roblox', 'short').
game_session_length('Baldur\'s Gate 3', 'long').
game_session_length('Little Nightmares', 'short').
game_session_length('The Legend of Zelda', 'long').


% Recommendation rules - updated for all categories
suitable_for_player(Game) :-
    game(Game),
    age_appropriate(Game),
    genre_match(Game),
    platform_available(Game),
    game_mode_match(Game),
    session_length_suitable(Game),
    violence_acceptable(Game),
    graphics_suitable(Game),
    story_suitable(Game),
    budget_suitable(Game),
    online_suitable(Game),
    skill_suitable(Game).

% Individual matching rules
age_appropriate(Game) :-
    player_age(PlayerAge),
    game_age_category(Game, GameAge),
    age_compatible(PlayerAge, GameAge).

age_compatible('adult', _).
age_compatible('teen', Age) :- 
    member(Age, ['child', 'teen']).
age_compatible('child', 'child').

genre_match(Game) :-
    player_genre(PreferredGenre),
    game_genre(Game, PreferredGenre).

platform_available(Game) :-
    player_platform(Platform),
    game_platform(Game, Platform).

game_mode_match(Game) :-
    player_game_mode(PreferredMode),
    game_mode(Game, PreferredMode).

session_length_suitable(Game) :-
    player_session_length(Preferred),
    game_session_length(Game, Preferred).

violence_acceptable(Game) :-
    player_violence(PlayerViolence),
    game_violence(Game, GameViolence),
    violence_compatible(PlayerViolence, GameViolence).

violence_compatible('yes', _).
violence_compatible('no', 'no').

graphics_suitable(Game) :-
    player_graphics(PlayerGraphics),
    game_graphics(Game, PlayerGraphics).

story_suitable(Game) :-
    player_story(PlayerStory),
    game_story(Game, GameStory),
    story_compatible(PlayerStory, GameStory).

story_compatible('high', Story) :- 
    member(Story, ['medium', 'high']).
story_compatible('medium', Story) :- 
    member(Story, ['low', 'medium', 'high']).
story_compatible('low', _).

budget_suitable(Game) :-
    player_budget(PlayerBudget),
    game_budget(Game, GameBudget),
    budget_compatible(PlayerBudget, GameBudget).

budget_compatible('pricey', _).
budget_compatible('cheap', Budget) :- 
    member(Budget, ['free', 'cheap']).
budget_compatible('free', 'free').

online_suitable(Game) :-
    player_online(PlayerOnline),
    game_online(Game, PlayerOnline).

skill_suitable(Game) :-
    player_skill(PlayerSkill),
    game_skill(Game, GameSkill),
    skill_compatible(PlayerSkill, GameSkill).

skill_compatible('expert', _).
skill_compatible('intermediate', Skill) :- 
    member(Skill, ['beginner', 'intermediate']).
skill_compatible('beginner', 'beginner').
"""

# Example usage
if __name__ == "__main__":
    # Sample answers - updated to match all your categories
    sample_answers = {
        'age': 'adult',                    # ['child','teen','adult']
        'genre': 'shooter',                   # ['rpg','shooter','puzzle','platformer','sports','horror','adventure']
        'platform': 'pc',                # ['pc','console','mobile']
        'session_length': 'medium',         # ['short','medium','long']
        'game_mode': 'multiplayer',      # ['multiplayer','singleplayer']
        'violence': 'yes',                # ['yes','no']
        'graphics': 'realistic',          # ['realistic','stylized','retro']
        'story': 'low',                  # ['low','medium','high']
        'budget': 'pricey',                # ['free','cheap','pricey']
        'online': 'yes',                   # ['yes','no']
        'skill': 'intermediate'           # ['beginner','intermediate','expert']
    }
    
    # Get recommendations
    recommendations = result(sample_answers)
    print("Game Recommendation Results:")
    print(f"Success: {recommendations['success']}")
    if recommendations['success']:
        print(f"Output: {recommendations['output']}")
    else:
        print(f"Error: {recommendations.get('error', 'Unknown error')}")
import subprocess
import tempfile
import os

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
        
        return {
            'success': result.returncode == 0,
            'output': result.stdout,
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
game('The Sims 4').
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
% Still adding attributes to each

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
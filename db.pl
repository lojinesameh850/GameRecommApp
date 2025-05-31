% game(Name, AgeGroup, Genre, Gender, SessionLength, Platform, GameMode, ViolenceTolerance, Graphics, StoryImportance, Budget, OnlineRequired, SkillLevel).

% age_labels = ["Child (3-12)", "Teen (13-19)", "Adult (20+)"]
% Genre (["RPG", "Shooter", "Puzzle", "Platformer", "Sports", "Horror", "Adventure"])
% Gender: Male, Female
% Session length: ["Short (1-2h)", "Medium (3-4h)", "Long (5h+)"]
% Preferred platform ["PC", "Console", "Mobile"]
% Game mode: ["Multiplayer", "Singleplayer"]
% Violence tolerance Yes No
% Graphics preference: "Realistic", "Stylized", "Retro"
% Story importance: ["Low", "Medium", "High"]
% Budget: ["Free", "Cheap (- $50)", "Pricey ($50+)"]
% Online required? Yes No
% Skill level: ["Beginner", "Intermediate", "Expert"]


game('Half-Life 2',
     ['Teen (13-19)', 'Adult (20+)'],
     ['Shooter', 'Adventure'],
     ['Male', 'Female'],
     ['Medium (3-4h)', 'Long (5h+)'],
     ['PC', 'Console'],
     ['Singleplayer'],
     'Yes',
     'Realistic',
     'High',
     'Cheap (- $50)',
     'No',
     ['Beginner', 'Intermediate']).

game('Terraria',
     ['Child (3-12)', 'Teen (13-19)', 'Adult (20+)'],
     ['Adventure', 'Platformer'],
     ['Male', 'Female'],
     ['Short (1-2h)', 'Medium (3-4h)', 'Long (5h+)'],
     ['PC', 'Console', 'Mobile'],
     ['Multiplayer', 'Singleplayer'],
     'No',
     'Retro',
     'Medium',
     'Cheap (- $50)',
     'No',
     ['Beginner', 'Intermediate', 'Expert']).

game('ARK: Survival Evolved',
     ['Teen (13-19)', 'Adult (20+)'],
     ['Adventure', 'Survival'],
     ['Male', 'Female'],
     ['Long (5h+)'],
     ['PC', 'Console'],
     ['Multiplayer', 'Singleplayer'],
     'Yes',
     'Realistic',
     'Medium',
     'Pricey ($50+)',
     'Yes',
     ['Intermediate', 'Expert']).

game('Marvel Rivals',
     ['Teen (13-19)', 'Adult (20+)'],
     ['Shooter', 'Action'],
     ['Male', 'Female'],
     ['Short (1-2h)', 'Medium (3-4h)'],
     ['PC', 'Console'],
     ['Multiplayer'],
     'Yes',
     'Stylized',
     'Medium',
     'Free',
     'Yes',
     ['Intermediate', 'Expert']).

game('Spelunky',
     ['Teen (13-19)', 'Adult (20+)'],
     ['Platformer', 'Adventure'],
     ['Male', 'Female'],
     ['Short (1-2h)', 'Medium (3-4h)'],
     ['PC', 'Console'],
     ['Singleplayer'],
     'No',
     'Retro',
     'Low',
     'Cheap (- $50)',
     'No',
     ['Intermediate', 'Expert']).


game('Tetris',                'Child (3-12)',     'Puzzle',      both,     'Short (1-2h)',   'Mobile',   'Singleplayer',  no,    'Retro',    'Low',      'Free',           no,   'Beginner').
game('League of Legends',     'Teen (13-19)',     'RPG',         male,     'Long (5h+)',     'PC',       'Multiplayer',   yes,   'Stylized', 'Medium',   'Free',           yes,  'Expert').
game('Journey',               'Adult (20+)',      'Adventure',   female,   'Short (1-2h)',   'Console',  'Singleplayer',  no,    'Stylized', 'High',     'Cheap (- $50)', no,   'Beginner').
game('Hades',                 'Adult (20+)',      'RPG',         male,     'Medium (3-4h)',  'PC',       'Singleplayer',  yes,   'Stylized', 'Medium',   'Cheap (- $50)', no,   'Expert').
game('Rocket League',         'Teen (13-19)',     'Sports',      both,     'Medium (3-4h)',  'Console',  'Multiplayer',   yes,   'Stylized', 'Low',      'Free',           yes,  'Intermediate').
game('Dead by Daylight',      'Adult (20+)',      'Horror',      male,     'Medium (3-4h)',  'PC',       'Multiplayer',   yes,   'Realistic','Medium',   'Pricey ($50+)',  yes,  'Expert').
game('Firewatch',             'Adult (20+)',      'Adventure',   female,   'Short (1-2h)',   'PC',       'Singleplayer',  no,    'Realistic','High',     'Cheap (- $50)', no,   'Beginner').
game('Hollow Knight',         'Teen (13-19)',     'Platformer',  male,     'Medium (3-4h)',  'PC',       'Singleplayer',  yes,   'Stylized', 'High',     'Cheap (- $50)', no,   'Expert').
game('Clash of Clans',        'Child (3-12)',     'Strategy',    both,     'Short (1-2h)',   'Mobile',   'Multiplayer',   no,    'Stylized', 'Low',      'Free',           yes,  'Beginner').

game('God of War',            'Adult (20+)',      'Adventure',   male,     'Long (5h+)',     'Console',  'Singleplayer',  yes,   'Realistic','High',     'Pricey ($50+)',  no,   'Expert').
game('It Takes Two',          'Adult (20+)',      'Platformer',  both,     'Medium (3-4h)',  'Console',  'Multiplayer',   no,    'Stylized', 'High',     'Pricey ($50+)',  yes,  'Intermediate').
game('Valorant',              'Teen (13-19)',     'Shooter',     male,     'Long (5h+)',     'PC',       'Multiplayer',   yes,   'Stylized', 'Low',      'Free',           yes,  'Intermediate').
game('Slay the Spire',        'Adult (20+)',      'Puzzle',      both,     'Short (1-2h)',   'PC',       'Singleplayer',  no,    'Stylized', 'Medium',   'Cheap (- $50)', no,   'Expert').
game('Roblox',                'Child (3-12)',     'Platformer',  both,     'Short (1-2h)',   'Mobile',   'Multiplayer',   no,    'Stylized', 'Low',      'Free',           yes,  'Beginner').
game('Baldur\'s Gate 3',      'Adult (20+)',      'RPG',         both,     'Long (5h+)',     'PC',       'Multiplayer',   yes,   'Realistic','High',     'Pricey ($50+)',  yes,  'Expert').
game('Little Nightmares',     'Teen (13-19)',     'Horror',      both,     'Short (1-2h)',   'PC',       'Singleplayer',  yes,   'Stylized', 'High',     'Cheap (- $50)', no,   'Intermediate').
game('The Legend of Zelda',   'Teen (13-19)',     'Adventure',   both,     'Long (5h+)',     'Console',  'Singleplayer',  yes,   'Stylized', 'High',     'Pricey ($50+)',  no,   'Intermediate').

SELECT
    g.id AS game_id,
    gr.id AS gamer_id,
    u.first_name || ' ' || u.last_name AS full_name,
    g.id AS game_id,
    g.name,
    g.creator,
    g.skill_level,
    g.number_of_players,
    g.game_type_id
    FROM levelupapi_game AS g
    JOIN levelupapi_gamer AS gr ON g.gamer_id = gr.id
    JOIN auth_user AS u ON gr.user_id = u.id;

SELECT * FROM levelupapi_game

SELECT
    gr.id AS gamer_id,
    u.first_name || ' ' || u.last_name AS full_name,
    e.id AS event_id,
    e.date,
    g.name AS game_name
FROM levelupapi_gamer AS gr
JOIN auth_user AS u ON gr.user_id = u.id
JOIN levelupapi_event as e ON e.host_id = gr.id
JOIN levelupapi_game AS g ON g.id = e.game_id
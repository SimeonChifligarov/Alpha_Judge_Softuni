CREATE OR REPLACE FUNCTION fn_creator_with_board_games(first_name_input VARCHAR(30))
RETURNS INT AS
$$
DECLARE
    total_games INT;
BEGIN
    SELECT COUNT(DISTINCT cbg.board_game_id)
    INTO total_games
    FROM creators c
    JOIN creators_board_games cbg ON c.id = cbg.creator_id
    WHERE c.first_name = first_name_input;

    RETURN total_games;
END;
$$
LANGUAGE plpgsql;

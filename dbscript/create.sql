USE ort;

CREATE TABLE Team (
    team_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    team_name VARCHAR(50),
    UNIQUE (team_name)
);

CREATE TABLE Player (
    osu_id INT PRIMARY KEY NOT NULL,
    team_id INT,
    pseudo VARCHAR(15),
    pp FLOAT,
    player_rank INT,
    qualifier_score INT,
    discordTag VARCHAR(99),
    FOREIGN KEY (team_id) REFERENCES Team(team_id)
);
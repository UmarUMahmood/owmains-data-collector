CREATE TABLE subreddit (
    subreddit_id int NOT NULL AUTO_INCREMENT,
    subreddit_name varchar(255) NOT NULL UNIQUE,
    PRIMARY KEY (subreddit_id)
);

CREATE TABLE subcount (
    id int NOT NULL AUTO_INCREMENT,
    day date NOT NULL,
    subreddit_id int NOT NULL,
    subscribers int NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (subreddit_id) REFERENCES subreddit(subreddit_id)
);

INSERT INTO subreddit (subreddit_name)
VALUES 
    ('Anamains'),
    ('Asheowmains'),
    ('Baptistemains'),
    ('Bastionmains'),
    ('Brigittemains'),
    ('Doomfistmains'),
    ('Dvamains'),
    ('Echomains'),
    ('Genjimains'),
    ('Hanzomain'),
    ('Junkratmains'),
    ('Luciomains'),
    ('Mccreemains'),
    ('Meimains'),
    ('Mercymains'),
    ('Moiramains'),
    ('Orisamains'),
    ('Pharahmains'),
    ('Reapermain'),
    ('Reinhardtmains'),
    ('Roadhogmains'),
    ('Sigmamains'),
    ('Soldier76mains'),
    ('Sombramains'),
    ('Symmetramains'),
    ('Torbjornmains'),
    ('Tracermains'),
    ('Widowmakermains'),
    ('Winstonmains'),
    ('Wreckingballmains'),
    ('Zaryamains'),
    ('Zenyattamains');

drop table author;
CREATE TABLE author
(
  id bigint NOT NULL,
  name character varying(15),
  age integer,
  genre character varying(15)
);

INSERT INTO author (id, name, age, genre) VALUES (5, 'hhh', 45, 'ttt')
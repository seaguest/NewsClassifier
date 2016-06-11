CREATE TABLE IF NOT EXISTS keyword (
	id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    
	keyword VARCHAR(30) NOT NULL UNIQUE
    
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS category (
	id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    
	category VARCHAR(30) NOT NULL UNIQUE
    
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS keyword_category (
	id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    
	keyword VARCHAR(30) NOT NULL,

	category VARCHAR(30) NOT NULL,
	
	probability float NOT NULL

)ENGINE=InnoDB DEFAULT CHARSET=utf8;


insert into keyword (keyword) values("nba");
insert into keyword (keyword) values("cba");
insert into keyword (keyword) values("tech");

insert into category (category) values("sport");
insert into category (category) values("entertainment");
insert into category (category) values("society");


insert into keyword_category (keyword,category,probability) values("nba","sport",0.8);
insert into keyword_category (keyword,category,probability) values("nba","entertainment",0.3);
insert into keyword_category (keyword,category,probability) values("cba","sport",0.8);
insert into keyword_category (keyword,category,probability) values("cba","entertainment",0.3);

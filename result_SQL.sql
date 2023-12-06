use attestation;

create table dogs (
id int primary key auto_increment,
name varchar(30),
skills varchar(30),
birt_date date);
create table cats (
id int primary key auto_increment,
name varchar(30),
skills varchar(30),
birt_date date);
create table hamsters (
id int primary key auto_increment,
name varchar(30),
skills varchar(30),
birt_date date);
create table horses (
id int primary key auto_increment,
name varchar(30),
skills varchar(30),
birt_date date);
create table donkeys (
id int primary key auto_increment,
name varchar(30),
skills varchar(30),
birt_date date);
create table camels (
id int primary key auto_increment,
name varchar(30),
skills varchar(30),
birt_date date);
insert into dogs (name, skills, birt_date)
values ("Jack", "aport", "2020-05-30");
insert into cats (name, skills, birt_date)
values ("Mick", "voise", "2021-05-30");
insert into horses (name, skills, birt_date)
values ("Hector", "run", "2019-05-30");
insert into camels (name, skills, birt_date)
values ("Boxer", "stay", "2021-10-30");
insert into donkeys (name, skills, birt_date)
values ("Danny", "sitdown", "2022-12-30");
drop table hamsters;
create table hamsters (
id int primary key auto_increment,
name varchar(30),
skills varchar(30),
birt_date date);
insert into hamsters (name, skills, birt_date)
values ("Danny", "sitdown", "2022-12-30");
drop table camels;
create table packAnimals (
id int primary key auto_increment,
name varchar(30),
skills varchar(30),
birt_date date);
insert into packAnimals (name, skills, birt_date) select  name, skills, birt_date from horses;
insert into packAnimals (name, skills, birt_date) select  name, skills, birt_date from donkeys;
select * from packAnimals;
drop table horses, donkeys;
CREATE TABLE young_animals AS
SELECT id, name, skills, birt_date, TIMESTAMPDIFF(MONTH, birt_date, CURDATE()) AS age_in_months
FROM (
    SELECT id, name, skills, birt_date
    FROM dogs
    WHERE birt_date BETWEEN DATE_SUB(CURDATE(), INTERVAL 3 YEAR) AND DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
    UNION
    SELECT id, name, skills, birt_date
    FROM cats
    WHERE birt_date BETWEEN DATE_SUB(CURDATE(), INTERVAL 3 YEAR) AND DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
    UNION
    SELECT id, name, skills, birt_date
    FROM hamsters
    WHERE birt_date BETWEEN DATE_SUB(CURDATE(), INTERVAL 3 YEAR) AND DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
    UNION
    SELECT id, name, skills, birt_date
    FROM packAnimals
    WHERE birt_date BETWEEN DATE_SUB(CURDATE(), INTERVAL 3 YEAR) AND DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
) AS subquery;
create table result (
id int primary key auto_increment,
name varchar(30),
skills varchar(30),
birt_date date);
insert into result (name, skills, birt_date) select name, skills, birt_date from packAnimals
union all
select name, skills, birt_date from dogs
union all
select name, skills, birt_date from cats
union all
select name, skills, birt_date from hamsters;
select * from result;



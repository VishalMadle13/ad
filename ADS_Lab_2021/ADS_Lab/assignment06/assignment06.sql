CREATE TABLE wce (
	prn varchar(50),
    name varchar(50),
    dept varchar(50)
);

CREATE TABLE wcesort (
	prn varchar(50),
    name varchar(50),
    dept varchar(50)
);

insert into wce values("cse01","shruti","CSE");

insert into wce values("cse02","sawan","CSE");

insert into wce values("cv01","teja","CIVIL");

insert into wce values("entc1","shreya","ENTC");

select * from wce;

CREATE TABLE first (
	prn varchar(50),
    name varchar(50)
);

CREATE TABLE second (
	prn varchar(50),
    dept varchar(50)
);

insert into first values("cse01","shruti");
insert into first values("cse02","sawan");
insert into first values("cv01","teja");
insert into first values("entc1","shreya");

insert into second values("cse01","CSE");
insert into second values("cse02","CSE");
insert into second values("cv01","CIVIL");
insert into second values("entc1","ENTC");


select * from wcesort;

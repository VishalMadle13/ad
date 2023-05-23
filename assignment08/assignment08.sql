create database assignment8;
use  assignment8;

create table Student(
prn varchar(14) not null,
quiz_id int not null,
marks int not null);

insert into Student values('2020CS02',2,20);
insert into Student values('2020CS06',3,20);



create user 'slave'@'10.40.1.17' identified by 'slave';
grant all privileges on assignment8.* to 'slave'@'10.40.1.17';
grant replication slave on *.* to 'slave'@'10.40.1.17';
select *from teacher;
select *from student;
alter table Teacher add primary key(sid);
insert into Teacher values(2,'Rusabh Patil');
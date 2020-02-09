create table branch(
code varchar(3);
name varchar(5);
assets int;
primary key(code);
);
create table customer(
ssn varchar(3);
name varchar(5);
place varchar(4);
primary key(ssn);
);

create table account(
accno varchar(3) primary key;
ssn varchar(5);
code varchar(3);
balance int;
foreign key(code) references branch(code) on delete cascade;
foreign key(ssn) references customer(code) on delete cascade;
primary key(code);
);
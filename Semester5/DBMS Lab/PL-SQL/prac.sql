set serveroutput on;

create or replace trigger tasha 
	before insert or update or delete on employee1
	begin 
	if to_char(sysdate,'Dy') in 'Thu'
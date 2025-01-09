
use collegedatabase;
delimiter //
create procedure generate_avg_table()
begin
declare done int default 0;
declare v_choicecode varchar(255);
declare v1_Cutoffrank int;
declare v1_Cutoffscore float;
declare v2_Cutoffrank int;
declare v2_Cutoffscore float;
declare v3_Cutoffrank int;
declare v3_Cutoffscore float;
declare c1 cursor for select * from jee_2023_24;
declare continue handler for not found set done=1;

open c1;
repeat
fetch c1 into v_choicecode,v1_Cutoffrank,v1_Cutoffscore,v2_Cutoffrank,v2_Cutoffscore,v3_Cutoffrank,v3_Cutoffscore;
if done =0 then
create table if not exists newtable as
select v_choicecode,(v1_Cutoffrank+v2_Cutoffrank+v3_Cutoffrank) as cutoffrank,(v1_Cutoffscore+v2_Cutoffscore+v3_Cutoffscore) as cutoffscore;
end if;
until done end repeat;
close c1;

end
//

delimiter ;
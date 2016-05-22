begin
  loop
    v :=F_FOUND_BOTTLENECK;
    P_OPTIMIZE(V);
    IF (F_PERFORMACNE) THEN
      EXIT;
    END IF;
  end loop;
end;
/

select table_name,index_name,column_name,column_position
from dba_ind_columns where table_name='TF_R_UNICARD'

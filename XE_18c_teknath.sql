CREATE TABLE test_table (RecordNumber NUMBER(3), CurrentDate DATE); 


DECLARE 
    i number(2);
BEGIN
    FOR i IN 1..50 LOOP
        INSERT INTO test_table (RecordNumber, CurrentDate) VALUES (i, SYSDATE());
    END LOOP;
END;

SELECT * FROM test_table;
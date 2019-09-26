-- https://programmers.co.kr/learn/courses/30/lessons/59045

SELECT INS.ANIMAL_ID, INS.ANIMAL_TYPE, INS.NAME
FROM ANIMAL_INS INS RIGHT JOIN ANIMAL_OUTS OUTS
    ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.ANIMAL_ID is NOT null 
    AND NOT INS.SEX_UPON_INTAKE = OUTS.SEX_UPON_OUTCOME
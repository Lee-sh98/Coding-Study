SELECT
    EC.ID,
    (
    SELECT
    COUNT(*)
    FROM ECOLI_DATA AS EC2
    WHERE EC.ID = EC2.PARENT_ID
    ) AS CHILD_COUNT
FROM
    ECOLI_DATA AS EC
    
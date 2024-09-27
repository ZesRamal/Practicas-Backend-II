TRUNCATE TABLE temperatura_data RESTART IDENTITY;

INSERT INTO temperatura_data (timestamp, value, condition)
SELECT
    TIMESTAMP '2024-09-10 00:00:00' + INTERVAL '5 seconds' * (generate_series(0, 999)) AS timestamp,
    random() * 30 AS value,
    'temperatura' AS condition
;
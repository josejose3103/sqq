LOAD DATA LOCAL INFILE 'C:/Users/tsuboi/OneDrive/Documents/table1.cvs' INTO TABLE article5 FIELDS TERMINATED BY ',' ENCLOSED BY '"' ;
SELECT SUM(kingaku) FROM article6 WHERE day BETWEEN '2022-01-11' AND '2022-01-25';
SELECT noukamei, SUM(kingaku) FROM article6 WHERE day BETWEEN '2022-01-11' AND '2022-01-25' GROUP BY noukamei ORDER BY kumikan;
SELECT * FROM article6 WHERE day BETWEEN '2022-01-11' AND '2022-01-25' AND kumikan = '12';
SELECT number, byoumei, kingaku FROM article6 WHERE day BETWEEN '2022-01-11' AND '2022-01-25' AND kumikan = '12';
SELECT number, byoumei, kingaku FROM article6 WHERE day BETWEEN '2022-01-11' AND '2022-01-25' AND kumikan = '12' INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/sa.csv';

 SELECT number, byoumei, kingaku FROM article6 WHERE d
 SELECT number, byoumei, kingaku FROM article6 WHERE day BETWEEN '2022-01-11' AND '2022-01-25' AND kumikan = '12' INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/sa2.csv' CHARACTER SET 'sjis' FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"';
 SELECT 農家名, SUM(金額) FROM article6 WHERE day BETWEEN '2022-01-11' AND '2022-01-25' GROUP BY 農家名 ORDER BY 組勘番号 INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/goukei.csv' CHARACTER SET 'sjis' FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"';
  SELECT number, 病名, 金額 FROM article6 WHERE day BETWEEN '2022-01-11' AND '2022-01-25' AND 組勘番号 = '12'; 
  SELECT DATE_FORMAT(day, '%Y%m') as YM, sum(金額) FROM article6 WHERE 農家名 = '田中和也' GROUP by DATE_FORMAT(day, '%Y%m');
  S
  
  SELECT 日時, 損坊内容, 金額 FROM article7 WHERE 日時 BETWEEN '2021-11-30' AND '2022-01-31' AND 組勘番号 = '12'; 
  ç
  SELECT * FROM article6 WHERE day BETWEEN '2022-01-11' AND '2022-01-25' AND 組勘番号 = '12'
  SELECT number, 病名, 金額 FROM article6 WHERE day BETWEEN '2022-01-11' AND '2022-01-25' AND 組勘番号 = '12';
  SELECT 農家名, SUM(金額) FROM article6 WHERE day BETWEEN '2022-01-11' AND '2022-01-25' GROUP BY 農家名, 組 勘番号 ORDER BY 組勘番号;
  ELECT 農家名, SUM(金額) FROM article7 WHERE 日時 BETWEEN '2022-01-11' AND '2022-01-25' GROUP BY 農家名, 組勘番号 ORDER BY 組勘番号;
  SELECT * FROM table4 WHERE personalID = '1514645329' INTO OUTFILE '/tmp/11.csv';;
  SELECT DATE_FORMAT(day, '%Y') as Y, sum(金額) FROM article6 GROUP by DATE_FORMAT(day, '%Y');
  SELECT number as 番号, byoumei as 病名, kingaku as 金額, day as 日付 FROM article3 WHERE day BETWEEN '2022-01-01' AND '2022-01-28' AND kumikanbangou = '22.0';
  media=# SELECT 
    CASE 
        WHEN EXTRACT(DAY FROM day) BETWEEN 11 AND 25 THEN '11-25'
        ELSE '26-10'
    END AS period,
    EXTRACT(YEAR FROM day) AS year,
    CASE 
        WHEN EXTRACT(DAY FROM day) BETWEEN 11 AND 25 THEN EXTRACT(MONTH FROM day)
        ELSE EXTRACT(MONTH FROM day + INTERVAL '1 month')
    END AS month,
    SUM(kingaku) AS total_sales
FROM article3
WHERE day >= '2024-01-01'  -- 必要に応じて期間を指定
GROUP BY year, month, period
ORDER BY year, month, period;
SELECT to_char(sum(kingaku),'¥9,999,999') as 合計 FROM article3 WHERE day BETWEEN '2025-01-01' AND '2025-01-28' AND kumikanbangou = '22.0';
    合計     
media=# SELECT number as 番号, byoumei as 病名, to_char(kingaku, '¥9,999,999') as金額, day as 日付 FROM article3 WHERE day BETWEEN '2022-01-01' AND '2022-01-28' AND kumikanbangou = '22.0';
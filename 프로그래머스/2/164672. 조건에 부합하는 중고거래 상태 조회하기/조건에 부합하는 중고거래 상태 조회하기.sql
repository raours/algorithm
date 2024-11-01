-- 코드를 입력하세요
SELECT BOARD_ID, WRITER_ID, TITLE, PRICE, 
CASE WHEN STATUS like 'SALE' then '판매중'
    when status like 'RESERVED' then '예약중'
    ELSE '거래완료'
    END as STATUS
FROM USED_GOODS_BOARD
WHERE CREATED_DATE like '2022-10-05'
order by board_id desc
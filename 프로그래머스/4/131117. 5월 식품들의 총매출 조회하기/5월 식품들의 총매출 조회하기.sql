-- 코드를 입력하세요
SELECT a.product_id, a.product_name, (a.price*b.Amount) TOTAL_SALES
from FOOD_PRODUCT a JOIN (select product_id, sum(amount) Amount 
                       from FOOD_ORDER
                       where produce_date like '2022-05%'
                       group by product_id) b
                       on a.product_id = b.product_id
order by TOTAL_SALES DESC, product_id
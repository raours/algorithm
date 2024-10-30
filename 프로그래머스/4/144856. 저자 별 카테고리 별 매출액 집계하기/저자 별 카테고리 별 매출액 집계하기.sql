-- 코드를 입력하세요
SELECT b.author_id, a.author_name, b.category, sum(b.price*bs.sales) as total_sales
from book b 
join book_sales bs on b.book_id = bs.book_id
join author a on a.author_id = b.author_id
where bs.sales_date like '2022-01%'
group by b.author_id, b.category
order by b.author_id, b.category desc
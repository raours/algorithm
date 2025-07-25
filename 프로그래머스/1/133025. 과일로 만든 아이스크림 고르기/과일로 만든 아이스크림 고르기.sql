SELECT h.FLAVOR 
FROM FIRST_HALF h
JOIN ICECREAM_INFO i
ON h.FLAVOR = i.FLAVOR
WHERE i.INGREDIENT_TYPE like '%fruit%'
GROUP BY h.FLAVOR 
HAVING SUM(h.TOTAL_ORDER) >= 3000
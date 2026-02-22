--  5 questions for Data with sentiment analysis

--1) Find number of businesses in each category
with CTE as (
Select business_id, trim(A.value) as category
from tbl_yelp_businesses
,lateral split_to_table(categories, ',') A
)
select category , count (*) as no_of_business
from cte
group by 1
order by 2 desc;

--2) Find top 10 users who have reviewed the most businesses in the Restaurant category
Select r.user_id, count(distinct r.business_id)
from tbl_yelp_reviews r inner join tbl_yelp_businesses b
on r.business_id = b.business_id
where b.categories ilike '%restaurant%'
group by 1
order by 2 desc
limit 10;

--3) Find most popular category of  businesses (based on number of reviews)
with CTE as (
Select business_id, trim(A.value) as category
from tbl_yelp_businesses
,lateral split_to_table(categories, ',') A
)
select category, count (*) as no_of_reviews
from cte inner join tbl_yelp_reviews r on cte.business_id = r.business_id
group by 1
order by 2 desc;

--4) Find the top 3 most recent reviews for each business
with CTE as(
Select r.*,b.name
,row_number() over(partition by r.business_id order by review_date desc) as rn

from tbl_yelp_reviews r inner join tbl_yelp_businesses b
on r.business_id = b.business_id
where b.categories ilike '%restaurant%'
)
Select * from CTE
where rn<=3;

--5) Find top 10 businesses with highest positive sentiment reviews
Select r.business_id, b.name, count(*) as total_reviews
from tbl_yelp_reviews r 
inner join tbl_yelp_businesses b
on r.business_id = b.business_id
where sentiments = 'Positive'
group by 1,2
order by 3 desc
limit 10;
SELECT * FROM customer 
where season  = 55


select gender , sum (purchase_amount )as revenue
from customer 
group by gender


select customer_id ,  purchase_amount
from customer
where discount_applied ='Yes' and purchase_amount >=(select avg(purchase_amount) from customer)



select customer.item_purchased , round(avg(customer.review_rating ::numeric),2 ) as Average_Rev
from customer  
group by item_purchased
order by avg(review_rating )desc
limit 5


select  shipping_type ,  round(AVG(purchase_amount) ,2)as Average_Purchases 
from customer 
where shipping_type in ('Standard', 'Express')
group by shipping_type


select subscription_status ,
count (customer_id) as all_customer,
round(avg(purchase_amount),2) as avg_spend,
round(sum(purchase_amount),2) as  total_revenue
from customer
group by subscription_status
order by total_revenue, avg_spend



select item_purchased , 
Round(100 * sum (case when discount_applied ='Yes' Then 1 else 0 End ) /count(*),2) as discount_rate
from customer
group by item_purchased
order by discount_rate desc
limit 5


with customer_type as 	 (
select customer_id , previous_purchases ,
case 
	when previous_purchases = 1 Then 'New' 
	when previous_purchases between 1 AND 10 Then 'Retrurning'
	else 'Loyal'
	end as customer_segment
from customer
)

select customer_segment , count(*) as "Number of Customers"
from customer_type
group by customer_segment



with item_counts as(
select category , item_purchased,
count(customer_id ) as total_orders,
row_number() over( partition  by category order by count (customer_id) desc) as item_rank 
from customer
group by category, item_purchased 

)
select item_rank, category , item_purchased , total_orders 
from item_counts 
where item_rank <=3
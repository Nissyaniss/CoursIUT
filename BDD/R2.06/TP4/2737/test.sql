(select name, customers_number from lawyers where
	customers_number = (
		select min(customers_number) from lawyers
	) or
	customers_number = (
		select max(customers_number) from lawyers
	)
	order by customers_number desc
)
UNION all
(select 'Average' as name, Round(avg(customers_number),0) as customers_number from lawyers)

/*Martin Vazquez
CSC 355 Section 501
Assignment 3
1.28.2020*/

@/Users/martinvazquez/Winter2020/CSC_355/store501.sql

--1
select  distinct city, count(city)
    from customer
    group by city
    having count(city) >= 1
    order by city;
    
--2
select title, price
    from item
    order by price;

--3
select title, type, price 
    from item
    where price < 15.00
    order by price desc;
    
--4
select title
    from item
    where title like '%West%'
    order by title;
    
--5
select distinct cid
    from purchase
    where pdate >= date '2019-01-01'
    order by cid;
    
--6
select cid, max(pdate)
    from purchase
    group by cid
    order by cid;
    
--7
select type, min(price)
    from item
    group by type
    order by type;

--8
select pdate, count(pdate)
    from purchase
    group by pdate
    order by count(pdate) desc;
    
--9
select pid, pdate 
    from customer inner join purchase on customer.id = purchase.cid
    where name = 'Reed'
    order by pid;
    
--10
select pid, price*quantity as TotalCost
    from purchase inner join item on purchase.iid = item.id
    order by TotalCost desc;
    

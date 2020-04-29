/*
Martin Vazquez
CSC 355 - 501
Assignmnent 4
6 February 2020
*/

--1
select count(salary) as "Employees Earning at Least 90000", avg(salary) as averageSalary 
    from employee
    where salary >= 90000;


--2
select dname, dnumber, max(salary) as "Department Salary Max"
    from (department inner join employee on dnumber = dno)
    group by dname, dnumber
    order by dnumber;
    
--3
select last, salary
    from(department inner join employee on dnumber = dno)
    where dname = 'Development' and gender = 'M'
    order by salary;

--4
select min(salary)
    from (assignment inner join  employee on employeeid = eid)
        inner join project on projectno = pnumber
    where pname = 'Automation';

--5
select pname, hours
    from (assignment inner join  employee on employeeid = eid)
        inner join project on projectno = pnumber
    where first = 'Ahmed' and last = 'Salman'
    group by pname, hours
    order by pname;
    
--6     
select eid, count(pname)
    from (assignment inner join  employee on employeeid = eid)
        inner join project on projectno = pnumber
    group by eid
    having count(pname) >= 3;
    
--7
select e.eid, e.first, e.last, d.first, d.age
    from (employee e inner join dependent d on e.eid = d.employeeid)
    where d.gender = 'M'
    order by d.age;

--8
select pnumber, pname, sum(nvl(hours, 0)) as "Total Hours"
    from (project left outer join assignment on pnumber = projectno)
        where plocation = 'Pittsburgh'
        group by pnumber, pname
        order by sum(hours) desc;
        


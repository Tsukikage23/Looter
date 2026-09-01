# Write your MySQL query statement below
Select name as Employee from Employee e where salary > (Select salary from Employee t where t.id = e.managerId)
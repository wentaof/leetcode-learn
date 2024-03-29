--176. 第二高的薪水
select (
    select
    salary from (
        select *,dense_rank() over( order by salary desc) as no from Employee
    ) t1
    where no =2  limit 1
) as SecondHighestSalary
--方法2
select (select distinct salary from Employee order by salary desc limit 1 offset 1) as SecondHighestSalary



--177. 第N高的薪水
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    select (
    select
    salary from (
        select *,dense_rank() over( order by salary desc) as no from Employee
    ) t1
    where no =N  limit 1
) as SecondHighestSalary

  );
END
--方法2
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
set N := N-1;
  RETURN (
    select (select distinct salary from Employee order by salary desc limit 1 offset N) as SecondHighestSalary

  );
END


CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N := N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT
            salary
      FROM
            employee
      GROUP BY
            salary
      ORDER BY
            salary DESC
      LIMIT N, 1
  );
END


--178. 分数排名
select score,dense_rank() over(order by score desc) as `rank` from Scores


--180. 连续出现的数字
select
distinct l1.num as ConsecutiveNums
from Logs l1
left join Logs l2 on l1.id +1 = l2.id
left join Logs l3 on l2.id +1 = l3.id
where l1.num = l2.num and l2.num = l3.num and l1.num = l3.num

--181. 超过经理收入的员工
select
a.name as Employee
from Employee a
left join Employee b on a.managerId  = b.id
where a.salary > b.salary



--183. 从不订购的客户
select
distinct a.Name as Customers
from Customers a
left join Orders b on a.Id = b.CustomerId
where  b.CustomerId is null

--184. 部门工资最高的员工
--772 ms
select
b.name as Department, t1.name as Employee , t1.Salary
from (
select *,dense_rank() over(partition by departmentId order by salary desc) as no from Employee )t1
left join Department b on t1.departmentId = b.id
where t1.no = 1
--349 ms
select
t3.name as Department,t2.name as Employee ,t2.salary as Salary
from (
select departmentId, max(salary) as max_salary from Employee group by departmentId )t1
left join Employee t2 on t1.departmentId = t2.departmentId and t1.max_salary = t2.salary
left join Department t3 on t2.departmentId = t3.id


--185. 部门工资前三高的所有员工
select
b.name as Department, t1.name as Employee , t1.Salary
from (
select *,dense_rank() over(partition by departmentId order by salary desc) as no from Employee )t1
left join Department b on t1.departmentId = b.id
where t1.no <= 3
order by Department,Salary
--官方答案
SELECT
    d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
FROM
    Employee e1
        JOIN
    Department d ON e1.DepartmentId = d.Id
WHERE
    3 > (SELECT
            COUNT(DISTINCT e2.Salary)
        FROM
            Employee e2
        WHERE
            e2.Salary > e1.Salary
                AND e1.DepartmentId = e2.DepartmentId
        )
;
--196. 删除重复的电子邮箱
delete from Person where id in (
    select id from (
        select id,row_number() over(partition by email order by id) no from Person
    )t1 where no > 1
)
--官网答案
DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id

--197. 上升的温度
select w1.id
from Weather w1,Weather w2
where datediff(w1.recordDate,w2.recordDate)=1 and w1.Temperature > w2.Temperature

SELECT
    weather.id AS 'Id'
FROM
    weather
        JOIN
    weather w ON DATEDIFF(weather.date, w.date) = 1
        AND weather.Temperature > w.Temperatur
--262. 行程和用户
select
request_at as 'Day', round(sum( if(status != 'completed',1,0)) * 1.0 / count(1),2) as 'Cancellation Rate'
from Trips a
join Users b on a.client_id = b.users_id and b.banned = 'No'
join Users c on a.driver_id = c.users_id and c.banned = 'No'
where request_at BETWEEN '2013-10-01' AND '2013-10-03'
group by request_at




SELECT T.request_at AS `Day`,
	ROUND(
			SUM(
				IF(T.STATUS = 'completed',0,1)
			)
			/
			COUNT(T.STATUS),
			2
	) AS `Cancellation Rate`
FROM Trips AS T
JOIN Users AS U1 ON (T.client_id = U1.users_id AND U1.banned ='No')
JOIN Users AS U2 ON (T.driver_id = U2.users_id AND U2.banned ='No')
WHERE T.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY T.request_at


--511. 游戏玩法分析 I

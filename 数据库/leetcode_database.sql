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

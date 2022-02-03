# Mysql

> * 접속
>
>   * ```
>     mysql -u root -p
>     ```
>   
> * 위치 바꾸기
>
>   * ```
>     cd /
>     ```
>
>   * ```
>     cd 경로
>     ```
>
>
## DataBase
>
>  * RDBMS(Relational DataBase Management System)
>    * 관계형 데이터 베이스
>    * 정형 데이터들의 관계를 정의
>  * NoSQL (Not only SQL)
>    * 비 정형 데이터 저장
>    * 빅데이터에 용이 (분산 저장 등)
>  * `Entity(table)` 데이터베이스에 저장하려고 하는 현실상의 개념 / 객체
>  * `Attribute(colunb)` Entity의 속성
>  * `Tuple(row)` Entity의 값
>
>데이터 베이스 사용 
>
>```
>use mysql;
>```

## SQL

> Structured Query Language : 구조화 된 질의 언어
>
> * `DDL (Data Definition Language)` 데이터 정의 언어(DB 스키마 정의,조작)
>
>   ⁉스키마 설계도나 조작도 정도로 생각
>
>   ⁉view : 다른 테이블/뷰 에 있는 데이터를 보여주기 위해 사용 (수정 불가)
>
>   ⁉Procedure : 특정 작업에 필요한 Query들을 함수처럼 사용
>
>   * `CREATE` 데이터베이스, 테이블, 뷰(view), 프로시저(procedure) 등을 생성
>
>     * ```
>       --데이서베이스 생성:  
>       create database x;
>       ```
>
>     * ```
>       -- 생성한 테이블에 Column주기 
>       create table x(
>       
>         id int,
>       
>         name varchar(100),
>       
>         phone char(13),
>       
>         address varchar(1000),
>       
>         job varchar(100)
>       
>       );
>       ```
>
>     * ```
>       --뷰 생성
>       create view 뷰 as select ~;
>       ```
>
>     * ```
>       --만든 테이블 확인 
>       desc students;
>       ```
>
>   * `ALTER` 데이터베이스,테이블,뷰,프로시저 등을 수정
>
>     * ```
>       --테이블 COLUMN추가 ADD
>       alter table x
>       add job varchar(100);
>       ```
>
>     * ```
>       --테이블 수정 MODIFY
>       alter table students
>       
>       modify job varchar(1000);
>       ```
>
>   * `DROP` 데이터베이스,테이블,뷰,프로시저 등을 삭제
>
>     * ```
>       --테이블 삭제
>       drop table x;
>       ```
>
>     * ```
>       --데이터 베이스 삭제(안에든거 전부 삭제)
>       drop database x;
>       ```
>
> * `DML (Data Manipulation Language)` 데이터 조작 언어(Data 조작)
>
>   * `SELECT` 데이터 읽기
>
>     * ```
>       --데이터 베이스의 저장된 값을 볼때 or 특정 선택시
>       select *
>       from x;
>       ```
>
>     * ```
>       --조건을 걸고 불러오기 where
>       select * --순서 3
>       from employees --순서 1
>       where hire_date >= '2000-01-01'; --순서 2
>       ```
>
>       * 컬럼의 값 연산(산술,비교 등) : >,>=,<,<=,=,!=(<>),BETWEEN,IN,NOT IN,ANY,...
>       * 조건의 연결 : AND, OR
>
>     * 순차 정렬
>
>       * ```
>         --오름차순 asc (안써도 디폴트값으로 적용됨)
>         select 컬럼
>         
>         from 테이블
>         
>         order by 컬럼 asc
>         
>         limit 100; --갯수 제한
>         ```
>
>       * ```
>         --내림차순 desc
>         select 컬럼
>         
>         from 테이블
>         
>         order by 컬럼 desc
>         
>         limit 100; --갯수 제한
>         ```
>
>       * 묶어서 보기
>
>         * ```
>           select 컬럼
>           from 테이블
>           group by 컬럼;
>           ```
>
>         * 조건을 추가해서
>
>           * ```
>             select count(*)
>             
>             from employees
>             
>             where gender = 'M';
>             ```
>
>           * ```
>             --그룹화 후 집계함수에 조건을 줄땐 where 대신 having 사용
>             select dept_no,count(dept_no)
>             
>             from dept_emp
>             
>             group by dept_no
>             
>             having count(dept_no) >50000;
>             ```
>
>   * `INSERT` 데이터 삽입
>
>     * ```
>       --데이터에 값을 넣을때
>       insert into 테이블
>       values(1,'hong-gd','010-1111-1111','seoul');
>       --모든 컬럼에 차례대로 값을 지정
>       ```
>
>     * ```
>       --특정 컬럼에만 값을 넣을때
>       insert into students(id,name,phone)
>       
>       value (2, 'kim-sd','02-222-2222');
>       ```
>
>   * `UPDATE` 데이터 수정
>
>     * ```
>       --데이터 값을 수정  update 테이블 set 컬럼
>       update students
>       
>       set phone = '010-2222-2222',
>       
>       address = 'suwon',
>       
>       job = 'engineer'
>       
>       where id = 2;
>       ```
>
>   * `DELETE` 데이터 삭제
>
>     * ```
>       delete from 테이블
>       테이블의 전부 삭제
>       ```
>
>     * ```
>       --조건에 맞는 값 삭제
>       delete from students
>       
>       where id = 1;
>       ```
>
> * `DCL (Data Control Language)` 데이터 제어 언어(Data 제어)
>
>   ⁉TCL(Transaction Controll Language) : COMMIT, ROLLBACK
>
>   * `COMMIT` 데이터,트랜잭션 저장
>   * `ROLLBACK` 데이터,트랜잭션 취소(가장 마지막 COMMIT으로 되돌아감)
>   * `GRANT` DB권한 부여
>   * `REVOKE` DB 권한 삭제

## MYSQL

> 서로 관계가 있는 테이블을 하나로 연결
>
> * `INNER JOIN `(a와 b라는 테이블을 하나로 연결/ 특정 컬럼이 같다는 기준으로)
>
>   * select 컬럼 from 테이블a inner join 테이블b on 테이블a.컬럼 = 테이블b.컬럼
>
>     * ```
>       select first_name,title
>       
>       from employees emp inner join titles tt on emp.emp_no = tt.emp_no
>       
>       limit 100;
>       ```
>
>       * inner은 안써도 디폴트값으로 들어갑니다.
>
>   * select 컬럼 from 테이블a inner join 테이블b using(컬럼) 
>
>     * ```
>       select *
>       
>       from employees join titles using(emp_no)
>       
>       limit 100;
>       ```
>
>       * 합쳐지면서 연결 컬럼을 한번만 나오게 합니다.
>
> * `NATURAL JOIN`
>
>   * select 컬럼 from 테이블a natural join 테이블b
>
>     * ```
>       select *
>       
>       from employees emp natural join titles tt
>       
>       limit 100;
>       ```
>
>       * 테이블a의 컬럼명과 테이블b의 컬럼명이 단 하나만 같은 경우에 사용됩니다.
>
> * `CROSS JOIN`
>
>   ⁉`CARTESIAN PRODUCTS` 두 Table 사이에 **유효 join 조건을 적지 않았을때** 해당 테이블에 대한 모든 데이터를 전부 결합하여 Table에 존재하는 행 갯수를 곱한 만큼의 결과값이 반환
>
>   * select 컬럼 from 테이블a cross join 테이블b
>
>     * ```
>       select count(*)
>       
>       from employees cross join titles;
>       ```
>
>   * select 컬럼 from 테이블a join 테이블b
>
>     * ```
>       select count(*)
>       
>       from employees join titles;
>       ```
>
> * `OUTER JOIN`
>
>   * `LEFT JOIN` 
>
>     * select 컬럼 from 테이블a left join 테이블b on 테이블a.컬럼 = 테이블b.컬럼
>
>     * ```
>       select *
>       
>       from join_a left join join_b using(ab);
>       ```
>
>       * 없는값을 NULL 왼쪽 기준 남은 부분 출력
>
>   * `RIGHT JOIN` 
>
>     * select 컬럼 from 테이블a right join 테이블b on 테이블a.컬럼 = 테이블b.컬럼
>
>     * ```
>       select *
>       
>       from join_a right join join_b using(ab);
>       ```
>
>       * 없는 값은 NULL 오른쪽 기준 남은 부분 출력
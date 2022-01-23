# Pandas

## 데이터 합치기

> - pandas는 두 개 이상의 데이터 프레임을 하나로 합치는
> - **병합(merge)**이나 **연결(concate)**을 지원
> - merge(), join(), concat()

### 데이터 병합

#### merge() 명령을 이용한 데이터 프레임 병합

>  - merge
>
>    - 두 데이터 프레임의 공통 열(column)이나 인덱스(index)를 기준으로 합침
>    - **key** : 기준이 되는 열 데이터
>
>  - 형식
>
>    - df.merge(df1) : 두 df를 병합시켜 준다.
>
>    - 기본은 inner join : 양쪽에 동일하게 존재하는 키만 표시
>
>    - key : 기준열을 의미
>
>      - 실제 데이터 필드거나 행 인덱스 일 수 있다.
>
>    - 병합방식
>
>      - inner join : 양쪽 df에서 모두 키가 존재하는 data만표시
>      - outer join : 한쪽에만 키가 존재하면 data를 표시
>      - 병합방식을 설정 : how=inner(생략가능), how=outer
>
>    - ex)
>
>      - ```
>        고객 정보를 담고 있는 데이터 프레임
>        df1 = pd.DataFrame({'고객번호':[1001,1002,1003,1004,1005,1006,1007],
>                           '이름':['둘리','도우너','또치','길동','희동','마이콜','영희']},
>                            columns=['고객번호','이름'])
>        ```
>
>      - ```
>        예금 정보 데이터 프레임
>        df2 = pd.DataFrame({'고객번호':[1001,1005,1006,1008,1001,1007],
>                           '금액':[10000,20000,15000,5000,100000,30000,]},
>                            columns=['고객번호','금액'])
>        ```
>
>  - **merge 명령으로 두 df를 병합하는 문법**
>
>    merge(df1, df2, how, on, left_on, right_on, left_index, right_index)
>
>    - 모든 인수 생략(병합 df를 제외한) 공통 이름을 갖고 있는 열
>
>    - '고객번호'가 키가 됨
>
>    - 양쪽에 모두 존재하는 키의 data만 보여주는`inner join` 방식을 사용
>
>      - ```
>        pandas.merge(df1, df2)
>        ```
>
>      - ```
>        df1.merge(df2)
>        ```
>
>  - **pandas.merge(데이터프레임1, 데이터프레임2)**
>
>    - 기준데이터 프레임은 왼쪽에
>
>      - ```
>        pd.merge(df1,df2)
>        ```
>
>  - how 인수를 사용한 다양한 병합
>
>    **merge( , how = 'outer')**
>
>    - how = inner/outer/left/right
>      - how=left : 왼쪽 df에 있는 모든 키의 데이터는 표시
>      - how=right : 오른쪽 df 에 있는 모든 키의 데이터는 표시
>
>    - outer join
>
>      - 키 값이 한쪽에만 있어도 데이터를 보여 줌
>      - 어느 한 df에 데이터가 존재하지 않으면 NaN으로 표시됨
>
>    - ```
>      pd.merge(df1,df2,how='outer')
>      ```
>
>  - 동일한 키 값이 있는 경우
>
>    - 키값이 같은 데이터가 여러개 있는 경우에는 있을 수 있는 모든 경우의 수를 따져서 조합을 만들어 낸다.
>
>    - 예제2)
>
>      - ```
>        df1 = pd.DataFrame({
>            '품종':['setosa','setosa','virginica','virginica'],
>            '꽃잎길이':[1.4, 1.3, 1.5, 1.3]},
>            columns=['품종','꽃잎길이'])
>        ```
>
>      - ```
>        df2 = pd.DataFrame({
>            '품종': ['setosa','virginica','virginica','ersicolor'],
>            '꽃잎너비':[0.4,0.3,0.5,0.3]},
>            columns=['품종','꽃잎너비'])
>        ```
>
>    - df1과 df2 를 병합
>      - 위 데이터에서 키 값 setosa에 대해
>      - df1에는 1.4와 1.3 2개의 데이터가 있고
>      - df2에는 0.4라는 1개의 데이터가 있으므로
>      - 병합 데이터에는 setosa가 (1.4,0.4)(1.3,0.4)의 2 경우가 표현된다.
>      - 키값 virginica의 경우에는 df1에 2개 df2에 2개의 데이터가 있으므로
>      - 2개와 2개의 조합에 의해 4개의 데이터가 표현된다.
>    
>  - 양쪽 데이터프레임에서 공통된 키만 표현
>
>    - ```
>      df1.head(1)
>      df2.head(1)
>      pd.merge(df1,df2)
>      pd.merge(df1,df2,how= 'outer')
>      pd.merge(df1,df2,how= 'left')
>      pd.merge(df1,df2,how= 'right')
>      ```
>
>  - merge()의 on 인수를 사용하여 기준열 명시하여 병합
>
>    - **key**
>
>      - 두 데이터 프레임에서 이름이 같은 열은 모두 키가 될 수 있다.
>      - 열이름이 같아도 키로 사용할 수 없는 열이 있으면 **on 인수로 기준열을 명시**해야 한다.
>      - **기준열을 직접 지정 : on=기준열 이름**
>      - 반환 결과에 동일 필드명이 있을 경우에는 필드명_x, 필드명_y로 필드명을 변경해서 표현
>
>    - ```
>      pd.merge(df1,df2,on='고객명')
>      ```
>
>    - **키가 되는 기준열 이름이 두 데이터 프레임에서 다르게 나타나는 경우**
>
>      - **left_on, right_on 인수**를 사용해서 기준열을 명시해야 함
>
>      - ```
>        pd.merge(df1,df2,left_on='이름',right_on='성명')
>        ```
>
>
>  * 인덱스 기준으로 병합
>    * 일반 데이터 열이 아닌 인덱스를 기준으로 merge 할수도 있음
>      - 인덱스를 기준열로 사용하려면
>        - left_index = True 또는
>        - right_index = True 설정을 하게 됨

####  join()을 이용한 병합

> **Dataframe1.join(Dataframe2. how='left/right/inner/outer', on=keys)**
>
> - 사용 방법은 merge()와 동일
>
> - 행 인덱스를 기준으로 결합
>
> - Dataframe1.join(Dataframe2. how='left')가 default값
>
> - ```
>   df1.join(df2,how='outer')
>   ```
>
> - 

### 데이터 연결

#### concat() 명령을 사용한 데이터 연결

> **pd.concat([left, right], axis=0, join='outer', ignore_index=False, keys=None)**
>
> - left, right : Series, DataFrame, Panel object 리스트
> - axis : 0은 위+아래로 합치기, 1은 왼쪽+오른쪽으로 합치기
> - join : 'outer': 합집합(union), 'inner': 교집합(intersection)
> - ignore_index : False: 기존 index 유지, True: 기존 index 무시
> - keys : 계층적 index 사용하려면 keys 튜플 입력
>
> - 기준열 없이 데이터를 합친다
>
> - 위 아래로 데이터를 결합하는 **행 결합(row bind)**이 기본
>
> - axis 속성을 1로 설정하면 열 결합(column bind)을 수행
>
> - 단순히 두 시리즈나 데이터프레임을 연결하기 때문에 **인덱스 값이 중복**될 수 있다.
>
> - 행결합 : pd.concat([df1,df2], axis=0)
>
> - 열결합 : pd.concat([df1,df2],axis=1)
>
> - 두 시리즈 데이터 연결
>
>   - 행방향으로 합침
>
>     - ```
>       pd.concat([s1,s2])
>       ```
>
>   - 열방향으로 합침
>
>     - ```
>       pd.concat([s1,s2],axis=1)
>       ```
>
> - **데이터 프레임 행 결합**
>
>   - 행을 모두 표현
>
>   - join 인수 생략 : 기본값이 'outer'로 지정되어 있음 (모든 열 표현)
>
>     - ```
>       pd.concat([df1,df2],join='outer')
>       ```
>
>   - 인덱스가 중복시  기본 인덱스로 재설정
>
>     - ```
>       result.reset_index(drop=True)
>       ```
>
>     -  인덱스 열은 제거
>
> - concat( , join = 'inner')
>
>   - 공통된 열만 표현
>
>   - ```
>     pd.concat([df1,df2],join='inner')
>     ```
>
> - **concat( , ignore_index = True)**
>
>   - 기존 인덱스 제거 후 제로베이스 인덱스 설정
>
>   - ```
>     pd.concat([df1,df2],join='inner',ignore_index=True)
>     ```
>
> - **concat( , keys=[])**
>
>   - 상위 레벨 인덱스 설정
>
>   - keys 파라미터를 통해 상위레벨 인덱스 설정 가능
>
>   - ```
>     result=pd.concat([df1,df2,df3],keys= ['x','y','z'])
>     ```
>
> - 다중 인덱스인 경우 데이터 접근 : .연산자를 이용한 체인 인덱싱
>
>   - ```
>     result.loc['z'].loc[1:2]
>     ```
>
> - concat() 를 이용한 열 결합
>
>   **pd.concat([df1,df2], axis=1, join='inner/outer')**
>
>   - axis=1
>     - 데이터프레임들의 열을 결합
>
>   - join='outer' : 기본 설정
>     - 모든 행을 표시하고 해당 행의 데이터가 없는 열의 원소는 NaN으로 표시
>
>   - join='inner'
>
>     - 병합하는 데이터프레임에 중복되는 인덱스의 행만 표시
>
>   - concat( , axis=1, )을 이용한 열 결합 : outer join이 기본으로 적용
>
>     - ```
>       pd.concat([df1,df2],axis=1,join='outer')
>       ```
>
>   - concat( , axis=0, )을 이용한 행 결합
>
>     - ```
>       pd.concat([df1,df2],axis=0,join='outer')
>       ```
>
>   - inner join이 적용된 열 결합
>
>     - ```
>       pd.concat([df1,df2],axis=1,join='inner')
>       ```




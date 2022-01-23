# Pandas

## 데이터조작

> - 데이터 집계
> - 빈도, 비율, 합계, 평균, 최대값, 최소값 등
> - 데이터 정렬
> - 결측치 처리
> - apply()
> - 데이터 범주화
> - 인덱스 변경

### 데이터 집계

###데이터 개수 세기
>
> - count() 함수
>
> - NaN값은 세지 않음
>
> - value_count() 함수
>
> - 시리즈에 count()적용하여 개수 세기
>
>   - ```
>     s.count()
>     ```
>
> - 데이터 프레임에 count()함수 적용
>
>   - 각 열마다 데이터 개수를 세기 때문에 누락된 부분을 찾을 때 유용

#### 난수 발생시켜 데이터프레임 생성

> - seed(값) 함수 사용하여 동일한 난수 발생
>
>   - seed : 난수 알고리즘에서 사용하는 기본 값
>   - seed 값이 같으면 동일한 난수 발생
>   - 예. np.random.seed(10)
>
> - 계속 변경되는 난수를 생성하려면 time.time()을 사용하여 시드값이 매번 변하도록 지정
>
>   - 예. np.random.seed(int(time.time())
>
> - 고정 시드값
>
>   - ```
>     np.random.seed(20)
>     np.random.randint(5,size=4)
>     ```
>
> - 변경 시드값
>
>   - ```
>     import time
>             
>     np.random.seed(int(time.time()))
>     np.random.randint(5,size=4)
>     ```
>
> - NaN 부여
>
>   - ```
>     df1.iloc[2,3]=np.nan
>     ```

####  카테고리 값 세기

> - 시리즈, 데이터프레임의 범주형 데이터에 대한 **범주별 빈도(비율) 계산**
> - **value_counts( )** 함수 적용

#### 시리즈 데이터의 빈도 계산

> - 시리즈의 값이 정수,문자열 등 카테고리 값인 경우에
>
> - 시리즈.value_counts()메서드를 사용해 각각의 값이 나온 횟수를 셀 수 있음
>
> - 파라미터 normalize=True 를 사용하면 각 값 및 범주형 데이터의 비율을 계산
>     - 시리즈.value_counts(normalize=True)
>     
> - ```
>     s2.value_counts()
>     ```

#### 범주형 데이터에 value_counts() 함수 적용

> - 범주형 데이터 : 관측 별과가 몇개의 버무 또는 항목의 형태로 나타나는 자료
>
>   - ex. 성별(남,여), 선호도(종다, 보통, 싫다), 혈액형(A,B,O,AB) 등
>
> - ```
>   titanic['alive'].value_counts(normalize=True)
>   ```
>
> - ```
>   titanic['alive'].value_counts()
>   ```

#### 데이터프레임에 value_counts() 함수 사용

> - 행을 하나의 value로 설정하고 동일한 행이 몇번 나타났는지 반환
>
> - 행의 경우가 인덱스로 개수된 값이 value로 표시되는 Series 반환
>
> - ```
>   df.value_counts()
>   ```
>
> - ```
>   df1.value_counts().sort_index()
>   df1.value_counts().sort_index().shape
>   df1.value_counts().sort_index().index
>   ```
>
> - column : 시리즈
>
>   - ```
>     df1[0].value_counts()
>     df1.iloc[2,3]=np.nan
>     df1
>     df1[3].value_counts()
>     ```

### 데이터 정렬

> - 데이터 정렬을 위한 정렬 함수 사용
> - **sort_index()** : 인덱스를 기준으로 정렬
> - **sort_value()** : 데이터 값을 기준으로 정렬

#### 시리즈 정렬

> * 인덱스가 순서 없이 반환
>
>   * ```
>     s2.value_counts()
>     ```
>
> * 인덱스 기준 정렬
>
>   * ```
>     s2.value_counts().sort_index()
>     ```
>
> * 인덱스 기준 내림차순 정렬
>
>   * ```
>     s2.value_counts().sort_index(ascending=False)
>     ```
>
> * 값을 기준으로 오름차순 정렬
>
>   * ```
>     s2.value_counts().sort_values()
>     ```
>
> * 값을 기준으로 내림차순 정렬
>
>   * ```
>     s2.value_counts().sort_values(ascending=False)
>     ```

#### 데이터 프레임 정렬

> - df.sort_values() : 특정열 값 기준 정렬
>   - 데이터프레임은 2차원 배열과 동일하기 때문에
>     - 정렬시 기준열을 줘야 한다. by 인수 사용 : 생략 불가
>     - by = 기준열, by=[기준열1,기준열2]
>   - 오름차순/내림차순 : ascending = True/False (생략하면 오름차순)
>
> - df.sort_index() : DF의 INDEX 기준 정렬
>
>   - 오름차순/내림차순 : ascending = True/False (생략하면 오름차순)
>
> - ```
>   df1.sort_values(by=0)
>   ```
>
> - 1열을 기준으로 정렬, 1열 값이 동일 할때는 2열값을 기준으로 정렬
>
>   - ```
>     df1.sort_values(by=[1,2])
>     ```
>
> - ```
>   df.sort_values(by='num_legs')
>   ```
>
> - 데이터프레임의 index를 기준으로 정렬
>
>   - 인덱스 기준 정렬
>
>     - ```
>       df.sort_index()
>       ```
>
>   - 인덱스 기준 내림차순 정렬
>
>     - ```
>       df.sort_index(ascending=False)
>       ```

### 행/열의 합계

> - **df.sum()** 함수 사용
>
> - 행과 열의 합계를 구할때는 sum(axis=0/1) - axis는 0이 기본
>
>   - 각 열의 합계를 구할때는 sum(axis=0)
>   - 각 행의 합계를 구할때는 sum(axis=1)
>
> - 각 행의 합계 계산
>
>   - ```
>     df2.sum(axis=1)
>     ```
>
> - 각 열의 합계 계산
>
>   - ```
>     df2.sum(axis=0)
>     ```

### 평균, 최소값, 최대값

> - 데이터프레임에 적용되는 집계 관련 함수
>
> - 평균 : mean(axis=0/1)
>
>   - ```
>     df2.mean(axis=0)
>     ```
>
> - 최소값 : min(axis=0/1)
>
>   - ```
>     df2.min(axis=0)
>     ```
>
> - 최대값 : max(axis=0/1)
>
>   - ```
>     df2.max(axis=0)
>     ```
>
> - 각 행의 합계를 새로운 열로 추가
>
>   - ```
>     df2['Rowsum']=df2.sum(axis=1)
>     ```
>
> - 각 열의 합계를 구한후에 행으로 추가
>
>   - ```
>     df2.loc['Coltotal']=df2.sum(axis=0)
>     ```

### 데이터 삭제

>  drop() 함수
>
>  * 행 삭제
>
>    * df.drop('행이름',0) : 행삭제
>
>      - 행삭제 후 df로 결과를 반환
>
>    * 원본에 반영되지 않으므로 원본수정하려면 저장 해야 함
>
>    * df.drop('행이름',0) : 행삭제  (행삭제 후 df로 결과를 반환)
>
>      * ```
>        df2 = df2.drop('Coltotal',0)
>        ```
>
>  * 열 삭제
>
>    * df.drop('행이름',1) : 열 삭제
>
>      - 행삭제 후 df로 결과를 반환
>
>    * 원본에 반영되지 않으므로 원본수정하려면 저장 해야 함
>
>    * df.drop('컬럼명(열이름)',1) 열삭제 - 삭제 후 df로 반환(원본반영안됨)
>
>      * ```
>        df2.drop('Rowsum',1)
>        ```

### 결측치 처리

> **NaN 값 처리** 함수
>
> - df.dropna(axis=0/1)
>   - NaN값이 있는 열 또는 행을 삭제
>   - 원본 반영되지 않음
>
> - df.fillna(0)
>
>   - NaN값을 정해진 숫자로 채움
>   - 원본 반영 되지 않음
>
> - 결측치 적용
>
>   - ````
>     df2.iloc[0,0]=np.nan
>     ````
>
> - 결측치 포함 행 삭제 : dropna()
>
>   - ```
>     df2.dropna()
>     ```
>
>   - #axis=0과 같음
>
> - 결측치 포함 열 삭제 : dropna(axis=1)
>
>   - ```
>     df2.dropna(axis=1)
>     ```
>
> - 결측치를 다른 값으로 대체 : fillna() 함수
>
>   - 결측치를 0으로 변경
>
>     - ```
>       df2.fillna(0)
>       ```
>
>     - fillna() 적용 후 결과값은 실수가 됨 (NaN이 실수형)
>
>   - 결측치를 1로 변경
>
>     - ```
>       df2.fillna(1)
>       ```

### 행/열에 동일한 연산 적용

> - 열 또는 행에 동일한 연산 반복 적용할 때
>
> - apply() 함수
>   - DataFrame의 행이나 열에 복잡한 연산을 vectorizing 할 수 있게 해주는 함수
>   - 매우 많이 활용되는 함수
>
> - 형식 : apply(반복적용할 함수, axis=0/1)
>
>   - 0 : 열마다 반복
>   - 1 : 행마다 반복
>   - 생략시 기본값 : 0
>
> - 데이터프레임의 각 열에 sum() 함수 적용
>
>   - ```
>     df3.apply(np.sum,0)
>     ```
>
>   - sum함수는 열 또는 행단위로 적용되는 함수여서 각 열별로 적용 됨
>
>   -  각 열에 대해 np.sum 함수를 반복 적용
>
> - 데이터프레임의 각 행에 sum() 함수 적용
>
>   - ```
>     df3.apply(np.sum,1)
>     ```
>
>   - 각 행에 대해 np.sum 함수를 반복 적용
>
> - 데이터프레임의 각 원소의 제곱값을 계산
>
>   - ```
>     df3.apply(np.square)
>     ```
>
>   - square 함수는 원소에 적용이 가능 한 함수이므로 열별로 원소에 대하여 벡터화 연산을 진행
>
>   - 각 열별 모든 원소에 대하여 np.square 함수 적용(제곱값)
>
> - 데이터프레임의 행별로 각 원소의 제곱값을 계산
>
>   - ```
>     df3.apply(np.square,1)
>     ```
>
>   - 원소에 대하여 진행하는 함수여서 열/행 모두 동일한 결과
>
>   - 행별 각 원소에 대하여  np.square 함수 연산을 진행 

### 사용자가 정의한 연산을 행/열단위 적용 : lambda() & apply()

> - 데이터프레임의 기본 집계함수(sum, min, max, mean 등)들은 행/열 단위 벡터화 연산을 수행함
>   - apply() 함수를 사용할 필요가 없음
>
> - apply() 함수 사용은 복잡한 연산을 해결하기 위한 lambda 함수나 사용자 정의 함수를 각 열 또는 행에 일괄 적용시키기 위해 사용
>
>   - lambda 함수로 필요한 연산 기능을 구현하고, apply()를 통해 열/행 단위로 적용
>
> - 집합데이터의 최대값과 최소값의 차이를 구하는 lambda 함수 정의
>
>   - ```
>     diff =lambda x:x.max()-x.min()
>     ```
>
> - 직접 연산으로 통해 최대값과 최소값 차이 계산
>
>   - ```
>     df3.max(axis=1)-df3.min(axis=1)
>     ```
>
> - 데이터프레임 각 열의 데이터에 대한 범주별 빈도 계산
>
>   - ```
>     df3.apply(pd.value_counts)
>     ```
>
> - 각 열의 데이터에 대한 범주별 빈도 계산 후, NaN값은 0으로 변환하고 전체 데이터 타입을 정수로 변환
>
>   - ```
>     df3.apply(pd.value_counts).fillna(0).astype(int)
>     ```

### 수치형 데이터를 범주형 데이터로 변환

> 데이터값을 카테고리 값으로 변환
>
>- 값의 크기를 기준으로 하여 카테고리 값으로 변환하고 싶을때
>  - **cut(data, bins, label)**
>    - data : 구간 나눌 실제 값
>    - bins : 구간 경계값
>    - label: 카테고리 값
>  - **qcut(data, bins, label)**

#### 구간 경계선을 선정하여 범주형 데이터로 변환 : cut()

> #### 리스트 데이터를 범주형 데이터로 변환
>
> 구간을 나눌 실제 값 : 관측 데이터
>
> 구간 경계값, 범주 라벨 설정
>
> * 구간 경계값 설정
>
>   * ```
>     bins=[0,4,15,25,35,60,100]
>     ```
>
> * 범주 라벨
>
>   * ```
>     labels = ['영유아','미성년자','청년','중년','장년','노년']
>     ```
>
> * 카테고리 생성 함수 cut() 적용
>
>   * ```
>     cutAge=pd.cut(ages,bins,labels=labels)
>     ```
>
> **참고: Categorical 클래스 객체**
>
> - 카테고리명 속성 : Categorical.categories
>
> - 코드 속성 : Categorical.codes
>
>   - 인코딩한 카테고리 값을 정수로 갖음
>
> - 데이터프레임 데이터를 범주형으로 변환
>
>   - ```
>     df4['age_cut']=pd.cut(df4.age,bins,labels=labels)
>     ```

#### 데이터 개수가 같도록 데이터 분할 : qcut()

> 구간 경계선을 지정하지 않고 데이터의 사분위수(quantile) 기준으로 분할
>
> - 형식 : pd.qcut(data,구간수,labels=[d1,d2....])
>
>
> - 예)1000개의 데이터를 4구간으로 나누려고 한다면
>     - qcut 명령어를 사용 한 구간마다 250개씩 나누게 된다.
>     - 예외)같은 숫자인 경우에는 같은 구간으로 처리한다.
>     
> - ```
>     qcutData=pd.qcut(data,4,labels=['Q1','Q2','Q3','Q4'])
>     ```
>
> - 값이 겹치면 같은 구간으로 들어가게 된다.
>
>
>     - ```
>         pd.value_counts(qcutData)
>         Q1    5
>         Q2    5
>         Q3    5
>         Q4    5
>         ```
>
>

### 인덱스 설정

> 데이터프레임 인덱스 설정: set_index(), reset_index()
>
> - 기본인덱스 : 0부터 1씩 증가하는 정수 인덱스
>   - 따로 설정하지 않으면 기존 인덱스는 데이터열로 추가 됨
>
> - set_index() : 기존 행 인덱스를 제거하고 데이터 열 중 하나를 인덱스로 설정해주는 함수
>
> - reset_index() : 기존 행인덱스를 제거하고 기본인덱스로 변경
>
> - 데이터프레임의 인덱스를 a열로 설정
>
>   - ```
>     df3 = df3.set_index('a')
>     ```
>
> - 행 인덱스를 제거하고 기본 인덱스로 설정
>
>   - ```
>     df3.reset_index(drop=True)
>     ```
>
> - 인덱스 이름 바꾸기
>
>   - ```
>     df3 = df3.rename(index={0:'1반'})
>     ```
>
> - 행인덱스의 첫번째 인덱스 값을 1반으로 변경
>
>   - ```
>     df3 = df3.rename(index={0:'1반'})
>     ```
>
> - 열이름 값 변경
>
>   - ```
>     df3 = df3.rename(columns={'b':'학생'})
>     ```




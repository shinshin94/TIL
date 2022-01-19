# WEB - Html

> 세가지 규칙 
>
> 1. http로 시작하는 주소가 있음
> 2. 검색하고 주소를 찾아가 약속과 형식에 따라 저장된 정보를 얻어옴
> 3. 정보들 사이의 관계도 가지고 옴
>
> Data는 중요
>
> Big Data 양 많아야 신뢰도 높아지고 학습 좋음
>

## 클라이언트 (=Browser)

서버로 요청

request(Get	,	post)					`get request header에 data를 담아서 전송 (queryString)`

​				⬆헤더 ⬆바디 저장   	`post body에 내용을 숨겨서 가져감`

![image-20220119221333533](WEB.assets/image-20220119221333533.png)

`Rest`  HTTP 표준 프로토콜에 따르는 모든 플랫폼에서 사용이 가능

`RestfulRESTful`은 일반적으로 REST라는 아키텍처를 구현하는 웹 서비스를 나타내기 위해 사용되는 용어


## 서버

클라이언트에 응답

요청에 맞는 데이터를 응답

document

---



## HTML

HyperText Markup Language

\- 온라인 상의 문서(document)를 만들기 위해 데이터를 __구조화__ 시키는 언어

`head`: 문서를 간단히 정의

`body` :문서의 내용

`foot`

markdown 텍스트 입력 기법

`<p style="color:red;"> Hello, World! /p>`

`<>` 여는 태그/

`style= `은 태그의 속성 

Hello,wordl! 해당 태그에 적용될 내용

 `</>`닫기

---

`html : 5` 기본의 형식

<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>Document</title>

</head>

<body>

  

</body>

</html>

![image-20220119230455588](WEB.assets/image-20220119230455588.png)



---

## 블록요소 Block_inline

줄 바꿈

블록 요소 안에 텍스트 /인라인 요소 포함가능

블록 요소 안에 블록 요소 포함 가능

## 인라인 inline

줄 바꿈 없음

인라인 요소 안에 텍스트 /인라인 요소 포함가능

인라인 요소 안에 블록 요소 포함 불가

live server

기본임

```
http://     #통신규약

127.0.0.1 = local host

.

.

5500  #포트 번호
```

/web01-html/index.html



## text

`<b>진하게</b>`
`<strong>진하게</strong>`
`<i>기울임</i>`
`<em>강조하여</em>`
`<small>작은 텍스트,코멘트</small>`
`위<sup>첨자</sup>`
`아래<sub>첨자</sub>`
`<ins>내용 추가 </ins>`
`<del>내용 삭제</del>`

## img
```
이미지의 특정 부분에 링크 걸기
<img src="./경로/파일명.확장자" alt="설명" width="가로크기px" height="세로크기px" usemap="#my"/>

  <map name ='my'>

​    <area shape="rect" coords="화면 좌표,화면 좌표,화면 좌표,화면 좌표" href="틍정부분링크.html" alt="설명">

  </map>
```

## href

`<a href='#a'>1번</a>` 뒤에 주소를 줘서 특정한곳으로 이동

## list

``` 
<h1>목록</h1>
    <h2>순차적 목록</h2>
    <ol>
        학원 오는 순서
        <li>눈을 뜬다</li>	#자동으로 1
        <li>침대에서 나온다</li>	#2
        <li>씻는다.		#3이 붙음
            <ol>
                <li>양치한다</li>	#3이 포함하는 순차적 목록 1
                <li>머리감는다</li>	#2
                <li>샤워한다</li>	#3
            </ol>			
        </li>				
        <li>옷입는다</li>	#다시 큰 순차로 4
        <li>출발한다</li>	#다시 큰 순차로 5
    </ol>
    <h2>비 순차적 목록</h2>
    <ul>
        점심고르기
        <li>굶는다</li>	.으로 표현
        <li>짜파게티</li>
        <li>편의점
            <ul>
                <li>불닭 + 치즈볶</li>	빈점으로 표현
                <li>도시락</li>	
                <li>컵라면</li>
                <li>삼각김밥</li>
                <li>샌드위치</li>
            </ul>
        </li>
    </ul>
    <h2>정의형 목록</h2>
    <dl>
        <dt>제목</dt>
        <dd>내용</dd>
    </dl>
    <dl>
        <dt>ds/de 커리큘럼</dt>	아무것도 안붙음
        <dd>python</dd>
        <dd>numpy / pandas</dd>
        <dd>html css js jq</dd>
        <dd>django</dd>
        <dd>crawling / visulization</dd>
        <dd>
            <dl>
                <dt>ds</dt>
                <dd>ml</dd>
                <dd>dl</dd>
                <dd>...</dd>
            </dl>
            <dl>
                <dt>de</dt>
                <dd>ml</dd>
                <dd>hadoop/spark</dd>
            </dl>
        </dd>
```

---

## TABLE

```
<table border="1"> #border 표의 굵기
        <colgroup>
            <col width="200px"/> #크기 지정
            <col width="200px"/>
            <col width="200px"/>
            <col width="200px"/>
        
        </colgroup>

        <thead>
            <tr>
                <th>컬럼1</th>
                <th>컬럼2</th>
                <th>컬럼3</th>
                <th>컬럼4</th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <td rowspan="2">1(열 합치기)</td>
                <td>2</td>
                <td>3</td>
                <td>4</td>
            </tr>
            <tr>
                <td>6</td>
                <td colspan="2">7(행 합치기)</td>
                <td>8</td>
            </tr>
            <tr>
                <td>9</td>
                <td>10</td>
                <td>11</td>
                <td>12</td>
            </tr>
        </tbody>
        <tfoot>
            <tr>
                <td colspan="4" align="center">행 4개합치기</td>
            </tr>
        </tfoot>
    </table>
```

---

## layout

```
    <header class="html5">
        <h1>제목</h1>
        <nav class="html5">
            <span><a href="#">메뉴1</a></span>
            <span><a href="#">메뉴2</a></span>
            <span><a href="#">메뉴3</a></span>
            <span><a href="#">메뉴4</a></span>
        </nav>
    </header>

    <section calss="html5">
        <article class="html5" id="left">
            <p>내용1</p>
        </article>

        <article class="html5" id="right">
            <p>내용2</p>
        </article>
    </section>

    <footer class="html5">
        <address>copyright &copy; all rights reserved ...</address>
    </footer>
```

클래스 메소드 사용

```
<head>

.html5{

​      border: 1px dotted red;

​      margin:10px;

}

<head/>
```

## form

```
<form action="html-form-res.html" method="post"> #action 에 있는 경로 저장=> submit시 폼 속성안에 있는 네임값과 벨류값을 저장해서 보내짐
        <fieldset>
            <legend>회원가입</legend>

            <p>ID : <input type="text" name="id" /></p>
            <p>PW : <input type="password" name="pw" /></p>
            <p>Email 수신 여부<br/>
                <input type="radio" name="rdo" value="y" />y  #radio 둘중 하나
                <input type="radio" name="rdo" value="n" />n
            
            
            </p>
            <p>관심분야
                <input type="checkbox" name="web" value="web"/>web<br/>
                <input type="checkbox" name="ai" value="ai"/>Data Science<br/>
                <input type="checkbox" name="engi" value="engi"/>Data Engineer #checkbox 체크되있는 애들만 저장
            </p>
            <p>하고 싶은말
                <textarea name="etc" cols="60" rows="10"></textarea>
            </p>
            <p>
                <input type="button"  value="그냥 버튼"/><br/>
                <input type="reset" value="취소"/><br/>#현재 폼에 있는 값을 clear
                <input type="submit" value="전송"/> 
                			#submit입력받은 폼에 정보들 action의 위치로 보내기 요청
            </p>
        </fieldset>
    </form>
```

---

## select

```
<select name="lunch">
                <option value="chicken">치킨</option>
                <option value="pizza">피자</option>
                <option value="sushi">초밥</option>
            </select>
```

셀렉트 박스 생성


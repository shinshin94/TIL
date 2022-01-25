# web-javascript

## 기본 설명

> * 소프트웨어에 실행시키는 처리 절차를 문자(텍스트)로 기술한 것
>
> * 동적인 기능을 한다
>
> * inline 방식
>
>   * ```
>     <li onclick="alert('inline 방식!!!');">inline 방식</li>
>     ```
>
> * 내부 작성 방식
>
>   * ```
>     <li onclick="embeddedFunction();">내부 작성 방식</li> #함수 호출
>     ```
>
>   * ```
>     호출받은 함수(head)에 써둠
>     <script type="text/javascript">
>     	function embeddedFunction(){
>     		var doc = document.getElementsByTagName("li")[1];
>     		doc.style.color = "red";
>     		doc.innerHTML = "<strong>javescript가 html 문서(document)를 변화시켰다!!!</strong>";
>     	}
>     </script>
>     ```
>
> * 외부 *.js 방식
>
>   * ```
>     <li onclick="fileFunction();">외부 *.js 방식 (file)</li>
>     ```
>
>   * ```
>     (head)
>     <script type="text/javascript" src="폴더위치/위치/부를파일명.js"></script>
>     ```
>
>   * ```
>     불러온 외부 위치 함수
>     function fileFunction(){
>         window.alert("외부 js file에서 실행됌!!");
>     }
>     ```
>
> * tip 불러올때 알림 띄우기
>
>   * ```
>     window.onload=function(){
>         alert("윈도우 로딩 됨! (로딩 후)");
>     }
>     ```

## var

> * 변수 선언 규칙
>
>   * 대소문자 구분
>   * 영문,$, _로 시작
>   * 영문,$, _,숫자 사용 가능
>   * 키워드(예약어) 사용 불가
>
> * 전역 변수 
>
>   * window 객체에 포함됨
>
> * 지역 변수 :
>
>   * 함수나 객체 내부에 선언
>
> * ```
>   var variable = 10; #전역변수
>                             
>   	function val01(){
>   	variable=variable+5;   #지역변수 
>   	document.getElementById("value01").innerHTML=
>   	"<b style='color:red; background: yellow;'>" + variable+"</b>";
>   }
>   ```

## typeof

> * 값의 타입을 알아볼때
>
> * 종류
>
>   * string            문자열
>   * number        숫자
>   * boolean       논리
>   * Null               null
>   * object           객체
>   * function       함수
>
> * ```
>   function jsType(){
>   	var inferVal="문자";
>   	alert(inferVal+"의 타입은 : " +typeof(inferVal));
>   }
>   ```

## window 객체의 대화형 메서드

> * alert()
>
>   * 경고, 코드 디버깅용
>
>   * ```
>     function alertFunc(){
>     alert("내용 출력 (단순 대화창)");
>     }
>     ```
>
> * confirm()
>
>   * 확인 / 취소 버튼 (true / false 리턴)
>
>   * 밑에는 확인을 누를시 파란색으로 변환 취소일시 되돌리게 만들어둠
>
>   * ```
>     function confirmFunc(){
>     	if(confirm("배경을 파란색으로 변환?")){
>     		alert("파란색으로 변환합니다.");
>     		document.body.style.backgroundColor='blue';
>     	} else {
>     		alert("배경식을 없앱니다.");
>     		document.body.style.backgroundColor='';
>     	}
>     }
>     ```
>
> * prompt()
>
>   * 텍스트박스, 확인/ 취소 버튼 (텍스트/null 리턴)
>
>   * 밑에는 텍스트 박스에 입력하여 값에 따라 설정을 줌
>
>   * ```
>     function promptFunc(){
>     	var txt = prompt("좋아하는 과목을 선택해 주세요\n[1:python 						2:html/css 3:javascript]","3");
>     	if (txt == 1) {
>     		alert("python 재밌죠!!!");
>     	} else if (txt == 2) {
>     		alert("문서 구조화 하고 스타일 지정 재밌죠!!!")
>     	}  else if (txt == 3) {
>     		alert("아직 몇개 안해봤는데 벌써 재밋냐")
>     	}  else if (txt == null) {
>     		alert("하나라도 좋아해주세요!")
>     	} else {
>     		alert("1이나 2 나 3만 입력해주세요")
>     	}
>     }
>     ```

## function

> * 함수의 종류
>
>   * 명시적 함수
>
>     * ```
>       function func01(){
>       	alert("함수의 이름이 있습니다.");
>       }	#일반적인 함수
>       ```
>
>   * 익명함수
>
>     * ```
>       var func02 = function(){ 	#변수의 값으로 함수가 있음
>       	alert("함수의 이름이 없어요 ...");	#바로 안에 내용이 출력됌
>       }	
>       ```
>
>   * 즉시 실행 함수
>
>     * ```
>       function func03(){
>       	(function(){
>       		alert("즉시 실행 함수");
>       	})(); #⬅이거 말하는거임
>       }
>       ```
>
>     * 함수의 끝에 ()를 넣음으로서 바로 내부에 있는 함수를 실행
>
>   * 함수 리터럴
>
>     * ```
>       function func04(){
>       	literalPrn(function(msg){alert(msg);});
>       }
>       ```
>
>     * ```
>       function literalPrn(literal){
>       	literal("안녕하세요. 함수 형태의 값!!! 입니다.")
>       }
>       ```
>
>     * 함수 func04에서 함수 literalPrn에 msg와 alert(msg)를 가져가서 호출함
>
>     * literalPrn(literal) => literalPrn(function(msg){alert(msg);})이 됌
>
>     * msg에 literal의 내용인 ("안녕하세요. 함수 형태의 값!!! 입니다.") 이 들어감
>
>     * alert 출력에 들어온 내용이 출력됌
>
>   * 외부함수
>
>     * ```
>       function closureFunc(val){
>       	var suffix = "님, 안녕하세요~";
>       	function innerFunc(){
>       		alert(val + suffix + "잘 부탁 드립니다");
>       	}
>       	return innerFunc;
>       }
>       var closureTest01 = closureFunc("멀캠");
>       ```
>
>     * 전역 변수인 closureTest01을 찾음
>
>     * 변수의 값에 함수 closureFunc("멀캠")이 있음
>
>     * 함수 closureFunc(val)에 val은 이미 "멀캠"으로 받아서 옴
>
>     * function closureFunc("멀캠")
>
>     * 함수 innerFunc에 closureFunc 안에 있는 내용과 전역 변수에 있던 "멀캠"을 같이 가져옴
>
>     * function innerFunc("멀캠")
>     
>     * alert에 가져온 값들을 넣어서 "멀캠 (val)+ 님, 안녕하세요(suffix)~ + 잘부탁드립니다" 로 innerFunc의 값이 리턴됌
>     
>     * closureFunc에서 innerFunc에서 리턴된 값을 그대로 쓰겠다고 return에 씀
>     
>     * 최종 출력 "멀캠님, 안녕하세요~잘부탁드립니다" (innerFunc에서 나온값임)

## control

> * if
>
>   * 조건문
>
>   * ```
>     function ifTest(){
>     	var i = prompt("숫자 1이나 2를 입력해 주세요");
>     	if (i == 1) {
>     		alert("1 입니다.");
>     	} else if (i == 2) {
>     		alert("2 입니다.");
>     	} else {
>     		alert("다른 숫자 입니다.");
>     	}
>     }
>     ```
>
> * switch
>
>   * 특정값으로 이동해서 출력 break를 안쓰면 다음걸로 이어서 계속 출력
>
>   * ```
>     function switchTest(){
>     	var season = prompt("봄 여름 가을 겨울 중 좋아하는 계절을 입력해 주세요");
>     	switch(season){
>     	case "봄":
>     		alert("봄에는 벚꽃엔딩");
>     		break
>     	case "여름":
>     		alert("여름은 바다죠!");
>     		break
>     	case "가을":
>     		alert("가을엔 단풍구경");
>     		break
>     	case "겨울":
>     		alert("겨울엔 스키장?");
>     		break
>     	default:
>     		alert("봄,여름,가을,겨울 중 하나만 입력해주세요");
>     	}
>     }
>     ```
>
> * for
>
>   * 특정 횟수를 반복문
>
>   * ```
>     function forTest(){
>     		//초기값;조건식;증감식
>     	for (var i=0; i<10;i++){
>     	console.log(i);
>     	}
>     }
>     ```
>
> * while
>
>   * 특정 조건에 반복문
>
>   * ```
>     function whileTest(){
>     	var i = 0;
>     	while (i<10){
>     	console.log(i);
>     	//i=i+1;
>     	//i+=1;
>     	//i++;
>     	//console.log(i++);
>     	//console.log(++i);
>     	}
>     }
>     ```
>
>   * 증감연산자 (++ / --)
>
>   * 변수++ : 변수의 값을 리턴한 뒤, 연산
>
>   * ++변수 : 연산을 먼저 하고, 변수의 값 리턴

## dom

> * dom 탐색 메서드
>
>   * querySelector
>
>     * node 한개를 선택한다
>
>     * ```
>       var doc = document.querySelector("#test")
>       ```
>
>   * querySelectorAll
>
>     * nodelist 전체를 선택한다
>
>     * ```
>       var doc = document.querySelectorAll("#test")[0];
>       ```
>
>     * 뒤에 인덱스를 지정해서 원하는 nodelist의 순번값을 불러올수 있다
>
> * 엘리먼트의 id로 탐색
>
>   * 엘리먼트 하나를 선택(중복 불가 ) - 반환 : 값 하나 (node)
>
>   * ```
>     함수
>     <script>
>     function searchId (){
>     	var doc = document.getElementById("test");
>     	//console.log(doc);
>     	doc.innerHTML="id 속성으로 탐색";
>     	doc.style.color = "red";
>     }
>     </script>
>     ```
>
>   * ```
>      함수 호출
>      <p id="test" onclick="searchId();">
>     ```
>
> * 엘리먼트의 name으로 탐색
>
>   * 엘리먼트를 여러 개 선택 - 반환 : 배열 (NodeList)
>
>   * ```
>     함수
>     function searchName(){
>     	//nodelist
>     	var doc = document.getElementsByName("test02");
>     	console.log(doc);
>     	doc[1].value = "name으로 탐색!!";
>     }
>     ```
>
>   * 인덱스를 지정해서 선택함
>
>   * ```
>     함수 호출
>     <p onclick="searchName();">
>     ```
>
> * 엘리먼트의 태그 이름으로 탐색
>
>   * 엘리먼트를 여러 개 선택 - 반환 : 배열(NodeList)
>
>   * ```
>     함수
>     function searchTag(){
>     	var doc = document.getElementsByTagName("p");
>     	doc[3].innerHTML= "tag 이름으로 탐색했음!!"
>     }
>     ```
>
>   * 인덱스 지정 선택
>
>   * ```
>     함수 호출
>     <p onclick="searchTag();">
>     ```

## object

> 객체의 구성
>
> * property : 속성
> *  function (method) : 기능
> *  this : 객체 내부의 메서드나 속성을 정의
> * prototype : 객체의 확장
> * 설계도를 기준으로 만들어진 물건이라 생각하면 편함
>
> ```
> 함수
> function objTest(){
> 	//객체 생성
> 
> 	obj01.prn();
> 
> }
> function object01() {
> 	this.name01="홍길동";	#this: 파이썬의 clss에서 self라고 생각
> 	var name02 = "hong =gd";
> 	this.getName02 = function(){
> 	return name02;
> 	}
> }
> ```
>
> ```
> 함수 호출
> <button onclick="objTest();">확인</button>
> ```

## string

> * 문자열 합치기
>
>   * ```
>     함수
>     function strTest01(){
>     	var str01 = "String";
>     	var str02 = "Test";
>                           
>     	var str03 = str01+ str02;
>                           
>     	var newString = str01.concat("Test","Java","Script");
>     	//alert(newString);
>                           
>     	var joinTest = ["5","10","15","20"].join("+")
>     	alert(joinTest);
>     }
>     ```
>
>   * 배열.joing('문자') : 배열 사이사이에 문자가 삽입됨(문자열로 반환)
>
>   * ```
>     함수 호출
>     <button onclick="strTest01();">
>     ```
>
> * 다른 자료형 합치기
>
>   * ```
>     함수
>     function strTest02(){
>     	var numVal = 12.5;
>     	var bool = true;
>                           
>     	var result = "string" + numVal + bool;
>                           
>     	var result2 = "a" + 10 + 20;
>     	alert(result2);
>     }
>     ```
>
>   * 문자열과 다른 타입이 만나면 문자열로 합쳐짐
>
>   * ```
>     함수 호출
>     <button onclick="strTest02();">
>     ```
>
> * 문자열 비교하기
>
>   * ```
>     함수
>     function strTest03(){
>     	var str = prompt("이름을 입력하세요");
>     	var span = document.getElementById("res");
>                           
>     	if (str == "멀캠"){
>     	span.textContent = str + "님 환영합니다";
>                           
>     	} else if (str.toLowerCase() == "multicampus") {
>     	span.textContent = str + ",Hello!";
>                           
>     	} else{
>     	span.textContent = "이름을 다시 한번 확인해 주세요!!"
>     	}
>                           
>     	// 자동 형변환
>     	var numVal = 10;
>     	if (numVal=="10") {
>     	alert("== 연산자 사용 : 숫자 10 입니다.");
>                           
>     	} else {
>     	alert("==연산자 사용 : 숫자 10이 아닙니다.");
>     	}
>                           
>     	//=== : 엄격한 비교
>     	if (numVal==="10") {
>     	alert("=== 연산자 사용 : 숫자 10 입니다.");
>                           
>     	} else {
>     	alert("===연산자 사용 : 숫자 10이 아닙니다.");
>     	}
>     	//문자열 객체
>     	var strObj = new string("멀캠");
>     	var strLiteral = "멀캠";
>                           
>     	if (strObj == strLiteral) {
>     	alert("문자가 같습니다.");
>     	} else {
>     	alert("문자가 다릅니다.");
>     	}
>     	                      
>     	//객체와 값은 다름
>     	if (strObj === strLiteral) {
>     	alert("문자가 같습니다.===");	
>     	} else {
>     	alert("문자가 다릅니다.===");
>     	}
>     }
>     ```
>
>   * ```
>     함수 호출
>     <button onclick="strTest03();">
>     ```
>
> * 문자열 검색하기
>
>   * ```
>     함수
>     function strTest04(){
>                           
>     	var strVal = "홍길동 이순신 유재석 강호동 홍길동";
>     	var prop = prompt("검색할 이름을 입력해 주세요");
>     	alert("indexOf : " + strVal.indexOf(prop));
>     	alert("lastIndexOf :" +strVal.lastIndexOf(prop))
>     }
>     ```
>
>     * indexOf : 왼쪽에서 -> 오른쪽으로 찾음
>     * lastIndexOf : 오른쪽에서 -> 왼쪽으로 찾음
>     * 검색한 단어의 첫번째 인덱스 !!
>     * 값이 존재하지 않으면 -1
>     * 파이썬의 index로 생각
>
>   * ```
>     함수 호출
>     <button onclick="strTest04();">
>     ```
>
> * 문자열 추출하기
>
>   * ```
>     함수
>     function strTest05(){
>     	var strVal = "문자열 추출하기. 관련 메소드:indexOf,substring";
>     	var startIndex = strVal.indexOf(":");
>     	var endIndex = strVal.lastIndexOf(",");
>     	var res = strVal.substring(startIndex,endIndex);	
>                           
>     	var splitVal = strVal.split(" ");
>     	alert(splitVal[1]);
>     }
>     ```
>
>   * 객체의 시작 인덱스로 부터 종료 인덱스 전 까지 문자열의 부분 문자열을 반환
>
>   * ```
>     함수 호출
>     <button onclick="strTest05();">
>     ```
>
> * 키워드 나누기
>
>   * ```
>     function strTest06() {
>     	var prop = prompt("쉼표로 구분하여 키워드를 입력해주세요","사과,바나							나,키위,수박");
>     	var propArr = prop.split(",");
>     
>     
>     	var propResult = "";
>     	for (var i=0; i < propArr.length; i++){
>     	propResult+=propArr[i] + "<br/>";
>     	}
>     	document.getElementById("key").innerHTML=propResult;
>                                                 
>     }
>     ```
>
>   * split("문자") 기준을 줘서 나누기 
>
>   * ```
>     <button onclick="strTest06();">
>     ```

## number

> * 숫자
>
>   * ```
>     함수
>     function numberObj(){
>     	//literal 값 자체
>     	var num01 = 3;
>     	//alert(num01 + ":" + typeof(num01)) #숫자
>                           
>     	var num02 = new Number(3);
>     	//alert(num02 + ":" + typeof(num02)); #객체형태
>                           
>     	//alert(parseInt("1")+1); #parseInt int형태로 바꿔줌
>                           
>     	// Not a Number
>     	//alert(parseInt("a")+1);	#NaN  잘못된 입력
>                           
>     	var prop = prompt("숫자만 입력해 주세요");
>     	if (isNaN(prop)) {			#IS함수 T/F로 반환
>     	alert("숫자가 아닙니다");
>     	} else {
>     	alert("숫자가 맞습니다")
>     	}
>     }
>     ```
>
>   * ```
>     함수 호출
>     <button onclick="numberObj();">
>     ```
>
> * 난수
>
>   * ```
>     함수
>     function randomNum() {
>                           
>     	var hundred = Math.floor(Math.random() * 101); #0~100난수
>                           
>     	var min = 10;
>     	var max = 100;
>     	var ran = Math.floor(Math.random()*(max-min)+min); #10~100난수
>     	alert(ran);
>                           
>     }
>     ```
>
>     * Math.random() : 0 <= x < 1
>     * Math.floor() : 내림
>     * Math.round() : 반올림
>     * Math.ceil() : 올림
>
>   * ```
>     함수 호출
>     <button onclick="randomNum();">
>     ```
>
> * 난수를 이용한 배경 색 변환
>
>   * ```
>     함수
>     function randomBG(){
>                           
>     	var rum = function(){
>     	return Math.floor(Math.random()*256);
>     	                      
>     	}
>     	document.body.style.backgroundColor = "rgb(" + rum() + "," + 										rum() + "," + rum() + ")";
>     }
>     ```
>
>   * style 색상 표현식 : rgb(256,256,256)
>
>   * ```
>     함수 호출
>     <button onclick="randomBG();">
>     ```
>
> * 난수를 이용한 원 그리기(1)
>
>   * ```
>     함수
>     <div id="circle">
>     function randomCircle(){
>     	var rnum = Math.floor(Math.random() * 200);
>     	var circle = document.getElementById("circle");
>                           
>     	circle.style.width = rnum + "px";
>     	circle.style.height = rnum + "px";
>                           
>     	circle.style.borderRadius = Math.floor(rnum/2) + "px";
>     	circle.style.display = "block";
>     }
>     ```
>
>   * rnum에 난수를 입력받고  rnum/2로 곡률 입력 
>
>   * ```
>     함수 호출
>     <button onclick="randomCircle();">
>     ```
>
> * 난수를 이용해 그린 원의 넓이와 둘레 구하기
>
>   * ```
>     함수
>     function circleArea(){
>     	#circle id에서 사용된 난수값+"px"를 가져옴. width이기에 가로값임
>     	var circleWidth=document.getElementById("circle").style.width;
>     	#substring으로 난수값px에서 뒤의 문자열 "px"를 제거
>     	var r2 = circleWidth.substring(0,circleWidth.length-2);
>     	                                            
>     	#alert(parseInt(circleWidth));이거로 가져오면 위에 두개 없이 간편
>     		숫자만 가져옴
>     		                                            
>     	#반지름을 구하기 위해 반으로 나눔
>     	var r = Math.floor(r2/2);
>                                                 
>     	alert(Math.PI*r*r);
>     	//document.getElementById("area").innerHTML=
>     	#⬆원의 넓이⬇				  Math.floor(Math.PI*r*r);
>     	document.getElementById("area").innerHTML=
>     								Math.floor(Math.PI*Math.pow(r,2));
>                                                 
>     	document.getElementById("len").innerHTML=
>     	#원의 지름					  Math.floor(Math.PI*r2);
>     
>     
>     }
>     ```
>
>   * Math.PI  파이값 3.14...
>
>   * ```
>     함수 호출
>     <button onclick="circleArea();">
>     ```

## date

> ```
> onload=function(){
> 	document.getElementsByTagName("button")[0].onclick = testDate01;
> 	document.getElementsByTagName("button")[1].onclick = testDate02;
> 	document.getElementsByTagName("button")[2].onclick = testDate03;
> 	document.getElementsByTagName("button")[3].onclick = testDate04;
> 	document.getElementsByTagName("button")[4].onclick = testDate05;
> }
> ```
>
> onload 모든 내용을 읽은 후에 실행됌
>
> * 오늘 날짜
>
>   * ```
>     function testDate01(){
>     	var inputDate = document.getElementById("today");
>                           
>     	var date = new Date();
>                           
>     	inputDate.innerHTML=date.toDateString()+"<br/>";
>     	inputDate.innerHTML+=date.toLocaleDateString() + "<br/>";
>     	inputDate.innerHTML+=date.toLocaleString() + "<br/>";
>     	inputDate.innerHTML+=date.toLocaleTimeString() +"<br/>";
>                           
>     }
>     ```
>
>     * inputDate 날짜 받기
>     * toDateString ()  Fri Jan 21 2022
>       * 날짜 부분을 변환하고 결과를 반환
>     * toLocaleDateString()    \2022. 1. 21.
>       * 날짜 부분을 지역의 언어에 맞는 문자열 표현
>     * toLocaleString()   \2022. 1. 21. 오후 11:47:33
>       * 지역 값에 따른 숫자 표기 방식을 적용하여, 문자열로 반환하는 역할
>     * toLocaleTimeString()  오후 11:47:33
>       *  시간 부분 문자열로 변환하고 결과
>
>   * ```
>     <span id="today"></span>
>     <button>오늘날짜</button>
>     ```
>
> * 오늘 날짜(표현)
>
>   * ```
>     function testDate02(){
>     	var date = new Date();
>     	var year = date.getFullYear();
>     	var month = date.getMonth() +1; //인덱스로 나옴(0~11)
>     	var day = date.getDate();
>     	var week = date.getDay(); //인덱스 값으로 나옴
>     	var dayOfWeek = ["일","월","화","수","목","금","토"];
>                           
>     	document.getElementById("today").innerHTML = 									year+"/"+month+"/"+day+"/"+dayOfWeek[week];
>                           
>     	date.prn();
>     }
>     ```
>
>   * 2022/1/21/금
>
>   * ```
>     <span id="today"></span>
>     <button>오늘날짜(표현)</button>
>     ```
>
> * 특정 날짜 출력하기
>
>   * ```
>     function testDate03(){
>     	var year = 2022;
>     	var month = 5;
>     	var day = 13;
>                           
>     	var date = new Date(year,month-1,day);
>                           
>     	document.getElementById("specific").innerHTML="취업 :" + date;
>     }
>     ```
>
>   * 취업 :Fri May 13 2022 00:00:00 GMT+0900 (한국 표준시)
>
>   * ```
>     함수 호출
>     <span id="specific"></span>
>     <button>특정 날짜</button>
>     ```
>
> * 경과 날짜 출력하기
>
>   * ```
>     function testDate04(){
>     	var dates = document.getElementById("dates").value;
>     	var inputDate = document.getElementById("inputdate").value;
>                           
>     	var date = new Date(dates);
>                           
>     	date.setDate(date.getDate() + parseInt(inputDate));
>                           
>     	document.getElementById("result").value = 															date.toLocaleDateString();
>     }
>     ```
>
>   * 날짜를 정하고 입력받은 만큼 더해서 출력
>
>   *  ```
>      입력과 함수 호출
>      <label>지정 날짜</label>
>      <input type="date" id="dates" size ="50"/>
>      <br/>
>      <label>경과일</label>
>      <input type="number" id="inputdate"/>
>      <br/>
>      <label>경과 후 날짜</label>
>      <input type="text" id="result" readonly="readonly"/>
>      <button>경과 날짜</button>
>      ```
>
> * D-day
>
>   * ```
>     function testDate05(){
>     	var dates02 = document.getElementById("dates02").value;
>     	var inputDate02=document.getElementById("inputdate02").value;
>                                                 
>     	var nowDate = new Date(dates02);
>     	var afterDate = new Date(inputDate02);
>                                                 
>     	var resultVal = (afterDate.getTime() - nowDate.getTime()) 													/(1000*60*60*24);
>                                                 
>     	document.getElementById("result02").value = resultVal;
>     }
>     ```
>
>     * getTime() : milliseconds 
>     * `(1000*60*60*24) =(초*분*초*일)`
>
>   * 시작 날짜와 종료 날짜를 정하고 남은 일수가 구해나옴
>
>   * ```
>     <label>시작 날짜</label>
>     <input type="date" id="dates02" size="50"/>
>     <br/>
>     <label>종료 날짜</label>
>     <input type="date" id = "inputdate02" />
>     <label>남은 일수</label>
>     <input type="text" id="result02" readonly="readonly"/>
>     <button>남은 일수 구하기</button>
>     ```

## array

> 배열 : 여러개의 값을 효과적으로 관리하는 객체
>
> * 비어있는 배열 만들기
>
>   * ```
>     var arrayObj=new Array(5)
>     ```
>
>     * 5칸짜리 빈공간을 만듬
>     * 비어있는것의 인덱스를 찾을시 undefinded
>
> * 배열 만들기 
>
>   * ```
>     var arrayObj = new Array(1,2,3,4,5)
>     arrayobj[2] = 7; //인덱스의 값을 바꿀수도 있음
>     ```
>
> * 다중 배열
>
>   * ```
>     function multiArr(){
>     	var len = 3; #배열의 크기를 정함
>     	var arr = new Array(len); //크기만큼의 1차원 배열을 만듬
>     	for (var i=0; i < arr.length;i++) {   //크기만큼의 2차원 배열을 만듬
>     	arr[i] = new Array(len);
>     	}
>     }
>     ```
>
>   * 반복문을 써서 간단히 2차원 배열을 만들수 있다
>
> * join 함수
>
>   * ```
>     function joinTest(){
>     	var nums = ['1','2',3,4,'5'];
>     	var res = nums.join("+");
>     	alert(eval(res));
>     }
>     ```
>
>     * join을 넣을시 사이에 join"+"가 들어간다
>     * 자바스크립트는 자동으로 형변환을 해줘서 15가 된다
>
> * 정렬
>
>   * 문자 정렬 sort()
>
>     * ```
>       function sortTest01(){
>       	var arr = ['a','d','b','c'];
>       	alert(arr);
>       	arr.sort();
>       	alert(arr);
>       }
>       ```
>
>     * 문자의 순서로 정렬된다
>
>   * 숫자 정렬 sort()
>
>     * ```
>       function sortTest02(){
>       	// 아무 함수도 넣지 않으면 ascii code 순으로 정렬된다
>       	var arr = [1,2,6,11,3,65,21];
>       	//alert(arr); 이대로 하면 아스키값
>       	arr.sort(compareNum); //정렬함수 넣음
>       	alert(arr);
>       }
>       ```
>
>     * 정렬함수
>
>     * ```
>       function compareNum(a,b){
>       	return a - b;
>       }
>       ```
>
>   * 거꾸로 정렬 reverse()
>
>     * ```
>       function reverseTest(){
>       	var arr = [19,2,3,6,22,100];
>       	arr.sort(function(a,b){return a-b}) //먼저 정렬해줌
>       	arr.reverse(); //역순으로 바꿔줌
>       	alert(arr);
>       }
>       ```
>
> * queue
>
>   * push
>
>     * 내용을 순서대로 넣는다
>
>   * shift
>
>     * 맨앞의 것을뺀다
>
>   * pop
>
>     * 맨 뒤의것을 뺀다
>
>   * ```
>     function pushAndShift(){
>     	var queue = new Array();
>     	queue.push("first"); # first 넣어줌
>     	queue.push("third"); # third 넣어줌
>     	alert(queue);	#출력 first,third
>     	var a = queue.shift(); #맨앞의 first 빠짐
>     	alert(a);	#first 확인
>     	alert(queue);	#third 남음
>     	queue.push('4th');	#4th 넣어줌
>     	alert(queue);	#third,4th 출력
>     	var b = queue.pop();	#4th빼줌
>     	alert(b);	#빠진게 4th 맞는지 확인
>     	alert(queue);	#third 출력
>     }
>     ```
>
> * slice
>
>   * 배열의 부분을 가지고 새로운 배열 생성
>
>   * ```
>     function sliceTest(){
>     	var arr01 = new Array(1,2,3,4,5,6,7);
>     	var slice01 = arr01.slice(1,3);
>     }
>     ```
>
>   * 인덱스 (시작,끝-1) 로 잘라서 가져올수 있다

## popup

> open(경로,이름,옵션)
>
> ```
> function popupTest(){
> 	window.open("위치","이름","width=300px,height=300px");
> }
> ```

## window

> * 팝업창 만들기
>
>   * ```
>     function openWin() {
>     	var url = "위치";
>     	var title = "이름";
>     	var prop = "top=200px,left=600px,width=500px,height=500px";
>     	window.open(url, title, prop); 
>     }
>     ```
>
>   * 위치의 내용
>
>     * ```
>       function test(){
>       	var val=document.getElementsByName("test")[0].value;
>       	opener.document.getElementsByTagName("h1")[1].innerHTML=val;
>       	close();
>       }
>       ```
>
>     * ```
>       <input type="text" name="test"/>
>       <input type="button" onclick="test()" value="전달"/>
>       ```
>
>   * ```
>     <h1>팝업창 만들기</h1>// 인덱스 값 1임
>     <button onclick="openWin()" name="btn">창열기</button>
>     ```
>
>     ```
>     <iframe name="이름"></iframe> //문서안의 새로운 문서,새로운 영역
>     ```
>
>     1. 클릭시 openWin 함수를 호출한다
>     2. openWin에 정의된 속성값에 맞게 위치에 있는 내용을 불러온다 (이름부분에)
>     3. 위치에 있는 함수에서 text를 입력할수 있다. 
>     4. 전달 버튼을 누를시 opener 즉 원래 있던곳인 body의 <h1>의 인덱스값 1부분에 내용이 입력된다
>
> * 회원가입
>
>   * ```
>     <h1>회원가입하기(div팝업창)</h1>
>     <button onclick="registForm()" name="btn">회원가입</button>
>     ```
>
>     1. 회원 가입을 누를시 registform 함수가 실행됩니다
>
>   * ```
>     function registForm() {
>     	document.getElementById("regist").style.display = "block";
>     	document.body.style.background = "gray";
>                                             
>     	var btns = document.getElementsByName("btn");
>     	for ( var i in btns) {				
>     	btns[i].disabled = "disabled";
>     	}
>     }
>     ```
>
>     1. Id값 regist를 불러오고 뒤에는 색상 회색으로 지정해줍니다
>     2. 향상된 for 문을 사용하여 내용들을 불러옵니다. 내용에는 속성값 인덱스 전부 들어있습니다
>     3. disabled를 사용해서 작동을 못하게 만들어줍니다
>
>   * ```
>     <div id="regist">
>     	<form>
>     		<table>
>     		<caption>회원가입</caption>
>     		<tr>
>     			<td>아이디</td>
>     			<td><input type="text" name="id" onclick="idchk()" readonly="readonly" /> 
>     				<input type="button" value="중복체크" onclick="idCheck()" /></td></tr>
>     		<tr>
>     			<td>패스워드</td>
>     			<td><input type="password" name="pwd" style="color: red;"/></td>
>     		</tr>
>     		<tr>
>     			<td colspan="2" align="center"><input type="button" value="확인" onclick="closeWin()" /></td>
>     		</tr>
>     		</table>
>     	</form>
>     </div>
>     ```
>
>     1. 아이디 input은 text타입의 읽기 전용입니다. 그래서 누를시 idchk함수로 넘어갑니다
>     2. 중복체크를 누를시 idchek함수로 넘어가는 버튼을 만들었습니다
>     3. 패스워드는 타입 패스워드라서 입력시 가려줍니다 색상은 붉은색으로 입력됩니다
>     4. 위치는 센터이며 확인 버튼을 누를시 closeWin함수가 실행됩니다.
>
>   * ```
>     function closeWin() {
>     	document.getElementById("regist").style.display = "none";
>     	document.body.style.background = "white";
>                                             
>     	var btns = document.getElementsByName("btn");
>     	for ( var i in btns) {
>     	btns[i].disabled = "";
>     	}
>     }
>     ```
>
>     1. 실행된 regist를 none으로 만듭니다.
>     2. 백그라운드를 다시 흰색으로 돌립니다
>     3. disabled로 사용을 막은것들을 다시 되돌립니다 
>
>   * ```
>     function idchk() {
>     	alert("중복체크를 확인하세요");
>     }
>     ```
>
>     1. 팝업창에 중복체크를 확인하세요 가 나옵니다.
>
>   * ```
>     function idCheck() {
>     	open("위치", "", "width=300px,height=300px");
>     }
>     ```
>
>     1. 위치의 내용을 불러옵니다.
>     2. 불러올때 속성으로 가로 300px 높이 300px로 불러옵니다
>
>   * ```
>     <table>
>     	<tr>
>     		<td>아이디</td>
>     		<td><input type="text" name="id"/></td>
>     	</tr>
>     	<tr>
>     		<td colspan="2">
>     			<input type="button" value="중복확인" onclick="confirmChk()"/>
>     			<input type="button" value="취소" onclick="self.close()"/>
>     		</td>
>     	</tr>
>     </table>
>     <div></div>
>     ```
>
>     1. text타입에 name은 id입니다
>     2. 중복확인을 누를시 confirmChk를 불러옵니다
>     3. 취소를 누를시 닫기는 함수입니다
>
>   * ```
>     var ids=["java","script"];
>                                             
>     function confirmChk(){
>     	var id=document.getElementsByName("id")[0].value;
>     	var div=document.getElementsByTagName("div")[0];
>     	if(ids.indexOf(id)!=-1){
>     		div.innerHTML="<b>아이디가 존재합니다.</b>";
>     	}else{
>     		var userId="사용할 수 있는 아이디입니다."
>     			+"<input type='button' value='확인'"
>     			+"onclick='insertId(\""+id+"\")'>"; //escape 시퀀스
>     		div.innerHTML=userId;          
>     	}
>     }
>     ```
>
>     1. 전역 변수로 ids 배열안에는 "java","script" 두개가 있습니다. 중복 아이디인지 확인용입니다.
>
>     2. 변수 id에 text로 입력했던 name id 값을 가져옵니다.
>
>     3. 변수 div에 div를 가져옵니다.
>
>     4. if문을 사용하여 전역 변수 ids배열에 가져온 id값이 있는지 확인합니다. 인덱스는 없을시 -1을 반환함
>
>        1. -1이외의 값일시 변수 div를 가져온 위치에 "아이디가 존재합니다" 출력
>
>     5. else일시 변수 userid에 "사용할 수 있는 아이디입니다 "
>
>        1. 새로운 input을 생성합니다. "확인" 버튼
>
>        2. 누를시 insertId함수에 "id" 를 넣어서 실행합니다. 
>
>        3. id는 변수가 아닌 문자열 형태 그대로 가져갑니다. *Escape Sequences*
>
>           ***Escape Sequences***란 프로그래밍 언어 특성상 표현할 수 없는 기능, 문자를 표현
>
>        4. 변수 div를 가져온곳에 userId의 내용을 출력합니다
>
>   * ```
>     function insertId(id){
>     	opener.document.getElementsByName("id")[0].value=id; 
>     	opener.document.getElementsByName("pwd")[0].focus();
>     	close(); 
>     }
>     ```
>
>     1. 창을 열었던곳의 네임 id(아이디에 readonly부분의 네임입니다) 에 값을 가져가줍니다. 내용은 문자열 "id" 의 값입니다
>     2. 창을 열었던곳 밑에 패스워드 칸에 초점을 둡니다. 네임은 pwd였습니다.
>     3. 그리고 현재 창을 닫습니다. 

## location

> * location.href
>
>   * ```
>     location.href="http://www.naver.com";
>     ```
>
>   * 지정한 경로로 이동합니다. 새로운 창이며 뒤로가기를 누를시 현재위치로 돌아옵니다
>
> * location.assign
>
>   * ```
>     location.assign("http://www.google.com")
>     ```
>
>   * 지정한 경로로 이동합니다.새로운 창이며 뒤로가기를 누를시 현재위치로 돌아옵니다
>
> * location.replace
>
>   * ```
>     location.replace("http://www.naver.com")
>     ```
>
>   * 지정한 경로로 이동합니다. 현재 창을 덮어쓰기 때문에 뒤로가기를 누를시 돌이킬수 없습니다.
>
> * location.reload()
>
>   * ```
>     location.reload()
>     ```
>
>   * 새로고침입니다.

## check

> 체크박스 속성 사용법입니다 
>
> * **스타일 지정입니다**
>
> ```
> #colorbox{
> 	width: 320px;
> 	height: 320px;
> 	position: relative;
> }
> #red, #green, #blue, #magenta{
> 	width: 150px;
> 	height: 150px;
> 	border: 1px solid black;
> 	position: absolute;
> }
> #green{
> 	left: 160px;
> }
> #blue{
> 	top: 160px;
> }
> #magenta{
> 	left: 160px;
> 	top: 160px;
> }
> ```
>
> 1. colorbox기본틀은 가로 320px 세로 320px 부모틀입니다
> 2. 빨강 그린 블루 진홍 가로 150px 세로 150px입니다 굵기는 1px고 위치는 부모의 기준에서 입니다
> 3. 그린은 왼쪽에서 160px 떨어진곳입니다
> 4. 파랑은 위에서 160px 떨어진곳입니다
> 5. 진홍은 왼쪽과 위에서 160 떨어진곳입니다.
> 6. 남은 레드는 처음부분입니다.
>
> * **체크박스 생성 밑 id,이름, 내용을 지정해줍니다**
>
> ```
> <div id="colorbox">
> 	<div id="red">red</div>
> 	<div id="green">green</div>
> 	<div id="blue">blue</div>
> 	<div id="magenta">magenta</div>
> </div>
> <div id="base">
> 	<from>
> 		<input type="checkbox" name="all" onclick="allCheck(this.checked);"/>전체 선택<br/>
> 
> 		<input type="checkbox" name="chk" value="red"/>빨강<br/>
> 		<input type="checkbox" name="chk" value="green"/>초록<br/>
> 		<input type="checkbox" name="chk" value="blue"/>파랑<br/>
> 		<input type="checkbox" name="chk" value="magenta"/>진홍<br/>
> 
> 		<input type="button" value="선택" onclick="selectColor();"/>
> 		<input type="button" value="취소" onclick="clearDiv();"/>
>  	</from>
>  </div>
> ```
>
> 1. 각 색깔별로 id값을 지정해줍니다.
> 2. 체크박스 속성으로 "전체 선택", " 빨강", "초록", "파랑", "진홍"  총5개를 만듭니다
> 3. "선택" 을 누를 시 selectColor 함수가 실행되는 버튼을 만듭니다.
> 4. "취소"를 누를 시 clearDiv 함수가 실행되는 버튼을 만듭니다.
>
> * **체크박스에서 체크 후 or 전 선택시 실행되는 함수입니다.**
>
> ```
> function selectColor(){
> 	var chks = document.getElementsByName("chk");
> 
> 	for (var i=0; i < chks.length;i++) {
> 		if (chks[i].checked) {
> 		document.getElementById(chks[i].value).style.backgroundColor = chks[i].value;
> 		} else {
> 		document.getElementById(chks[i].value).style.backgroundColor = '';
> 		}
> 	}
> }
> ```
>
> 1. 변수에 chk를 받아옵니다.
> 2. for문으로 길이만큼 확인합니다. 무엇을?
> 3. if로 chks의 인덱스 값에 체크가 되어있다면 색상을 chks[i]의 내용으로 지정해줍니다
> 4. else 는 색상 없습니다.
>
> * **전체 선택시 함수입니다**
>
> ```
> function allCheck(bool){
> 	var chks = document.getElementsByName("chk");
> 
> 	for (var i =0; i< chks.length; i++){
> 	chks[i].checked = bool;
> 	}
> }
> ```
>
> 1. allcheck(bool)의 bool 은 변수입니다 
> 2. 변수 chks에 이름 chk를 받아옵니다.
> 3. for문을 사용해서 전부 체크값을 true or false로 바꿔줍니다. 이건 논리 맞습니다
>
> * **취소 함수입니다**
>
> ```
> function clearDiv(){
> 	allCheck(false);
> 
> 	var colorbox = document.querySelectorAll("#colorbox>div");
> 	for (var i=0;i<colorbox.length;i++) {
> 	colorbox[i].style.backgroundColor = "";
> 	}
> }
> ```
>
> 1. allCheck 함수를 false 값으로 불러줍니다.
> 2. 변수 colorbox에 selectorAll에 colorbox>div 를 넣어 가져옵니다. 자식
> 3. for문에 colorbox의 길이를 넣고 길이만큼 colorbox[i]인덱스에 none으로 바꿔줍니다.

## dom

> * 그림 넘기기
>
>   * 스타일 지정
>
>   * ```
>     <style>
>     	a>img{width:50px; height: 50px;}
>     	#gallery{width: 200px; height: 200px;}
>     	p{width: 350px; height: 250px;}
>     	img{vertical-align: middle;}
>     	a{text-decoration: none;}
>     </style>
>     ```
>
>     * 크기와 높기 위치를 지정해줍니다
>
>   * 바디
>
>   * ```
>     <div id="gallerywrap">
>     	<p>
>     		<a href="http://www.naver.com" onclick="return prevGallery();">
>     			<img src="resources/imgs/arrowleft.png" alt="왼쪽화살표" />
>     		</a>
>                                         
>     		<img id="gallery" src="resources/imgs/img01.png" alt="gallery">
>                                         
>     		<a href="#next" onclick="nextGallery();">
>     		<img src="resources/imgs/arrowright.png" alt="오른화살표" />
>     		</a>
>     	</p>
>     </div>
>     ```
>
>     * 클릭시 prevGallery함수값을 return 받습니다.
>       * 왼쪽 화살표 이미지입니다  주소값입니다
>     * 가운데 출력될 이미지 입니다
>     * 클릭시 nextGallery함수가 실행됩니다.
>       * 오른쪽 화살표 이미지입니다 주소값입니다
>
>   * 함수
>
>   * ```
>     var num =1;
>                                         
>     function prevGallery(){
>     	num--;
>     	if (num <1) {
>     	num = 6;    
>     	}
>     	document.getElementById("gallery").src = "resources/imgs/img0"+num+".png";
>                                         
>     	return false; 
>     }
>     ```
>
>     * num--는 num = num-1과 같습니다 클릭시 전역변수 num의 값이 바뀝니다.
>     * if문으로 num이 0이 될시 자신의 마지막 사진의 번호로 바뀌게 지정해줍니다.
>     * id의 값 gallery에 출력될 이미지를 img num .png 파일로 바뀌게 해줍니다.
>     * return을 false로 하여 값의 반환을 막습니다 다음 이벤트인 www.naver.com을 막힙니다.(요거 써보려고 넣음)
>
>   * ```
>     function nextGallery(){
>     	num++;
>     	if (num >6) {
>     	num = 1;    
>     	}
>     	document.getElementById("gallery").src = "resources/imgs/img0"+num+".png";
>                                         
>     	return 
>     }
>     ```
>
>   * 클릭시 전역변수 num값이 1씩 더해집니다
>
>   * 마찬가지로 id의 값 gallery에 출력될 이미지를 img num .png 파일로 바뀌게 해줍니다.

## nodelist

> * 부모 node, 자식 node 탐색
>
>   * ```
>     <h1>부모탐색,자식탐색</h1>
>     <div>
>     	<p>child01</p>
>     	<p>child02</p>
>     	<p>child03</p>
>     </div>
>                                         
>     <button onclick="searchPar();">부모탐색</button>
>     <br/>
>     <button onclick="searchChi();">자식탐색</button>
>     ```
>
>   * 부모 탐색 함수
>
>     * ```
>       function searchPar(){
>       	var child02 = document.getElementsByTagName("p")[1];
>       	var div = child02.parentNode;
>       	alert(div);
>       	alert(typeof(div));
>       	alert(div.nodeName);
>       	div.style.backgroundColor="violet";
>       }
>       ```
>
>       * p의 인덱스 1번을 변수 child02에 지정합니다
>       * 변수 div = child02의 부모노드로 지정합니다.
>       * objectHTMLDivElement 출력
>       * 타입 object
>       * node네임은 DIV
>       * div위치에 색상 violet으로 바꿔줬습니다
>
>   * 자식 탐색 함수
>
>     * ```
>       function searchChi() {
>       	var div = document.getElementsByTagName("div")[0];
>                                                             
>       	var divChildren = div.childNodes;
>       	for (var i = 0;i<divChildren.length;i++){
>       		console.log(divChildren[i].nodeName);
>       	}
>       }
>       ```
>
>       * 변수 div는 div인덱스 0번째입니다
>       * 변수 divChildren은 div자식노드들입니다
>       * 콘솔에 자식노드들이 전부 나옵니다.
>       * 자식노드들에는 공백도 포함되어있어 전체 길이는 7입니다. 

## elementCreate

> * 엘리먼트 객체 생성
>
>   * ```
>     createElement("tagname")
>     ```
>
>   * ```
>     function elementCreate(){
>     	var div = document.createElement("div");        
>                     
>     	var attr = document.createAttribute("style");      
>     	attr.nodeValue = "border:2px solid blue";             
>     	div.setAttributeNode(attr);  
>     }
>     ```
>
>     1.  변수인 div에 div를 만듭니다.
>     2. 변수 attr에 빈 스타일을 만들어줍니다
>     3. 빈스타일에 색상과 속성을 지정해줍니다
>     4. 처음 지정한 div에 만들어진 스타일을 주어 생성합니다.
>
> * txt객체 생성
>
>   * ```
>     createTextNode("txt")
>     ```
>
>   * ```
>     function elementCreate(){
>     	var div = document.createElement("div");  
>     	div.setAttribute("style","border:2px solid red;")
>                     
>     	var txt = document.createTextNode("엘리먼트 생성!!");
>     	div.appendChild(txt); 
>     	document.body.appendChild(div);
>     }
>     ```
>
>     1. 변수 div에 새로운 div 생성
>     2. 생성한 div에 속성값을 줍니다
>     3. 변수 txt에 내용을 입력하여 만들어줍니다
>     4. 변수 div에 txt내용을 넣습니다.
>     5. body의 끝부분에 div의 내용을 넣어줍니다.
>
> * 객체의 속성
>
>   * ```
>     createAttribute("attributename")
>     ```
>
>   * ```
>     setAttributeNode(attribute 객체)
>     ```
>
>   * ```
>     setAttribute("attributename", "attributevalue")
>     ```

## imagine

> 이미지 생성과 삭제
>
> * 스타일
>
>   * ```
>     <style>
>     	img, #imgview{
>     	width: 300px;
>     	height: 300px;
>     	}
>     </style>
>     ```
>
>     1. 이미지 크기와 불러올 장소의 크기를 지정해줍니다
>
>
> * 함수 호출 버튼과 선택
>
>   * ```
>     <body>   
>       <input type="radio" name="rdobtn" value="img01.png"/>img01<br/>
>       <input type="radio" name="rdobtn" value="img02.png"/>img02<br/>
>       <input type="radio" name="rdobtn" value="img03.png"/>img03<br/>
>             
>       <button onclick="createImg();">이미지 생성</button>
>       <button onclick="deleteImg();">이미지 삭제</button>
>             
>       <div id="imgview"><img src="" /></div>
>     </body>
>     ```
>
>     1. 라디오 입력으로 1개의 값만 선택할수 있습니다.
>
>     2. 이미지 생성 함수 호출 버튼입니다
>
>     3. 이미지 삭제 함수 호출 버튼입니다
>
>     4. div 이미지를 받을 위치입니다.
>   
> * 이미지 생성 함수입니다
>
>   * ```
>     function createImg(){
>     	var radios = document.getElementsByName("rdobtn");
>             
>     	var radioVal=""; 
>     	for (var i=0; i< radios.length;i++) {
>     		if (radios[i].checked) {
>     			radioVal = "resources/imgs/" + radios[i].value;
>     		}
>     	}
>             
>     	var img = document.createElement("img");
>     	img.setAttribute("src",radioVal);
>             
>     	var div = document.getElementById("imgview");
>     	var chd = document.querySelector("#imgview > img");
>     	div.replaceChild(img,chd);
>     }
>     ```
>     
>     1. name이 rdobtn인 요소들을 변수 radios에 가지고 옵니다 
>     2. 빈 변수 radioVal을 만들어 줍니다
>     3. for문을 사용하여 raidios의 인덱스 값에 체크가 있는곳을 확인합니다.
>     4. 체크되있는곳을 찾았다면 변수 radioVal에 "이미지주소" + 체크된 곳 raidos의 value값을 가져옵니다
>     5. 변수 img에 새로운 img를 생성해줍니다
>     6. 이미지에 주소를 radioVal로 설정해 줍니다.
>     7. 변수 div의 id에 imgview를 저장해줍니다.
>     8. 변수 chd에 #imgview에 img가 자식속성으로 선택되어 들어갑니다.
>     9. div에 속성이 지정된 img와 chd가 바뀐상태로 나옵니다.
>   
> * 이미지 삭제 함수입니다.
>
>
>   * ```
>     function deleteImg(){
>     	document.querySelector("#imgview > img").src = "";
>     }
>     ```
>
>     1. imgview의 img에 none값을 줍니다.
>
>   * ```
>     document.getElementById("imgview").innerHTML= "<img src=''/>";
>     ```
>
>     1. 다른 방법입니다. 함수에 넣으면 똑같이 실행됩니다.
>
> 

## tag

> * body입니다
>
> * ```
>   <body>
>               
>       <h1>태그 추가하기</h1>
>           
>       <button onclick="addAppend();">appendChild()</button>
>       <button onclick="addInsert();">insertBefore()</button>
>       <button onclick="moveElement();">element 이동</button>
>           
>       <fieldset id="addele">
>           <legend>부모태그</legend>
>           <div>div</div>
>       </fieldset>
>   </body>
>   ```
>
>   1. 각 함수를 호출할 버튼을 생성하였습니다.
>   2. 부모태그로 쓸것을 표시하여두었습니다.
>
> * appendChild()
>
>   * ```
>     <button onclick="addAppend();">appendChild()</button>
>     ```
>
>   * ```
>     function addAppend() {
>     	var fieldset = document.getElementById("addele");
>     	var p = document.createElement("p");
>             
>     	p.textContent = "자식 태그들 중 가장 마지막에 넣어진다.";
>             
>     	fieldset.appendChild(p);
>     }
>     ```
>
>     1. 변수 fieldset에 id addele를 저장합니다
>     2. 변수 p에 새로운 p를 생성합니다.
>     3. p의 내용으로 "자식 태그들 중 가장 마지막에 넣어진다"  를 넣어줍니다.
>     4. 변수 fieldset(위치 addele)에 마지막 부분에 p를 추가해줍니다 .div뒷부분입니다.
>
> * insertBefore() 
>
>   * ```
>     <button onclick="addInsert();">insertBefore()</button>
>     ```
>
>   * ```
>     function addInsert(){
>     	var newP = document.createElement("p");
>     	var fieldset = document.getElementById("addele");
>             
>     	newP.textContent = "엘리먼트의 앞에 넣어진다." + (count++);
>             
>     	var oldDiv = document.querySelector("fieldset > div");
>     	fieldset.insertBefore(newP,oldDiv);
>     }
>     ```
>
>     1. 변수 newP에 새로운 p를 생성합니다.
>     2. 변수 fieldset에 id addele를 가져옵니다.
>     3. newP의 내용으로 "엘리먼트의 앞에 넣어진다 "내용이 들어가고 count++를 줍니다.
>     4. 변수 oldDiv에 fieldset의 자식으로 div를 지정해줍니다.
>     5. 변수 fieldset(addele)의 위치 div전에 oldDiv의 내용이 카운트되며 위에서부터 1,2,3,...으로 추가됩니다. 
>
> * element 이동
>
>   * ```
>     <button onclick="moveElement();">element 이동</button>
>     ```
>
>   * ```
>     function moveElement(){
>     	var moveEle = document.querySelector("fieldset").children[1];
>     	var addEle = document.body;
>     	addEle.appendChild(moveEle);
>                     
>     }
>     ```
>
>     1. 변수 moveEle에 fieldset의 인덱스 1번값을 지정합니다.
>     2. 변수 addEle에 body를 지정합니다.
>     3. addEle(body)의 뒤에 fieldset 인덱스 1번값을 추가합니다.

## ex)createCell

> * body 부분입니다.
>
>   * ````
>     <body>
>   
>         <form>
>             <table id="intable">
>                 <tr>
>                     <td>아이디</td>
>                     <td><input type="text" name="id" /></td>
>                 </tr>
>                 <tr>
>                     <td>비밀번호</td>
>                     <td><input type="text" name="pw"/></td>
>                 </tr>
>                 <tr>
>                     <td>주소</td>
>                     <td><input type="text" name="addr"/></td>
>                 </tr>
>                 <tr>
>                     <td>전화번호</td>
>                     <td><input type="text" name="phone"/></td>
>                 </tr>
>             </table>
>             <input type="button" value="추가" onclick="tableVal();"/>
>             <input type="button" value="삭제" onclick="deleteAll();"/>
>         </form>
>     ````
>
>     1. input타입으로 입력할수 있게 만들며 name은 id로 지정해줍니다.
>     2. 마찬가지로 비밀번호,주소,전화번호 각각 name을 지정해줍니다.
>     3. "추가" 버튼입니다. 누를시 tableVal 함수가 실행됩니다.
>     4. "삭제" 버튼입니다. 누를시 deleteAll함수가 실행됩니다. 
>
>   * ```
>         <div id = "addtable">
>             <table border="1" id="ctb">
>                 <col width="100px" />
>                 <col width="100px" />
>                 <col width="300px" />
>                 <col width="200px" />
>                 <col width="100px" />
>                 <thead>
>                     <tr>
>                         <th>아이디</th>
>                         <th>비밀번호</th>
>                         <th>주소</th>
>                         <th>전화번호</th>
>                         <th>삭제</th>
>                     </tr>
>                 </thead>
>                 <tbody id="addtr"></tbody>
>             </table>
>         </div>
>     </body>
>     ```
>
>     1. 아이디부터 차례대로 가로 100,100 300,200,100크기의 열을 생성합니다.
>     2. tbody의 id는 addtr입니다. 이곳에 새로운 각열의 내용에 맞는 새로운 행을 추가할겁니다.
>
> * tableVal함수입니다
>
>   * ```
>     function tableVal(){
>     	var doc = document.forms[0];
>     	var vals = [doc.id.value, doc.pw.value, doc.addr.value, doc.phone.value]
>     
>     	for (var i=0; i < vals.length;i++) {
>     	if(vals[i] == null || vals[i] =="" || vals[i] == undefined){
>     		alert("제대로 입력했는지 다시 한번 확인해주세요!");
>     		return;
>     		}
>     	}
>     
>     	document.getElementById("addtr").appendChild(createRow(vals));
>     }
>     ```
>
>     1. 변수 doc에 form인덱스 0번째를 지정해줍니다.
>
>     2. 변수 vals에 form[0]에서 입력했던 아이디(id),비밀번호(pw),주소(addr),전화번호(phone)의 내용을 받아옵니다.
>
>     3. for문을 사용하여 vals의 내용중 null이 있는지 빈칸이 있는지 값을 찾을수 없는지 유효성을 검사합니다.
>
>        *1개라도 검사에 적합하지 않을시 "제대로 입력했는지 다시 한번 확인해주세요!"를 출력*
>   
>     4. id가 addtr인것을 불러오고 그 뒤에 추가합니다.createRow함수의 내용을 ✅
>   
> * createRow함수입니다
>
>   * ```
>     function createRow(vals){
>     	var tr = document.createElement("tr");
>     
>     	for (var i = 0; i < vals.length; i++){
>     		var td = document.createElement("td");
>     		td.textContent = vals[i];
>     		tr.appendChild(td)
>     	}
>     
>     	var deleteTd=document.createElement("td");
>     	deleteTd.innerHTML = "<input type='button' value='삭제' onclick ='delRow(this)'>";
>     	tr.appendChild(deleteTd);
>     	return tr;
>     }
>     ```
>
>     1. 변수 tr에 tr을 새롭개 만들어 줍니다.
>     2. for문을 사용하여 전의 함수 tableVal에서 가져온 vals의 길이만큼 반복합니다.
>     3. 반복하는 동안 변수 td에 새로운 td를 만들고 그 안에 vals의 인덱스에 있는값을 넣습니다.
>     4. 변수 tr(새 tr)의 위치에 td의 내용들이 추가됩니다.  (아이디,비밀번호,주소,전화번호)
>     5. 변수 deleteTd에 새로운 td를 추가해줍니다.
>     6. deleteTd는 "삭제" 버튼형식으로  누를시 delRow함수☢가 실행됩니다.
>     7. tr에 새로운td(deleteTd)를 마지막부분에 추가합니다
>     8. 방금까지 만들어진 새 tr과 그 속의 td내용들이 ✅에 전부 들어갑니다.
>
>
> * delRow함수입니다
>
>   * ```
>     function delRow(ele){
>     
>     	var delTr = ele.parentNode.parentNode;
>     	var tbody = document.getElementById("addtr");	
>     	tbody.removeChild(delTr);
>     }
>     ```
>
>     1. 변수 delTr에 이것("삭제"버튼)의 부모(td)의 부모(tr)를 지정해줍니다
>     2. 변수 tbody에 id addtr을 받아옵니다.
>     3. 변수 tbody(addtr)에서 현재 받아온 delTr을 지워줍니다.
>
> * deleteAll함수입니다.
>
>   * ```
>             function deleteAll(){
>                 var tbody = document.getElementById("addtr");
>     
>                 while(tbody.hasChildNodes()){
>                     tbody.removeChild(tbody.lastChild);
>                 }
>             }
>     ```
>
>     1. 변수 tbody 에 id addtr을 받아옵니다.
>     2. while문으로 tbody(addtr)의 자식노드(tr)들을 선택해줍니다.
>     3. tbody(addtr)의 마지막 자식(tr)부터 차례대로 지워줍니다. 전부 사라질때까지


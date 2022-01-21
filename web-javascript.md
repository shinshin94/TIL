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
>     

 
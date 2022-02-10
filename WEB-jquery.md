# WEB-jquery

> ​      jquery 기본 작성법!
>
> * 불러오기 
>   * `<script src="resources/js/jquery-3.6.0.min.js"></script>`
>   * `<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>`
>
> * selector 표현식
>
> ​      `jQuery("selector").method();` -> `$("selector").method();`
>
> ​      `$("p").css("color","red");`
>
> *  기능 구현!!!
>
> ​      `onload=function(){  }` ->  `$(function(){   });`
>
> ​	      `$(document).ready(function(){   });`
>
> 

## basic

> * 이미지 숨기기
>
>   * ```
>     <button id="test-btn">click me</button>
>     <div>
>     	<img src="resources/imgs/img01.png" alt="img01"/>
>     </div>
>     ```
>
>   * ```
>     $(function(){
>     	$("#test-btn").click(function(){
>     		alert("클릭했음!!");
>     	});
>               
>     	$("img").click(function(){
>     		$(this).hide();
>     	});
>     });
>     ```
>
>     1. "click me"를 누를시 "클릭했음"을 띄우는 버튼의 함수입니다.
>     2.  img를 클릭시 누른것을 숨기는 함수입니다.
>
> * 이미지 보이기
>
>   * ```
>     <button onclick="showImg();">이미지 보이기</button>
>     ```
>
>   * ```
>     function showImg(){
>     	$("img").show();
>     }
>     ```
>
>     1. 버튼을 누르면 감춰진 이미지가 나오는 함수입니다.
>
> * 이미지 축소
>
>   * ```
>     <button onclick="resizeImg();">이미지 축소</button>
>     ```
>
>   * ```
>     function resizeImg(){
>     	$("img").css({"width":"100px","height":"100px"});
>     }
>     ```
>
>   * ```
>     function resizeImg(){
>     	$("img").css("width","100px").css("height","100px");
>     }
>     ```
>
>     1. 버튼을 누르면 가로 100px, 높이 100px로 이미지 크기가 변경됩니다.
>     2. 두가지 형태로 쓸수 있습니다.
>
> * 이미지 추가
>
>   * ```
>     <button onclick="addImg();">이미지 추가</button>
>     ```
>
>   * ```
>     function addImg(){
>     	$("img").last().after("<img src='위치/img01.png'/>");
>     }
>     ```
>
>     1. 버튼을 누를시 이미지를 새로 추가합니다.
>
> * 이미지 숨기기/보이기
>
>   * ```
>     <button onclick="toggleImg();">이미지 숨기기/보이기</button>
>     ```
>
>   * ```
>     function toggleImg(){
>     	$("img").toggle();
>     }
>     ```
>
>     1. 버튼을 누르면 이미지를 숨기고 다시 누르면 나타나는 함수입니다.

## selector

> * 태그 선택
>
>   * ```
>     <button onclick="selector01();">태그 선택</button>
>     ```
>
>   * ```
>     function selector01(){
>     	$("span").css("color","red");
>     	$("#view").text('$("span").css("color","red");');
>     }
>     ```
>
>     1. "태그 선택" 버튼을 누를시 실행되는 함수입니다.
>     2. span에 해당하는것에 빨강 색상을 줍니다.
>     3. #view부분에 텍스트로 '$("span").css("color","red");' 이 출력됩니다.
>
>   * ```
>     <ul>
>     	<li><span>tag로 선택</span></li>
>     	<li id="t1">id로 선택</li>
>     	<li class="t2">class로 선택</li>
>     	<li><span>parent child로 선택</span></li>
>     	<li><b><span>parent &gt; child</span></b>로 선택</li>
>     	<li>:nth-child(n/odd/even)로 선택</li>
>     	<li>:first-child로 선택</li>
>     	<li>:last-child로 선택</li>
>     </ul>
>     <div id="view"></div>
>     ```
>
>     * 색상 변경 적용 되는것들
>       * tag로 선택
>       * parent child로 선택
>       * parent &gt; child
>
> * id선택(t1)
>
>   * ```
>     <button onclick="selector02();">id선택(t1)</button>
>     ```
>
>   * ```
>     function selector02(){
>     	$("#t1").css("color","green");
>     	$('#view').text('$("#t1").css("color","green");');
>     }
>     ```
>     
>     1. "id 선택" 버튼을 누를시 실행되는 함수입니다.
>     2. t1에 해당하는것에 초록 색상을 줍니다.
>     3. #view부분에 텍스트로 '$("#t1").css("color","green");' 이 출력됩니다.
>     
>   * ```
>     <ul>
>     	<li><span>tag로 선택</span></li>
>     	<li id="t1">id로 선택</li>
>     	<li class="t2">class로 선택</li>
>     	<li><span>parent child로 선택</span></li>
>     	<li><b><span>parent &gt; child</span></b>로 선택</li>
>     	<li>:nth-child(n/odd/even)로 선택</li>
>     	<li>:first-child로 선택</li>
>     	<li>:last-child로 선택</li>
>     </ul>
>     <div id="view"></div>
>     ```
>   
>     * 색상 변경 적용 되는것들
>       * id로 선택
>   
> * class 선택(t2)
>
>   * ```
>     <button onclick="selector03();">class 선택(t2)</button>
>     ```
>
>   * ```
>     function selector03(){
>     	$(".t2").css("color","violet");
>     	$("view").text('$(".t2").css("color","violet");');
>     }
>     ```
>
>     1. "class 선택" 버튼을 누를시 실행되는 함수입니다.
>     2. t2에 해당하는것에 보라 색상을 줍니다.
>     3. #view부분에 텍스트로'$(".t2").css("color","violet");' 이 출력됩니다.
>
>   * ```
>     <ul>
>     	<li><span>tag로 선택</span></li>
>     	<li id="t1">id로 선택</li>
>     	<li class="t2">class로 선택</li>
>     	<li><span>parent child로 선택</span></li>
>     	<li><b><span>parent &gt; child</span></b>로 선택</li>
>     	<li>:nth-child(n/odd/even)로 선택</li>
>     	<li>:first-child로 선택</li>
>     	<li>:last-child로 선택</li>
>     </ul>
>     <div id="view"></div>
>     ```
>
>     * 색상 변경 적용 되는것들
>       * class로 선택
>
> * p c 선택
>
>   * ```
>     <button onclick="selector04();">p c 선택</button>
>     ```
>
>   * ```
>     function selector04(){
>     	$("li span").css("background-color","blue");
>     	$("#view").text('$("li span").css("background-color","blue");');
>     }
>     ```
>
>     1. "p c 선택" 버튼을 누를시 실행되는 함수입니다.
>     2. li span 에 해당하는것의 배경에 파랑 색상을 줍니다.
>     3. #view부분에 텍스트로'$("li span").css("background-color","blue");' 이 출력됩니다.
>
>   * ```
>     <ul>
>     	<li><span>tag로 선택</span></li>
>     	<li id="t1">id로 선택</li>
>     	<li class="t2">class로 선택</li>
>     	<li><span>parent child로 선택</span></li>
>     	<li><b><span>parent &gt; child</span></b>로 선택</li>
>     	<li>:nth-child(n/odd/even)로 선택</li>
>     	<li>:first-child로 선택</li>
>     	<li>:last-child로 선택</li>
>     </ul>
>     <div id="view"></div>
>     ```
>
>     * 색상 변경 적용 되는것들
>       * tag로 선택
>       * parent child로 선택
>       * parent &gt;  child
>
> * p &gt; c 선택
>
>   * ```
>     <button onclick="selector05();">p &gt; c 선택</button>
>     ```
>
>   * ```
>     function selector05(){
>     	$("li > span").css("color","yellow");
>     	$("#view").text('$("li > span").css("color","yellow");');
>     }
>     ```
>
>     1. "p &gt; c 선택" 버튼을 누를시 실행되는 함수입니다.
>     2. li > span 에 해당하는것에 노랑 색상을 줍니다.
>     3. #view부분에 텍스트로 '$("li > span").css("color","yellow");' 이 출력됩니다.
>
>   * ```
>     <ul>
>     	<li><span>tag로 선택</span></li>
>     	<li id="t1">id로 선택</li>
>     	<li class="t2">class로 선택</li>
>     	<li><span>parent child로 선택</span></li>
>     	<li><b><span>parent &gt; child</span></b>로 선택</li>
>     	<li>:nth-child(n/odd/even)로 선택</li>
>     	<li>:first-child로 선택</li>
>     	<li>:last-child로 선택</li>
>     </ul>
>     <div id="view"></div>
>     ```
>
>     * 색상 변경 적용 되는것들
>       * tag로 선택
>       * parent child로 선택
>       * ❌주의 parent &gt;  child 는 손자라서 선택되지 않는다❌
>
> * nth-child 선택
>
>   * ```
>     <button onclick="selector06();">nth-child 선택</button>
>     ```
>
>   * ```
>     function selector06(){
>     	$("li:nth-child(even)").css("background-color","yellow");
>     	$("#view").text('$("li:nth-child(6)").css("background-color","yellow");');
>     }
>     ```
>
>     1. "nth-child 선택" 버튼을 누를시 실행되는 함수입니다.
>     2. li:nth-child(even) 에 해당하는것의 배경에 노랑 색상을 줍니다.
>        * `even` 짝수  		`odd`홀수
>     3. li에 짝수번째가 선택됩니다.
>     4. #view부분에 텍스트로 '$("li:nth-child(6)").css("background-color","yellow");' 이 출력됩니다.
>
>   * ```
>     <ul>
>     	<li><span>tag로 선택</span></li>
>     	<li id="t1">id로 선택</li>
>     	<li class="t2">class로 선택</li>
>     	<li><span>parent child로 선택</span></li>
>     	<li><b><span>parent &gt; child</span></b>로 선택</li>
>     	<li>:nth-child(n/odd/even)로 선택</li>
>     	<li>:first-child로 선택</li>
>     	<li>:last-child로 선택</li>
>     </ul>
>     <div id="view"></div>
>     ```
>
>     * 색상 변경 적용 되는것들
>       * id로 선택
>       * parent child로 선택
>       * :nth-child(n/odd/even)로 선택
>       * :last-child로 선택
>
> * first-child 선택
>
>   * ```
>     <button onclick="selector07();">first-child 선택</button>
>     ```
>
>   * ```
>     function selector07(){
>     	$("li:first-child").css("background-color","yellowgreen");
>     	$("#view").text('$("li:first-child").css("background-color","yellowgreen");');
>     }
>     ```
>
>     1. "first-child 선택" 버튼을 누를시 실행되는 함수입니다.
>     2. li:first-child 에 해당하는것의 배경에 연노랑 색상을 줍니다.
>     3. li에 가장 첫번째 부분입니다.
>     4. #view부분에 텍스트로 '$("li:first-child").css("background-color","yellowgreen"이 출력됩니다.
>
>   * ```
>     <ul>
>     	<li><span>tag로 선택</span></li>
>     	<li id="t1">id로 선택</li>
>     	<li class="t2">class로 선택</li>
>     	<li><span>parent child로 선택</span></li>
>     	<li><b><span>parent &gt; child</span></b>로 선택</li>
>     	<li>:nth-child(n/odd/even)로 선택</li>
>     	<li>:first-child로 선택</li>
>     	<li>:last-child로 선택</li>
>     </ul>
>     <div id="view"></div>
>     ```
>
>     * 색상 변경 적용 되는것들
>       * tag로 선택
>
> * last-child 선택
>
>   * ```
>     <button onclick="selector08();">last-child 선택</button>
>     ```
>
>   * ```
>     function selector08(){
>     	$("li:last-child").css("color","orange");
>     	$("#view").text('$("li:last-child").css("color","orange");');
>     }
>     ```
>
>     1. "last-child 선택" 버튼을 누를시 실행되는 함수입니다.
>     2. li:last-child 에 해당하는것에 오렌지 색상을 줍니다.
>     3. li에 가장 마지막 부분입니다.
>     4. #view부분에 텍스트로 '$("li:last-child").css("color","orange");'이 출력됩니다.
>
>   * ```
>     <ul>
>     	<li><span>tag로 선택</span></li>
>     	<li id="t1">id로 선택</li>
>     	<li class="t2">class로 선택</li>
>     	<li><span>parent child로 선택</span></li>
>     	<li><b><span>parent &gt; child</span></b>로 선택</li>
>     	<li>:nth-child(n/odd/even)로 선택</li>
>     	<li>:first-child로 선택</li>
>     	<li>:last-child로 선택</li>
>     </ul>
>     <div id="view"></div>
>     ```
>
>     * 색상 변경 적용 되는것들
>       * :last-child로 선택
>
> * reset
>
>   * ```
>     <button onclick="cls();">reset</button>
>     ```
>
>   * ```
>     function cls(){
>     	$("*").css("color","black").css("background-color","");
>     	$("#view").text("")
>     }
>     ```
>
>     * "reset"을 누를시 전부 초기화 되는 버튼입니다.
>     * *로 전부 선택한후 색상을 black(디폴트 값),배경을 비어있게 지정합니다.
>     * view에도 비어있게 만듭니다.

## input

> *  input 박스입니다.
>
>   * ```
>     <input type="text" />
>     <br/>
>     <input type="button" value="선택" onclick="inputText();" />
>     ```
>
>   * ```
>     function inputText(){
>     	var txt = $("input:text").val();
>     	alert(txt);
>     }
>     ```
>
>     1. text를 입력하는 칸입니다. 다음줄에 "선택"을 누를시 inputext함수가 실행됩니다.
>     2. 변수 txt에 text에 입력한 내용을 받아옵니다 (val=value)
>     3. 입력한 내용을 창으로 띄웁니다.
>
> * 라디오박스입니다.
>
>   * ```
>     <input type="radio" value="radio val" onclick="inputRadio();"/>radio
>     <br/>
>     <div id="a"></div>
>     ```
>
>   * ```
>     function inputRadio(){
>     	var radioVal = $("input:radio").val();
>     	$("#a").html(radioVal);
>     }
>     ```
>
>     1. 라디오박스 형태로 체크할수 있습니다. 체크시 inputRadio함수가 실행됩니다.
>     2. 변수 radioVal에 radio에 입력된 내용을 받아옵니다.
>     3. id의a 에 받아온 radio의 내용을 출력합니다. (html=innerHtml)
>
> * 체크박스입니다.
>
>   * ```
>     <input type="checkbox" value="check val" onclick="inputCheck();"/>check
>     <br/>
>     <div id="a"></div>
>     ```
>
>   * ```
>     function inputCheck(){
>     	var checkVal = $("input:checkbox").val()
>     	$("#a").html(checkVal);
>     }
>     ```
>
>     1. 체크박스 형태로 체크할수 있습니다. 체크시 inputCheck함수가 실행됩니다.
>     2. 변수 checkVal에 checkbox에 입력된 내용을 받아옵니다.
>     3. id의 a 에 받아온 checkbox의 내용을 출력합니다. (html=innerHtml)
>
> * select박스입니다.
>
>   * ```
>     <select>
>     	<option value="one">1</option>
>     	<option value="two">2</option>
>     	<option value="three">3</option>
>     </select>
>     ```
>
>   * ```
>     $(function(){
>     	$("select").change(function(){
>     		var option = $("select > option:selected");
>     		alert(option.val());
>     		alert($("select>option").index(option));
>     	});
>     });
>     ```
>
>     1. 셀렉트 박스를 바디에 생성합니다.
>     2. 셀렉트 박스가 변할시 실행되는 함수입니다.
>     3. 변수 option 은 select의 자식으로 option에 선택된 것으로 받아옵니다.
>     4. 선택된것의 내용을 창에 띄웁니다.
>     5. 선택된것의 인덱스 값을 창에 띄웁니다

## checkbox✅

## element search

> * body입니다.
>
>   * ```
>     <pre>
>     	<b>eq() : 선택한 엘리먼트들 중에 인덱스로 탐색</b>
>     	<b>slice() : 선택한 엘리먼트들 중에 인덱스 길이로 탐색</b>
>     	<b>first() : 선택한 엘리먼트들 중에 첫번째 요소</b>
>     	<b>last() : 선택한 엘리먼트들 중에 마지막 요소</b>
>     </pre>
>           
>     <div>
>     	<p>eq()</p>
>     	<p>slice</p>
>     	<p>first()</p>
>     	<p>last()</p>
>     </div>
>     ```
>
>     * 센스있게 설명 적어두기
>
> * head 입니다.
>
>   * ```
>     $(function(){
>     	$("div>p").eq(0).click(function(){
>     		$("pre b").eq(0).toggle();
>     	});
>     ```
>
>     1. div의 자식으로 p를 선언하고 p의 0번째 인덱스를 클릭시 실행되는함수입니다.
>     2. pre속의 b의 인덱스 0번째를 숨기기/보이기 해줍니다.
>
>   * ```
>     	$("div > p").eq(1).click(function(){
>     		$("pre b").slice(1,2).toggle();
>     	});
>     ```
>
>     1. div의 자식으로 p를 선언하고 p의 1번째 인덱스를 클릭시 실행되는함수입니다.
>     2. pre속의 b의 인덱스중 1부터 2전까지를 숨기기/보이기 해줍니다.
>
>   * ```
>     	$("div > p").eq(2).click(function(){
>     		$("pre b").first().css("color","red").end().eq(2).toggle().end().last().text("진짜되네");
>     	});
>     ```
>
>     1. div의 자식으로 p를 선언하고 p의 2번째 인덱스를 클릭시 실행되는함수입니다.
>     2. pre속의 b의 인덱스 첫번째(0)에 빨강 색상을 지정해줍니다
>     3. b의 인덱스 2번째에는 숨기기/보이기를 해줍니다.
>     4. b의 마지막 인덱스에는 text "진짜되네"로 내용을 바꿔줍니다.
>
>   * ```
>     	$("div > p").eq(3).click(function(){
>     		$("pre b").last().css("background-color","skyblue");
>     	});
>     });
>     ```
>
>     1. div의 자식으로 p를 선언하고 p의 3번째 인덱스를 클릭시 실행되는함수입니다.
>     2. pre속의 b의 인덱스 마지막에 배경 색상을 하늘파랑으로 지정해줍니다.

## parent

> * body입니다
>
>   * ```
>     <pre>
>     	<b>find("selector") : 선택한 엘리먼트의 자손들 중에 탐색</b>
>     	<b>children("selector") : 선택한 엘리먼트의 자식들 중에 탐색</b>
>     	<b>parent() / parents("selector") : 선택한 엘리먼트의 부모 / 조상 탐색</b>
>     	<b>next("selector") : 선택한 엘리먼트 다음에 따라오는 요소 탐색</b>       
>     </pre>
>           
>     <div>
>     	<p><b>1</b></p>
>     	<p id="chd">2</p>
>     	<p>3</p>
>     	<p>4</p>
>     	<p>5</p>
>     </div>
>     ```
>
>     * 내용에 설명을 적어두었습니다.
>
> * head입니다.
>
>   * ```
>     <script>
>     	$(document).ready(function(){
>     		$("div").find("b").css({"font-size": "30px","color":"red"});
>     		$("div").children("#chd").text("2.children()");
>     		$("p > b").parent().css("background-color","hotpink");
>     		$("p > b").parents("div").css("background-color","yellow");
>     		$("p").eq(0).next().css("color","blue");
>     	})
>     </script>
>     ```
>
>     * div에서 b를 찾습니다.(find) 가장먼저 만난 b의폰트 사이즈를 30px로 색상을 빨강으로 바꿔줍니다 
>     * div의 자식 id chd를 찾아서 2.children() 으로 내용을 바꿔줍니다.
>     * p의 자식으로 b를 선언하고 가장 처음 부모(인덱스 0)의 색상을 핫핑크로 바꿔줍니다.
>     * p의 자식으로 b를 선언하고 div를 선택해주고 배경색상 노랑을 줍니다. (핫핑크는 우선연산이라 안바뀝니다.)
>     * p의 인덱스값 0번(eq(0))의 다음(next)값인 인덱스 1번의 색상을 파랑으로 바꿔줍니다. (2.children())

## add()

> * body입니다.
>
>   * ```
>     <div>
>     	<p>add()</p>
>     	<span>add():선택한 엘리먼트에 추가적으로 selector 표현식을 작성할 때 사용</span>
>     	<p>is()</p>
>     	<b>선택한 엘리먼트들 중에 구하는 엘리먼트가 있는지 확인할 때 사용</b>
>     </div>
>     ```
>
>     * 설명입니다.
>
> * head입니다
>
>   * ```
>     $(function(){
>     	$("p:eq(0)").add("span").css("color","red")
>                 
>     	$("div").children().click(function(){
>     		if($(this).prop("tagName")=="SPAN"){
>     			alert("span tag click!!!");
>     			$(this).css("color","aqua");
>     			//$(this).attr("title","abc");
>     			//$(this).prop("title","abc");
>     		}
>     		if($(this).is("p")){
>     			$(this).css("background-color","violet");
>     		}
>     	})
>     	$("b").click(function(){
>     		$("div").children().css("background-color","");
>     		$("p:eq(0)").add("span").css("color","red");
>     	})
>     });
>     ```
>
>     * p의 0번째 인덱스 그리고(add) span에 빨간 색상을 추가해줍니다 
>     * div의 자식중 클릭시 실행되는 함수입니다.
>     * 만약 누를것 tagName이 span일시 "span tag click!!!"을 띄웁니다.그리고 span을 파랑으로 바꿉니다.
>     * 만약 누를것중에 p가 있다면 누른것의 배경색상을 보라색으로 바꿉니다.
>     * b를 누르면 실행되는 함수입니다. div의 자식들의 배경색상을 비어있게 만들고 p의 0번째인덱스와 span의 색상을 빨강으로 바꿉니다.

## hover

>* body입니다.
>
>  * ```
>    <b>DOM 탐색 메서드</b>
>    <br/>
>    <div id="menu1" class="menu">
>    	<a href="#a">필터링 메서드</a>
>    	<div>.eq()</div>
>    	<div>.slice()</div>
>    	<div>.first()</div>
>    	<div>.last()</div>
>    	</div>
>             
>    <div id="menu2" class="menu">
>    	<a href="#b">트리 탐색 메서드</a>
>    	<div>.find()</div>
>    	<div>.children()</div>
>    	<div>.parent()</div>
>    	<div>.next()</div>
>    </div>
>             
>    <div id="menu3" class="menu">
>    	<a href="#c">탐색 메서드</a>
>    	<div>.add()</div>
>    	<div>.is()</div>
>    </div>
>    ```
>
>* head입니다.
>
>  * ```
>    $(function(){
>    	$(".menu div").css("display",'none');
>    	$(".menu").hover(function(){
>    	$(this).children("div").toggle();
>    	});
>    })
>    ```
>
>    1. menu 의 div 를 보이지 않게 none 으로 해주세요
>    2. menu의 위에 마우스를 올릴시(hover) 실행되는 함수입니다.
>    3. 지금 올린것의 자식들div를 보여주세요. (마우스를 내릴시 숨겨집니다.)
>
>  * ```
>    $(function(){
>    	$(".menu div").css("display",'none');
>    	$(".menu").hover(
>    		//handler in
>    		function(){
>    			$(this).children("div").show();
>    		},
>    		// handler out
>    		function(){
>    		$(this).children("div").hide();
>    		}
>    	)
>    })
>    ```
>
>    * 다른 방법입니다.

## event

> * 이벤트 전파 : 각요소가 서로 포함관계(중첩)인 경우 요소 중 하나에 이벤트가 발생하면
>
> ​            중첩된 요소들도 이벤트가 전파된다.
>
> * 이벤트 전파 막기
>
> ​        \- stopPropagation() :이벤트 요소의 전파 막기 / break와 같은 느낌입니다
>
> ​        \- preventDefault() : 이벤트에 의한 기본 동작 막기
>
> ​        \- return false : 위의 기능 두개 모두 적용
>
> * body입니다.
>
>   * ```
>     <span>unbind() : 이벤트 해제</span>
>     <div>
>     	<p>
>     		<a href="http://www.naver.com">클릭!</a>
>     	</p>
>     	<p>클릭</p>
>     </div>
>           
>     <div>
>     	<p>
>     		<a href="http://www.google.com">클릭!</a>
>     	</p>
>     	<p>클릭</p>
>     </div>
>     <button>요소 추가</button>
>     ```
>
> * head입니다.
>
>   * ```
>     $(function(){
>     	$("a:eq(0)").click(function(){
>     		alert("a 클릭!");
>     	});
>     	$("p").click(function(e){
>     		alert("p 클릭!");
>     		e.preventDefault();
>     	});
>     	$("div").click(function(){
>             alert("div 클릭!");
>     });
>     ```
>
>     1. a의 0번째 인덱스 클릭시 "a 클릭!"의 창을 띄웁니다 
>     2. 다음으로 "p 클릭!" 창을 띄웁니다. 
>     3. 그 다음 "div 클릭! "창을 띄웁니다.
>     4. 기본동작인 naver주소로 넘어가지 않습니다.
>
>   * ```
>     	$("a:eq(1)").bind({
>     		"mouseover":function(){
>     			$(this).css("color","gold");
>     		},
>     		"mouseout":function(){
>     			$(this).css("color","");
>     		}
>                 
>     	});
>     ```
>
>     1. a의 인덱스 1번째에 다음 내용을 묶어줍니다.
>     2. 마우스를 올릴시 함수입니다.
>     3. a의 인덱스1번에 올릴시 색상이 금색으로 바뀝니다.
>     4. 마우스를 올리지 않을시 함수입니다.
>     5. a의 인덱스 1번의 색상이 비어있습니다. (초기값)
>
>   * ```
>     	$("span").click(function(){
>     		$("a:eq(1)").unbind();
>     	})
>     ```
>
>     1. span을 클릭시 다음 함수가 실행됩니다.
>     2. a의 인덱스 1번째를 더이상 묶지 않습니다. (bind 내용이 사용되지 않음)
>
>   * ```
>     	$("button").click(function(){
>     		$("body").append("<p>새로 추가된 p</p>");
>     	})
>     ```
>
>     1. "클릭" 버튼을 누르면 실행되는 함수입니다.
>     2. body위치 안의 마지막에 "새로 추가된 p"가 <p></p>의 안에 들어가있는 형태로 생성됩니다.
>
>   * ```
>     	$("body").on("click","p",function(){
>     		alert("새로 추가되는 요소도 이벤트 적용!");
>     	});
>     });
>     ```
>
>     1. body의 on입니다. on이기 때문에 나중에 실행됩니다. p를 클릭시 발동되는 함수라는 내용입니다
>     2. 함수의 내용으로는 "새로 추가되는 요소도 이벤트 적용!"을 창으로 띄웁니다.

## accodian

> 태그를 기준으로 내용 보이기/가리기
>
> * body입니다.
>
>   * ```
>     <p>메뉴 만들기</p>
>     <ul type="square" class="main_menu">
>     	<li class="sub_menu1"><b>(1)선택</b>
>     		<ul type="circle" class="sub_menu2">
>     			<li>1선택</li>
>     			<li>1-2선택</li>
>     		</ul>
>     	</li>
>     	<li class="sub_menu1"><b>(2)선택</b>
>     		<ul type="circle" class="sub_menu2">
>     			<li>2선택</li>
>     			<li>2-1선택</li>
>     		</ul>
>     	</li>
>     	<li class="sub_menu1"><b>(3)선택</b>
>     		<ul type="circle" class="sub_menu2">
>     			<li>3선택</li>
>     		</ul>
>     	</li>
>     	<li class="sub_menu1"><b>(4)선택</b>
>     		<ul type="circle" class="sub_menu2">
>     			<li>4-1선택</li>
>     			<li>4-2선택</li>
>     		</ul>
>     	</li>
>     </ul>
>     ```
>
>     * 마우스를 클릭시 나타낼 내용입니다.
>
> * head입니다
>
>   * ```
>     $(function(){
>     	$("b").click(function(){
>     		$(this).next().slideToggle();
>     		$(this).parent().siblings().find("ul").slideUp();
>     	})
>     })
>     ```
>
>     1. b를 클릭했을때의 함수입니다.
>     2. 선택한것<b>의 다음<ul>을 슬라이드형태로 보이기/숨기기 합니다
>     3. 선택한것<b>의 부모의 형제들(siblings)에서 찾습니다(find) "ul"을 그리고 slideUp해줍니다(가리기)

## class

> 이미지  확대 축소 입니다.
>
> * style입니다.
>
>   * ```
>     <style>
>     	img{width: 200px; height: 200px;}
>     	.addsize{width: 300px; height: 300px;}
>     	.onoff{display: none;}
>     </style>
>     ```
>
>     * 이미지의 기본 크기는 가로 200px 높이 200px입니다.
>     * addsize에 대한 크기는 가로 300px 높이 300px입니다
>     * onoff시 디스플레이 값을 none으로  바꿔줍니다.
>
> * body입니다.
>
>   * ```
>     <button id="btn">class on/off</button>
>     <br/>
>     <img src="resources/imgs/img01.png" alt="img01" title="이미지 1번" />
>     <img src="resources/imgs/img02.png" alt="img02" title="이미지 2번" />
>     <img src="resources/imgs/img03.png" alt="img03" title="이미지 3번" />
>     ```
>
>     1. id 가 btn인 "class on/off" 버튼입니다.
>     2. 내용으로 3개의 이미지가 있습니다.
>
> * head입니다.
>
>   * ```
>     $(document).ready(function(){
>     	$("#btn").click(function(){
>     		$("img").toggleClass("onoff")
>     	})
>             
>     	$("img").click(function(){
>     		if($(this).hasClass("addsize")){
>     			$(this).removeClass("addsize").attr("title","이미지 축소됨");
>     		} else {
>     			$(this).addClass("addsize").attr("title","이미지 확대됨");
>     		}
>     	})
>     })
>     ```
>
>     1.  실행시 호출되는 함수입니다.
>     2. id가 btn인 것을 클릭시 실행되는 함수입니다.
>        1. 이미지에 대해 toggleClass인 onoff(style)를 활성/비활성 합니다
>     3. 이미지를 클릭시 실행되는 함수입니다.
>        1. 만약 선택한 이미지에 addsize(style)가 있다면 
>           1. 선택한 이미지에있는  addsize(style)를 지우고 tittle에 이미지 축소됨을 만들어줍니다. 
>        2. 없다면
>           1. 선택한 이미지에 addsize(style) 더해줍니다. 그리고 tittle에 이미지 확대됨을 써줍니다.

## insert (inside)

> **prepend, append의 사용법입니다.**
>
> * head입니다
>
>   * ```
>     $(function(){
>     	var cnt=0
>     	$("button:eq(0)").click(function(){
>     		$("div").prepend($("<p>").addClass("prepend").text("prepend"+(++cnt)));
>     	})
>     	$("button:eq(1)").click(function(){
>     		$("div").append($("<p>").addClass("append").text("append"+(++cnt)));
>     	})
>     	$("button:eq(2)").click(function(){
>     		$("div").html("<b>html 요소를 바꾼다.</b>")
>     	})
>     	$("button:eq(3)").click(function(){
>     		$("div").text("<b>text 요소를 바꾼다.</b>")
>     	})
>     })
>     ```
>
>     1. 실행되는 함수입니다.
>     2. 전역 변수 cnt는 추가되는 위치를 알기 쉽게 하기 위해 넣었습니다.
>     3. 버튼의 인덱스 0 번째를 클릭했을시 실행되는 함수입니다. 0️⃣
>        1. div의 앞쪽에 <P>에 클래스 prepend를 추가하고 내용으로  prepend와 cnt값을 추가해 줍니다.   <p class="prepend">prepend1</p>
>     4. 버튼의 인덱스 1 번째를 클릭했을시 실행되는 함수입니다.1️⃣
>        1. div의 뒤쪽에 <P>에 클래스 append를 추가하고 내용으로  prepend와 cnt값을 추가해 줍니다.   <p class="append">append2</p>
>     5. 버튼의 인덱스 2 번째를 클릭했을시 실행되는 함수입니다.2️⃣
>        1.  div에 현재 html 형식<b>을 받아 "html 요소를 바꾼다."를 출력합니다.
>     6. 버튼의 인덱스 3 번째를 클릭했을시 실행되는 함수입니다.3️⃣
>        1. div에 텍스트 `"<b>text 요소를 바꾼다.</b>"`를 출력합니다
>
> * body입니다.
>
>   * ```
>     <body>   
>         <button>prepend</button> 0️⃣
>         <button>append</button>  1️⃣
>         <button>html</button>    2️⃣
>         <button>txt</button>     3️⃣
>                 
>         0️⃣
>         <div>
>            2️⃣ <p>내부 삽입1</p>  3️⃣
>            2️⃣ <p>내부 삽입2</p>  3️⃣
>         </div>
>                 
>         1️⃣
>     </body>
>     ```
>
>     * 각 버튼을 눌렀을때 추가되는 위치나 바뀌는 위치입니다.

## insert (outside)

> **after,before,insertAfter,inserBefore의 사용법입니다**
>
> * head부분입니다.
>
>   * ```
>     $(function(){
>     	$("button:eq(0)").click(function(){
>     		$("#base").after("<div>새로운 엘리먼트(after)</div>");
>     	});
>     	$("button:eq(1)").click(function(){
>     		$("<div>새로운 엘리먼트(inserAfter)</div>").insertAfter("#base");
>     	});
>     	$("button:eq(2)").click(function(){
>     		$("#base").before("<div>새로운 엘리먼트(before)</div>");
>     	});
>     	$("button:eq(3)").click(function(){
>     		$("<div>새로운 엘리먼트(insertBefore)</div>").insertBefore("#base");
>     	});
>     });
>     ```
>
>     * 버튼 인덱스 0번째를 클릭시 실행되는 함수입니다.
>
>       * base의 뒤에 div태그 내용은 새로운 엘리먼트(after) 가 추가됩니다. 
>
>     * 버튼 인덱스 1번째를 클릭시 실행되는 함수입니다.
>
>       * div태그이고 내용은 새로운 엘리먼트(inserAfter)가 base 뒤에 추가됩니다.
>
>     * 버튼 인덱스 2번째를 클릭시 실행되는 함수입니다.
>
>       * base의 앞에 div태그 내용은 새로운 엘리먼트(before) 가 추가됩니다
>
>     * 버튼 인덱스 3번째를 클릭시 실행되는 함수입니다.
>
>       * div태그이고 내용은 새로운 엘리먼트(inserBefore)가 base 앞에 추가됩니다
>
>       ✅after,before은 타겟을 앞에 잡고 만들기 때문에 함수를 내용에 추가할수 있습니다✅
>
>       ✅inserAfter, inserBefore은 함수를 쓸수 없습니다. ✅
>
> * body입니다
>
>   * ```
>         <button>after()</button>		0️⃣
>         <button>inserAfter()</button>	1️⃣
>         <button>before()</button>		2️⃣
>         <button>insertBefore()</button> 3️⃣
>     		0️⃣	1️⃣
>         <div id="base">
>             <p>외부 삽입</p>
>         </div>
>         	2️⃣	3️⃣
>     ```
>
>     * 각각 누를시 들어가는 위치입니다.

## replace

> **replaceWith 와 replaceAll의 사용법입니다.**
>
> * head입니다.
>
>   * ```
>     $(function(){
>     	$("button:first").click(function(){
>     		$("p").replaceWith("<p><b>replaceWith()</b></p>")
>     	});
>     	$("button:last").click(function(){
>         	$("<p><b>replaceAll()</b></p>").replaceAll("p");
>     	})
>     })
>     ```
>
>     * 첫번째(인덱스 0번째) 버튼을 누를시 실행되는 함수입니다
>
>       * p 의 부분을 `<p><b>replaceWith()</b></p>`인 것으로 교체합니다.
>
>     * 마지막(인덱스 -1번째) 버튼을 누를시 실행되는 함수입니다
>
>       * 내용이 `<p><b>replaceAll()</b></p>` 형식을 적용하여 p부분에 교체해줍니다
>
>       ✅replaceWith는 함수를 적용할수 있지만 replaceAll은 타겟이 뒤라서 불가능합니다✅
>
> * body입니다.
>
>   * ```
>     <body>    
>         <div>
>             <p>DOM 대체</p>
>         </div>
>         <button>바꾸기(replaceWith)</button>
>         <button>바꾸기(replaceAll)</button>
>     </body>
>     ```
>
>     * 둘다 버튼을 누를시 "DOM 대체" 부분이 바뀝니다

## slotmachine

> * style입니다.
>
>   * ```
>     <style>
>     	img{
>     	width: 150px;
>     	height: 150px;
>     	float: left;
>     	}
>     	#menubox{position: relative;}
>     	#menu{overflow: auto;}
>     	.sel{
>     	width: 140px;
>     	height: 140px;
>     	border: 5px dotted red;
>     	position: absolute;
>     	left: 300px;
>     	}
>     	button{
>     	width: 150px;
>     	height: 50px;
>     	margin-left: 300px;
>     }
>     </style>
>     ```
>
>     * 이미지 크기 가로 150px, 높이 150px 왼쪽 정렬으로 지정해주었습니다
>     * 부모는 menubox 입니다
>     * menu가 ovreflow될시 자동으로 형태를 맞춰줍니다
>     * sel은 가로 140px 높이 140p 5px 단위의 도트 레드로 찍히며 위치는 부모기준 왼쪽에서 300px 입니다.
>     *  버튼의 크기는 가로150px 높이 50px 왼쪽으로부터 300 거리입니다
>
> * head입니다.
>
>   * ```
>     <script>
>     	$(function(){
>     		setInterval(function(){
>     			var div = $("#menu");
>     			$(".active").first().appendTo(div);
>     		},150);
>     		$("button").click(function(){
>     			$("img").toggleClass("active");
>     			if($("button").text() == "start"){
>     				$("button").text("stop");
>     			} else {
>     				$("button").text("start");
>     			}
>     		})
>     	})
>     </script>
>     ```
>
>     1. setInterval 함수입니다.
>     2. 변수 div에 menu를 저장해둡니다.
>     3. active 클래스 를 생성하고 첫번째 div에 append div(menu의 내용)를 추가해줍니다 150밀리세컨트 마다.
>     4. 버튼을 클릭시 함수가 실행됩니다.
>     5. 이미지의 클래스가"active"가 보이거나 사라집니다.
>        1. 만약 버튼의 text가 start라면 버튼의 text를 stop으로 바꿔줍니다
>        2. 아니라면 버튼의 text를 start로 바꿔줍니다.
>
> * body입니다.
>
>   * ```
>     <div id="menubox">
>     	<div class="sel"></div>
>             
>     	<div id="menu">
>     		<img src="resources/imgs/img01.png" alt="img01"/>
>     		<img src="resources/imgs/img02.png" alt="img02"/>
>     		<img src="resources/imgs/img03.png" alt="img03"/>
>     		<img src="resources/imgs/img04.png" alt="img04"/>
>     		<img src="resources/imgs/img05.png" alt="img05"/>
>     		<img src="resources/imgs/img06.png" alt="img06"/>
>     	</div>
>             
>     <button>start</button>
>     ```
>
>     * div위에 6개의 이미지가 가로로 정렬되고 붉은 도트점 상자 그리고 이미지 밑에는 stop 버튼이 있습니다.

## wrap

> **wrap, unwrap, wrapInner, wrapAll 의 사용법입니다**
>
> * style입니다
>
>   * ```
>     <style>
>     	.box{border: 2px solid red;}
>     	#menu{background-color: skyblue;text-align: right;}
>     	a{text-decoration: none; font-size: 20px;}
>     	#menu div{display: inline-block; margin-right: 10px;}
>     </style>
>     ```
>
>   * 
>
> * head입니다.
>
>   * ```
>     $(function(){
>     	var $box = $("<div>").addClass("box");
>     	$(".sub_menu:first").wrap($box);
>     ```
>
>     1. 변수 $box 에 div에 클래스 box를 추가한 내용을 넣어줍니다.
>     2. 첫번째 sub_menu(인덱스 0번째)를 $box(<div class=box>)에 감싸(wrap)집니다.(sub_menu가 하위로 들어가짐)
>
>   * ```
>     	$(".sub_menu").click(function(){
>     		$(".sub_menu").each(function(){
>     			if($(this).parent().is(".box")){
>     				$(this).unwrap(".box");
>     			}
>     		})
>     		$(this).wrap($box);
>     	})
>     ```
>
>     1. sub_menu를 클릭시 실행되는 함수입니다.
>     2. sub_menu의 전부(i) 하나하나 확인하는 함수입니다. 
>     3. 만약 지금(i)의 부모가 box라면 지금(i)의 박스를 해제(unwrap)합니다
>     4. each문을 벗어나고 click 상태에서 지금 클릭한 것은 변수 $box로 감싸줍니다
>
>   * ```
>     	$("a").wrapInner("<span></span>");
>     ```
>
>     * a를 찾아서 a의 안에를 <span>으로 감싸줍니다.
>
>   * ```
>     	$("a").wrapAll("<b></b>");
>     })
>     ```
>
>     * a를 찾아서 한곳에 묶어 <b>로 감싸줍니다.
>
> * body입니다.
>
>   * ```
>     <div id="menu">
>     	<div class="sub_menu">
>     		<a href="#"><span>공부</span></a>
>     	</div>
>     	<div class="sub_menu">
>     		<a href="#">study</a>
>     	</div>
>     	<div class="sub_menu">
>     		<a href="#">html</a>
>     	</div>
>     	<div class="sub_menu">
>     		<a href="#">javascript</a>
>     	</div>
>     	<div class="sub_menu">
>     		<a href="#">jq</a>
>     	</div>
>     </div>
>     ```

## delete

> **remove, detach, empty의 사용법입니다.**
>
> * head입니다.
>
>   * ```
>     $(document).ready(function(){
>     	$("p:eq(0)").click(function(){
>     		$(this).remove();
>     	})
>         
>     	$("p:eq(1)").click(function(){
>     		var ele = $(this).detach();
>     		$("h1").append(ele);
>     	})
>         
>     	$("p:eq(2)").click(function(){
>     		$(this).parent().empty();
>     	})
>     })
>     ```
>
>     * p의 인덱스 0번째를 클릭시 실행되는 함수입니다.
>       * 클릭한 p를 제거합니다
>     * p의 인덱스 1번째를 클릭시 실행되는 함수입니다.
>       * 변수 ele에 선택한p의 제거값을 저장합니다.
>       * h1에 변수 ele의 내용을 추가합니다.
>     * p의 인덱스 2번째를 클릭시 실행되는 함수입니다.
>       * 지금 선택한 p의 부모(div)의 내용을 제거합니다
>
> * body입니다
>
>   * ```
>     <h1>엘리먼트 제거하기</h1>
>     <div>
>     	<p>remove()</p>
>     	<p>detach()</p>
>     	<p>empty()</p>
>     </div>
>     ```
>
>     * remove()를 클릭시 <p>remove()</p>가 제거
>     * detach()클릭시 ele변수 저장되고 제거
>     * empty()클릭시 div안의 내용 제거

## ajax

> **jquery에서의 ajax입니다**
>
> 1. url  :통신할 경로(주소) ✅
>
> 2. method : 전송 방식(get(default) /post)✅
>
> 3. async : 비동기(defalut)/동기✅
>
> 4. dataType : 전송받을 데이터의 타입(xml,json,html,script,...) ✅
>
> 5. data:{"key":value},  : 전송할 데이터
>
> ✅ 친것만 사용해도 작동은 합니다.
>
> * style입니다.
>
>   * ```
>     <style>
>     	*{margin: 0px; padding: 0px;}
>     	table{width: 400px;}
>     	table tr:nth-child(odd){background-color: orange;}
>     	fieldset{width: 400px;}
>     	body{width: 1000px; margin: 50px auto;}
>     </style>
>     ```
>
>     1. 테이블 가로 400px
>     2. 테이블의 tr의 홀수번째에 배경색상 오렌지를 줍니다
>     3. fieldset의 가로는 400px입니다.
>     4. body의 가로는 1000px 여백 50
>
> * head입니다.
>
>   * ```
>     $(function(){
>     	$("#emp_search").click(function(){
>     		var empid = $("input[name=empid]").val();
>     		if (!isNaN(empid) && (empid >= 100) && (empid <=206)){
>     			$.ajax({
>     				url:"emplist.xml",                 
>     				method:"get",                       
>     				async:true,                        
>     				dataType:"xml",                                   
>                     success:function(data){            
>                     	var empInfo = $(data).find("EMPLOYEE_ID:contains("+empid+")").parent();
>                     	if((empInfo).is("ROW")){
>                     		$("table input").each(function(i){
>     							$(this).val($(empInfo).children().eq(i).text());
>     						})
>     					} else {
>     						alert("검색 대상이 존재하지 않습니다...")
>     					}
>     				},
>     				error:function(request,error){      
>     					alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
>     				}
>     			})
>         
>     		} else{
>     			alert("사원번호를 다시 확인해주세요")
>     		}
>     	})
>     })
>     ```
>
>     1. emp_search 클릭시 실행되는 함수입니다.
>        1. 변수 empid에 name empid에 입력된 값을 가져옵니다
>        2. 만약 empid의 값이 없지 않다면 그리고(&&) empid의 값이 100보다 크거나 같다면 (&&) empid의 값이 206보다 작거나 같다면
>           1. ajax를 호출합니다
>              1. 주소는 emplist.xml
>              2. 전송방식은 get
>              3. 비동기 true
>              4. 데이터타입 xml
>              5. 호출 성공시 실행 함수(data)
>                 1. 변수 empInfo에 data에서  EMPLOYEE_ID : 특정문자열 empid(2번에서 받아온값입니다)과 일치하는 부모를 찾아서 가져옵니다.
>                 2. 만약 empInfo가 ROW라면
>                    1. table input에 각각의 function(i) 함수를 실행합니다.
>                       1. 선택한것의 내용은(empInfo의 자식들에 i번쨰 인덱스의 text입니다.)
>                 3. 만약 아니라면
>                    1. "검색 대상이 존재하지 않습니다..." 창을 띄웁니다
>              6. 호출 실패시 실행 함수(요청,에러)입니다
>                 1. "code"+실패 코드 +다음줄+ "message"+ 요청에 대한 내용+다음줄+"error"+에러 내용
>        3. 만약 empid값이 맞지않다면
>           1. ""사원번호를 다시 확인해주세요"" 창을 띄웁니다
>
> * body입니다.
>
>   * ```
>     <body>    
>         <h1>데이터 가져오기</h1>
>         <fieldset>
>             <legend>사원정보 조회</legend>
>             <input type="text" name="empid"/>
>             <input type="button" id="emp_search" value="조회"/>
>         </fieldset>
>         <table>
>             <tr>
>                 <th>사원번호</th>
>                 <td><input type="text" name="empnum" /></td>
>             </tr>
>             <tr>
>                 <th>이    름</th>
>                 <td><input type="text" name="lastname" /></td>
>             </tr>
>             <tr>
>                 <th>이 메 일</th>
>                 <td><input type="text" name="email" /></td>
>             </tr>
>             <tr>
>                 <th>전화번호</th>
>                 <td><input type="text" name="phone" /></td>
>             </tr>
>             <tr>
>                 <th>입사일</th>
>                 <td><input type="text" name="hire" /></td>
>             </tr>
>         </table>
>     </body>
>     ```
>
> * 가져올 내용
>
>   * ```
>     <ROWSET>
>       <ROW>
>         <EMPLOYEE_ID>100</EMPLOYEE_ID>
>         <LAST_NAME>King</LAST_NAME>
>         <EMAIL>SING</EMAIL>
>         <PHONE_NUMBER>111.111.4567</PHONE_NUMBER>
>         <HIRE_DATE>1187. 6. 17 오전 12:00:00</HIRE_DATE>
>       </ROW>
>     ```

## menu

> **hide(),show(),toggle(),slideUp(),slideDown(),slideToggle()**
>
> **fadeOut(),fadeIn(),fadeTo(),fadeToggle(),animate()를 사용한 메뉴만들기입니다.**
>
> * style입니다.
>
>   * ```
>     <style>
>         img{
>             width: 200px;
>             height: 200px;
>             position: absolute;
>             left: 200px;
>             top: 100px;
>         }
>         p{
>             width: 100px;
>             border: 1px solid red;
>             position: absolute;
>             left: 10px;
>             display: none;
>         }
>     </style>
>     ```
>
>     * img는 가로 200px 높이 200px 위치는 상대적으로 왼쪽 200px 위에서 100px위치에 생성합니다.
>     * p는 가로100px 굵기1px 붉은색상입니다. 위치는 상대적이며 왼쪽 10px 표시는 none
>
> * head입니다.
>
>   * ```
>     $(function(){
>     	$("b").click(function(){
>     		$("p").toggle();
>     		$("p").each(function(i){
>     			$(this).animate({
>     				"top":50*(i+1)+ "px"
>     			},1000);
>     		})
>     	})
>     ```
>
>     1. b를 클릭했을때 실행되는 함수입니다.
>        1. p를 숨기기/보이기 합니다.
>        2. p의 각각에 다음 함수(인덱스 i번째에)를 적용합니다.
>           1. 지금 선택된것에 움직임(animate)을 줍니다
>              1. 위에서부터 50*(i+1) px로 줍니다.
>           2. 1000밀리세컨드의 속도로
>
>   * ```
>         $("p").on("click",function(){
>             var ele = $(this);
>             ele.css("background","hotpink");
>             ele.siblings("p").css("background-color","")
>     ```
>
>     1. p를 클릭했을때 실행되는 함수입니다.
>        1. 변수 ele는 지금 선택한것 p 입니다.
>        2. ele에 배경은 핫핑크 색상으로 바뀝니다.
>        3. ele의 형제들 p에겐 배경색상을 없게 해줍니다.
>
>   * ```
>             if(ele.is("p:contains(hide)")){
>             	$("img").hide();
>             }
>     ```
>
>        					1. 만약 ele가 <p>hide</P>를 선택한 것이라면
>        	       					1. 이미지를 숨깁니다.
>
>   * ```
>             if(ele.is("p:contains(show)")){
>             	$("img").show()
>             }
>     ```
>
>     1. 만약 ele가 <p>show</P>를 선택한 것이라면
>        					1. 이미지를 보여줍니다.
>
>   * ```
>             if(ele.is("p:contains(toggle)")){
>             	$("img").toggle();
>             }
>     ```
>
>     1. 만약 ele가 <p>toggle</P>를 선택한 것이라면
>        					1. 이미지를 숨기기/보이기 해줍니다.
>
>   * ```
>             if(ele.is("p:contains(slideUp)")){
>             	$("img").slideUp();
>             }
>     ```
>
>     1. 만약 ele가 <p>slideUp</P>를 선택한 것이라면
>        					1. 이미지를 슬라이드업하여 가립니다.
>
>   * ```
>             if(ele.is("p:contains(slideDown)")){
>             	$("img").slideDown();
>             }
>     ```
>
>     1. 만약 ele가 <p>slideDown</P>를 선택한 것이라면
>        					1. 이미지를 슬라이드 다운 하여 보여줍니다.
>
>   * ```
>             if(ele.is("p:contains(slideToggle)")){
>             	$("img").slideToggle()
>             }
>     ```
>
>     1. 만약 ele가 <p>slideToggle</P>를 선택한 것이라면
>        					1. 이미지를 슬라이드하며 가리기/보이기 해줍니다.
>
>   * ```
>             if(ele.is("p:contains(fadeOut)")){
>             	$("img").fadeOut();
>             }
>     ```
>
>     1. 만약 ele가 <p>fadeOut</P>를 선택한 것이라면
>        					1. 이미지가 서서히 사라집니다.
>
>   * ```
>             if(ele.is("p:contains(fadeIn)")){
>             	$("img").fadeIn();
>             }
>     ```
>
>     1. 만약 ele가 <p>fadeIn</P>를 선택한 것이라면
>        					1. 이미지를 서서히 보여줍니다.
>
>   * ```
>             if(ele.is("p:contains(fadeTo)")){
>             	$("img").fadeTo(4000,0.2)
>             }
>     ```
>
>     1. 만약 ele가 <p>fadeTo</P>를 선택한 것이라면
>        					1. 이미지를 서서히 사라짐/ 보이게 해줍니다 속도는 4000 밀리세컨드에 투명도는 0.2입니다 
>
>   * ```
>             if(ele.is("p:contains(fadeToggle)")){
>             	$("img").fadeToggle();
>             }
>     ```
>
>     1. 만약 ele가 <p>fadeToggle</P>를 선택한 것이라면
>        					1. 이미지를 서서히 사라짐/보이기 해줍니다.
>
>   * ```
>             if(ele.is("p:contains(animate)")){
>             	$("#image01").animate({
>                 	"width" :"500px",
>                 	"height" : "500px",
>                 	"left" : "600px",
>                 	"top":"0px"
>                 },2000)
>             }
>       	})
>     })
>     ```
>
>     1. 만약 ele가 <p>animate</p> 라면
>        1.  id image01을 찾아서 움직임 효과를 줍니다.
>           1. 가로 500px 크기에
>           2. 높이 500px 크기로 바뀌고
>           3. 왼쪽에서 600px 위치로
>           4. 위에서 0px  위치로 바뀝니다.
>        2. 2000밀리세컨드의 속도로
>
> * body 입니다.
>
>   * ```
>     <body>    
>         <b>메뉴</b>
>         <div>
>             <p>hide()</p>
>             <p>show()</p>
>             <p>toggle()</p>
>             <p>slideUp()</p>
>             <p>slideDown()</p>
>             <p>slideToggle()</p>
>             <p>fadeOut()</p>
>             <p>fadeIn()</p>
>             <p>fadeTo()</p>
>             <p>fadeToggle()</p>
>             <p>animate()</p>
>         </div>
>         <img src="이미지경로/img01.png" alt="image01" id="image01"/>
>     </body>
>     ```
>
>     * 각각의 함수를 호출할 P들입니다.


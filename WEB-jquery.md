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

## checkbox

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

# WEB-jquery

> ​      jquery 기본 작성법!
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
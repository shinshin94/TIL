# Web-css

## css 기본 문법

> 문서의 스타일을 지정해주는 언어
>
> * inline 
>
>   * 태그안에서 사용
>   * 예시
>     *  `<b style="color: red;">1. 인라인 스타일</b>`
>
> * 내부
>
>   * head 안에서 사용
>
>   * 예시
>
>     * ```
>        <head>	
>        	<style>
>                 
>          	p{
>                 
>            	background-color: coral;
>                 
>           	}
>                 
>         		</style>
>       </head>
>
> * 외부
>
>   * link 태그 사용
>
>   * 예시
>
>     * ```
>       <head>
>       	<link rel="stylesheet" href="resources/css/css01.css" 			type="text/css"/>
>       </head>
>       ```

## selector 선택자

> * 타입
>
>   * ```
>     pre{
>           
>       text-align: center;
>           
>     }
>     ```
>
> * id
>
>   * ```
>     \#s-id01{
>           
>       color: hotpink;
>           
>     }
>     ```
>
> * class
>
>   * ```
>     .s-cls01{
>           
>       background-color: black;
>           
>       color: white;
>           
>     }
>     ```
>
> * 전체
>
>   * ```
>     *{
>           
>       text-align: right;
>           
>     }
>     ```
>
> * 자식
>
>   * ```
>     \#atc > p {
>           
>       color:yellowgreen;
>           
>     }
>     ```
>
> * 인접
>
>   * ```
>     span+pre{
>           
>       background-color: cornflowerblue;
>           
>     }
>     ```
>
> * 하위
>
>   * ```
>     \#atc02 span{
>           
>       color:chocolate;
>           
>     }
>     ```
>
> * 속성
>
>   * ```
>     p[title]{
>           
>       background-color: grey;
>           
>     }
>     ```
>
> * 가상클래스
>
>   * link
>
>     * 기본 설정
>
>     * ```
>       a:link{
>                   
>         color: green;
>                   
>         font-size: 20pt;
>                   
>       }
>       ```
>
>   * visited 
>
>     * 한번 가보았던 곳
>
>     * ```
>       a:visited{
>                   
>         color: gold;
>                   
>       }
>       ```
>
>   * hover
>
>     * 마우스를 올렸을시 반응
>
>     * ```
>       a:hover{
>                   
>         background-color: black;
>                   
>         color: white;
>                   
>       }
>       ```
>
>   * active
>
>     * 마우스로 누를때
>
>     * ```
>       a:active{
>                         
>         background-color: yellow;
>                         
>         color:tomato;
>                         
>       }
>       ```
>
## font

> * font-weight
>
>   * 글자 굵기 속성
>
>   * ```
>     font-weight: bold;
>     ```
>
> * font-style
>
>   * 글자 모양 정하는 속성
>
>   * ```
>      font-style: italic;
>     ```
>
> * font-variant
>
>   * 소문자를 작은 크기의 대문자로 바꿔줌
>
>   * ```
>     font-variant: small-caps;
>     ```
>
> * font-size
>
>   * 글자 사이즈
>
>   * ```
>     font-size: 25px;
>     ```
>
> * line-height
>
>   * 줄 높이 정하기
>
>   * ```
>     line-height: 500%;
>     ```
>
> * font-family
>
>   * 글씨체
>
>   * ```
>     font-family: "궁서";
>     ```
>
> * 폰트 등록
>
>   * ```
>     @font-face {
>                 font-family: "폰트";
>                 src: url(위치/위치/폰트.ttf);
>             }
>     ```
>
> * tip 한줄로 쓸때
>
>   * "**style→variant→weight→size/line-height→family**"
>   * `p {font:italic small-caps bold 30px/15px serif;}`

## box

> * 상자 꾸미기
>
> * ```
>   .box{
>   	width: 600px;
>   	border: 3px #123456 double;
>   }
>   dt{
>   	background: #abcdef;
>   	text-align: center;
>   	font-size: 20px;
>   	letter-spacing: 15px;
>   	padding: 15px;   #안쪽 영역
>   	border-bottom: #123456 5px double;
>   }
>   	dd{
>   	padding: 10px;
>       
>   }
>   ```

  ## float

> * 방향을 정하고 그쪽으로 정렬 그리고 남는부분은 다른것으로 채워짐
>
> * ```
>   p span{
>               border: 3px dotted red;
>               float: right; #오른쪽으로 정렬됌
>           }
>   ```

## clear

> *  float 의 효과를 무시하고 그 다음 위치에 자신의 내용을 채움
>
> * ```
>   #box03{
>               clear: both; #위에는 float로 정렬된것과 그 옆에는 여백으로 남겨짐
>               			 # 그리고 다음 위치인 밑에 정렬됌
>               background-color: gray;
>               padding: 10px;
>       
>           }
>   ```

## display

> * 요소를 어떻게 보여줄지 정함
>
> * ```
>   #menu p{
>   	display: inline; #인라인
>   }
>   #login{
>   	display: none; #none이라서 안보임
>   }
>   ```

## overflow

> * 영역을 지정하고 넘치는 것들에  효과를 지정해줄수있다 (ex 숨기기,스크롤,...)
>
> * ```
>   #body{
>   	width: 300px;
>   	height: 100px;
>   	border: 1px solid red;
>   	overflow: auto;
>   }
>   ```

## position

> * relative
>
>   * 원래 자신의 위치에서 얼마나 움직이는지 위치 지정
>
> * absolute
>
>   * 부모의 위치 기준으로, 상대적으로 얼마나 움직이는지 위치 지정
>   * 부모에 relative가 없을시 body 기준
>
> * z-index
>
>   * 화면 앞쪽으로 나오는정도
>   * 이해안될시 3차원으로 생각 (모니터 안에 있는게 내쪽으로 나온다 생각)
>
> * fixed
>
>   * 브라우저 기준으로 위치 지정
>
> * ```
>   .myblue{
>   	background: blue;
>   	position: absolute;
>   	left: 100px;	#왼쪽에서 100px 떨어진 곳
>   	top :30px;		#위에서 30px 떨어진 곳
>   	z-index: 2px	
>   }
>   .mygreen{
>   	background: green;
>   	position: relative;
>   	left: 30px;
>   	top: -30px;
>   }
>   ```

## border

> * 테두리 속성 정하기
>
> * ```
>   li{
>   	list-style: none;
>   	width: 100px;
>   	height: 100px;
>   	text-align: center;
>   	float: left;
>   	    
>   	border-radius: 50px 50px 50px 50px; #왼쪽위부터 시계방향으로  곡률을 줌
>   	color: yellow;
>   	font-size: 50px;
>   }
>   ```
>
> * tip
>
>   * 브라우저마다 다르게 주고 싶을때
>
>   * ```
>     -webkit-border-radius: 50px 50px 50px 50px;
>     -moz-border-radius: 50px 50px 50px 50px;
>     -ms-border-radius: 50px 50px 50px 50px;
>     -o-border-radius: 50px 50px 50px 50px;
>     webkit: 구글,사파리
>     moz : 파이어폭스
>     ms : 익스플로러
>     o : 오페라
>     ```

## transform

> * translate
>
>   * 위치 이동
>
>   * ```
>     #tlate{
>         transform: translate(50px,50px);
>     }
>     ```
>
> * rotate
>
>   * 회전
>
>   * ```
>     #trotate{
>     	transform: rotate(30deg);
>     }
>     ```
>
> * scale
>
>   * 크기
>
>   * ```
>     #tscale{
>     	transform: scale(0.5,0.5);
>     }
>     ```
>
>   * 
>
> * skew
>
>   * 변형
>
>   * ```
>     #tskew{
>     	transform: skew(20deg,10deg);
>     }
>     ```
>
> * transition
>
>   * 속성 전환
>
>   * ```
>     #tran{
>     	transition: width 0.5s, background 1.5s linear,transform 1.5s;
>     }
>     ```











/* 가상 클래스 선택자 */

a:link{

  color: green;

  font-size: 20pt;

}

a:visited{

  color: gold;

}

a:hover{

  background-color: black;

  color: white;

}

a:active{

  background-color: yellow;

  color:tomato;

}



input:checked{

  width:100px;

  height: 100px;

}

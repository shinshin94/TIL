# Django

## 가상 환경

> 1. virtual environments (venv)
>    * python -m venv ??(이름)
>    * venv 실행
>    * windows
>      * .\??(이름)\Script\activate.bat
> 2. conda 가상환경
>    * 설치시
>    * conda create -n myweb python=3.9
>      * y
>    * `conda activate myweb` 가상환경 만들기
>    * `conda info --envs` 가상환경 위치
>    * 원활한 동작을 위해 환경변수도 추가해줍니다.(고급 시스템 기능- 시스템 속성 -환경변수)
>      * 시스템 변수에 anaconda3 추가 (변수 값에는 위치를 지정해줍니다.)
>      * 시스템 변수중에 Path를 편집을 클릭한 후 안에서 새로 만들기를 누른후 아래 것들을 추가해줍니다.
>        * %anaconda3%
>        * %anaconda3%\Library\mingw-w64\bin
>        * %anaconda3%\Library\bin
>        * %anaconda3%\Scripts
>        * %anaconda3%\condabin
>    * pip install django

## 개념

> * Model
>
>   * 데이터베이스
>
> * View
>
>   * 데이터를 처리해줍니다.
>
> * Template
>
>   * 데이터를 표현해줍니다
>
> * ```
>   Request ➡  URLConf ➡ ㅡㅡㅡㅡㅡㅡㅡㅡㅡ ⬅➡ Model ⬅➡ DB
>   		   (urls.py)  |View(views.py)|
>   Response ⬅ Template⬅ ㅡㅡㅡㅡㅡㅡㅡㅡㅡ
>   ```
>
> * ```
>   						URL RESOLUTION
>   					  ↗	 (urls.py)	  ↘
>   Client			Request					VIEW
>    ↕				 ↗						   ↘
>   Webserver ⬅➡ WSGI		middleware		   VIEW ⬅➡ MODEL ⬅➡ MANAGERS
>   			 (wsgi.py)	  	🔁🔄	    (views.py) (models.py)    ↕	
>   			     ↖						  ↙					  DATABASE
>   			   RESPONSE				  TEMPLATE
>   			   		   ↖ 			↙	
>   			   			   TEMPLATE
>   			   			   (*.html)
>   ```
>
> * cmd창 사용
>
>   * `cd /workspaces/workspace_django` 프로젝트를 만들 위치입니다.
>
>   * `django-admin startproject hello` 새로운 프로젝트 생성입니다. 이름은 hello
>
>   * `python manage.py startapp hello01` 프로젝트 밑에 앱을 새로 생성합니다. 이름은 hello01
>
>   * `cd mysite `위치 이동
>
>   * `python manage.py runserver` 서버 실행입니다.
>
>   * `python manage.py makemigrations dbtest` 데이터테이블을 만듭니다. 이름은 dbtest
>
>   * `python manage.py migrate` 데이터베이스 생성
>
>   * `sqlite3 db.sqlite3` SQLite 데이터베이스 파일 database에 대한 연결하여 엽니다
>
>   * `python manage.py makemigrations dbtest` 새로운 모델을 만들었습니다.
>
>   * `python manage.py sqlmigrate` sqlmigrate명령은 migration 이름을 인수로 받아, 실행하는 SQL 문장을 보여줍니다.
>
>   * `python manage.py shell` cmd창에 내용을 직접 입력시
>
>     * ```
>       >python manage.py shell 
>       >>> from dbtest.models import MyBoard
>       >>> from django.utils import timezone 
>       >>> test = MyBoard(myname='testuser',mytitle='test title',mycontent='test 1234',mydate=timezone.now())	--추가할 셀과 값을 입력해줍니다.
>       >>> type(test)	--셀의 타입을 확인합니다.
>       <class 'dbtest.models.MyBoard'>
>       >>> test.save()	--셀을 저장합니다.
>       >>> MyBoard.objects.all()		--Myboardf의 정보를 가져옵니다.
>       <QuerySet [<MyBoard: MyBoard object (1)>]>
>       exit() --나가기
>       ```

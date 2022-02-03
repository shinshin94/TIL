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
>    * `cd /workspaces/workspace_django` 프로젝트를 만들 위치입니다.
>    * `django-admin startproject hello` 새로운 프로젝트 생성입니다. 이름은 hello
>    * `python manage.py startapp hello01` 프로젝트 밑에 앱을 새로 생성합니다.
>    * cd mysite
>    * python manage.py runserver 서버 실행입니다.


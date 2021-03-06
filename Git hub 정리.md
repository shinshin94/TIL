# Git hub 정리



## Git bash

### 기본 설명 
>* CLI 환경 작업 
### 명령어
>   * `~ `       현재의 위치를 알려준다
>   * `date`   현재의 시간을 확인할때 사용
>   * `ls `        현재 있는 위치의 파일과 폴더를 알려줌
>     * -a  를 붙일시 숨긴 파일도 같이 표시됌
>   * `cd` 현재 위치를 변경할때 사용할수 있음
>     *  .  현재 위치 표시
>     *  .. 상위 위치로 이동
>     * 현재  위치에서 특정한곳으로 이동시 주소와 `/` 를 사용하여 이동함
>   * `clea`r 현재까지 입력한 값들을 지움
>   * `touch` 파일을 만듦
>   * `mkdir` 폴더를 만듬
>   * `start` 실제 화면에서 새롭게 특정 파일이나 폴더를 열때 사용한다
>   * `code . `현재 위치에서 visual studio 오픈시 사용
>   * `rm` 삭제 명령어 (*asterisk wildcard) 
>     * CLI 환경에서 삭제이므로 되돌릴수 없음 
>     * ex) `rm *.txt`(그 영역에 있는 텍스트 유형 삭제)
>     * ex) `rm -rf*`(그 영영에 있는 전부 삭제)
>   * `git config user.name` 이름 확인시 사용
>   * `git config user.email` 이메일 확인시 사용
>   * `git config --gloabal user.name` 이름 변경시 사용
>   * `git config --gloabla user.email` 이메일 변경시 사용
>   * `git config --unset --global user.name` 이름 삭제시(--global 설정이 아닐시 --global만 빼고 입력)
>   * `git config --unset --global user.email`(--global 설정이 아닐시 --global만 빼고 입력)

## VS(비주얼 스튜디오)

### 기본 설명

> * CLI와 GUI 환경을 같이 사용한다
>
> * 보통  Git hub와 관련하여 많이 쓰곤 한다

### 명령어

> * `git init` 현재 위치의 폴더를 Git으로 관리하겠다고 선언
>   * ※절대로 홈 폴더는 지정하지 않습니다.
> * `git status` Git의 현재 상황을 알아볼때 사용합니다
> * `git add` 현재 Git 선언후 추가할 사항을 올립니다.
>   * `git add . `현재의 있는것들을 모두 추가할때 사용
> * `git commit -m '커밋메시지'` 올려진 상황에 커멘트를 달고 저장합니다. 
> * `git log` 저장된 모든 상황이 나옵니다.  q로 탈출 가능합니다.
>   * `git log --oneline` log의 전체적인 상황중 주소와 커멘트만 표시됩니다. 
> * `git checkout head~` 저장된 주소값으로 이동할때 사용합니다.
> * `git checkout maste`r 이동후 다시 돌아올때 선언합니다.
> * `git remote -v` Git hub의 링크를 확인합니다
> * `git remote add origin 주소` Git hub의 링크를 연결할때 사용합니다.
> * `git push origin master` GIt hub에 저장한것을 올릴때 사용합니다.
> * `git pull origin master` GIt hub에 저장된것을 내려받을때 사용합니다.
> * `git branch`  현재 어떤 브랜치가 내 작업 공간에 있는지 확인`ls`와 비슷하다
> * `git branch 브랜치명` 새로운 임시 저장소를 만들때 이용합니다.
> * `git switch 브랜치명` 임시저장소로 이동하거나 돌아올때 사용합니다
> * `git merge 브랜치명`  현재있는곳과 해당 브랜치(임시 저장소)를 합칠때 사용합니다

## 타이포라

#### header

> `<h1>` 부터 `<h6>`까지 표현
>
> \# 의 개수로 표현하거나 `<h1></h6>` 사용
>
> 글자 크기가 아니라 항목의 목차같이 주요하게 나눌때 사용

####  list

순서 만들기 \* 나 \- 를 사용해서 점을 찍고 tab으로 부속적인 것을 표현

`>`인용문 사용시 용이함

#### 인라인과 블럭

 ` ``` `를 사용하여  블럭

`양옆에 하나 사용으로 감싸줌 인라인

#### 이미지와 링크

`![]()` 이미지를 올릴때 대괄호는  이름 소괄호는 주소를 입력

`[]()`똑같이 이름과 주소를 입력 앞에 ! 의 차이

보통 코드를 보지않으면 않나옴

#### 테이블

표를 작성시 사용

`|` 3번 누르고  컬럼을 작성 왼쪽 위로 표 수를 조절함

표안에서 CITL 과 ENTER 로 열 추가 쉬움

| 깃 베스  | 🤷‍♂️   |      |
| -------- | ---- | ---- |
| 비쥬얼   | 🤦‍♂️   |      |
| 타이포라 | 🙋‍♂️   |      |
|          |      |      |

#### 기타

* 글씨체와 구분선
  * *이탤릭체* `*` 나 `_`로 _감싸줌_
  * **보드체는** `**`나`__`__로 감싸줌__
  * ~~취소선~~`~~`로 감싸줌
* `---`로 사용

---


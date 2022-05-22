# Git & GitHub사용법
> GitHub의 아이디를 만든 상태부터 입니다.
>
## GitHub ➡New repository

> 새로운 저장소를 만듭니다
>
> 소스 코드가 저장되는곳 (1가지의 프로젝트라고 생각하면 됩니다.)
>
> * Repository name
>   * 저장소의 이름
> * 저장 방법 선택
>   * Public
>     * 오픈 소스로 누구나 볼수 있습니다
>     * 무료
>   * Private
> * Initalize this repository with a README ( 필수는 아닙니다.)
>   * Add.gitignore:None
>     * 보통 남들이 못보게 다양한 개인적인 환경 설정을 보통 지정
>   * Add a license:None
>     * 오픈소스 라이센스중에 어떤것을 선택했는지 알려주기 위해 선택
>

## Git 다운로드

> 1. https://git-scm.com/
>    * 사이트 접속
> 2. Downloads 클릭
> 3. 자신의 환경에 맞게 설치합니다.
> 4. 보통 그대로 전부 next를 클릭하여 설치합니다.

## Git 명령어 및 환경 설정

> 명령 프롬프트 창에서 실행합니다. (cmd)
>
> * git --version
>   * 현재 설치된 git의 버젼 및 os를 나타내줍니다.
> * git config --global user.name shinshin94
>   * global
>     * 컴퓨터 전체에서 동일한 옵션을 적용하려고 설정
>   * user.name <id>
>     * 자신의 GitHub 유저명을 지정줍니다.
> * git config --global user.email aodvl2@gmail.com
> * cd <연동할 폴더 위치>
> * git clone https://github.com/shinshin94/TIL.git
>   * 만들어둔 GitHub repository 를 복사하여 주소에 있는 내용들을 가져옵니다
>   * 컴퓨터의 git을 local repository라고 부름 ( github 주소는 원격지(리모트) repository )
> * git add <변경된 파일명>
> * git commit -m "git과 github 복습1"
>   * -m 뒤에는 github에 올릴시 표시를 위한 짧은 메세지를 넣어줍니다.
> * git push
>   * github에 업로드 합니다.
> * 순서 
>   1. 저장소에 파일의 변동이 생김
>   2. 변동된 파일을 `git add <변경된 파일명>`
>   3. `git commit -m "짧은 메세지"` 로 변동 사항을 짧게 요약해서 넣어줌
>   4. `git push` 를 사용하여 github에 업로드


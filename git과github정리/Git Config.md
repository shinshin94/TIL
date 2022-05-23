# Git Config

> Git의 환경 설정
>
> 추가시 .gitconfig에 저장됩니다
>
> * git config --list
>   * 현재 git의 환경 설정 목록
> * git config --global user.name "test"
>   * git할 사용자 이름
>   * 보통 github와 동일하게 해줍니다
> * git config --global user.email "test@test.com"
>   * git할 이메일 이름
>   * 보통 github와 동일하게 해줍니다
> * .gitconfig에 저장된 내용을 직접 변경해도 적용 됩니다.
> * git config --global core.editor vi
>   * 사용할 editor를 지정해줄수 있습니다.
> * git config에서 해당 내용이 겹치는 경우
>   * global로 설정한것보다 특정 프로젝트에 직접 설정해준것을 우선시 합니다.
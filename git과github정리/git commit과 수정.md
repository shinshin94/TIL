# git commit과 수정

> git pull로 작업 시작시 변화 사항을 확인하고 업데이트 생활화 해줌
>
> * git log
>   * commit 내용과 해당 commit의 log내역을 확인할수 있음
> * git reset --hard 889e4b4ed6f7f26fbc408bfc28eaf1f1bf52f2d2
>   * 해당 commit의 위치로 돌아감( 그 이후 commit한 내용들은 전부 삭제)
>   * 로컬은 commit 당시의 상황으로 돌아감
>   * git push시 오류( 로컬과 git hub가 내용이 다르기 때문)
>     * git push -f
>       * 강제 푸쉬임
>       * 로컬과 같이 hard로 요청해서 돌아간 그대로 github도 돌아감
> * git commit --amend
>   * 특정 editor가 실행됨
>   * 수정을 원할시 a 입력
>   * 수정 완료시 esc버튼 누르고 :wq!입력


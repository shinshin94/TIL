# Git Commit2

>  날짜 변경 및 committer 변경
>
> * git rebase -i <로그내역>
>
>   * 수정할 해쉬값의 전 값을 로그내역으로 요청
>   * 수정할 commit의 pick을 edit으로 변경후 저장하고 나옴
>   * GIT_COMMITER_DATE="Oct 1 10:00:00 2020 +0000" git commit --amend -no-edit --date "Oct 1 10:00:00 2020 +0000"
>     * 요일은 따로 입력하지 않아도 됩니다.
>     * 로그내역에는 해당 날짜 정보로 변경됩니다.
>   * git rebase --continue
>     * 변경된 내용을 반영
>
> * git filter-branch -f --env-filter \
>
>   * ```
>     'if [ $GIT_COMMIT = <로그 내역>]
>     then
>     	export GIT_AUTHOR_DATE="mon Oct 1 10:00:00 2020 +0000"
>     	export GIT_COMMITER_DATE="Mon Oct 1 10:00:00 2020 +0000"
>     fi'
>     ```
>
>     * if문을 사용하여 원하는 날짜로 입력하여 변경
>
>   * 완료
>
> * 직접 입력
>
>   * ```
>     git filter-branch -f --env-filter '
>     OLD_EMAIL="test2@text.com"
>     CORRECT_NAME="shinshin94"
>     CORRECT_EMAIL="aodvl2@gmail.com"
>
>     if [ $GIT_COMMITTER_EMAIL = $OLD_EMAIL ]
>     then
>     	export GIT_COMMITTER_NAME="$CORRECT_NAME"
>     	export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
>     fi
>     if [ $GIT_AUTHOR_EMAIL = $OLD_EMAIL ]
>     then
>     	export GIT_AUTHOR_NAME="$CORRECT_NAME"
>     	export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
>     fi'
>     ```
>
>     * if문을 사용하여 변경


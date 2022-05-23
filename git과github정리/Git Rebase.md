# Git Rebase

> 특정한 commit을 수정/삭제
>
> 삭제는 팀 프로젝트일시 권장하지는 않음 (개인 프로젝트일시는 상관 없음)
>
> * git rebase -i Head~3
>
>   * -i 
>
>     * 인터렉티브 모드 
>
>   * Head~3
>
>     * 최근 3개를 불러옴
>
>   * ex)
>
>     * ```
>       pick f147404 git과 github 복습5
>       pick 35e9d2e git과 github 복습6
>       pick 8e809d6 git과 github 복습7
>
>       # Rebase 5a61195..8e809d6 onto 5a61195 (3 commands)
>       ```
>
>       1. 수정하고 싶은 pick 부분을 reword로 바꾸어 쓰고 저장하고 나옵니다.
>       2. 나올시 바로 해당 부분의 상세 정보가 나오는데 이때 commit을 바꿔주시면 됩니다.
>       3. 수정 완료
>
>   * git rebase <로그 내역>
>
>     * 해당 commit의 앞쪽까지 2개를 불러옵니다.
>
> * git rebase -i Head~3
>
>   * ex)
>
>     * ```
>       pick f147404 git과 github 복습5
>       pick 35e9d2e git과 github 복습6
>       pick 8e809d6 git과 github 복습7
>
>       # Rebase 5a61195..8e809d6 onto 5a61195 (3 commands)
>       ```
>
>       1. 수정하고 싶은 pick 부분을 drop으로 바꾸어 쓰고 저장하고 나옵니다.
>       2. 삭제 완료
>
> * 기타 git rebase 사용시 commad
>
>   * ```
>     # Commands:
>     # p, pick <commit> = use commit
>     # r, reword <commit> = use commit, but edit the commit message
>     # e, edit <commit> = use commit, but stop for amending
>     # s, squash <commit> = use commit, but meld into previous commit
>     # f, fixup [-C | -c] <commit> = like "squash" but keep only the previous
>     #                    commit's log message, unless -C is used, in which case
>     #                    keep only this commit's message; -c is same as -C but
>     #                    opens the editor
>     # x, exec <command> = run command (the rest of the line) using shell
>     # b, break = stop here (continue rebase later with 'git rebase --continue')
>     # d, drop <commit> = remove commit
>     # l, label <label> = label current HEAD with a name
>     # t, reset <label> = reset HEAD to a label
>     # m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]
>     # .       create a merge commit using the original merge commit's
>     # .       message (or the oneline, if no original merge commit was
>     # .       specified); use -c <commit> to reword the commit message
>     #
>     # These lines can be re-ordered; they are executed from top to bottom.
>     #
>     # If you remove a line here THAT COMMIT WILL BE LOST.
>     ```
>
>     * 입력시 이런식으로 친절하게 command를 알려줍니다
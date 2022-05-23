# Git log 다루기

> * git log
>   * commit 내역을 보여줍니다
>   * q 로 나올수 있습니다.
> * git log --stat
>   * 해당 log에서 추가된 line 정보를 알려줍니다.
> * graph
>   * branch와 병합 정보를 그래프로 출력하여 보기 좋게 표기
> * p
>   * commit 에 적용된 구체적인 항목 표기
>   * ex) git log -p -3
>     * log의 마지막에서부터 3개(-3)까지 보여줍니다
> * pretty
>   * 각각의 commit 내역이 출력됩니다.
>   * ex) git log --pretty=oneline
>     * 한줄로 commit 내역 출력
>   * ex) git log --pretty=format:"%h -> %an, %ar : %s" --graph
>     * h는 commit할때 해쉬값을 표현
>     * an 작성자 이름
>     * ar 작성 날짜
>     * s commit 메세지의 주제
>     * branch의 병합을 그래프로 보여줌
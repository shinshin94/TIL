# Git 원격 저장소 (Remote Repository) 관리하기

> * git remote
>   * 원격 저장소 확인
>   * 원격 저장소의 목록을 보여줍니다. (보통은 아무것도 안했을시 origin이 전부)
> * git remote show origin
>   * 해당 원격 저장소의 상세내용 확인
> * git remote add test <주소>
>   * 특정한 원격 저장소를 추가할때 사용
>   * remote add <저장할 저장소 이름>
> * git remote rename test temp
>   * remote rename <변경전 이름> <변경 후 이름>
>   * 사전에 등록한 원격 저장소의 이름을 바꿉니다.
> * git remote -v
>   * 원격 저장소의 이름별 fetch 및 push의 위치를 나타내줌
> * git log origin/maser
>   * 해당 원격 저장소의 log를 확인
> * git remote rm temp
>   * 원격 저장소 삭제
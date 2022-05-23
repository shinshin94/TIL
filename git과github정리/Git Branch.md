# Git Branch

> 동시에 여러 개발자들이 프로젝트에서 각기 다른 기능을 개발할 수 있도록 하는 기능
>
> * Git 저장소를 만들시 자동으로 마스터 브랜치로 생성됨
>   * 일반적으로 배포가 가능한 수준의 안정된 버전
>   * 기능을 하위와 같이 병렬식 구성을 함
>   * Develop Branch
>     * master브랜치를 건드리기 전에 개발용임
>     * 신기능이 정상 수행하고 마스터 브랜치에 반영해도 좋다고 판단시 합침
>   * Bug Fix Branch
>     * 버그 수정
> * 통합 브랜치 : 배포가 가능한 수준의 브랜치로 일반적으로 마스터 브랜치
> * 토픽 브랜치 : 특정한 기능을 위해 만들어진 브랜치로 일반적으로 마스터 브랜치 이외의 다른 브랜치
> * git branch
>   * git branch develop
>     * 다른 branch를 만듬
> * git checkout develop
>   * 해당 branch로 사용을 바꿈
> * git merge develop
>   * master branch를 사용하는 상황에서 합칠 branch를 입력
>   * git push를 할시 github에도 합쳐진 내용이 반영됨
> * git branch -d develop
>   * -d <삭제할 브랜치 명>
>   * 해당 branch를 제거합니다
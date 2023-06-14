설정과 초기화
=========

<br/>

전역 사용자명/이메일 구성하기
--------------------------
1. git config --global user.name "<'Your name'>"
    * `git config --global user.name "<EXAMPLE2023>"`

2. git config --global user.email "<'Your address'"
    * `gif config --global user.email "<id@email.com>"`

<br/>

저장소 별 사용자명/이메일 구성하기
-------------------------------
* 해당 저장소 디렉터리 이동 후 사용 가능
-------------------------------
1. git config user.name "<'Your name'>"
    * `git config user.name "<EXAMPLE2023>"`

2. git config user.email "<'Your address'>"
    * `git config user.email "<id@emil.com>"`

<br/>

전역 설정 정보 조회
-----------------
1. git config --global --list

<br/>

저장소별 설정 정보 조회
---------------------
1. git config --list

<br/>

Git의 출력결과 색상 활성화
------------------------
1. git config --global color.ui "auto"

<br/>

새로운 저장소 초기화
------------------
1. mkdir /path/nweDir
    * `mkdir newDir (현재 디렉토리에서 생성)`
2. cd /path/newDir
    * `cd newDir (현재 디렉토리에서 이동)`
3. git init
    * `git init`

<br/>

저장소 복제
----------
1. git clone <'target url'>
    * `git clone https://github.com/PX4/PX4-Autopilot.git`
   
<br/>

<br/>

기본적인 사용법
=========

<br/>

새로운 파일을 추가하거나 존재하는 파일 스테이징하고 커밋하기
-------------------------------------------------------
1. git add <'File'>
    * git add readme.md
2. git commit -m "Message"
    * git commit -m "readme.md file add"

<br/>

파일의 일부를 스테이징하기
-----------------------
1. git add -p [<'File'>[<File>[etc Files]]]

<br/>

add 명령에서 Git 대화 모드를 사용하여 파일 추가하기
-----------------------------------------------
1. git add -i

<br/>

수정되고 추적되는 파일의 변경 사항 스테이징하기
-------------------------------------------
1. git add -u[<'adress'> [<address>]]

<br/>

수정되고 추적되는 모든 파일의 변경 사항 커밋하기
--------------------------------------------
1. git commit -m "<'Messages'>" -a

<br/>

작업 트리의 변경 사항 돌려놓기
---------------------------
1. git checkout HEAD <'File'>[<File>]

<br/>

커밋되지 않고 스테이징된 변경 사항 재설정하기
-----------------------------------------
1. git reset HEAD <'File'>[<File>]

<br/>

마지막 커밋 고치기
----------------
1. git commit -m "<'Messages'>" - -amend

<br/>

이전 커밋을 수정하고 커밋 메세지를 재사용하기
-----------------------------------------
1. git commit -C HEAD - -amend
   
<br/>

<br/>

브랜치
=====

<br/>

지역 브랜치 목록 보기
-------------------
1. git branch

<br/>

원격 브랜치 목록 보기
-------------------
1. git branch -r

<br/>

지역과 원격을 포함한 모든 브랜치 목록 보기
--------------------------------------
1. git branch -a

<br/>

현재 브랜치에서 새로운 브랜치 생성하기
----------------------------------
1. git branch <'New branch'>

<br/>

다른 브랜치 체크아웃 하기
----------------------
1. git checkout <'Target branch'>
    * `git checkout v1.12.3`

<br/>

현재 브랜치에서 새로운 브랜치 생성하고 체크아웃하기
----------------------------------------------
1. git checkout -b <'New branch'>
    * `git checkout -b v1.13.3`

<br/>

다른 시작 지점에서 브랜치 생성하기
-------------------------------
1. git branch <'New branch'> <Dir>

<br/>

기존의 브랜치를 새로운 브랜치로 덮어쓰기
------------------------------------
1. git branch -f <'Old branch'> [<'Target dir'>]

<br/>

브랜치를 옮기거나 브랜치명 변경하기
-------------------------------
1. git checkout -m <'Old branch'> <'New branch'>
    * `<새로운 브랜치>가 존재하지 않는 경우`

2. git checkout -M <'Old branch'> <'New branch'>
    * `<무조건 덮어쓰기>`

설정과 초기화
=========

<br/>

전역 사용자명/이메일 구성하기
--------------------------
1. git config --global user.name "<이름>"
    * `git config --global user.name "<EXAMPLE2023>"`

2. git config --global user.email "<이메일>"
    * `gif config --global user.email "<id@email.com>"`

<br/>

저장소 별 사용자명/이메일 구성하기
-------------------------------
* 해당 저장소 디렉터리 이동 후 사용 가능
-------------------------------
1. git config user.name "<이름>"
    * `git config user.name "<EXAMPLE2023>"`

2. git config user.email "<이메일>"
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
1. git clone <경로>
    * `git clone https://github.com/PX4/PX4-Autopilot.git`

<br/>

Submodule을 포함하는 Git 저장소를 가져오기
-----------------------------------------
1. git clone --recursive <경로>
    * `git clone --recursive https://github.com/PX4/PX4-Autopilot.git`

<br/>

참고 사이트
-------------------------------------------
[명령어 참조](https://medium.com/@joongwon/git-git-%EB%AA%85%EB%A0%B9%EC%96%B4-%EC%A0%95%EB%A6%AC-c25b421ecdbd)

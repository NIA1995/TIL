Git 명령어
=========

전역 사용자명/이메일 구성하기
--------------------------
1. git config --global user.name "Your name"
    > git config --global user.name "EXAMPLE2023"

2. git config --global user.email "Your address"
    > gif config --global user.email "id@email.com"

저장소 별 사용자명/이메일 구성하기
-------------------------------
* 해당 저장소 디렉터리 이동 후 사용 가능
-------------------------------
1. git config user.name "Your name" 
    > `git config user.name "EXAMPLE2023"`

2. git config user.email "Your address"
    > `git config user.email "id@emil.com"`
    
전역 설정 정보 조회
-----------------
1. git config --global --list

저장소별 설정 정보 조회
---------------------
1. git config --list

Git의 출력결과 색상 활성화
------------------------
1. git config --global color.ui "auto"

새로운 저장소 초기화
------------------
1. mkdir /path/nweDir
    > mkdir newDir (현재 디렉토리에서 생성)
2. cd /path/newDir
    > cd newDir (현재 디렉토리에서 이동)
3. git init
    > git init

저장소 복제
----------
1. git clone <target url>
    * git clone https://github.com/PX4/PX4-Autopilot.git


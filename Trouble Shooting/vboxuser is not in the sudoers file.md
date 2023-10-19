# vboxuser is not in the sudoers file

VitrualBox에 우분투를 처음 설치하고 sudo su 명령어로 슈퍼 계정에 접근할 때 오류가 발생하였다.

해결 방법은 아래와 같다.



## Step 1

su root 명령어를 사용하여 root 사용자로 변경하고 비밀번호를 입력.

![image-20231019102037911](C:\Users\AstroX\AppData\Roaming\Typora\typora-user-images\image-20231019102037911.png)



## Step 2

apt-get install sudo -y를 사용하여 sudo 패키지 설치

![image-20231019102217660](C:\Users\AstroX\AppData\Roaming\Typora\typora-user-images\image-20231019102217660.png)



## Step 3

sudo 그룹에 vboxuser 추가

![image-20231019102251806](C:\Users\AstroX\AppData\Roaming\Typora\typora-user-images\image-20231019102251806.png)



## Step 4

/etc/sudoers의 권한 변경

![image-20231019102329270](C:\Users\AstroX\AppData\Roaming\Typora\typora-user-images\image-20231019102329270.png)



## Step 5

재부팅 후 sudo su 명령어 테스트

![image-20231019102447624](C:\Users\AstroX\AppData\Roaming\Typora\typora-user-images\image-20231019102447624.png)

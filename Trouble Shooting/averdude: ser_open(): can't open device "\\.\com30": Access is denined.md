# averdude: ser_open(): can't open device "\\.\com30": Access is denined.

![03](https://github.com/NIA1995/TIL/blob/3ac9789c7217be9af7b82d273fd682ae65f2c2d7/Trouble%20Shooting/Images/03.png)

## Window 환경에서 문제의 해결책은 아래 두 가지 경우이다.

### 1. device manager > ports > Uninstall all ports and reconnect

### 2. take off "serial monitor"

#### 아두이노 나노 환경에서는 시리얼 모니터를 꺼준 뒤 코드를 업로드하면 정상적으로 작동하였다.

![04](https://github.com/NIA1995/TIL/blob/3ac9789c7217be9af7b82d273fd682ae65f2c2d7/Trouble%20Shooting/Images/04.png)

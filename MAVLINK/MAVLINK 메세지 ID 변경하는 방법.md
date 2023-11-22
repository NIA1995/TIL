
#TIL


1. 메세지 ID 값 변경을 원하는 프로젝트의 message_definitions 폴더에서 해당 메세지를 찾는다.
	1.  QGC : qgroundcontrol/libs/mavlink/include/mavlink/v2.0/message_definitions
	2.  PX4 : PX4-Autopilot/mavlink/include/mavlink/v2.0/message_definitions (1.12.3)
	3.  PX4 : PX4-Autopilot/src/modules/mavlink/mavlink/message_definitions (1.15.0)
2. 기존에 사용되는 메세지 ID와 사용 예정인 메세지 ID 구간을 피해서 ID 값을 변경한다.
	1.  [일반 메세지](https://mavlink.io/en/messages/common.html)
	2.  메세지 할당 영역
		1. ardupilotmega.xml : 11000 - 11999
		2. ASLUAV.xml : 8000 - 8999
		3. common.xml : 301 - 10000
		4. minimal.xml : 0 - 300
		5. development.xml : 42000 - 42999
		6. uAvionix.xml : 10001 - 10999
		7. storm32.xml : 60000 - 60049
		8. AVSSUAS.xml : 60050 - 60099
		9. Herelink.xml : 50000 - 50099
		10. ras_a.xml : 51000 - 51999
		11. csAirLink.xml : 52000 - 52099(send) , 52100 - 52499(receive)
		12. 최대 할당 영역 < 60000
3. MAVLink Generator를 통해 메세지를 생성한다.
	1. PX4, QGC의 경우 C언어, 2.0v의 프로토콜을 사용해 생성하면 된다.
4. 기존 메세지 폴더에 넣어 프로젝트를 새로 빌드한다.

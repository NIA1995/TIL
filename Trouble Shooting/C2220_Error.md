# C2220 : 다음 경고는 오류로 처리됩니다.

<br/>
해결법
------

* 전처리기 사용하여 제외하기
  * #pragma warning(suppress:2220)
  * #pragma warning(disable:2220)
  * #define _CRT_SECURE_NO_WARNINGS

* 프로젝트 설정 변경하기(Qt)
  * /WX 삭제하기
    * QMAKE_CXXFLAGS_WARN_ON += /WX /W3 > QMAKE_CXXFLAGS_WARN_ON += /W3

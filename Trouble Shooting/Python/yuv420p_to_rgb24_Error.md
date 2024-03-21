> 증상

색을 정상적으로 출력하지 못하고 일부 색이 반전되어 보이는 현상

![](https://github.com/NIA1995/TIL/blob/main/Trouble%20Shooting/Python/Images/yuv420p_to_rgb24_Error/Error_01.png)

> 문제 원인

numpy 형식인 원본 이미지는 matplot으로 보여줄 때 기본적으로 RGB 형식을 사용하는데, cv2의 경우 보여줄 때 BGR 방식을 사용하여 색이 반전되서 보인다.

> 해결 방법

`img = cv2.cvtColor(myFrame, cv2.COLOR_RGB2BGR)`으로 색상 반전 적용

> 참고

- https://codingpackage.tistory.com/19

# Web

### 브라우저 동작 과정  

브라우저의 주요 기능 : 사용자가 선택한 자원을 서버에 요청하고 브라우저에 표시하는 것  
자원의 주소는 URI(Uniform Resource Identifier)에 의해 정해진다.  
웹 표준화 기구인 W3C를 따른다.  

동작 과정
1. HTML 문서 파싱. 태그를 DOM 노드로 변환.
2. 외부 CSS 파일과 함께 포함된 스타일 요소 파싱. 렌더 트리 생성.
3. 렌더 트리 배치. 각 노드가 화면의 정확한 위치에 표시.
4. 렌더 트리 그리기

*참고링크 - [https://d2.naver.com/helloworld/59361](https://d2.naver.com/helloworld/59361)*


### TCP / UDP

|                | TCP            | UDP             |
|----------------|----------------|-----------------|
| 연결 방식      | 연결형 서비스  | 비연결형 서비스 |
| 패킷 교환      | 가상 회선 방식 | 데이터그램 방식 |
| 전송 순서 보장 | 보장함         | 보장하지 않음   |
| 신뢰성         | 높음           | 낮음            |
| 전송 속도      | 느림           | 빠름            |

TCP는 `신뢰성이 높고 느리다`, UDP는 `신뢰성이 낮고 빠르다`

- UDP  
    HTTP/3는 UDP 선택. QUIC을 사용. TCP는 제약조건이많고 UDP가 속도 더 빠름. 핸드쉐이크 과정 최적화.  
    - HTTP/3가 UDP를 사용함으로써 기존 프로토콜보다 나아진 점  
        연결 설정 시 레이턴시 감소  
        흐름 제어의 속도 개선  
        멀티플렉싱을 지원  
        클라이언트의 IP가 바뀌어도 연결이 유지됨  
    *참고링크 - [HTTP/3는 왜 UDP를 선택한 것일까?](https://evan-moon.github.io/2019/10/08/what-is-http3/?fbclid=IwAR2CBX8JPOKuUph3frQoodM969mTlmv9tyLQRFd72QGCZOakmq-DBs1t7LU)*

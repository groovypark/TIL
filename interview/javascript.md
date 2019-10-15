# JavaScript

### 호이스팅

변수와 함수를 먼저 읽어버린뒤 코드를 실행시킨다?
그래서 var같은 경우는 레퍼런스 에러가 안난다.
이런 것들을 방지하고자 const, let이 생겻다.
cosnt는 변수 재선언, 재할당 모두 불가능하다.

### 클로저

함수안에 변수와 내장함수가 있는데, 그 내장함수에서 바깥에 있는 변수에 접근할 때.
- 해결방법  
    즉시실행함수
- 쓰는 이유
    객체지향 oop처럼 privite으로 쓰기 위해. 정보은닉. 캡슐화  

### 이벤트 루프

비동기 처리할 때, 콜백함수를 이벤트 루프에서 처리해서 순서가 되면 실행 시켜주는 것?  
이벤트 루프는 `현재 실행중인 태스크가 없는지'와 '태스크 큐에 태스크가 있는지`를 반복적으로 확인하는 것
- 모든 비동기 API들은 작업이 완료되면 콜백 함수를 태스크 큐에 추가한다.
- 이벤트 루프는 '현재 실행중인 태스크가 없을 때'(주로 호출 스택이 비워졌을 때) 태스크 큐의 첫 번째 태스크를 꺼내와 실행한다.

![Event loop](https://image.toast.com/aaaadh/real/2018/techblog/eventloop.jpg)

*참고링크 - [https://meetup.toast.com/posts/89](https://meetup.toast.com/posts/89)*

### var, let, const / let, const 차이

var는 `function-scoped`이고, let, const는 `block-scoped`

```javascript
// 이미 만들어진 변수이름으로 재선언했는데 아무런 문제가 발생하지 않는다.
var a = 'test'
var a = 'test2'

// hoisting으로 인해 ReferenceError에러가 안난다.
c = 'test'
var c
```
let과 const의 차이점은 변수의 immutable여부이다.  
let은 변수에 재할당이 가능하지만,  
const는 변수 재선언, 재할당 모두 불가능하다.  


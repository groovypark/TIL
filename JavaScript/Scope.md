# 스코프 (scope)

스코프란 현재 접근할 수 있는 변수들의 범위를 뜻한다. 즉, 변수와 매개변수(parameter)의 접근성과 생존기간을 뜻한다. 따라서 유효범위 개념을 잘 알고 있다면 변수와 매개변수의 접근성과 생존기간을 제어할 수 있다. 

##### 유효범위의 종류

- 전역 유효범위(Global Scope)
  - 스크립트 내 어느 곳에서든 참조된다.
- 지역 유효범위(Local Scope)
  - 정의된 함수 안에서만 참조되는 것을 의미하며, 함수 밖에서는 참조하지 못한다.

### 스코프를 생성하는 구문

- function

  ```javascript
  function f() {
    var a = "a";
  }
  console.log(typeof a === "undefined");	//true
  ```

  함수 외부에서 내부에 선언된 변수에 접근할 수 없다.

- catch

  ```javascript
  try {
    throw new exception("fake exception");
  } catch (err) {
    var test = "test";
    console.log(err instanceof ReferenceError === true); //true
  }
  console.log(test === "test");						 //true
  console.log(typeof err === "undefined");			  //true
  ```

  매개변수(err)들은 새로운 내부 스코프에 포함되어 그다음으로 오는 블록 안에서만 접근할 수 있다. 반면 블록 안에서 새로 정의한 변수(test)들은 블록 외부에서도 접근할 수 있다. 

- with - 사용하지 말아야 할 구문

  ```javascript
  with ({inScope: "inScope"}) {
    var notInScope = "notInScope";
    console.log(inScope === "inScope");		    //true
  }
  console.log(typeof inScope === "undefined");	//true
  console.log(notInScope === "notInScope");	    //true
  ```

  파라미터로 받은 변수만 스코프 내부에서 접근할 수 있다. catch 구문과 마찬가지임.



### with 구문을 자제해야 하는 이유

- 스코프를 생성함으로써 생기는 추가 자원 소모

- 소스의 모호성

  - 변수 이름이 같을 경우

- ECMAScript 6 표준에서 with 구문 제외

- DOM 스타일 설정 문제

  - style에 설정되지 않았던 속성을 추가하고 싶을 때는 with 구문으로 추가할 수 있는 방법이 없다.

    ```javascript
    with (document.getElementById("myDiv").style) {
      background = "yellow";
      color = "red";
      border = "1px solid black";
    }
    ```

  - with 구문의 대체 방안

    ```javascript
    var s = document.getElementById("myDiv").style;
    s.background = "yellow";
    s.color = "red";
    s.border = "1px solid black";
    ```
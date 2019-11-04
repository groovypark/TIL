---
title: 프론트엔드 면접 질문(Frontend Job Interview Questions)
description: 
categories: 
tags: Frontend JavaScript
---

![JavaScript](https://www.zuaneducation.com/blog/wp-content/uploads/2018/09/Interview-Questions-and-Answers.jpg)

이론만 중요한게아니라 실제 어떻게 쓰이는지 알아야함.

### 클로저- 예시코드, 해결방법

* 예시코드
    ```javascript
    var fns = []
    var k = 0;
    (() => {
    for(var i = 0 ;i<10;i++){
        fns.push(function() {
            debugger;
        console.log(i);
        console.log(k);
        })
        k++;
    }
    })();
    fns.forEach(f=>f())
    ```

함수를 fns에 넣고, 나중에 forEach로 실행시킬 때 클로저 발생.  
현재 스코프에 없는 i에 접근하려고 함.  
k는 전역변수이기 때문에 클로저가 아님.  
함수를 모두 넣은 후 i값은 10이 되므로 나중에 forEach에서 실행되는 i값은 10으로 계속 찍히게 된다.  


* 해결방법  
    즉시실행함수를 쓴다.
    ```javascript
    (() => {
        for (var i = 0; i < 10; i++){
            fns.push(function(){
            console.log(i);
            }())
        }
    })();
    ```


### 이벤트, 버블링, 제이쿼리

* 버블링 : 안쪽 div부터 타고 올라가는 방식 (defualt값)
* 캡쳐링 : 바깥쪽 div부터 타고 내려가는 방식 (옵션값으로 변경 가능)

```html
<body>
    <div class="a">
        <div class="b">
        </div>
    </div>
</body>
</html>

<script>
    const handler = (e) => {
            console.log(e.currentTarget.className);
    };
    document.getElementsByClassName('a')[0].addEventListener('click', handler, true);   // addEventListener의 세번째 값이 true면 캡처링, false면 버블링. defualt는 false
    document.getElementsByClassName('b')[0].addEventListener('click', handler);
</script>

<style>
    .a {
        width: 550px;
        height: 530px;
        background: yellow;
    }
    .b {
        width: 250px;
        height: 230px;
        background: red;
    }
</style>
```

* 중단 방법
    ```javascript
    event.stopPropagation()
    ```

*참고링크 - [event-bubbling-capturing](https://wonism.github.io/event-bubbling-capturing/)*

### 호이스팅

1. 선언문을 읽음
2. 위에서 부터 실행

```javascript
console.log(test);
var test = 'test'
```
다른 언어라면, test가 없다고 에러가 발생했겠지만  
var test;를 호이스트하기 때문에 `undefined`라고 하고 넘어간다.

함수 호이스팅은 함수를 끌어올리지만 변수의 값은 끌어올리지 않는다. (아래 함수표현식, 선언식에서 확인)

### 함수표현식, 선언식

- 선언식
    ```javascript
    console.log(test())
    var test = () => {
    }
    // 에러발생. Uncaught TypeError: test is not a function
    ```
- 함수표현식
    ```javascript
    console.log(test())
    function test(){
    }
    // 정상작동. test 함수에 대한 선언을 호이스팅하여 global 객체에 등록시키기 때문
    ```

*참고링크 - [function expressions vs declarations](https://joshua1988.github.io/web-development/javascript/function-expressions-vs-declarations/)*

<!-- TODO -->
### 클래스 프로토타입

```javascript
function func1() {
	var a = 1;
	var b = 2;
}
func1.prototype.sum = function sum(){
	return this.a+this.b;
}

function func2() {
	var a = 1;
	var b = 2;
	function sum(){
        return this.a+this.b;
    }
}

var func1 = new func1();
var func2 = new func2();

// TODO 
console.log(func1.sum() == func2.sum());
```

*참고링크 - [[Javascript ] 프로토타입 이해하기](https://medium.com/@bluesh55/javascript-prototype-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-f8e67c286b67)*

### es3와 es6차이점

### .call()

### 투두엠븨씨 - 웹팩사용해서 es6문법으로 만들기

### 기타 - 함수 만들어 쓰기

```javascript
const calculate = {
    sum(a,b) {
        return a + b;
    },
	substract(a,b) {
		return a -b;
    },
	multiply(a,b) {
		return a*b;
    }
}
calcultate.sum(1,2) //3
```

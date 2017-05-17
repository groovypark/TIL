---
layout: post
title: JavaScript
tags: [git, github, javascript]
---

JavaScript는 웹페이지를 동적으로, 프로그래밍적으로 제어하기 위해서 고안된 언어이다. 웹브라우저에서 유일하게 사용할 수 있는 프로그래밍 언어이다. 최근에는 자바스크립트가 웹을 벗어나서 광범위하게 사용되고 있다.

[http://opentutorials.org/course/50](http://opentutorials.org/course/50)
JavaScript 사전



### 숫자와 문자

자바스크립트에서는 큰따옴표나 작은따옴표가 붙지 않은 숫자는 숫자로 인식한다.

`alert(1.2 + 1.3);`	`alert(2 * 5);` 	`alert(6 / 2)`

```
Math.pow(3,2);		// 9,	3의 2승
Math.round(10.6);	// 11,	10.6을 반올림
Math.ceil(10.2);	// 11,	10.2를 올림
Math.floor(10.6);	// 10,	10.6을 내림
Math.sqrt(9);		// 3,	3의 제곱근
Math.random();		// 0부터 1.0 사이의 랜덤한 숫자
```



문자는 "(큰 따옴표) 혹은 '(작은 따옴표) 중의 하나로 감싸야 한다. String이라고 한다.

`alert('groovypark\'s coding');`	

`alert(typeof "1");` 	결과 : string	(typeof : 값의 데이터 형을 알려줌)







### 변수

변수는 var로 시작한다.  var은 변수를 선언하겠다는 것을 의미한다. 



### 비교 연산자

**==**

동등 연산자로 좌항과 우항을 비교해서 서로 값이 같다면 true 다르면 false.

**===**

일치 연산자로 좌항과 우항이 '정확'하게 같을 때 true 다르면 false.

즉, **데이터 형이 같은 경우에만 같다고 판단.** 따라서 == 연산자 대신 === 연산자를 쓰는 것을 강력하게 권한다.



### 문법

**prompt()함수 - String prompt([String message], [String defaultValue])**

`prompt(' ');`  

- 문자열을 입력할 때 사용
- 숫자를 입력 받아야 하는 경우는 문자열로 입력 받은 뒤 변환
- 첫번째 매개변수는 입력 창에서 띄워줄 메시지
- 두번째 매개변수는 입력 부분의 기본 값



**document.write()**

`document.write("출력할 내용");`

문서를 출력해줌.


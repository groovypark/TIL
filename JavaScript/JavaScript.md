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


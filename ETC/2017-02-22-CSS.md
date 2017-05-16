---
layout: post
title: CSS
---

## CSS소개

HTML안에 섞여 있었던 디자인의 기능이 CSS로 분화됨.

1. HTML이 정보에 전념하게 하기 위해서
2. CSS라고 하는 언어는 디자인에 훨씬 더 효율적인 문법체계를 가지고 있기 때문에





## 선택자

### 선택자와 선언

어떤 태그를 디자인하기 위해서는 디자인하려는 태그를

1. 선택하고 (선택자)
2. 선택한 대상에게 효과를 줘야 한다. (선언)





### 선택자의 종류

- 태그 선택자

  모든 선택자에 디자인 적용.

   `li{ color:red; }`

- 아이디 선택자

  고유한 하나의 태그에만 아이디 부여해서 디자인 적용.

  `#select{ font-size:50px; }`

  `<li id="select"> </li>`

- 클래스 선택자

  여러 개의 태그를 클래스로 그룹핑해서 디자인 적용.

  `.deactive{ text-decoration: line-through; }`

  `<li class="deactive"> </li>`




### 부모 자식 선택자

- 조상 자손 선택자

  `ul li{ color:red; }`

- 부모 자식 선택자

  `#lecture>li{ border:1px solid red; }`

- 중복해서 사용하는 경우

  `ul,ol{ background-color: powderblue; }`



### 선택자 공부 팁

[http://flukeout.github.io/](http://flukeout.github.io/)

CSS 선택자를 게임의 형식을 통해서 익힐 수 있는 사이트



### 가상 클래스 선택자

링크와 관련된 가상 클래스 선택자

- :link - 방문한 적이 없는 링크
- :visited - 방문한 적이 있는 링크
- :hover - 마우스를 롤오버 했을 때
- :active - 마우스를 클릭했을 때

**위의 선택자는 순서대로 지정하는 것이 좋습니다.** 특히 visited의 경우는 보안상의 이유로 아래와 같은 속성만 변경이 가능합니다.

- color
- background-color
- border-color
- outline-color
- The color parts of the fill and stroke properties


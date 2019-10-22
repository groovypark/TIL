# var, let, const / let, const 차이

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

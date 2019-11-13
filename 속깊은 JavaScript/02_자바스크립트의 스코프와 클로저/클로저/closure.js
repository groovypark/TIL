// 클로저의 예
function outer () {
    var count = 0;
    var inner = function () {
        return ++count;
    };
    return inner;
}
var increase = outer();

console.log(increase());    // 1
console.log(increase());    // 2

// 클로저는 스코프안에 스코프 즉, function 안에 function 이 선언되었을 때이다.
// 원래 count는 outer() 함수의 로컬 변수이므로 일반적인 방법으로는 외부에서 접근할 수 없다. 하지만, inner 함수가 호출되어 count 변수의 값을 증가시킨다.
// 마치 객체지향 언어에서 'private 변수'와 비슷하다.

// ---
// 클로저의 응용 예
function outer () {
    var count = 0;
    return {
        increase: function () {
            return ++count;
        },
        decrease: function () {
            return --count;
        }
    };
}
var counter = outer();
console.log(counter.increase());    //1
console.log(counter.increase());    //2
console.log(counter.decrease());    //1

var counter2 = outer();
console.log(counter2.increase());   //1

// counter와 counter2 변수는 함수가 호출될 때 별도의 스코프가 생성되어 count변수가 따로 저장된다.
// 하지만 함수간 공유할 수 있게 count를 static 변수로 만들수 있을까?

// ---
// 클로저로 구현하는 static 변수
var countFactory = (function () {
    var staticCount = 0;
    return function () {
        var localCount = 0;
        return {
            increase: function () {
                return {
                    static: ++staticCount,
                    local: ++localCount
                };
            },
            decrease: function () {
                return {
                    static: --staticCount,
                    local: --localCount
                };
            }
        };
    };
}());

var counter = countFactory(), counter2 = countFactory();
console.log(counter.increase());    // {static: 1, local: 1}
console.log(counter.increase());    // {static: 2, local: 2}
console.log(counter2.decrease());   // {static: 1, local: -1}
console.log(counter.increase());    // {static: 2, local: 3}

// IIFE로 스코프를 하나 더 추가하여 클로저 생성.

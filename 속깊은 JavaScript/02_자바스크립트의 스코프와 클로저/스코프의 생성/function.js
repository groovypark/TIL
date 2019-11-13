function foo() {
    var b = "Can you access me?";
}
console.log(typeof b === "undefined");

// for-loop는 블록 외부에서 내부에 있는 변수에 접근 가능.
// foo()는 함수이기 때문에 외부에서 내부에 선언된 변수에 접근 불가능.
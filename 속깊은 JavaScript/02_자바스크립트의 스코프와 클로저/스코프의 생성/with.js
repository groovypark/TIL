with ({inScope: "You can't see me"}) {
    var notInScope = "but you can see me";
    console.log(inScope === "You can't see me");
}
console.log(typeof inScope === "undefined");
console.log(notInScope === "but you can see me");

// with구문은 eval구문과 함께 사용해야하지 말아야 할 구문이다.
// with구문을 이용하면 바로 스코프를 생성함으로써 생기는 추가 자원 소모가 일어난다.
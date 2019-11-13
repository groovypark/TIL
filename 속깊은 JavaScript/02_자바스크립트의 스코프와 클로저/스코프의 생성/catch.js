try {
    throw new exception("face exception");
} catch (err) {
    var test = "can you see me";
    console.log(err instanceof ReferenceError === true);
}
console.log(test === "can you see me");
console.log(typeof err === "undefined");

// err 변수는 catch 블록에서는 접근할 수 있지만, 외부에서는 접근할 수 없다.
// test 변수는 catch 블록 외부에서도 접근할 수 있다.
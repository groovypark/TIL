# LinkedList

```javascript
class Node{
  constructor(val){
    this.val = val;
    this.next = null;
  }
}
class LinkedList{
  constructor(){
    this.head = new Node("head");
    this.tail = this.head;
  }
  add(val){
      let newNode = new Node(val);
      let tailNode = this.tail;
      tailNode.next = newNode;
      this.tail = newNode;
      return newNode;
  }
  find(val){
    let currNode = this.head;
    while(currNode.val !== val){
      if(!currNode.next) {
        return null;
      }
      currNode = currNode.next;
    }
    return currNode;
  }
  
  remove(val){
    let currNode = this.head;
    while(currNode.next) {
      if (currNode.next.val === val){
        if(currNode.next === this.tail) {
          currNode.next = null;
          this.tail = currNode;
          return true;
        }
        currNode.next = currNode.next.next;
        return true;
      }
      currNode = currNode.next;
    }
    return null
  }
}

let linkedList = new LinkedList();
linkedList.add(1);
linkedList.add(2);
linkedList.add(3);
linkedList.add(4);

linkedList.find(1);
linkedList.find(4);

linkedList.remove(4);
linkedList.remove(2);
```

*참고링크 - [연결 리스트(Linked List)](https://takeuu.tistory.com/172), [자료구조 연결리스트](https://jeong-pro.tistory.com/126)*

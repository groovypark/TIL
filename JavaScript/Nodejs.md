---
layout: post
title: Nodejs
tags: [git, github, nodejs]
---

Nodejs에서 제공하는 기본 코드

```const http = require(&#39;http&#39;);
const hostname = '127.0.0.1';

const port = 1337;

http.createServer((req, res) => {

  res.writeHead(200, { 'Content-Type': 'text/plain' });

  res.end('Hello World\n');

}).listen(port, hostname, () => {

  console.log(Server running at http://${hostname}:${port}/);

});

```

**http.createServer**

createServer를 이용하여 서버를 생성. 

**listen(port, hostname, ()**

서버를 이용하여 이 컴퓨터에 리스닝을 시킴.  변수로 port, hostname을 전달. port번호를 리스닝하도록 시키고 사용자가 hostname으로 접속했을 때 응답하라는 명령어.

**res.end('Hello World\n'); **

Hello World라는 텍스트를 응답하도록 하는 코드.

\*  Ctrl+c : 콘솔창에서 실행중인 서버를 종료함 (나감).




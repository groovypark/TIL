---
layout: post
title: GIT
---

# GIT 명령어

### 기존 프로젝트를 그대로 Github 저장소에 올리기

**두가지 방법**

1. Repo를 새로 만들고 기존 프로젝트 파일을 몽땅 옮겨준 후 커밋한다.

2. Repo를 새로 만들고 기존 프로젝트 폴더에서 `git init`을 한 후 `remote` 연결을 하고 푸시한다.

   > \# 업로드 할 프로젝트 폴더로 이동 후 git repo 만들기
   >
   > `git init`
   >
   > \# 원격 Repo와 연결. 저장소이름을 origin이라고 하면 편함
   >
   > `git remote add 저장소이름 https://github.com/아이디/원격저장소이름.git`
   >
   > \#상태확인
   >
   > `git status`
   >
   > \# 프로젝트 파일 모두 추가
   >
   > `git add .`
   >
   > \# 커밋하기
   >
   > `git commit -m "커밋 메시지"`
   >
   > `git push 저장소이름 master`
   >
   > \#최신상태로 업데이트
   >
   > `git pull 저장소이름 master`




- clear : 창을 깨끗하게 지워줌
- git add 파일명 : untracked files의 파일들을 git가 추적하도록 하거나 파일은 수정했지만 아직 스테이징 영역에 올라가지 않은(Changed but not updated) 파일들을 스테이징 영역에 올립니다.


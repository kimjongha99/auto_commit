#!/bin/bash

date=$(date)
github_Id="kimjongha99"
github_Token=$GITHUB_TOKEN    # 환경 변수에서 토큰 가져오기
github_Address="github.com/kimjongha99/auto_commit.git"
sourceDir="/home/ubuntu/auto_commit/auto_commit"
logFile="./push.log"

cd $sourceDir

# 가상환경 활성화
source venv/bin/activate

# Python 스크립트 실행
python main.py

echo "========= push Start (Date: $date) =========" >> $logFile 2>&1

git add -A
echo "git add -A" >> $logFile 2>&1

git commit -m "$date news update"
echo "git commit completed" >> $logFile 2>&1

git push https://$github_Id:$github_Token@$github_Address >> $logFile 2>&1

echo "========= push OK (Date: $date) =========" >> $logFile 2>&1

#!/bin/bash
date=$(date)
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
git push origin main >> $logFile 2>&1
echo "========= push OK (Date: $date) =========" >> $logFile 2>&1

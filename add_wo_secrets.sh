#!/usr/bin/env bash
git add -A
echo "전채 추가"
git reset requirements.txt
git reset .secrets
echo "시크릿 리콰이어먼츠 제거"
git status
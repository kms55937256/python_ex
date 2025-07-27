#8.3
import os
import sys

print(f"현재 작업 디렉토리: {os.getcwd()}")
print(f"Python 버전: {sys.version}")
print(f"운영체제: {os.name}")
print(f"환경 변수 PATH 일부: {os.environ.get('PATH').split(os.pathsep)[:3]}")

path = "/Users/username/documents/report.txt"
dir_name, file_name = os.path.split(path)
file_base, file_ext = os.path.splitext(file_name)

print("파일 경로 정보:")
print(f"- 디렉토리: {dir_name}")
print(f"- 파일명: {file_base}")
print(f"- 확장자: {file_ext}")

print(f"파일 존재 여부: {os.path.exists(path)}")
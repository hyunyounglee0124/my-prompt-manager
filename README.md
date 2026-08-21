# 👔 남성 패션 블로그 프롬프트 매니저 (My Prompt Manager)

> **"효율적인 패션 블로깅을 위한 나만의 AI 프롬프트 저장소"**  
> 파이썬 기초부터 파일 입출력, Git 버전 관리까지의 학습 과정을 담은 프로젝트입니다.

<br>

## 🚀 프로젝트 개요
남성 패션 블로그를 운영할 때 반복적으로 사용하는 AI 프롬프트(시티보이룩, 워크웨어 등)를 체계적으로 관리하기 위해 개발되었습니다. 단순히 텍스트를 저장하는 것을 넘어, 검색, 즐겨찾기, 데이터 영속성(JSON)을 구현하는 데 초점을 맞췄습니다.

<br>

## ✨ 주요 기능 (Key Features)

| 기능 | 설명 |
| :--- | :--- |
| **📥 데이터 영속성** | `JSON` 형식을 사용하여 프로그램 종료 후에도 데이터가 유지됨 |
| **🔍 스마트 검색** | 제목 키워드 검색 및 카테고리별 필터링 기능 |
| **⭐ 즐겨찾기** | 자주 사용하는 프롬프트를 별도로 관리 (Toggle 방식) |
| **📈 조회수 트래킹** | 어떤 프롬프트를 가장 많이 참조했는지 확인 가능 |
| **🛠 CRUD 완비** | 프롬프트 생성(C), 조회(R), 수정(U), 삭제(D) 기능 제공 |

<br>

## 🛠 기술 스택 (Tech Stack)
- **Language:** ![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)
- **Version Control:** ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)
- **Storage:** JSON (File-based Database)

<br>

## 📂 프로젝트 구조
```text
my-prompt-manager/
├── main.py                # 프로그램 메인 로직 (함수형 구조)
├── fashion_prompts.json   # 프롬프트 데이터 저장 파일 (DB)
└── README.md              # 프로젝트 문서
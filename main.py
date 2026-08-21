import json
import os

# 전역 변수 설정
FILENAME = "fashion_prompts.json"
CATEGORIES = ["코디 가이드", "이미지 생성", "브랜드 분석", "SNS 포스팅"]

def load_data():
    """파일에서 데이터를 불러오거나 남성 패션 초기 데이터를 생성합니다."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        # 남성 패션 맞춤형 초기 데이터 (과제 필수 조건: 3개 이상)
        return [
            {
                "title": "남성 시티보이룩 코디 가이드",
                "content": "20대 남성을 위한 오버핏 시티보이룩 스타일링 팁과 필수 아이템 5가지를 추천해줘.",
                "category": "코디 가이드",
                "views": 0,
                "favorite": False
            },
            {
                "title": "워크웨어 스타일 AI 이미지 프롬프트",
                "content": "빈티지한 워크자켓과 데님을 입은 남성이 오래된 차고 앞에 서 있는 고화질 사진 생성.",
                "category": "이미지 생성",
                "views": 0,
                "favorite": False
            },
            {
                "title": "남성 미니멀룩 브랜드 분석",
                "content": "코스(COS)와 아르켓(ARKET)의 남성복 스타일 차이점과 가성비 대안 브랜드를 분석해줘.",
                "category": "브랜드 분석",
                "views": 0,
                "favorite": False
            }
        ]

def save_data(prompts):
    """데이터를 JSON 파일로 저장합니다."""
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=4)

def show_menu():
    """메뉴 UI를 출력합니다."""
    print("\n" + "="*45)
    print("👔 남성 패션 블로그 프롬프트 매니저")
    print("="*45)
    print("1. 새 프롬프트 추가")
    print("2. 전체 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 키워드 검색")
    print("5. 상세 내용 보기 (조회수 증가)")
    print("6. 즐겨찾기 등록/해제")
    print("7. 즐겨찾기 목록 확인")
    print("0. 저장 및 종료")
    print("="*45)

def add_prompt(prompts):
    """새로운 남성 패션 프롬프트를 추가합니다."""
    print("\n--- 📝 새 프롬프트 추가 ---")
    title = input("제목: ")
    content = input("내용: ")
    
    print("\n카테고리 선택:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}. {cat}")
    
    try:
        cat_idx = int(input("번호 선택: ")) - 1
        category = CATEGORIES[cat_idx]
    except:
        category = "기타"

    new_item = {
        "title": title,
        "content": content,
        "category": category,
        "views": 0,
        "favorite": False
    }
    prompts.append(new_item)
    print(f"\n✅ '{title}' 추가 완료!")

def list_prompts(prompts):
    """목록을 출력합니다."""
    print(f"\n--- 📋 프롬프트 목록 (총 {len(prompts)}개) ---")
    for i, p in enumerate(prompts):
        fav = "⭐" if p.get("favorite") else "  "
        print(f"[{i}] {fav} {p['title']} ({p['category']}) | 조회수: {p['views']}")

def view_detail(prompts):
    """상세 내용을 확인하고 조회수를 올립니다."""
    list_prompts(prompts)
    try:
        idx = int(input("\n상세히 볼 번호 선택: "))
        p = prompts[idx]
        p['views'] += 1  # 조회수 증가
        print("\n" + "-"*40)
        print(f"제목: {p['title']}")
        print(f"분류: {p['category']}")
        print(f"내용: {p['content']}")
        print(f"조회수: {p['views']}")
        print("-"*40)
    except:
        print("❌ 잘못된 번호입니다.")

def toggle_favorite(prompts):
    """즐겨찾기를 설정하거나 해제합니다."""
    list_prompts(prompts)
    try:
        idx = int(input("\n즐겨찾기 등록/해제할 번호 선택: "))
        prompts[idx]['favorite'] = not prompts[idx]['favorite']
        status = "등록" if prompts[idx]['favorite'] else "해제"
        print(f"✅ '{prompts[idx]['title']}' 즐겨찾기 {status} 완료!")
    except:
        print("❌ 잘못된 번호입니다.")

def main():
    prompts = load_data()
    
    while True:
        show_menu()
        choice = input("선택 : ")
        
        if choice == "1":
            add_prompt(prompts)
        elif choice == "2":
            list_prompts(prompts)
        elif choice == "3":
            cat_query = input("조회할 카테고리명: ")
            filtered = [p for p in prompts if cat_query in p['category']]
            list_prompts(filtered)
        elif choice == "4":
            keyword = input("검색어 입력: ")
            filtered = [p for p in prompts if keyword in p['title'] or keyword in p['content']]
            list_prompts(filtered)
        elif choice == "5":
            view_detail(prompts)
        elif choice == "6":
            toggle_favorite(prompts)
        elif choice == "7":
            fav_list = [p for p in prompts if p.get("favorite")]
            list_prompts(fav_list)
        elif choice == "0":
            save_data(prompts)
            print("💾 데이터가 저장되었습니다. 프로그램을 종료합니다.")
            break
        else:
            print("❌ 잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()

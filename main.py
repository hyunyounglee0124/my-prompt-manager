import json
import os
import csv
import webbrowser 

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
    print("8. 마크다운으로 내보내기")
    print("9. CSV로 내보내기")
    print("10. 통계 보기")
    print("11. 삭제하기")
    print("0. 저장 및 종료")
    print("0. 저장 및 종료")
    print("="*45)

def add_prompt(prompts):
    """새로운 남성 패션 프롬프트를 추가합니다."""
    print("\n--- 📝 새 프롬프트 추가 ---")
    title = input("제목: ")
    content = input("내용: ")
def add_prompt(prompts):
    title = input("제목: ")
    content = input("내용: ")
    url = input("참고 URL (없으면 엔터): ") # <--- 추가
    
    # ... 카테고리 선택 코드 생략 ...

    new_item = {
        "title": title,
        "content": content,
        "category": category,
        "url": url if url else "없음", # <--- 추가
        "views": 0,
        "favorite": False
    }
    prompts.append(new_item)
    
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
        idx = int(input("\n상세히 볼 번호를 입력하세요: "))
        p = prompts[idx]
        p['views'] += 1  # 조회수 증가

        print("\n" + "-"*40)
        print(f"제목: {p['title']}")
        print(f"분류: {p['category']}")
        print(f"내용: {p['content']}")
        
        # --- 링크 출력 및 자동 열기 기능 추가 ---
        url = p.get('url', '없음') 
        print(f"링크: {url}")
        print(f"조회수: {p['views']}")
        print("-"*40)

        # 링크가 http로 시작하면 자동으로 브라우저 실행
        if url.startswith("http"):
            print(f"\n🔗 연결된 링크(동영상/이미지)를 브라우저에서 엽니다...")
            webbrowser.open(url)
        # ---------------------------------------

    except (ValueError, IndexError):
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

def export_to_markdown(prompts):
    """프롬프트를 카테고리별로 정리하여 Markdown 파일로 저장합니다."""
    if not prompts:
        print("❌ 내보낼 데이터가 없습니다.")
        return

    filename = "prompt_export.md"
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("# 🚀 나의 프롬프트 저장소\n\n")
            
            for category in CATEGORIES:
                f.write(f"## 📂 {category}\n")
                # 해당 카테고리에 속하는 프롬프트만 필터링
                category_items = [p for p in prompts if p['category'] == category]
                
                if not category_items:
                    f.write("*(등록된 프롬프트가 없습니다)*\n\n")
                    continue
                    
                for p in category_items:
                    fav = "⭐" if p.get('favorite') else ""
                    f.write(f"### {p['title']} {fav}\n")
                    f.write(f"- **조회수:** {p.get('views', 0)}\n")
                    f.write(f"- **내용:**\n  ```text\n  {p['content']}\n  ```\n\n")
        
        print(f"✅ '{filename}' 파일로 내보내기가 완료되었습니다!")
    except Exception as e:
        print(f"❌ 파일 저장 중 오류 발생: {e}")
def export_to_csv(prompts):
    """프롬프트를 CSV 파일로 저장합니다."""
    if not prompts:
        print("❌ 내보낼 데이터가 없습니다.")
        return
    filename = "prompts_data.csv"
    try:
        with open(filename, "w", newline="", encoding="utf-8-sig") as f:
            fieldnames = ["title", "category", "views", "favorite", "content", "url"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for p in prompts:
                writer.writerow({
                    "title": p['title'],
                    "category": p['category'],
                    "views": p.get('views', 0),
                    "favorite": "O" if p.get('favorite') else "X",
                    "content": p['content'],
                    "url": p.get('url', '없음')
                })
        print(f"✅ '{filename}' 저장 완료!")
    except Exception as e:
        print(f"❌ 오류 발생: {e}")

def show_statistics(prompts):
    """데이터 통계를 보여줍니다."""
    if not prompts: return
    total = len(prompts)
    total_views = sum(p.get('views', 0) for p in prompts)
    most_viewed = max(prompts, key=lambda x: x.get('views', 0))
    print(f"\n📊 총 개수: {total}개 | 총 조회수: {total_views}회")
    print(f"🔥 인기 1위: {most_viewed['title']} ({most_viewed['views']}회)")

def delete_prompt(prompts):
    """프롬프트를 삭제합니다."""
    list_prompts(prompts)
    try:
        idx = int(input("\n🗑️ 삭제할 번호 (취소 -1): "))
        if idx != -1:
            removed = prompts.pop(idx)
            print(f"✅ '{removed['title']}' 삭제되었습니다.")
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
        elif choice == "8":
            export_to_markdown(prompts)
        elif choice == "9": 
            export_to_csv(prompts)
        elif choice == "10": 
            show_statistics(prompts)
        elif choice == "11": 
            delete_prompt(prompts)
            save_prompts(prompts)
        elif choice == "0":
            save_data(prompts)
            print("💾 데이터가 저장되었습니다. 프로그램을 종료합니다.")
            break
        else:
            print("❌ 잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()

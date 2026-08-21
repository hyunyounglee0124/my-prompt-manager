import json
import os

def main():
    filename = "prompts.json"
    categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]
    prompts = []

    # 파일에서 데이터 불러오기
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            prompts = json.load(f)

    while True:
        print("\n=== 📋 나만의 프롬프트 관리 ===")
        print("1. 프롬프트 추가")
        print("2. 프롬프트 목록")
        print("3. 카테고리별 조회")
        print("4. 프롬프트 검색")
        print("5. 프롬프트 상세 보기")
        print("6. 즐겨찾기 관리 (등록/해제)")
        print("7. 즐겨찾기 목록")
        print("0. 종료")
        
        choice = input("선택: ")

        if choice == "1":
            print("\n=== 프롬프트 추가 ===")
            title = input("제목: ")
            content = input("내용: ")
            print("\n카테고리 선택:")
            for i, cat in enumerate(categories, 1):
                print(f"{i}) {cat}")
            cat_choice = int(input("선택: ")) - 1
            
            new_item = {
                "title": title, "content": content,
                "category": categories[cat_choice], "favorite": False
            }
            prompts.append(new_item)
            print("✅ 프롬프트가 추가되었습니다!")

        elif choice == "2":
            print("\n=== 프롬프트 목록 ===")
            for i, p in enumerate(prompts, 1):
                star = "⭐" if p.get('favorite') else ""
                print(f"{i}. [{p['category']}] {p['title']} {star}")
            print(f"\n총 {len(prompts)}개의 프롬프트")

        elif choice == "3":
            print("\n=== 카테고리별 조회 ===")
            for i, cat in enumerate(categories, 1): print(f"{i}) {cat}")
            cat_idx = int(input("선택: ")) - 1
            selected_cat = categories[cat_idx]
            filtered = [p for p in prompts if p['category'] == selected_cat]
            for i, p in enumerate(filtered, 1):
                print(f"{i}. {p['title']} {'⭐' if p.get('favorite') else ''}")

        elif choice == "4":
            search_word = input("\n검색어: ")
            results = [p for p in prompts if search_word in p['title'] or search_word in p['content']]
            for i, p in enumerate(results, 1):
                print(f"{i}. [{p['category']}] {p['title']}")
            print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")

        elif choice == "5":
            idx = int(input("\n상세 보기 할 번호 입력: ")) - 1
            p = prompts[idx]
            print("─" * 30)
            print(f"제목: {p['title']}\n카테고리: {p['category']}\n즐겨찾기: {'⭐' if p.get('favorite') else 'X'}")
            print("─" * 30)
            print(f"내용:\n{p['content']}\n" + "─" * 30)

        elif choice == "6":
            idx = int(input("\n즐겨찾기 등록/해제할 번호 입력: ")) - 1
            prompts[idx]['favorite'] = not prompts[idx].get('favorite', False)
            print(f"'{prompts[idx]['title']}' 상태 변경 완료!")

        elif choice == "7":
            print("\n=== 즐겨찾기 목록 ===")
            for i, p in enumerate([p for p in prompts if p.get('favorite')], 1):
                print(f"{i}. [{p['category']}] {p['title']} ⭐")

        elif choice == "0":
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(prompts, f, ensure_ascii=False, indent=4)
            print("종료합니다. 데이터가 저장되었습니다.")
            break

if __name__ == "__main__":
    main()
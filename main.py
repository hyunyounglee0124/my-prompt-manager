def main():
    # 프롬프트들을 저장할 빈 리스트(바구니)를 만듭니다.
    prompts = []

    while True:
        print("\n--- 📝 프롬프트 관리자 ---")
        print("1. 프롬프트 추가")
        print("2. 프롬프트 전체 보기")
        print("3. 종료")

        choice = input("원하는 메뉴 번호를 선택하세요: ")

        if choice == "1":
            # 사용자로부터 프롬프트를 입력받습니다.
            new_prompt = input("저장할 프롬프트를 입력하세요: ")
            # 리스트(바구니)에 추가합니다.
            prompts.append(new_prompt)
            print(f"\n✅ '{new_prompt}' 가 저장되었습니다!")

        elif choice == "2":
            # 저장된 프롬프트들을 보여줍니다.
            print("\n--- 📋 저장된 프롬프트 목록 ---")
            if not prompts:
                print("저장된 프롬프트가 없습니다.")
            else:
                for i, p in enumerate(prompts, 1):
                    print(f"{i}. {p}")

        elif choice == "3":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()
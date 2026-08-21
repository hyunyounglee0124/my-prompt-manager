print("hello Python")
print("hello Python")
print("GitHub 연결 성공!")

def main():
    while True:
        print("\n--- 📝 프롬프트 관리자 ---")
        print("1. 프롬프트 추가")
        print("2. 프롬프트 전체 보기")
        print("3. 종료")
        
        choice = input("원하는 메뉴 번호를 선택하세요: ")
        
        if choice == "1":
            print("\n(아직 개발 중...) 프롬프트를 추가하는 기능을 만들 예정입니다.")
        elif choice == "2":
            print("\n(아직 개발 중...) 저장된 프롬프트를 보여주는 기능을 만들 예정입니다.")
        elif choice == "3":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()
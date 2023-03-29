# 컴퓨터공학과 20234005 박재현
print("컴퓨터공학과 20234005 박재현")

print("\n")

A = "철학"; A10 = "형이상학"; A20 = "논리학"; A30 = "동서양철학" 
A11 = "형이상학과 탈형이상학"; A12 = "윤리형이상학"; A13 = "도덕형이상학"
A21 = "논리학 입문"; A22 = "기호논리학"; A23 = "논리학 추론과 증명"
A31 = "논어, 사람의 길을 열다"; A32 = "서양철학사"; A33 = "자유론"
B = "종교"; B10 = "불교"; B20 = "기독교"; B30 = "이슬람교"
B11 = "초기불교입문"; B12 = "반야심경"; B13 = "도표로 읽는 불교 교리"
B21 = "순전한 기독교"; B22 = "살이있는 신"; B23 = "나는 왜 믿는가"
B31 = "쿠란"; B32 = "이슬람의 모든 것"; B33 = "무슬림 전도학 개론"
C = "사회과학"; C10 = "통계학"; C20 = "경제학"; C30 = "정치학"
C11 = "수리통계학개론"; C12 = "예제를 통한 회귀분석"; C13 = "통계의 미학"
C21 = "자본론"; C22 = "거시경제학"; C23 = "국부론"
C31 = "정치학 개론"; C32 = "국제관계이론"; C33 = "정치사상사"
D = "자연과학"; D10 = "수학"; D20 = "물리학"; D30 = "생명과학"
D11 = "수학의 쓸모"; D12 = "틀리지 않는 법"; D13 = "페르마의 마지막 정리"
D21 = "모든 순간의 물리학"; D22 = "현대물리학"; D23 = "시간은 흐르지 않는다"
D31 = "이중나선"; D32 = "세상을 바꾼 생명과학"; D33 = "사피엔스"
E = "기술과학"; E10 = "의학"; E20 = "건축공학"; E30 = "기계공학"
E11 = "의학생리학"; E12 = "쉽게 풀어쓴 의학용어"; E13 = "임상화학"
E21 = "구조와 건축"; E22 = "건축공학개론"; E23 = "다음 세대가 살고 싶은 공간"
E31 = "도구와 기계의 원리"; E32 = "적정기술의 이해"; E33 = "제어 시스템 공학"
F = "예술"; F10 = "건축물"; F20 = "조형예술"; F30 = "공예미술"
F11 = "건축, 예술과 하나되다"; F12 = "건축은 공학인가 예술인가"; F13 = "세상을 뒤흔든 건축미술"
F21 = "조형예술의 역사적 문법"; F22 = "새로운 조형예술의 이해"; F23 = "조형예술과 자연의 관계"
F31 = "세계현대공예미술"; F32 = "전통공예 5인전"; F33 = "공예LIBRARY"

print("\n")

select = 0
recomcat = 0
recomnum = 0
import random
recomcat = random.choice('ABCDEF')
recomnum = ('11','12','13','21','22','23','31','32','33')
recomnum = random.choice(recomnum)
searchcat = 0
selectcat2 = 0
selectbook = 0
searchcat2 = 0
searchbook = 0
floor = 0
floor2 = 0

print("CSE 도서관에 오신 것을 환영합니다.\n")
print("이 프로그램은 (카테고리/세부 카테고리/도서) 코드를 입력받아 그 위치를 출력하는 프로그램입니다.\n")
print("카테고리 코드는 A~F의 알파벳 한 글자로 이루어져 있으며")
print("세부 카테고리 코드는 'A10', 'F30' 등 카테고리의 뒤에 수 10,20,30을 붙여 나타내고")
print("도서 코드는 'A11', 'F33' 등 코드의 첫째 자리 수에 1,2,3을 대입하여 나타냅니다.\n")
print("지정된 형식 외의 코드를 입력하면 에러가 발생하니 코드를 정확히 기입하여 주시기 바랍니다.\n")
print("코드 목록은 다음과 같습니다.\n")
print("카테고리: A[철학] B[종교] C[사회과학] D[자연과학] E[기술과학] F[예술]\n")
print("세부 카테고리: A10[형이상학] A20[논리학] A30[동서양철학]")
print("               B10[불교] B20[기독교] B30[이슬람교]")
print("               C10[통계학] C20[경제학] C30[정치학]")
print("               D10[수학] D20[물리학] D30[생명과학]")
print("               E10[의학] E20[건축공학] E30[기계공학]")
print("               F10[건축물] F20[조형예술] F30[공예미술]\n")
print("도서: A11[형이상학과 탈형이상학] A12[윤리형이상학] A13[도덕형이상학]\n")
print("     A21[논리학 입문] A22[기호논리학] A23[논리학 추론과 증명]\n")
print("     A31[논어] A32[차라투스트라는 이렇게 말했다] A33[자유론]\n")
print("     B11[초기불교입문] B12[반야심경] B13[도표로 읽는 불교 교리]\n")
print("     B21[순전한 기독교] B22[살아있는 신] B23[나는 왜 믿는가]\n")
print("     B31[쿠란] B32[이슬람의 모든 것] B33[무슬림 전도학 개론]\n")
print("     C11[수리통계학개론] C12[예제를 통한 회귀분석] C13[통계의 미학]\n")
print("     C21[자본론] C22[거시경제학] C23[국부론]\n")
print("     C31[정치학 개론] C32[국제관계이론] C33[정치사상사]\n")
print("     D11[수학의 쓸모] D12[틀리지 않는 법] D13[페르마의 마지막 정리]\n")
print("     D21[모든 순간의 물리학] D22[현대물리학] D23[시간은 흐르지 않는다]\n")
print("     D31[이중나선] D32[세상을 바꾼 생명과학] D33[사피엔스]\n")
print("     E11[의학생리학] E12[쉽게 풀어쓴 의학용어] E13[임상화학]\n")
print("     E21[구조와 건축] E22[건축공학개론] E23[다음 세대가 살고 싶은 공간]\n")
print("     E31[도구와 기계의 원리] E32[적정기술의 이해] E33[제어 시스템 공학]\n")
print("     F11[건축, 예술과 하나되다] F12[건축은 공학인가 예술인가] F13[세상을 뒤흔든 건축미술]\n")
print("     F21[조형예술의 역사적 문법] F22[새로운 조형예술의 이해] F23[조형예술과 자연의 관계]\n")
print("     F31[세계현대공예미술] F32[전통공예 5인전] F33[공예LIBRARY]\n")

print("오늘의 추천 도서는 %s%s 입니다.\n" %(recomcat,recomnum))

select = input("찾으시는 코드 유형을 선택해주세요: ")
while select not in ('카테고리,세부 카테고리,도서'):
    print("Error! 코드 유형은 '카테고리', '세부 카테고리', '도서' 세 가지 입니다.\n")
    select = input("찾으시는 코드 유형을 선택해주세요: ")
print("\n")

if select == "세부 카테고리":
    selectcat2 = "Y"

if select == "도서":
    selectbook = "Y"

if select == "카테고리":
    searchcat = input("찾으시는 카테고리 코드를 입력해주세요: ")
    while searchcat not in ('A,B,C,D,E,F'):
        print("Error! 카테고리 코드는 A-F의 알파벳 '한 글자'만 입력해주세요.\n")
        searchcat = input("찾으시는 카테고리 코드를 입력해주세요: ")
    print("\n")
    if searchcat == "A":
        floor = 1
        print("해당 카테고리는 '%s'이며 %d층의 %s관에 있습니다.\n" %(A,floor,A))
    if searchcat == "B":
        floor = 1
        print("해당 카테고리는 '%s'이며 %d층의 %s관에 있습니다.\n" %(B,floor,B))
    if searchcat == "C":
        floor = 2
        print("해당 카테고리는 '%s'이며 %d층의 %s관에 있습니다.\n" %(C,floor,C))
    if searchcat == "D":
        floor = 2
        print("해당 카테고리는 '%s'이며 %d층의 %s관에 있습니다.\n" %(D,floor,D))
    if searchcat == "E":
        floor = 3
        print("해당 카테고리는 '%s'이며 %d층의 %s관에 있습니다.\n" %(E,floor,E))
    if searchcat == "F":
        floor = 3
        print("해당 카테고리는 '%s'이며 %d층의 %s관에 있습니다.\n" %(F,floor,F))
    selectcat2 = input("세부 카테고리를 찾으시겠습니까? (Y/N) ")
    while selectcat2 not in ('Y,N'):
        print("Error! Y 또는 N을 입력해주세요.\n")
        selectcat2 = input("세부 카테고리를 찾으시겠습니까? (Y/N) ")
    print("\n")
    if selectcat2 == "Y":
        select = "세부 카테고리"
    else:
        selectbook = input("도서를 찾으시겠습니까? (Y/N) ")
        while selectbook not in ('Y,N'):
            print("Error! Y 또는 N을 입력해주세요.\n")
            selectbook = input("도서를 찾으시겠습니까? (Y/N) ")
        if selectbook == "Y":
            select = "도서"
        else:
            select = 0
            print("\n")
            print("이용해 주셔서 감사합니다.")
            print("\n")            

if select == "세부 카테고리":
    searchcat2 = input("찾으시는 세부 카테고리 코드를 입력해주세요: ")
    while searchcat2 not in ('A10,A20,A30,B10,B20,B30,C10,C20,C30,D10,D20,D30,E10,E20,E30,F10,F20,F30'):
        print("Error! 세부 카테고리 코드는 'A10', 'F30' 등 카테고리의 뒤에 수 10,20,30을 붙여 나타냅니다.\n")
        searchcat2 = input("찾으시는 세부 카테고리 코드를 입력해주세요: ")
    print("\n")
    if searchcat2 == "A10":
        floor2 = 1
        print("해당 세부 카테고리는 '%s'이며 %s관의 %d층 칸에 있습니다.\n" %(A10,A,floor2))
    if searchcat2 == "A20":
        floor2 = 2
        print("해당 세부 카테고리는 '%s'이며 %s관의 %d층 칸에 있습니다.\n" %(A20,A,floor2))
    if searchcat2 == "A30":
        floor2 = 3
        print("해당 세부 카테고리는 '%s'이며 %s관의 %d층 칸에 있습니다.\n" %(A30,A,floor2))
    if searchcat2 == "B10":
        floor2 = 1
        print("해당 세부 카테고리는 '%s'이며 %s관의 %d층 칸에 있습니다.\n" %(B10,B,floor2))
    if searchcat2 == "B20":
        floor2 = 2
        print("해당 세부 카테고리는 '%s'이며 %s관의 %d층 칸에 있습니다.\n" %(B20,B,floor2))
    if searchcat2 == "B30":
        floor2 = 3
        print("해당 세부 카테고리는 '%s'이며 %s관의 %d층 칸에 있습니다.\n" %(B30,B,floor2))
    if searchcat2 == "C10":
        floor2 = 1
        print("해당 세부 카테고리는 '%s'이며 %s관의 %d층 칸에 있습니다.\n" %(C10,C,floor2))
    if searchcat2 == "C20":
        floor2 = 2
        print("해당 세부 카테고리는 '%s'이며 %s관의 %d층 칸에 있습니다.\n" %(C20,C,floor2))
    if searchcat2 == "C30":
        floor2 = 3
        print("해당 세부 카테고리는 '%s'이며 %s관의 %d층 칸에 있습니다.\n" %(C30,C,floor2))
    if searchcat2 == "D10":
        floor2 = 1
        print("해당 세부 카테고리는 '%s'이며 %s관의 %d층 칸에 있습니다.\n" %(D10,D,floor2))
    if searchcat2 == "D20":
        floor2 = 2
        print("해당 세부 카테고리는 '%s'이며 %s관의 %d층 칸에 있습니다.\n" %(D20,D,floor2))
    if searchcat2 == "D30":
        floor2 = 3
        print("해당 세부 카테고리는 '%s'이며 %s관의 %d층 칸에 있습니다.\n" %(D30,D,floor2))
    if searchcat2 == "E10":
        floor2 = 1
        print("해당 세부 카테고리는 '%s'이며 %s관의 %d층 칸에 있습니다.\n" %(E10,E,floor2))
    if searchcat2 == "E20":
        floor2 = 2
        print("해당 세부 카테고리는 '%s'이며 %s관의 %d층 칸에 있습니다.\n" %(E20,E,floor2))
    if searchcat2 == "E30":
        floor2 = 3
        print("해당 세부 카테고리는 '%s'이며 %s관의 %d층 칸에 있습니다.\n" %(E30,E,floor2))
    if searchcat2 == "F10":
        floor2 = 1
        print("해당 세부 카테고리는 '%s'이며 %s관의 %d층 칸에 있습니다.\n" %(F10,F,floor2))
    if searchcat2 == "F20":
        floor2 = 2
        print("해당 세부 카테고리는 '%s'이며 %s관의 %d층 칸에 있습니다.\n" %(F20,F,floor2))
    if searchcat2 == "F30":
        floor2 = 3
        print("해당 세부 카테고리는 '%s'이며 %s관의 %d층 칸에 있습니다.\n" %(F30,F,floor2))
    selectbook = input("도서를 찾으시겠습니까? (Y/N) ")
    while selectbook not in ('Y,N'):
        print("Error! Y 또는 N을 입력해 주세요.\n")
        selectbook = input("도서를 찾으시겠습니까? (Y/N) ")
    if selectbook == "Y":
        select = "도서"
    else:
        select = 0
        print("\n")
        print("이용해 주셔서 감사합니다.")
        print("\n")

bookcode = 'A11,A12,A13,A21,A22,A23,A31,A32,A33,B11,B12,B13,B21,B22,B23,B31,B32,B33,C11,C12,C13,C21,C22,C23,C31,C32,C33,D11,D12,D13,D21,D22,D23,D31,D32,D33,E11,E12,E13,E21,E22,E23,E31,E32,E33,F11,F12,F13,F21,F22,F23,F31,F32,F33'

print("\n")
if select == "도서":
    searchbook = input("찾으시는 도서 코드를 입력해주세요: ")
    while searchbook not in bookcode:
        print("Error! 지정된 형식의 도서 코드를 입력해주세요. Ex) A11, F33\n")
        searchbook = input("찾으시는 도서 코드를 입력해주세요: ")
    print("\n")
    if searchbook == 'A11':
        floor = 1
        floor2 = 1
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(A11,floor,A,floor2))
    if searchbook == 'A12':
        floor = 1
        floor2 = 1
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(A12,floor,A,floor2))
    if searchbook == 'A13':
        floor = 1
        floor2 = 1
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(A13,floor,A,floor2))
    if searchbook == 'A21':
        floor = 1
        floor2 = 2
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(A21,floor,A,floor2))
    if searchbook == 'A22':
        floor = 1
        floor2 = 2
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(A22,floor,A,floor2))
    if searchbook == 'A23':
        floor = 1
        floor2 = 2
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(A23,floor,A,floor2))
    if searchbook == 'A31':
        floor = 1
        floor2 = 3
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(A31,floor,A,floor2))
    if searchbook == 'A32':
        floor = 1
        floor2 = 3
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(A32,floor,A,floor2))
    if searchbook == 'A33':
        floor = 1
        floor2 = 3
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(A33,floor,A,floor2))
    if searchbook == 'B11':
        floor = 1
        floor2 = 1
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(B11,floor,B,floor2))
    if searchbook == 'B12':
        floor = 1
        floor2 = 1
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(B12,floor,B,floor2))
    if searchbook == 'B13':
        floor = 1
        floor2 = 1
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(B13,floor,B,floor2))
    if searchbook == 'B21':
        floor = 1
        floor2 = 2
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(B21,floor,B,floor2))
    if searchbook == 'B22':
        floor = 1
        floor2 = 2
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(B22,floor,B,floor2))
    if searchbook == 'B23':
        floor = 1
        floor2 = 2
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(B23,floor,B,floor2))
    if searchbook == 'B31':
        floor = 1
        floor2 = 3
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(B31,floor,B,floor2))
    if searchbook == 'B32':
        floor = 1
        floor2 = 3
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(B32,floor,B,floor2))
    if searchbook == 'B33':
        floor = 1
        floor2 = 3
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(B33,floor,B,floor2))
    if searchbook == 'C11':
        floor = 1
        floor2 = 1
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(C11,floor,C,floor2))
    if searchbook == 'C12':
        floor = 2
        floor2 = 1
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(C12,floor,C,floor2))
    if searchbook == 'C13':
        floor = 2
        floor2 = 1
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(C13,floor,C,floor2))
    if searchbook == 'C21':
        floor = 2
        floor2 = 2
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(C21,floor,C,floor2))
    if searchbook == 'C22':
        floor = 2
        floor2 = 2
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(C22,floor,C,floor2))
    if searchbook == 'C23':
        floor = 2
        floor2 = 2
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(C23,floor,C,floor2))
    if searchbook == 'C31':
        floor = 2
        floor2 = 3
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(C31,floor,C,floor2)) 
    if searchbook == 'C32':
        floor = 2
        floor2 = 3
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(C32,floor,C,floor2))
    if searchbook == 'C33':
        floor = 2
        floor2 = 3
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(C33,floor,C,floor2))   
    if searchbook == 'D11':
        floor = 2
        floor2 = 1
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(D11,floor,D,floor2))
    if searchbook == 'D12':
        floor = 2
        floor2 = 1
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(D12,floor,D,floor2))
    if searchbook == 'D13':
        floor = 2
        floor2 = 1
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(D13,floor,D,floor2))
    if searchbook == 'D21':
        floor = 2
        floor2 = 2
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(D21,floor,D,floor2))
    if searchbook == 'D22':
        floor = 2
        floor2 = 2
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(D22,floor,D,floor2))
    if searchbook == 'D23':
        floor = 2
        floor2 = 2
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(D23,floor,D,floor2))
    if searchbook == 'D31':
        floor = 2
        floor2 = 3
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(D31,floor,D,floor2))
    if searchbook == 'D32':
        floor = 2
        floor2 = 3
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(D32,floor,D,floor2))
    if searchbook == 'D33':
        floor = 2
        floor2 = 3
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(D33,floor,D,floor2))
    if searchbook == 'E11':
        floor = 2
        floor2 = 1
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(E11,floor,E,floor2))
    if searchbook == 'E12':
        floor = 3
        floor2 = 1
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(E12,floor,E,floor2))
    if searchbook == 'E13':
        floor = 3
        floor2 = 1
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(E13,floor,E,floor2))
    if searchbook == 'E21':
        floor = 3
        floor2 = 2
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(E21,floor,E,floor2))
    if searchbook == 'E22':
        floor = 3
        floor2 = 2
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(E22,floor,E,floor2))
    if searchbook == 'E23':
        floor = 3
        floor2 = 2
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(E23,floor,E,floor2))
    if searchbook == 'E31':
        floor = 3
        floor2 = 3
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(E31,floor,E,floor2))
    if searchbook == 'E32':
        floor = 3
        floor2 = 3
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(E32,floor,E,floor2))
    if searchbook == 'E33':
        floor = 3
        floor2 = 3
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(E33,floor,E,floor2))
    if searchbook == 'F11':
        floor = 3
        floor2 = 1
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(F11,floor,F,floor2))
    if searchbook == 'F12':
        floor = 3
        floor2 = 1
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(F12,floor,F,floor2))
    if searchbook == 'F13':
        floor = 3
        floor2 = 1
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(F13,floor,F,floor2))
    if searchbook == 'F21':
        floor = 3
        floor2 = 2
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(F21,floor,F,floor2))
    if searchbook == 'F22':
        floor = 3
        floor2 = 2
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(F22,floor,F,floor2))
    if searchbook == 'F23':
        floor = 3
        floor2 = 2
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(F23,floor,F,floor2))
    if searchbook == 'F31':
        floor = 3
        floor2 = 3
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(F31,floor,F,floor2))
    if searchbook == 'F32':
        floor = 3
        floor2 = 3
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(F32,floor,F,floor2))
    if searchbook == 'F33':
        floor = 3
        floor2 = 3
        print("해당 도서는 '%s'이며 %d층 %s관 %d층 칸에 있습니다.\n"%(F33,floor,F,floor2))
    print("이용해 주셔서 감사합니다.")
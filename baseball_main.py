print('''
어떤 야구 경기가 궁금하신가요?
1. 한국야구(KBO) | 2. 해외야구(MLB, NPB)
''')
num = input("선택 : ")

if num == '1':
    print('''
    한국야구(KBO)의 어떤 것이 궁금하신가요?
    1. 오늘의 경기 결과 | 2. 팀순위 | 3. 투수 순위 | 4. 타자 순위 | 5. 이름으로 찾기
    ''')
    num = input('선택 : ')
    if num == '1' :
        import kbo_today
    
    elif num == '2' :
        import kbo_teamrank





elif num == '2' :
    print('''
    메이저리그(MLB)와 일본프로야구(NPB) 중 어디가 궁금하신가요?
    1. 메이저리그(MLB) | 2. 일본프로야구(NPB)
    ''')
    num = input('선택 : ')
    if num == '1' :
        print('''
        메이저리그(MLB)의 어떤 리그가 궁금하신가요?
        1. 내셔널 리그 | 2. 아메리칸 리그
        ''')
        num = input('선택 : ')
        if num == '1' :
            print('''
            메이저리그 내셔널 리그의 어떤 것이 궁금하신가요?
            1. 오늘의 경기 결과 | 2. 팀순위 | 3. 투수 순위 | 4. 타자 순위 | 5. 이름으로 찾기
            ''')
            num = input('선택 : ')
            if num =='1' :
                import mlb_today
           
            elif num =='2' :
                import mlb_national_teamrank

        elif num == '2' :
            print('''
            메이저리그 아메리칸 리그의 어떤 것이 궁금하신가요?
            1. 오늘의 경기 결과 | 2. 팀순위 | 3. 투수 순위 | 4. 타자 순위 | 5. 이름으로 찾기
            ''')
            num = input('선택 : ')
            if num =='1' :
                import mlb_today

            elif num =='2' :
                import mlb_american_teamrank

    elif num =='2' :
        print('''
        일본프로야구(NPB)의 어떤 리그가 궁금하신가요?
        1. 센트럴 리그 | 2. 퍼시픽 리그
        ''')
        num = input('선택 : ')
        if num =='1' :
            print('''
            센트럴 리그의 어떤 것이 궁금하신가요?
            1. 오늘의 경기 결과 | 2. 팀순위 | 3. 투수 순위 | 4. 타자 순위 | 5. 이름으로 찾기
            ''')
            num = input('선택 : ')
            if num =='1' :
                import npb_today

            elif num =='2' :
                import npb_central_teamrank

        elif num =='2' :
            print('''
            퍼시픽 리그의 어떤 것이 궁금하신가요?
            1. 오늘의 경기 결과 | 2. 팀순위 | 3. 투수 순위 | 4. 타자 순위 | 5. 이름으로 찾기
            ''')
            num = input('선택 : ')
            if num =='1' :
                import npb_today

            elif num =='2' :
                import npb_pacific_teamrank
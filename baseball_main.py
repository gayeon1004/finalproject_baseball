import mylib_kbo_pitcher
import dbdb_kbo_pitcher
import mylib_kbo_batter
import dbdb_kbo_batter

print('''
어떤 야구 경기가 궁금하신가요?
1. 한국야구(KBO) | 2. 해외야구(MLB, NPB)
''')
num = input("선택 : ")

if num == '1':
    import create_kbo_pitcher_tb
    import create_kbo_batter_tb
    print('''
    한국야구(KBO)의 어떤 것이 궁금하신가요?
    1. 오늘의 경기 결과 | 2. 팀순위 | 3. 투수 순위 | 4. 타자 순위 | 5. 이름으로 찾기
    ''')
    num = input('선택 : ')
    if num == '1' :
        import kbo_today
    
    elif num == '2' :
        import kbo_teamrank

    elif num == '3' :
        import kbo_pitcher_rank

    elif num == '4' :
        import kbo_batter_rank

    elif num == '5':
        m_list = mylib_kbo_pitcher.kbo_picher()
        # print(m_list)
        dbdb_kbo_pitcher.save_data(m_list)
        name = input('선수이름입력: ')
        m_list = dbdb_kbo_pitcher.get_one_data(name)
        for m in m_list:
            print(f'{m[0]}위 {m[1]} {m[2]} - 평균자책 : {m[3]} | 승 : {m[4]} | 세이브 : {m[5]} | 탈삼진 : {m[6]} | WHIP : {m[7]} | WAR : {m[8]}')

        m_list = mylib_kbo_batter.kbo_batter()
        # print(m_list)
        dbdb_kbo_batter.save_data(m_list)
        # name = input('선수이름입력: ')
        m_list = dbdb_kbo_batter.get_one_data(name)
        for m in m_list:
            print(f'{m[0]}위 {m[1]} {m[2]} - 타율 : {m[3]} | 홈런 : {m[4]} | 타점 : {m[5]} | 도루 : {m[6]} | OPS : {m[7]} | WAR : {m[8]}')

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

            elif num =='3' :
                import mlb_national_pitcher_rank

            elif num =='4' :
                import mlb_national_batter_rank

            elif num =='5' :
                m_list = mylib_kbo_pitcher.kbo_picher()
                # print(m_list)
                dbdb_kbo_pitcher.save_data(m_list)
                name = input('선수이름입력: ')
                m_list = dbdb_kbo_pitcher.get_one_data(name)
                for m in m_list:
                    print(f'{m[0]}위 {m[1]} {m[2]} - 평균자책 : {m[3]} | 승 : {m[4]} | 세이브 : {m[5]} | 탈삼진 : {m[6]} | WHIP : {m[7]} | WAR : {m[8]}')

                m_list = mylib_kbo_batter.kbo_batter()
                # print(m_list)
                dbdb_kbo_batter.save_data(m_list)
                # name = input('선수이름입력: ')
                m_list = dbdb_kbo_batter.get_one_data(name)
                for m in m_list:
                    print(f'{m[0]}위 {m[1]} {m[2]} - 타율 : {m[3]} | 홈런 : {m[4]} | 타점 : {m[5]} | 도루 : {m[6]} | OPS : {m[7]} | WAR : {m[8]}')

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

            elif num =='3' :
                import mlb_american_pitcher_rank

            elif num =='4' :
                import mlb_american_batter_rank

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

            elif num =='3' :
                import npb_central_pitcher_rank

            elif num =='4' :
                import npb_central_batter_rank

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

            elif num =='3' :
                import npb_pacific_pitcher_rank

            elif num =='4' :
                import npb_pacific_batter_rank
ans = []
def solution(today, terms, privacies):
    y, m, d = map(int, today.split('.')) # 오늘 날짜
    di = {}
    for term in terms: # 약관별 유효기간을 딕셔너리에 담기
        di[term.split()[0]] = int(term.split()[1])

    tc = 1
    for privacy in privacies:
        date, t = privacy.split()
        yy, mm, dd = map(int, date.split('.')) # 가입일자
        n = di[t] # 해당 약관의 유효기간(개월)

        nm = mm + n
        if dd == 1:
            dd = 28
            nm -= 1
        else:
            dd -= 1

        while nm > 12:
            nm -= 12
            yy += 1

        if y>yy or (y==yy and m>nm) or (y==yy and m==nm and d>dd):
            ans.append(tc)
        tc += 1
        
    return ans
import requests

INF = 1000000007
color_to_diff = {
    "gray" : (0, 400),
    "brown" : (400, 800),
    "green" : (800, 1200),
    "cyan" : (1200, 1600),
    "blue" : (1600, 2000),
    "yellow" : (2000, 2400),
    "orange" : (2400, 2800),
    "red" : (3200, 3600),
    "silver" : (3600, 4000),
    "gold" : (4000, INF)
}

def get_problems(lower, upper) :
    res = requests.get("https://kenkoooo.com/atcoder/resources/problem-models.json")
    if res.status_code != 200 : return []

    problem_models = res.json()
    for problem in problem_models.items():
        try:    
            if problem[1]["difficulty"] < 0:
                problem[1]["difficulty"] = 0
        except KeyError:
            problem[1]["difficulty"] = 100000000007
    return [problem[0] for problem in problem_models.items() if lower <= int(problem[1]["difficulty"]) < upper]

def parse(message):
    if message[1] == '-' : return INF, INF

    message += '-'
    left = 1; right = 1
    lower = INF; upper = INF    

    while(right < len(message)) : 
        if message[right] == '-' :
            if left == 1 : lower = int(message[left:right])
            else : upper = int(message[left:right])
            left = right + 1 
        elif not message[right].isdecimal(): 
            return INF,INF 
        right += 1

    if lower == INF or upper == INF : return INF,INF
    return int(lower), int(upper)

def color_req(message):
    color = message
    if color in color_to_diff.keys() :
        diffculties = color_to_diff[color]
        return diffculties[0], diffculties[1]

    return INF, INF

def fix_code_fes_link(contest):
    return "cf" + contest[15:17] + contest[17:len(contest)]

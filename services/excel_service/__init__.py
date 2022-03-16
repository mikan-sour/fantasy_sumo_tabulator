import gspread
import os
import itertools
import time

sa_path = os.path.join(os.getcwd(),".config","gspread","service_account.json")
sa = gspread.service_account(filename=sa_path)
wb = sa.open("March2022FantasySumo")

def get_wb():
    return wb

def get_selected_rikishi(ws):
    raw_list = ws.get("B3:B43")
    return  list(itertools.chain(*raw_list))

def write_data(ws, match_results, drafted_rikishi):
    cell_range = range(3, 44)
    for i, num in enumerate(cell_range):
        if drafted_rikishi[i] == "Total:":
            continue
        print(f'write for {drafted_rikishi[i]}')
        if i in [15,25,35]:
            print(f'sleep for 60 seconds to not hit the API limit at index {i}')
            time.sleep(60)
            print("starting again")
        for mat in match_results:
            rik = drafted_rikishi[i]
            if rik not in mat.values():
                continue
            m = mat["kimarite"]
            winner = mat["winner"]
            loser = mat["loser"]
            l = "Win"
            h = loser
            if rik == loser:
                l = "Lose"
                h = winner

            ws.update(f'H{num}', h)
            ws.update(f'L{num}', l)
            ws.update(f'M{num}', m)


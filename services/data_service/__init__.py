
def data_service(todays_matches):
    match_results = []
    for match in todays_matches:
        summary = {
            "kimarite": match["technic_name_eng"].title()
        }

        east = match["east"]
        west = match["west"]
        if east.get("result_image") == 'result_ic01.gif':
            winner = east.get("shikona_eng")
            loser = west.get("shikona_eng")
        else:
            winner = west.get("shikona_eng")
            loser = east.get("shikona_eng")
        summary.update({"winner": winner})
        summary.update({"loser": loser})

        match_results.append(summary)
    return match_results
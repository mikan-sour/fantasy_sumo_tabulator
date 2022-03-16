import data_client as dc
import services.data_service as ds
import services.excel_service as es
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--day', type=int)
args = parser.parse_args()

def run_app():
    day = args.day
    if day is None:
        day = 2 #
        print(f'Check if running for debugging purposes, using value {day}')


    print(f'Collecting sumo data for day {day}')

    todays_matches = dc.get_data(day)
    match_results = ds.data_service(todays_matches)

    print("fetched and organized match data")
    tab = f'day{day}'
    wb = es.get_wb()
    ws = wb.worksheet(tab)
    ws.update(f'H1', tab)
    drafted_rikishi = es.get_selected_rikishi(ws)

    print("made a list of rikishi")
    es.write_data(ws, match_results, drafted_rikishi)


    print('finished')
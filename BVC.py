import requests
import json
requests.packages.urllib3.disable_warnings()

API_KEY = '1f18b6d0-1b58-4d88-8e7f-67181e7b165c'


def get_analysis(api_key, wav_path):
    res = requests.post("https://token.beyondverbal.com/token",
                        data={"grant_type": "client_credentials", "apiKey": api_key})
    token = res.json()['access_token']
    headers = {"Authorization": "Bearer "+token}
    pp = requests.post("https://apiv3.beyondverbal.com/v3/recording/start", json={"dataFormat": {"type": "WAV"}},
                       verify=False, headers=headers)
    recording_id = pp.json()['recordingId']
    with open(wav_path, 'rb') as wavdata:
        r = requests.post("https://apiv3.beyondverbal.com/v3/recording/"+recording_id,
                          data=wavdata, verify=False, headers=headers)
        return r.json()


def get_mood_groups(api_key, group_name):
    res = requests.post("https://token.beyondverbal.com/token",
                        data={"grant_type": "client_credentials", "apiKey": api_key})
    token = res.json()['access_token']
    headers = {"Authorization": "Bearer " + token}
    resp = requests.get('https://apiv3.beyondverbal.com/v3/moods/{}/{}'.format(group_name, 'en-us'), headers=headers)
    return resp.json()


if __name__ == "__main__":
    """
    # Get analysis results from Pulp fiction sequence
    json_result_pulp_fiction = get_analysis(API_KEY, "bitch_converted.wav")
    with open("analysis_result_pulp_fiction.json", 'w') as f:
        json.dump(json_result_pulp_fiction, f)

    # Get analysis result from Blues Brothers sequence
    json_result_blues_brothers = get_analysis(API_KEY, "wasnt_my_fault_converted.wav")
    with open("analysis_result_blues_brothers.json", 'w') as f:
        json.dump(json_result_blues_brothers, f)

    # Get analysis result from GoT Varys sequence
    json_result_power = get_analysis(API_KEY, "got_s2e3_power_converted.wav")
    with open("analysis_result_got_power.json", 'w') as f:
        json.dump(json_result_power, f)

    # Get analysis result from GoT Tyrion sequence
    json_result_bastard = get_analysis(API_KEY, "got_s1e1_bastard_converted.wav")
    with open("analysis_result_got_bastard.json", 'w') as f:
        json.dump(json_result_bastard, f)
    """

    groups = ["Group7", "Group11", "Group21", "Composite"]
    for group in groups:
        with open("group_table_for_{}.json".format(group), 'w') as file:
            json.dump(get_mood_groups(API_KEY, group_name=group), file)

    print("Done")





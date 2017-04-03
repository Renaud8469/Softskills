import json


def detect_discomfort(analysis_path):
    with open(analysis_path, "rb") as f:
        analysis = json.load(f)["result"]

    moods = []
    for segment in analysis["analysisSegments"]:
        mood_groups = segment["analysis"]["Mood"]
        for mood in mood_groups:
            if "Group7" in mood:
                moods.append(mood["Group7"]["Primary"]["Phrase"])
            if "Group11" in mood:
                moods.append(mood["Group11"]["Primary"]["Phrase"])
            if "Group21" in mood:
                moods.append(mood["Group21"]["Primary"]["Phrase"])
            if "Composite" in mood:
                moods.append(mood["Composite"]["Primary"]["Phrase"])




import json

from src.high_score import HighScoreStore


def test_missing_file_starts_at_zero(tmp_path):
    assert HighScoreStore(tmp_path / "score.json").load() == 0


def test_score_is_saved_and_only_moves_up(tmp_path):
    store = HighScoreStore(tmp_path / "nested" / "score.json")
    assert store.save_if_new_record(12) == 12
    assert store.load() == 12
    assert store.save_if_new_record(4) == 12
    assert json.loads(store.path.read_text()) == {"best_score": 12}


def test_corrupt_file_is_recovered(tmp_path):
    path = tmp_path / "score.json"
    path.write_text("not json", encoding="utf-8")
    store = HighScoreStore(path)
    assert store.load() == 0
    assert store.save_if_new_record(3) == 3


def test_negative_scores_never_become_the_record(tmp_path):
    store = HighScoreStore(tmp_path / "score.json")
    assert store.save_if_new_record(-10) == 0

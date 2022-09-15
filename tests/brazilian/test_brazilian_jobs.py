from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    mock = {"salary": "3000", "title": "Motorista", "type": "full time"}

    assert mock in read_brazilian_file("tests/mocks/brazilians_jobs.csv")

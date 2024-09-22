from mylib.lib import *

data_path = "data/spotify.csv"

# test read_data will work from lib.py
def test_read_data():
    df = read_data(data_path)
    assert df is not None
    assert df.shape == (114000, 21)
    df.head()


# test calc_stats will work from lib.py
def test_calc_stats():
    df = read_data(data_path)
    summary_stats = calc_stats(df)
    # assert that calculations match
    assert summary_stats[summary_stats["column"] == "popularity"]["mean"].values[
        0
    ] == round(df["popularity"].mean(), 2)
    assert summary_stats[summary_stats["column"] == "popularity"]["median"].values[
        0
    ] == round(df["popularity"].median(), 2)
    assert summary_stats[summary_stats["column"] == "popularity"]["std_dev"].values[
        0
    ] == round(df["popularity"].std(), 2)
    print("All assertions passed for calc_stats.")


if __name__ == "__main__":
    test_read_data()
    test_calc_stats()

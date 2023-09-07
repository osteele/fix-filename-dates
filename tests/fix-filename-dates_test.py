import os
import re
from datetime import datetime

from fix_filename_dates import (compute_new_filename, get_filename_pairs,
                                get_filenames)


def test_get_filenames(tmpdir):
    test_dir = tmpdir.mkdir("test_dir")
    test_files = [
        "file1.txt",
        "file2.txt",
        "file3.txt",
        "file4.txt",
        "file5.txt",
    ]

    for file in test_files:
        with open(os.path.join(test_dir, file), "w") as f:
            f.write("test")

    expected_files = [
        os.path.join(test_dir, "file1.txt"),
        os.path.join(test_dir, "file2.txt"),
        os.path.join(test_dir, "file3.txt"),
        os.path.join(test_dir, "file4.txt"),
        os.path.join(test_dir, "file5.txt"),
    ]
    actual_files = list(get_filenames([test_dir]))
    assert set(expected_files) == set(actual_files)


def test_compute_new_filename(tmpdir):
    test_dir = tmpdir.mkdir("test_dir")
    test_files = [
        "file1.txt",
        "file2.txt",
        "file3.txt",
        "file4.txt",
        "file5.txt",
    ]

    test_dates = [
        "January 1, 2022",
        "February 2, 2022",
        "March 3, 2022",
        "April 4, 2022",
        "May 5, 2022",
    ]

    for i, file in enumerate(test_files):
        date = test_dates[i]
        date_str = datetime.strptime(date, "%B %d, %Y").strftime("%Y-%m-%d")
        new_filename = f"file_{date_str}.txt"
        with open(os.path.join(test_dir, file), "w") as f:
            f.write("test")

    expected_filenames = [
        "file_2022-01-01.txt",
        "file_2022-02-02.txt",
        "file_2022-03-03.txt",
        "file_2022-04-04.txt",
        "file_2022-05-05.txt",
    ]
    for i, file in enumerate(test_files):
        expected_filename = expected_filenames[i]
        actual_filename = compute_new_filename(os.path.join(test_dir, file))
        assert expected_filename == actual_filename


def test_get_filename_pairs(tmpdir):
    test_dir = tmpdir.mkdir("test_dir")
    test_files = [
        "file1.txt",
        "file2.txt",
        "file3.txt",
        "file4.txt",
        "file5.txt",
    ]

    test_dates = [
        "January 1, 2022",
        "February 2, 2022",
        "March 3, 2022",
        "April 4, 2022",
        "May 5, 2022",
    ]

    for i, file in enumerate(test_files):
        date = test_dates[i]
        date_str = datetime.strptime(date, "%B %d, %Y").strftime("%Y-%m-%d")
        new_filename = f"file_{date_str}.txt"
        with open(os.path.join(test_dir, file), "w") as f:
            f.write("test")

    expected_pairs = [
        (
            os.path.join(test_dir, "file1.txt"),
            os.path.join(test_dir, "file_2022-01-01.txt"),
        ),
        (
            os.path.join(test_dir, "file2.txt"),
            os.path.join(test_dir, "file_2022-02-02.txt"),
        ),
        (
            os.path.join(test_dir, "file3.txt"),
            os.path.join(test_dir, "file_2022-03-03.txt"),
        ),
        (
            os.path.join(test_dir, "file4.txt"),
            os.path.join(test_dir, "file_2022-04-04.txt"),
        ),
        (
            os.path.join(test_dir, "file5.txt"),
            os.path.join(test_dir, "file_2022-05-05.txt"),
        ),
    ]
    actual_pairs = list(get_filename_pairs([test_dir]))
    assert set(expected_pairs) == set(actual_pairs)

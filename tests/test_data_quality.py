import csv


def test_customer_record_count():
    with open("data/customers.csv", "r") as file:
        rows = list(csv.DictReader(file))

    assert len(rows) == 4


def test_no_duplicate_customer_ids():
    with open("data/customers.csv", "r") as file:
        rows = list(csv.DictReader(file))

    customer_ids = [row["customer_id"] for row in rows]

    assert len(customer_ids) == len(set(customer_ids))


def test_no_null_customer_ids():
    with open("data/customers.csv", "r") as file:
        rows = list(csv.DictReader(file))

    for row in rows:
        assert row["customer_id"] is not None
        assert row["customer_id"] != ""
import random
from datetime import timedelta, datetime, timezone
from faker import Faker
import pprint

end = datetime.now(timezone.utc)
start = end - timedelta(days=5 * 365)


def random_date(start=start, end=end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )


def random_strings(n):
    fake = Faker()
    return [fake.word() for _ in range(n)]


def random_ints(n):
    return [random.randint(0, 100) for _ in range(n)]


def random_floats(n):
    return [random.random() * 100 for _ in range(n)]


def random_dates(n):
    return [random_date() for _ in range(n)]


type_mapper = {
    "str": "string",
    "int": "integer",
    "float": "numeric",
    "datetime": "date",
}


def generate_random_dataframe(n, m):
    fake = Faker()
    num_rows = random.randint(n, m)
    num_cols = random.randint(6, 14)

    df = {}
    # Ensure at least one column of each specified type
    df[f"{fake.word()}_0"] = random_strings(num_rows)
    df[f"{fake.word()}_1"] = random_ints(num_rows)
    df[f"{fake.word()}_2"] = random_floats(num_rows)
    df[f"{fake.word()}_3"] = random_dates(num_rows)
    # Add additional columns
    for i in range(4, num_cols):
        random_fn = random.choice(
            [random_strings, random_ints, random_floats, random_dates]
        )
        df[f"{fake.word()}_{i}"] = random_fn(num_rows)

    # column names
    names = list(df.keys())

    # column types formatted as agreed upon for frontend display
    dtypes = [type_mapper[type(df[name][0]).__name__] for name in names]

    # values is list of rows, with dates into strings
    values = [
        [str(x) if isinstance(x, datetime) else x for x in row]
        for row in zip(*[df[name] for name in names])
    ]
    return {"names": names, "dtypes": dtypes, "values": values}


if __name__ == "__main__":
    df = generate_random_dataframe(4, 10)
    pprint.pprint(df)

from example_module.logging import logger_wraps


@logger_wraps(level="INFO")
def test(name: str) -> int:
    name_cleaned = name.replace(".", "").replace(" ", "")
    name_length = len(name_cleaned)

    print(f"Hello {name}, your name has {name_length} letters!")

    return name_length


def main() -> int:
    name_len = test(name="John A.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for name in dir(hidden_4):
        if not name.startswith("_"):
            value = getattr(hidden_4, name)
            if not callable(value):
                print(name)

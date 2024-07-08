def outer():
    x = "hello"

    def inner():
        nonlocal x
        x += " world"
        return x

    return inner()

print(outer())

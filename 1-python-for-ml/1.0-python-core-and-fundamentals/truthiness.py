samples = [
    0,
    1,
    "",
    "text",
    [],
    [1],
    {},
    {
        "k": 1,
    },
    None,
]

print(samples)
for item in samples:
    if item:
        print(repr(item), "Truthy")
    else:
        print((repr(item)), "Falsy")

# demo
print("Demo")
score = 95
name = "John"
print(f"{name} scored {score}% (next:{score+1}%)")

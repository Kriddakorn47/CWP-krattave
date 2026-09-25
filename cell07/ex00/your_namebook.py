def array_of_names(persons):
    return [
        first_name.capitalize() + " " + last_name.capitalize()
        for first_name, last_name in persons.items()
    ]


persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
print(array_of_names(persons))
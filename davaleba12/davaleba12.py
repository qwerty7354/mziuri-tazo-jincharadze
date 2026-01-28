emails_2011 = []
countries = set()

with open("clients.txt", "r", encoding="utf-8") as file, \
     open("filtered_clients.txt", "w", encoding="utf-8") as new_file:

    for line in file:
        line = line.strip()
        if not line:
            continue

        name, email, country, birth_date = line.split(";")

        # a
        if country in ("Spain", "Germany"):
            new_file.write(name + "\n")

        # b
        year = birth_date.split("/")[-1]
        if year == "2011":
            emails_2011.append(email)

        # c
        countries.add(country)

print("2011 wels dabadebulebis email-ebi:")
print(emails_2011)

print("\nqveynebis sia (unikaluri):")
print(list(countries))
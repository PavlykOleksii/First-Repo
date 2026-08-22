import csv


def write_contacts_to_file(filename, contacts):
    field_names = contacts[0].keys()
    with open(filename, 'w', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)

def read_contacts_from_file(filename):
    contacts = []
    with open(filename, "r", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            row["favorite"] = row["favorite"] == "True"
            contacts.append(row)

    return contacts
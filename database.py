entries = []

def add_entry(entryContent, entryDate):
    entries.append({"content": entryContent,
                    "date": entryDate,
                    })

def get_entries():
    return entries

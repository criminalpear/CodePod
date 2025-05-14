import db

def search_snippets(query):
    results = []
    all_snips = db.get_all_snippets()
    query = query.lower()

    for _, title, lang, code in all_snips:
        if query in title.lower() or query in code.lower():
            results.append({"title": title, "language": lang, "code": code})
    return results

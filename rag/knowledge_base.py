from pathlib import Path
import re


# Location of the knowledge base
KNOWLEDGE_FILE = (
    Path(__file__).parent.parent
    / "data"
    / "helpdesk_knowledge.txt"
)


def load_knowledge_base():
    """
    Load the IT helpdesk knowledge base from the text file.
    """

    if not KNOWLEDGE_FILE.exists():
        return ""

    with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as file:
        return file.read()


def search_knowledge(query):
    """
    Search the knowledge base and return the most relevant
    complete troubleshooting section.
    """

    knowledge = load_knowledge_base()

    if not knowledge:
        return None

    # Split the file whenever a new Problem begins.
    sections = re.split(r"(?=Problem:)", knowledge)

    query_words = set(
        re.findall(r"\b[a-zA-Z]+\b", query.lower())
    )

    best_section = None
    best_score = 0

    for section in sections:

        section = section.strip()

        # Ignore headings and general information.
        if not section.startswith("Problem:"):
            continue

        section_words = set(
            re.findall(r"\b[a-zA-Z]+\b", section.lower())
        )

        # Count matching words between query and section.
        score = len(query_words.intersection(section_words))

        if score > best_score:
            best_score = score
            best_section = section

    if best_section is None:
        return None

    return best_section


# Test the knowledge base directly
if __name__ == "__main__":

    test_query = "My Wi-Fi is connected but internet is not working"

    result = search_knowledge(test_query)

    print("\n--- Knowledge Base Test ---\n")

    if result:
        print(result)
    else:
        print("No matching information found.")

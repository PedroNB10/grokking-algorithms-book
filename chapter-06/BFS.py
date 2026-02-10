from collections import deque

graph: dict[str, list[str]] = {
        "YOU": ["BOB", "ALICE", "CLAIRE"],
        "BOB": ["ANUJ", "PEGGY"],
        "PEGGY": [],
        "ALICE": ["PEGGY"],
        "CLAIRE": ["THOM", "JONNY"],
        "ANUJ": [],
        "THOM": [],
        "JONNY": [],
    }
# silly function to check if a person is a seller btw
def person_is_seller(person: str):
    return person[-1].lower() == "m"


def search(name:str):
    search_queue = deque()
    search_queue += graph[name]

    searched = []  # this array is how you keep track of people you've searched before

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
                print(f"searched order: {searched}")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    print(f"searched order: {searched}")
    return False


if __name__ == "__main__":
    search("YOU")

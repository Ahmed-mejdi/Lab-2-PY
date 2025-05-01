import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
def main():
    url = "https://news.ycombinator.com/item?id=42919502"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    # find all elements with class="ind" and indent level = 0
    elements = soup.find_all(class_="ind", indent=0)
    # for each of these elements, find the next element with class="comment"
    comments = [e.find_next(class_="comment") for e in elements]

    # Map of technologies keyword to search for, initialized at 0
    keywords = {"python": 0, "javascript": 0, "typescript": 0, "go": 0, "c#": 0, "java": 0, "rust": 0}

    for comment in comments:
        # Get the comment text and convert it to lowercase
        comment_text = comment.get_text().lower()

        # Split comment into words
        words = comment_text.split(" ")

        # Clean the words using strip and keep unique ones
        words = {w.strip(".,/:;!@()[]{}<>\"'") for w in words}

        # Count keywords if present in this post
        for k in keywords:
            if k in words:
                keywords[k] += 1

    # Print final counts
    print(keywords)
    # plot a bar graph
    plt.bar(keywords.keys(), keywords.values())
# Add labels
    plt.xlabel("Language")
    plt.ylabel("# of Mentions")
    plt.show()

if __name__ == "__main__":
    main()

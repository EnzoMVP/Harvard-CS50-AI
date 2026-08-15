import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    total_num_pages = len(corpus)
    links = corpus[page]
    num_links = len(links)
    eopage_probability = (1 - damping_factor) / total_num_pages
    transition = {}
    if links:
        probability_links = damping_factor / num_links
        for page_ in corpus.keys():
            transition[page_] = eopage_probability
            if page_ in links:
                transition[page_] += probability_links
    else:
        eopage_probability = 1 / total_num_pages
        for page_ in corpus.keys():
            transition[page_] = eopage_probability

    return  transition

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pages = list(corpus.keys())
    page = [random.choice(pages)]
    samples = []
    page_rank = {}

    for sample in range(n):
        samples.append(page[0])
        transition = transition_model(corpus, page[0], damping_factor)
        page = random.choices(pages, list(transition.values()))

    for page_ in pages:
        page_rank[page_] = samples.count(page_) / n

    return page_rank

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    page_rank = {}
    f = (1 - damping_factor) / len(corpus)
    for key in list(corpus.keys()):
        page_rank[key] = 1 / len(corpus)

    while True:
        dif = float('-inf')
        previous = page_rank.copy()
        for key_ in list(corpus.keys()):
            g = 0
            for page in list(corpus.keys()):
                if key_ in corpus[page]:
                    g += previous[page] / len(corpus[page])
            page_rank[key_] = f + damping_factor * g

        for k in list(corpus.keys()):
            if abs(previous[k] - page_rank[k]) > dif:
                dif = abs(previous[k] - page_rank[k])

        if dif < 0.001:
            break

    return page_rank

if __name__ == "__main__":
    main()

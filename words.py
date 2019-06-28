from urllib.request import urlopen
import sys
 

def fetch_words(url):
    """Fecth a list of words from a URL.

    Args:
        URL: The URL of a UTF-8 text document.
        
    Returns:
        A list of string containg the words from the document.

    """

    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                    story_words.append(word)
    return story_words


def print_items(items):
      """Iteriates through the list.

    Args:
        Items: iteriates through the objects.
        
    Returns:
        Prints the interable objects.
        
    """   
    for item in items:
        print(item)


def main(url):
     """Calls the fetch_words() and the print_items() function.

    Args:
        sys.argv: returns a list of command line arguments passed to a Python script.
        
    Returns:
        A list of string containg the words from the document

    """
    words =  fetch_words(url)
    print_items(words) 


if __name__ == "__main__":
    main(sys.argv[1])       


    #pep257
    #google python style guid
    
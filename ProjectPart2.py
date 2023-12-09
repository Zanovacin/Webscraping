import plotly.graph_objs as go
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from operator import itemgetter

def scrape_quotes(url):
    author_quotes_count = {}
    quote_lengths = []
    quotes = []
    tag_counts = {}

    while True:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, 'html.parser')

        quotes_list = soup.findAll('small', attrs={"class": "author"})
        quote_data = soup.findAll('div', attrs={"class": "quote"})

        for author in quotes_list:
            author_name = author.text.strip()

            if author_name in author_quotes_count:
                author_quotes_count[author_name] += 1
            else:
                author_quotes_count[author_name] = 1

        for quote in quote_data:
            quote_text = quote.text.strip()
            quote_length = len(quote_text)
            quote_lengths.append(quote_length)
            quotes.append((quote_text, quote_length))

            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            for tag in tags:
                if tag in tag_counts:
                    tag_counts[tag] += 1
                else:
                    tag_counts[tag] = 1

        next_button = soup.find('li', class_='next')
        if next_button and next_button.find('a'):
            current_page = int(url.split('/')[-2])
            url = f'http://quotes.toscrape.com/page/{current_page + 1}/'
        else:
            break

    overall_avg_length = sum(quote_lengths) / len(quote_lengths)
    print('Quote Statistics:')
    print('-----------------------------')
    print(f'Overall average length of quotes: {overall_avg_length:.2f} characters')
    print()

#Longest quote
    max_length = 0
    longest_quote = None
    for quote in quotes:
        if quote[1] > max_length:
            max_length = quote[1]
            longest_quote = quote

#Shortest quote
    min_length = 10000000
    shortest_quote = None
    for quote in quotes:
        if quote[1] < min_length:
            min_length = quote[1]
            shortest_quote = quote

    print(f'Longest Quote:')
    print(f'---------------')
    print(f'{longest_quote[0]} ({longest_quote[1]} characters)')
    print()

    print(f'Shortest Quote:')
    print(f'----------------')
    print(f'{shortest_quote[0]} ({shortest_quote[1]} characters)')
    print()

    print('Author Statistics:')
    print('-----------------------------')
    for author, count in author_quotes_count.items():
        print(f"{author}: {count} quotes")

    most_author = max(author_quotes_count, key=author_quotes_count.get)
    least_author = min(author_quotes_count, key=author_quotes_count.get)

    print(f'Author with the most quotes: {most_author}')
    print(f'Author with the least quotes: {least_author}')
    print()

    return author_quotes_count, tag_counts

initial_url = 'http://quotes.toscrape.com/page/1/'
result, tags_result = scrape_quotes(initial_url)

# Top 10 Authors
author_list = [{'Author': author, 'Quotes': count} for author, count in result.items()]
author_list = sorted(author_list, key=itemgetter('Quotes'), reverse=True)[:10]

fig_authors = go.Figure(data=[go.Bar(x=[author['Author'] for author in author_list],
                                     y=[quote['Quotes'] for quote in author_list])])
fig_authors.update_layout(title='Top 10 Authors and Their Corresponding Quotes', xaxis_title='Authors', yaxis_title='Quotes')
fig_authors.show()

# Top 10 Tags
tags_list = [{'Tag': tag, 'Occurrences': count} for tag, count in tags_result.items()]
tags_list = sorted(tags_list, key=itemgetter('Occurrences'), reverse=True)[:10]

fig_tags = go.Figure(data=[go.Bar(x=[tag['Tag'] for tag in tags_list],
                                  y=[occurance['Occurrences'] for occurance in tags_list])])
fig_tags.update_layout(title='Top 10 Tags Based on Popularity', xaxis_title='Tags', yaxis_title='Instances')
fig_tags.show()

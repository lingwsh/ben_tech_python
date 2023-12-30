from bs4 import BeautifulSoup
import pandas as pd

def get_text(element):
    '''Get text from a BeautifulSoup element'''
    if element is None:
        return ""
    return element.get_text().strip()

def get_list_text(element_list):
    '''Get text from a list of BeautifulSoup elements'''
    return [get_text(element) for element in element_list]

def subscribers_to_int(subscribers_raws):
    '''Replace K and M with 000 and 000000'''
    subscribers_list = []
    for subscribers_raw in subscribers_raws:
        subscribers_raw = subscribers_raw.replace(' subscribers', '')
        if subscribers_raw is not int:
            if subscribers_raw in [None, '']:
                subscribers_raw = 0
            elif subscribers_raw.endswith('K'):
                subscribers_raw = int(float(subscribers_raw[:-1]) * 1000)
            elif subscribers_raw.endswith('M'):
                subscribers_raw = int(float(subscribers_raw[:-1]) * 1000000)
            else:
                subscribers_raw = int(subscribers_raw)
        subscribers_list.append(subscribers_raw)
    return subscribers_list

def get_descs(soup):
    '''Get description from a BeautifulSoup element'''
    # Find all div by id "content-section"
    content_sections = soup.find_all('div', id='content-section')
    descs = []
    for content_section in content_sections:
        desc = content_section.find('yt-formatted-string', id='description')
        descs.append(get_text(desc))
    return descs

def data_to_excel(file_path):
    '''Data extraction from html file and write to excel'''
    # Read the html file
    html = None
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    # Parse the html
    soup = BeautifulSoup(html, 'html.parser')
    # Find div by id = "grid-container"
    title_divs = soup.find_all('div', {'id': 'text-container'})
    id_spans = soup.find_all('span', {'id': 'subscribers'})
    subscribers_spans = soup.find_all('span', {'id': 'video-count'})

    # youtube dict info
    # info = {
    #     "title:": "",
    #     "id": "",
    #     "subscribers": "",
    #     "subscribers_raw": "",
    #     "desc": ""
    # }

    titles = get_list_text(title_divs)
    ids = get_list_text(id_spans)
    subscribers_raws = get_list_text(subscribers_spans)
    subscribers = subscribers_to_int(subscribers_raws)
    descs = get_descs(soup)
    # print(titles[:5])
    # print(ids[:5])
    # print(subscribers_raws[:5])
    # print(subscribers[:5])
    # print(descs[:5])

    df = pd.DataFrame(columns=['Like', 'Title', 'subscribers_raw', 'subscribers', 'ID', 'url', 'desc'])
    df['Title'] = titles
    df['ID'] = ids
    df['subscribers_raw'] = [i.replace(' subscribers', '') for i in subscribers_raws]
    df['subscribers'] = subscribers
    df['desc'] = descs
    df['url'] = 'https://www.youtube.com/' + df['ID']
    df['Like'] = ""

    # Order by subscribers descending
    df = df.sort_values(by=['subscribers'], ascending=False)

    # Write to excel
    df.to_excel('all_ytb_channel.xlsx', index=False)
    print("Success export to excel")

if __name__ == '__main__':
    file_path = 'all_ytb_channel.html'
    data_to_excel(file_path)

from bs4 import BeautifulSoup
import requests
'''NB the code below is just for practice purposes since the 
data extracted may not be in line according to the terms and conditions
of the website whose url is used'''
data = requests.get('https://news.ycombinator.com/news')
response = data.text
soup = BeautifulSoup(response, 'html.parser')
titles = soup.find_all(name ='a', class_='titlelink')
votes = soup.find_all(name='span', class_='score')
users = soup.find_all(name='a', class_='hnuser')
time_commented = soup.find_all(name='span', class_='age')
links = soup.find_all(name='span', class_='sitestr')
def titles_():
    title_texts = [title.getText() for title in titles]
    return title_texts
def votes_():
    total_votes = [vote.getText() for vote in votes]
    return total_votes
def users_():
    commenters = [user.getText() for user in users]
    return commenters

def comment_time():
    time = [time.getText() for time in time_commented]
    return time

def links_():
    lin = [link.getText() for link in links]
    return lin



import urllib.request
import bs4

g_followers = urllib.request.urlopen('https://github.com/taleofbor404?tab=followers').read()
g_following = urllib.request.urlopen('https://github.com/taleofbor404?tab=following').read()

def parseHTML(input):
    html = bs4.BeautifulSoup(input, features='html.parser')
    output = []
    for follower in html.findAll('a', {'class' : 'd-inline-block no-underline mb-1', 'data-hovercard-type':'user'}):
        full_name = ''
        for name in follower.findAll('span'):
            if len(name.text) > 0:
                full_name += name.text + ' '
        full_name.strip()
        output.append(full_name)

    return output

def notFollowingBack():
    return set(parseHTML(g_following)) - set(parseHTML(g_followers))

def needToFollowBack():
    return set(parseHTML(g_followers)) - set(parseHTML(g_following))






from django import template
from urllib.parse import urlparse, parse_qs, urlsplit

register = template.Library()

def embed_url(value):
    url = None

    if 'vimeo' in value:
        """
        - http://vimeo.com/119054553
        - http://vimeo.com/channels/staffpicks/119054553
        - http://vimeo.com/groups/filmschool/videos/116200417
        - //player.vimeo.com/video/119054553
        """
        query = urlparse(value)
        p = query.path.split('/')
        video_id = p[len(p)-1]

        url = '//player.vimeo.com/video/'+video_id

    elif 'youtu' in value:
        """
        Examples:
        - http://youtu.be/0TGTXMqUrD0
        - http://www.youtube.com/watch?v=0TGTXMqUrD0&feature=feedu
        - http://www.youtube.com/embed/0TGTXMqUrD0
        - http://www.youtube.com/v/0TGTXMqUrD0?version=3&amp;hl=en_US
        """
        query = urlparse(value)

        if query.hostname == 'youtu.be':
            video_id = query.path.split('/')[1]
        if query.hostname in ('www.youtube.com', 'youtube.com'):
            if query.path == '/watch':
                p = parse_qs(query.query)
                video_id = p['v'][0]
            if query.path[:7] == '/embed/':
                video_id = query.path.split('/')[2]
            if query.path[:3] == '/v/':
                video_id = query.path.split('/')[2]
        url = 'https://www.youtube.com/embed/'+video_id+'?rel=0'

    return url

def get_video_id(value):
    video_id = None

    if 'vimeo' in value:
        """
        - http://vimeo.com/119054553
        - http://vimeo.com/channels/staffpicks/119054553
        - http://vimeo.com/groups/filmschool/videos/116200417
        - //player.vimeo.com/video/119054553
        """
        query = urlparse(value)
        p = query.path.split('/')
        video_id = p[len(p)-1]

    elif 'youtu' in value:
        """
        Examples:
        - http://youtu.be/0TGTXMqUrD0
        - http://www.youtube.com/watch?v=0TGTXMqUrD0&feature=feedu
        - http://www.youtube.com/embed/0TGTXMqUrD0
        - http://www.youtube.com/v/0TGTXMqUrD0?version=3&amp;hl=en_US
        """
        query = urlparse(value)

        if query.hostname == 'youtu.be':
            video_id = query.path.split('/')[1]
        if query.hostname in ('www.youtube.com', 'youtube.com'):
            if query.path == '/watch':
                p = parse_qs(query.query)
                video_id = p['v'][0]
            if query.path[:7] == '/embed/':
                video_id = query.path.split('/')[2]
            if query.path[:3] == '/v/':
                video_id = query.path.split('/')[2]


    return video_id

register.filter('embed_url', embed_url)
register.filter('get_video_id', get_video_id)

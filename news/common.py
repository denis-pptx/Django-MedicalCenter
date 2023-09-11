import os


def get_path_to_html(news):
    publish_date = news.publish_date
    return os.path.join(
        'news',
        'news_archive',
        str(publish_date.year),
        str(publish_date.month).zfill(2),
        str(publish_date.day).zfill(2),
        f'{news.pk}.html'
    )


html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>{title}</h1>
    <hr>
    <h3>{publish_date}</h3>
    <p>{summary}</p>
</body>
</html>
'''

def generate_h1(title: str) -> str:
    """
    Generates an HTML h1 tag with indentation.

    :param title: The title of the article.
    :return: A formatted h1 tag.
    """
    return f'<h1>\n    {title}\n</h1>'


def generate_article(content: str) -> str:
    """
    Generates an HTML article tag with indentation.

    :param content: The content of the article.
    :return: A formatted article tag.
    """
    return f'<article>\n    {content}\n</article>'


def generate_div(comment: str) -> str:
    """
    Generates an HTML div tag with indentation.

    :param comment: The comment text.
    :return: A formatted div tag.
    """
    return f'<div>\n    {comment}\n</div>'


def generate_html(title: str, content: str, comments: list[str]) -> str:
    """
    Generates an HTML representation of an article with comments.

    :param title: The title of the article.
    :param content: The content of the article.
    :param comments: A list of comments about the article.
    :return: A formatted HTML string.
    """
    html_output = [
        generate_h1(title),
        generate_article(content)
    ]

    html_output.extend(generate_div(comment) for comment in comments)

    return '\n'.join(html_output)


if __name__ == '__main__':
    article_title = input()
    article_content = input()

    comments_list = []
    while True:
        comment = input()
        if comment == 'end of comments':
            break
        comments_list.append(comment)

    result = generate_html(title=article_title, content=article_content, comments=comments_list)
    print(result)

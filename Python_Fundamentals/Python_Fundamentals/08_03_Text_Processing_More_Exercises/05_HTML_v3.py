def generate_html(title: str, content: str, comments: list[str]) -> str:
    """
    Generates an HTML representation of an article with comments, formatted with indentation.

    :param title: The title of the article.
    :param content: The content of the article.
    :param comments: A list of comments about the article.
    :return: A formatted HTML string.
    """
    html_output = [
        f'<h1>\n    {title}\n</h1>',
        f'<article>\n    {content}\n</article>'
    ]

    html_output.extend(f'<div>\n    {comment}\n</div>' for comment in comments)

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

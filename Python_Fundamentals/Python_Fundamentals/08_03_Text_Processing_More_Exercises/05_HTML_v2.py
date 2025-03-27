def format_article(title: str, content: str, comments: list[str]) -> str:
    """Formats an article with a title, content, and comments in HTML structure."""
    html_output = [
        '<h1>',
        f'    {title}',
        '</h1>',
        '<article>',
        f'    {content}',
        '</article>',
    ]

    for comment in comments:
        html_output.extend([
            '<div>',
            f'    {comment}',
            '</div>'
        ])

    return '\n'.join(html_output)


if __name__ == '__main__':
    title_input: str = input().strip()
    content_input: str = input().strip()
    comments_list: list[str] = []

    while True:
        comment: str = input().strip()
        if comment == 'end of comments':
            break
        comments_list.append(comment)

    result: str = format_article(title_input, content_input, comments_list)
    print(result)

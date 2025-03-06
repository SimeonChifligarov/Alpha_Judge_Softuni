class Email:
    """
    Represents an email with sender, receiver, content, and sent status.
    """

    def __init__(self, sender: str, receiver: str, content: str) -> None:
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self) -> None:
        self.is_sent = True

    def get_info(self) -> str:
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


if __name__ == '__main__':
    emails = []

    while True:
        data = input()
        if data == 'Stop':
            break

        current_sender, current_receiver, current_content = data.split()
        emails.append(Email(sender=current_sender, receiver=current_receiver, content=current_content))

    indices = [int(idx) for idx in input().split(', ')]

    for index in indices:
        emails[index].send()

    for email in emails:
        print(email.get_info())

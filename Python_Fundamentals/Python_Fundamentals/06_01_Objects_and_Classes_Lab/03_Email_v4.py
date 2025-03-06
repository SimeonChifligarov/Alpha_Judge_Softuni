class Email:
    def __init__(self, sender: str, receiver: str, content: str):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        """Marks the email as sent."""
        self.is_sent = True

    def get_info(self) -> str:
        """Returns email information in the specified format."""
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


if __name__ == '__main__':
    emails = []

    while True:
        data = input()
        if data == 'Stop':
            break

        sender, receiver, content = data.split()
        emails.append(Email(sender, receiver, content))

    sent_indices = list(map(int, input().split(', ')))

    # for index in sent_indices:
    #     if 0 <= index < len(emails):
    #         emails[index].send()
    [emails[index].send() for index in sent_indices if 0 <= index < len(emails)]

    # for email in emails:
    #     print(email.get_info())
    [print(email.get_info()) for email in emails]

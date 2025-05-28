class EmailValidator:
    """
    This class is about an email validator that checks usernames, mails, and domains.

    Args:
        min_length (int): The minimum length of the username.
        mails (list): The list of valid mails.
        domains (list): The list of valid domains.
    """

    def __init__(self, min_length: int, mails: list[str], domains: list[str]) -> None:
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain: str) -> bool:
        return domain in self.domains

    def validate(self, email: str) -> bool:
        name, _, rest = email.partition('@')
        mail, _, domain = rest.partition('.')
        if not name or not mail or not domain:
            return False
        return all([
            self.__is_name_valid(name),
            self.__is_mail_valid(mail),
            self.__is_domain_valid(domain)
        ])

    def __str__(self) -> str:
        return f'EmailValidator(min_length={self.min_length}, mails={self.mails}, domains={self.domains})'

    def __repr__(self) -> str:
        return f'EmailValidator(min_length={self.min_length}, mails={self.mails}, domains={self.domains})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, EmailValidator):
            return False
        return self.min_length == other.min_length and self.mails == other.mails and self.domains == other.domains

    def __hash__(self) -> int:
        return hash((self.min_length, tuple(self.mails), tuple(self.domains)))


if __name__ == '__main__':
    # mails_list = ['gmail', 'softuni']
    # domains_list = ['com', 'bg']
    # email_validator_instance = EmailValidator(min_length=6, mails=mails_list, domains=domains_list)
    # print(email_validator_instance.validate(email='pe77er@gmail.com'))
    # print(email_validator_instance.validate(email='georgios@gmail.net'))
    # print(email_validator_instance.validate(email='stamatito@abv.net'))
    # print(email_validator_instance.validate(email='abv@softuni.bg'))
    pass

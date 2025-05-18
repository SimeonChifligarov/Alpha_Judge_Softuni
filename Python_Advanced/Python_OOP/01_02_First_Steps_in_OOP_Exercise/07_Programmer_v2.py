class Programmer:
    """
    This class is for a programmer. It stores their name, main language, and skill level.

    Args:
        name (str): The programmer's name
        language (str): The language they currently use
        skills (int): How many skill points they have
    """

    def __init__(self, name: str, language: str, skills: int) -> None:
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name: str, language: str, skills_earned: int) -> str:
        """
        This method lets the programmer watch a course and gain skills if it's in their language.

        Args:
            course_name (str): The name of the course
            language (str): The language of the course
            skills_earned (int): How many skills they gain from it

        Returns:
            str: Message about watching or not watching the course
        """
        if language == self.language:
            self.skills += skills_earned
            return f'{self.name} watched {course_name}'
        return f'{self.name} does not know {language}'

    def change_language(self, new_language: str, skills_needed: int) -> str:
        """
        This method changes the programmer's language if they have enough skills.

        Args:
            new_language (str): The new language to switch to
            skills_needed (int): How many skills are needed

        Returns:
            str: Message about success, already knowing, or needing more skills
        """
        if self.skills >= skills_needed:
            if self.language != new_language:
                old_language = self.language
                self.language = new_language
                return f'{self.name} switched from {old_language} to {new_language}'
            return f'{self.name} already knows {new_language}'
        needed_skills = skills_needed - self.skills
        return f'{self.name} needs {needed_skills} more skills'

# if __name__ == '__main__':
#     dev_name = 'Alice'
#     dev_language = 'Python'
#     dev_skills = 60
#     dev_instance = Programmer(name=dev_name, language=dev_language, skills=dev_skills)
#     print(dev_instance.watch_course(course_name='Intro to Python', language='Python', skills_earned=30))
#     print(dev_instance.watch_course(course_name='C++ Basics', language='C++', skills_earned=20))
#     print(dev_instance.change_language(new_language='Java', skills_needed=50))
#     print(dev_instance.change_language(new_language='Java', skills_needed=100))
#     print(dev_instance.change_language(new_language='Java', skills_needed=80))
#     print(dev_instance.change_language(new_language='Java', skills_needed=70))

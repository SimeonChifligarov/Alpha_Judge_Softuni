class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if not language == self.language:
            return f'{self.name} does not know {language}'

        self.skills += skills_earned
        return f'{self.name} watched {course_name}'

    def change_language(self, new_language, skills_needed):
        if self.skills < skills_needed:
            needed_skills = skills_needed - self.skills
            return f'{self.name} needs {needed_skills} more skills'

        if new_language == self.language:
            return f'{self.name} already knows {self.language}'

        previous_language = self.language
        self.language = new_language
        return f'{self.name} switched from {previous_language} to {new_language}'

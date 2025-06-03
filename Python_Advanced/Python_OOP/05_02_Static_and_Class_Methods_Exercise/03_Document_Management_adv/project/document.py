from project.category import Category
from project.topic import Topic


class Document:
    """This class creates a document linked to category and topic."""

    def __init__(self, document_id: int, category_id: int, topic_id: int, file_name: str) -> None:
        self.id: int = document_id
        self.category_id: int = category_id
        self.topic_id: int = topic_id
        self.file_name: str = file_name
        self.tags: list[str] = []

    @classmethod
    def from_instances(cls, document_id: int, category: Category, topic: Topic, file_name: str) -> 'Document':
        return cls(document_id, category.id, topic.id, file_name)

    def add_tag(self, tag_content: str) -> None:
        if tag_content not in self.tags:
            self.tags.append(tag_content)

    def remove_tag(self, tag_content: str) -> None:
        if tag_content in self.tags:
            self.tags.remove(tag_content)

    def edit(self, new_file_name: str) -> None:
        self.file_name = new_file_name

    def __repr__(self) -> str:
        tags_as_string: str = ', '.join(self.tags)
        return f'Document {self.id}: {self.file_name}; category {self.category_id}, topic {self.topic_id}, tags: {tags_as_string}'


if __name__ == '__main__':
    # document_instance = Document(document_id=1, category_id=1, topic_id=1, file_name='finalize project')
    pass

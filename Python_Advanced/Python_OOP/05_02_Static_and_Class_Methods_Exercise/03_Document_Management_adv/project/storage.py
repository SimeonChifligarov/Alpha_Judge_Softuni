from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    """This class stores categories, topics, and documents together."""

    def __init__(self) -> None:
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        category_instance = self.__find_by_id(collection=self.categories, entity_id=category_id)
        if category_instance:
            category_instance.edit(new_name=new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        topic_instance = self.__find_by_id(collection=self.topics, entity_id=topic_id)
        if topic_instance:
            topic_instance.edit(new_topic=new_topic, new_storage_folder=new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        document_instance = self.__find_by_id(collection=self.documents, entity_id=document_id)
        if document_instance:
            document_instance.edit(new_file_name=new_file_name)

    def delete_category(self, category_id: int) -> None:
        category_instance = self.__find_by_id(collection=self.categories, entity_id=category_id)
        if category_instance:
            self.categories.remove(category_instance)

    def delete_topic(self, topic_id: int) -> None:
        topic_instance = self.__find_by_id(collection=self.topics, entity_id=topic_id)
        if topic_instance:
            self.topics.remove(topic_instance)

    def delete_document(self, document_id: int) -> None:
        document_instance = self.__find_by_id(collection=self.documents, entity_id=document_id)
        if document_instance:
            self.documents.remove(document_instance)

    def get_document(self, document_id: int) -> Document | None:
        return self.__find_by_id(collection=self.documents, entity_id=document_id)

    def __repr__(self) -> str:
        return '\n'.join(repr(document) for document in self.documents)

    @staticmethod
    def __find_by_id(collection: list, entity_id: int) -> object | None:
        found_entities = [entity for entity in collection if entity.id == entity_id]
        if found_entities:
            return found_entities[0]
        return None


if __name__ == '__main__':
    # storage_instance = Storage()
    pass

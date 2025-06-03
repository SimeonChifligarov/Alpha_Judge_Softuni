class Topic:
    """This class creates a topic linked to a storage folder."""

    def __init__(self, topic_id: int, topic_name: str, storage_folder: str) -> None:
        self.id: int = topic_id
        self.topic: str = topic_name
        self.storage_folder: str = storage_folder

    def edit(self, new_topic: str, new_storage_folder: str) -> None:
        self.topic = new_topic
        self.storage_folder = new_storage_folder

    def __repr__(self) -> str:
        return f'Topic {self.id}: {self.topic} in {self.storage_folder}'


if __name__ == '__main__':
    # topic_instance = Topic(topic_id=1, topic_name='daily tasks', storage_folder='C:\\work_documents')
    pass

from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    def create(self, entity):
        """Create a new entity in the repository."""
        pass

    @abstractmethod
    def find_all(self):
        """Retrieve all entities from the repository."""
        pass

    @abstractmethod
    def find_by_id(self, entity_id):
        """Retrieve an entity from the repository by its ID."""
        pass

    @abstractmethod
    def update(self, entity_id, updated_entity):
        """Update an existing entity in the repository."""
        pass

    @abstractmethod
    def delete(self, entity_id):
        """Delete an entity from the repository by its ID."""
        pass
# Python-Clean-Architecture

### Entities

Enterprise Business Objects
Enterprise Business Rules

### Interactors

Application Specific Business Rules

### Repositories

Interface for Data Layer interaction

### Common

Common Objects used throughout the library
Request Objects
Response Objects

### Flow of interactions

External to Library ---> Request Objects -> Interactor -> Repository -> Business Entities -> Interactor -> Response Object ---> Exits the Library

## Common Commands
py.test --cov-config pytest.ini --cov=core/entities tests/
py.test --cov-config pytest.ini --cov-report term-missing --cov=core/entities tests/
py.test --cov-config pytest.ini --cov-report html:cov_html --cov=core/entities tests/
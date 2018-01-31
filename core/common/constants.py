import os

# Instance folder path, make it independent.
INSTANCE_FOLDER_PATH = os.path.join('/tmp', 'instance')

EVENT_TYPES = {
    1: 'update',
    2: 'update',
    3: 'assign',
    4: 'hold',
    5: 'close'
}
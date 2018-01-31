from core.common.entity_model import EntityModel
import logging

logger = logging.getLogger(__name__)

class Notification(EntityModel):


    def __init__(self, user_id, badge_count, generated, event_type, message):
        self.user_id = user_id
        self.badge_count = badge_count
        self.generated = generated
        self.event_type = event_type
        self.message = message


    @classmethod
    def from_dict(cls, adict):
        logger.info("from_dict")
        return cls(
            user_id=adict['user_id'],
            badge_count=adict['badge_count'],
            generated=adict['generated'],
            event_type=adict['event_type'],
            message=adict['message'],
            arn=adict['arn']
        )


if __name__ == "__main__":
    ob = Notification('1234567890', '52', '2017-01-05', '3', 'Hello')

    print(ob.message)

    dict = {
        'user_id': '0987654311',
        'badge_count': '52',
        'generated': '2018-02-05',
        'event_type': '3',
        'message': '2nd object',
        'arn': '2nd/arn'
    }

    do = Notification.from_dict(dict)
    print(do.message)
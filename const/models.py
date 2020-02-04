import json
import uuid

from django.db import models

DEFAULT_PARAMS = '{\n' \
                 '    "key1": "value1",\n' \
                 '    "key2": "value2",\n' \
                 '    "key3": "value3"\n' \
                 '}'

# Требуемые константы, в случае их отсутствия будут отображаться на странице сайта
REQUIRED = {
    'footer': {"copywriter": "SET VALUE"},
    'address': {"title": "SET VALUE", "phone": "SET VALUE", "location": "SET VALUE"},
    'header': {"title": "SET VALUE", "up_title": "SET VALUE", "up_remark": "SET VALUE"},
    'main': {"title": "SET VALUE"}
}


class Const(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    params = models.TextField(default=DEFAULT_PARAMS)

    def as_dict(self):
        try:
            params = json.loads(self.params)
        except ValueError:
            params = None
        return {
            self.name: params
        }

    def get_json_all(self):
        data = [obj.as_dict() for obj in Const.objects.all()]
        js_data = {'REQUIRED': REQUIRED}
        for item in data:
            js_data.update(item)
        # json_formatted_str2 = json.dumps(data, indent=2)
        return js_data

from itertools import groupby

from rest_framework.renderers import JSONRenderer


class MDMenuRenderer(JSONRenderer):
    format = 'md_menu'

    def render(self, data, accepted_media_type=None, renderer_context=None):

        data.sort(key=lambda elem: elem['category']['name'])
        groups = groupby(data, key=lambda elem: elem['category']['name'])
        data = [{'category': k, 'items': [x for x in v]} for k, v in groups]

        return super(MDMenuRenderer, self).render(data=data,
                                                  accepted_media_type=accepted_media_type,
                                                  renderer_context=renderer_context)


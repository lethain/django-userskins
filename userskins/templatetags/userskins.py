
from django import template

register = template.Library()


@register.tag
def userskin(parser, token):
    return UserskinNode()

class UserskinNode(template.Node):
    def render(self, context):
        skin = template.Variable("userskins_skin").resolve(context)
        use_compress = template.Variable("userskins_use_compress").resolve(context)
        if use_compress:
            pass
        else:
            return u'<link rel="stylesheet" href="%s">' % skin

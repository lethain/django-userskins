
from django import template
try:
    from compress.templatetags import compressed
except ImportError:
    compressed = None

register = template.Library()


@register.tag
def userskin(parser, token):
    return UserskinNode()

class UserskinNode(template.Node):
    def render(self, context):
        skin = template.Variable("userskins_skin").resolve(context)
        print skin
        use_compress = template.Variable("userskins_use_compress").resolve(context)
        if use_compress:
            node = compressed.CompressedCSSNode(skin)
            print node
            return node.render({skin:skin})
            
        else:
            return u'<link rel="stylesheet" href="%s">' % skin

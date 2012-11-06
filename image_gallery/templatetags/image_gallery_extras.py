from django import template


register = template.Library()


@register.inclusion_tag('image_gallery/show_gallery.html', takes_context=True)
def show_gallery(context, gallery):
    context['prettyPhoto_id'] = context.get('prettyPhoto_id', 0) + 1
    my_context = {'gallery': gallery,
                  'prettyPhoto_id': context['prettyPhoto_id']}
    return my_context

from django import template

register=template.Library()

@register.filter(name='raws')
def raws(list_data,raw_size):
    raws=[]
    i=0
    for data in list_data:
        raws.append(data)
        i+=1
        if i==raw_size:
            yield raws
            i=0
            raws=[]
    yield raws



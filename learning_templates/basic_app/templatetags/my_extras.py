from django import template

register = template.Library()

def cut(value, arg) :
    return value.replace(arg, '')
    
# def pos(fig):
    fig = str(fig)
    if fig[-1] == '1' :
        return fig + 'st'
    elif fig[-1] == '2' :
        return fig + 'nd'
    elif fig[-1] == '3' :
        return fig + 'rd'
    else:
        return fig + 'th'

register.filter('cut', cut)
# register.filter('pos', pos)
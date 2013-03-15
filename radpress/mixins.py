from radpress.forms import ZenModeForm


class ZenModeViewMixin(object):
    """
    Receives all common context data for required for zen mode.
    """
    template_name = 'radpress/zen_mode.html'
    form_class = ZenModeForm

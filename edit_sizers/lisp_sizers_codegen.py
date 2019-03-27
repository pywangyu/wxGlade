"""
Lisp generator functions for the various wxSizerS

@copyright: 2002-2004 D.H. aka crazyinsomniac on sourceforge.net
@copyright: 2013-2016 Carsten Grohmann
@copyright: 2017-2019 Dietmar Schwertberger
@license: MIT (see LICENSE.txt) - THIS PROGRAM COMES WITH NO WARRANTY
"""

import common
from .edit_sizers import BaseSizerBuilder, SlotGenerator


class BaseLispSizerBuilder(BaseSizerBuilder):
    "Lisp base class for all sizer code generators"

    language = 'lisp'

    tmpl_SetSizer = '(wxWindow_SetSizer %(parent_widget)s (%(sizer_name)s obj))\n'
    tmpl_Fit = '(wxSizer_Fit (%(sizer_name)s obj) %(parent_widget)s)\n'
    tmpl_SetSizeHints = '(wxSizer_SetSizeHints (slot-%(sizer_name)s obj) %(parent_widget)s)\n'

    tmpl_wparent = '(slot-frame obj)'
    """Only in Lisp the widgets parent statement differs between
    C{slot-frame obj} and C{slot-top-window obj}.

    @todo: Clarify why the widget parent differs between different sizers in Lisp.

    see: L{_get_wparent()}
    """

    def _get_wparent(self, obj):
        window = obj.parent_window
        if not window.IS_CLASS:
            parent = '(slot-%s obj)' % self.codegen._format_name(window.name)
        else:
            parent = self.tmpl_wparent
        return parent


class LispBoxSizerBuilder(BaseLispSizerBuilder):
    klass = 'wxBoxSizer'

    tmpl = '(setf (%(sizer_name)s obj) (wxBoxSizer_Create %(orient)s))\n'

    tmpl_wparent = '(slot-top-window obj)'


class LispWrapSizerBuilder(LispBoxSizerBuilder):
    klass = 'wxWrapSizer'
    tmpl = '(setf (%(sizer_name)s obj) (wxWrapSizer_Create %(orient)s))\n'


class LispStaticBoxSizerBuilder(BaseLispSizerBuilder):
    klass = 'wxStaticBoxSizer'
    tmpl = '(setf (%(sizer_name)s obj) (StaticBoxSizer_Create (wxStaticBox:wxStaticBox_Create %(parent_widget)s %(label)s) %(orient)s))\n'


class LispGridSizerBuilder(BaseLispSizerBuilder):
    klass = 'wxGridSizer'
    tmpl = '(setf (%(sizer_name)s obj) (wxGridSizer_Create %(rows)s %(cols)s %(vgap)s %(hgap)s))\n'


class LispFlexGridSizerBuilder(LispGridSizerBuilder):
    klass = 'wxFlexGridSizer'

    tmpl_AddGrowableRow = '(wxFlexGridSizer_AddGrowableRow (%(sizer_name)s obj) %(row)s)\n'
    tmpl_AddGrowableCol = '(wxFlexGridSizer_AddGrowableCol (%(sizer_name)s obj) %(col)s)\n'


class LispGridBagSizerBuilder(LispGridSizerBuilder):
    klass = 'wxGridBagSizer'
    tmpl = '(setf (%(sizer_name)s obj) (wxGridSizer_Create %(vgap)s %(hgap)s))\n'


def initialize():
    cn = common.class_names
    cn['EditBoxSizer'] = 'wxBoxSizer'
    cn['EditWrapSizer'] = 'wxWrapSizer'
    cn['EditStaticBoxSizer'] = 'wxStaticBoxSizer'
    cn['EditGridSizer'] = 'wxGridSizer'
    cn['EditFlexGridSizer'] = 'wxFlexGridSizer'
    cn['EditGridBagSizer'] = 'wxGridBagSizer'

    lispgen = common.code_writers.get("lisp")
    if lispgen:
        awh = lispgen.add_widget_handler
        awh('wxBoxSizer', LispBoxSizerBuilder())
        awh('wxWrapSizer', LispWrapSizerBuilder())
        awh('wxStaticBoxSizer', LispStaticBoxSizerBuilder())
        awh('wxGridSizer', LispGridSizerBuilder())
        awh('wxFlexGridSizer', LispFlexGridSizerBuilder())
        awh('wxGridBagSizer', LispGridBagSizerBuilder())

    common.register('lisp', "sizerslot", SlotGenerator("lisp"))

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 6d2f15a1b50c+ on Sat Jan 28 14:21:58 2017
#

import wx
import wx.calendar
import wx.grid

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class All_Widgets_Frame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: All_Widgets_Frame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.All_Widgets_menubar = wx.MenuBar()
        global mn_IDUnix; mn_IDUnix = wx.NewId()
        global mn_IDWindows; mn_IDWindows = wx.NewId()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_OPEN, _("&Open"), _("Open an existing document"))
        wxglade_tmp_menu.Append(wx.ID_CLOSE, _("&Close file"), _("Close current document"))
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.ID_EXIT, _("E&xit"), _("Finish program"))
        self.All_Widgets_menubar.Append(wxglade_tmp_menu, _("&File"))
        wxglade_tmp_menu = wx.Menu()
        self.mn_Unix = wx.MenuItem(wxglade_tmp_menu, mn_IDUnix, _("Unix"), _("Use Unix line endings"), wx.ITEM_RADIO)
        wxglade_tmp_menu.AppendItem(self.mn_Unix)
        self.Bind(wx.EVT_MENU, self.onSelectUnix, id=self.mn_Unix.GetId())
        self.mn_Windows = wx.MenuItem(wxglade_tmp_menu, mn_IDWindows, _("Windows"), _("Use Windows line endings"), wx.ITEM_RADIO)
        wxglade_tmp_menu.AppendItem(self.mn_Windows)
        self.Bind(wx.EVT_MENU, self.onSelectWindows, id=self.mn_Windows.GetId())
        wxglade_tmp_menu.AppendSeparator()
        self.mn_RemoveTabs = wx.MenuItem(wxglade_tmp_menu, wx.ID_ANY, _("Remove Tabs"), _("Remove all leading tabs"), wx.ITEM_CHECK)
        wxglade_tmp_menu.AppendItem(self.mn_RemoveTabs)
        self.Bind(wx.EVT_MENU, self.onRemoveTabs, id=self.mn_RemoveTabs.GetId())
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu_sub = wx.Menu()
        self.mn_RemoveWhiteSpaces = wx.MenuItem(wxglade_tmp_menu_sub, wx.ID_ANY, _("Remove"), _("Remove leading whitespace characters"), wx.ITEM_RADIO)
        wxglade_tmp_menu_sub.AppendItem(self.mn_RemoveWhiteSpaces)
        self.Bind(wx.EVT_MENU, self.OnRemoveWhiteSpaces, id=self.mn_RemoveWhiteSpaces.GetId())
        self.mn_KeepWhiteSpaces = wx.MenuItem(wxglade_tmp_menu_sub, wx.ID_ANY, _("Keep"), _("Don't touch leading whitespace characters"), wx.ITEM_RADIO)
        wxglade_tmp_menu_sub.AppendItem(self.mn_KeepWhiteSpaces)
        self.Bind(wx.EVT_MENU, self.OnKeepWhiteSpaces, id=self.mn_KeepWhiteSpaces.GetId())
        wxglade_tmp_menu.AppendSubMenu(wxglade_tmp_menu_sub, _("Leading spaces"), "")
        self.All_Widgets_menubar.Append(wxglade_tmp_menu, _("&Edit"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_item = wxglade_tmp_menu.Append(wx.ID_HELP, _("Manual"), _("Show the application manual"))
        self.Bind(wx.EVT_MENU, self.onShowManual, id=wxglade_tmp_item.GetId())
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.ID_ABOUT, _("About"), _("Show the About dialog"))
        self.All_Widgets_menubar.Append(wxglade_tmp_menu, _("&Help"))
        self.SetMenuBar(self.All_Widgets_menubar)
        # Menu Bar end
        self.All_Widgets_statusbar = self.CreateStatusBar(1, wx.ST_SIZEGRIP)
        
        # Tool Bar
        self.All_Widgets_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.All_Widgets_toolbar)
        self.All_Widgets_toolbar.AddLabelTool(wx.ID_UP, _("UpDown"), wx.ArtProvider.GetBitmap(wx.ART_GO_UP, wx.ART_OTHER, (32, 32)), wx.ArtProvider.GetBitmap(wx.ART_GO_DOWN, wx.ART_OTHER, (32, 32)), wx.ITEM_CHECK, _("Up or Down"), _("Up or Down"))
        self.All_Widgets_toolbar.AddLabelTool(wx.ID_OPEN, _("Open"), wx.EmptyBitmap(32, 32), wx.NullBitmap, wx.ITEM_NORMAL, _("Open a new file"), _("Open a new file"))
        # Tool Bar end
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY, style=wx.NB_BOTTOM)
        self.notebook_1_wxBitmapButton = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.bitmap_button_icon1 = wx.BitmapButton(self.notebook_1_wxBitmapButton, wx.ID_ANY, wx.Bitmap("icon.xpm", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_empty1 = wx.BitmapButton(self.notebook_1_wxBitmapButton, wx.ID_ANY, wx.EmptyBitmap(10, 10))
        self.bitmap_button_icon2 = wx.BitmapButton(self.notebook_1_wxBitmapButton, wx.ID_ANY, wx.Bitmap("icon.xpm", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE | wx.BU_BOTTOM)
        self.bitmap_button_art = wx.BitmapButton(self.notebook_1_wxBitmapButton, wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_GO_UP, wx.ART_OTHER, (32, 32)), style=wx.BORDER_NONE | wx.BU_BOTTOM)
        self.notebook_1_wxButton = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.button_3 = wx.Button(self.notebook_1_wxButton, wx.ID_BOLD, "")
        self.notebook_1_wxCalendarCtrl = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.calendar_ctrl_1 = wx.calendar.CalendarCtrl(self.notebook_1_wxCalendarCtrl, wx.ID_ANY, style=wx.calendar.CAL_MONDAY_FIRST | wx.calendar.CAL_SEQUENTIAL_MONTH_SELECTION | wx.calendar.CAL_SHOW_SURROUNDING_WEEKS)
        self.notebook_1_wxCheckBox = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.checkbox_1 = wx.CheckBox(self.notebook_1_wxCheckBox, wx.ID_ANY, _("one (unchecked)"))
        self.checkbox_2 = wx.CheckBox(self.notebook_1_wxCheckBox, wx.ID_ANY, _("two (checked)"))
        self.checkbox_3 = wx.CheckBox(self.notebook_1_wxCheckBox, wx.ID_ANY, _("three"), style=wx.CHK_2STATE)
        self.checkbox_4 = wx.CheckBox(self.notebook_1_wxCheckBox, wx.ID_ANY, _("four (unchecked)"), style=wx.CHK_3STATE)
        self.checkbox_5 = wx.CheckBox(self.notebook_1_wxCheckBox, wx.ID_ANY, _("five (checked)"), style=wx.CHK_3STATE | wx.CHK_ALLOW_3RD_STATE_FOR_USER)
        self.checkbox_6 = wx.CheckBox(self.notebook_1_wxCheckBox, wx.ID_ANY, _("six (undetermined)"), style=wx.CHK_3STATE | wx.CHK_ALLOW_3RD_STATE_FOR_USER)
        self.notebook_1_wxCheckListBox = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.check_list_box_1 = wx.CheckListBox(self.notebook_1_wxCheckListBox, wx.ID_ANY, choices=[_("one"), _("two"), _("three"), _("four")])
        self.notebook_1_wxChoice = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.choice_empty = wx.Choice(self.notebook_1_wxChoice, wx.ID_ANY, choices=[])
        self.choice_filled = wx.Choice(self.notebook_1_wxChoice, wx.ID_ANY, choices=[_("Item 1"), _("Item 2 (pre-selected)")])
        self.notebook_1_wxComboBox = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.combo_box_empty = wx.ComboBox(self.notebook_1_wxComboBox, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.combo_box_filled = wx.ComboBox(self.notebook_1_wxComboBox, wx.ID_ANY, choices=[_("Item 1 (pre-selected)"), _("Item 2")], style=wx.CB_DROPDOWN)
        self.notebook_1_wxDatePickerCtrl = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.datepicker_ctrl_1 = wx.DatePickerCtrl(self.notebook_1_wxDatePickerCtrl, wx.ID_ANY, style=wx.DP_SHOWCENTURY)
        self.notebook_1_wxGauge = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.gauge_1 = wx.Gauge(self.notebook_1_wxGauge, wx.ID_ANY, 20)
        self.notebook_1_wxGrid = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.grid_1 = wx.grid.Grid(self.notebook_1_wxGrid, wx.ID_ANY, size=(1, 1))
        self.notebook_1_wxHyperlinkCtrl = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.hyperlink_1 = wx.HyperlinkCtrl(self.notebook_1_wxHyperlinkCtrl, wx.ID_ANY, _("Homepage wxGlade"), _("http://wxglade.sf.net"))
        self.notebook_1_wxListBox = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.list_box_empty = wx.ListBox(self.notebook_1_wxListBox, wx.ID_ANY, choices=[])
        self.list_box_filled = wx.ListBox(self.notebook_1_wxListBox, wx.ID_ANY, choices=[_("Item 1"), _("Item 2 (pre-selected)")], style=wx.LB_MULTIPLE | wx.LB_SORT)
        self.notebook_1_wxListCtrl = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.list_ctrl_1 = wx.ListCtrl(self.notebook_1_wxListCtrl, wx.ID_ANY, style=wx.BORDER_SUNKEN | wx.LC_REPORT)
        self.notebook_1_wxRadioBox = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.radio_box_empty1 = wx.RadioBox(self.notebook_1_wxRadioBox, wx.ID_ANY, _("radio_box_empty1"), choices=[""], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.radio_box_filled1 = wx.RadioBox(self.notebook_1_wxRadioBox, wx.ID_ANY, _("radio_box_filled1"), choices=[_("choice 1"), _("choice 2 (pre-selected)"), _("choice 3")], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.radio_box_empty2 = wx.RadioBox(self.notebook_1_wxRadioBox, wx.ID_ANY, _("radio_box_empty2"), choices=[""], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.radio_box_filled2 = wx.RadioBox(self.notebook_1_wxRadioBox, wx.ID_ANY, _("radio_box_filled2"), choices=[_("choice 1"), _("choice 2 (pre-selected)")], majorDimension=0, style=wx.RA_SPECIFY_COLS)
        self.notebook_1_wxRadioButton = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.radio_btn_1 = wx.RadioButton(self.notebook_1_wxRadioButton, wx.ID_ANY, _("Alice"), style=wx.RB_GROUP)
        self.text_ctrl_1 = wx.TextCtrl(self.notebook_1_wxRadioButton, wx.ID_ANY, "")
        self.radio_btn_2 = wx.RadioButton(self.notebook_1_wxRadioButton, wx.ID_ANY, _("Bob"))
        self.text_ctrl_2 = wx.TextCtrl(self.notebook_1_wxRadioButton, wx.ID_ANY, "")
        self.radio_btn_3 = wx.RadioButton(self.notebook_1_wxRadioButton, wx.ID_ANY, _("Malroy"))
        self.text_ctrl_3 = wx.TextCtrl(self.notebook_1_wxRadioButton, wx.ID_ANY, "")
        self.notebook_1_wxSlider = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.slider_1 = wx.Slider(self.notebook_1_wxSlider, wx.ID_ANY, 5, 0, 10)
        self.notebook_1_wxSpinButton = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.tc_spin_button = wx.TextCtrl(self.notebook_1_wxSpinButton, wx.ID_ANY, _("1"), style=wx.TE_RIGHT)
        self.spin_button = wx.SpinButton(self.notebook_1_wxSpinButton, wx.ID_ANY , style=wx.SP_VERTICAL)
        self.notebook_1_wxSpinCtrl = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.spin_ctrl_1 = wx.SpinCtrl(self.notebook_1_wxSpinCtrl, wx.ID_ANY, "4", min=0, max=100, style=wx.SP_ARROW_KEYS | wx.TE_RIGHT)
        self.notebook_1_wxSplitterWindow_horizontal = wx.ScrolledWindow(self.notebook_1, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        self.splitter_1 = wx.SplitterWindow(self.notebook_1_wxSplitterWindow_horizontal, wx.ID_ANY)
        self.splitter_1_pane_1 = wx.Panel(self.splitter_1, wx.ID_ANY)
        self.label_top_pane = wx.StaticText(self.splitter_1_pane_1, wx.ID_ANY, _("top pane"))
        self.splitter_1_pane_2 = wx.Panel(self.splitter_1, wx.ID_ANY)
        self.label_buttom_pane = wx.StaticText(self.splitter_1_pane_2, wx.ID_ANY, _("bottom pane"))
        self.notebook_1_wxSplitterWindow_vertical = wx.ScrolledWindow(self.notebook_1, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        self.splitter_2 = wx.SplitterWindow(self.notebook_1_wxSplitterWindow_vertical, wx.ID_ANY)
        self.splitter_2_pane_1 = wx.Panel(self.splitter_2, wx.ID_ANY)
        self.label_left_pane = wx.StaticText(self.splitter_2_pane_1, wx.ID_ANY, _("left pane"))
        self.splitter_2_pane_2 = wx.Panel(self.splitter_2, wx.ID_ANY)
        self.label_right_pane = wx.StaticText(self.splitter_2_pane_2, wx.ID_ANY, _("right pane"))
        self.notebook_1_wxStaticBitmap = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.bitmap_empty = wx.StaticBitmap(self.notebook_1_wxStaticBitmap, wx.ID_ANY, wx.EmptyBitmap(32, 32))
        self.bitmap_file = wx.StaticBitmap(self.notebook_1_wxStaticBitmap, wx.ID_ANY, wx.Bitmap("icon.xpm", wx.BITMAP_TYPE_ANY))
        self.bitmap_nofile = wx.StaticBitmap(self.notebook_1_wxStaticBitmap, wx.ID_ANY, wx.Bitmap("non-existing.bmp", wx.BITMAP_TYPE_ANY))
        self.bitmap_art = wx.StaticBitmap(self.notebook_1_wxStaticBitmap, wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_PRINT, wx.ART_OTHER, (32, 32)))
        self.notebook_1_wxStaticLine = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.static_line_2 = wx.StaticLine(self.notebook_1_wxStaticLine, wx.ID_ANY, style=wx.LI_VERTICAL)
        self.static_line_3 = wx.StaticLine(self.notebook_1_wxStaticLine, wx.ID_ANY, style=wx.LI_VERTICAL)
        self.static_line_4 = wx.StaticLine(self.notebook_1_wxStaticLine, wx.ID_ANY)
        self.static_line_5 = wx.StaticLine(self.notebook_1_wxStaticLine, wx.ID_ANY)
        self.notebook_1_wxStaticText = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.label_1 = wx.StaticText(self.notebook_1_wxStaticText, wx.ID_ANY, _("red text (RGB)"), style=wx.ALIGN_CENTER)
        self.label_4 = wx.StaticText(self.notebook_1_wxStaticText, wx.ID_ANY, _("black on red (RGB)"), style=wx.ALIGN_CENTER)
        self.label_5 = wx.StaticText(self.notebook_1_wxStaticText, wx.ID_ANY, _("green on pink (RGB)"), style=wx.ALIGN_CENTER)
        self.notebook_1_Spacer = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.label_3 = wx.StaticText(self.notebook_1_Spacer, wx.ID_ANY, _("Two labels with a"))
        self.label_2 = wx.StaticText(self.notebook_1_Spacer, wx.ID_ANY, _("spacer between"))
        self.notebook_1_wxTextCtrl = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.text_ctrl = wx.TextCtrl(self.notebook_1_wxTextCtrl, wx.ID_ANY, _("This\nis\na\nmultiline\nwxTextCtrl"), style=wx.TE_CHARWRAP | wx.TE_MULTILINE | wx.TE_WORDWRAP)
        self.notebook_1_wxToggleButton = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.button_2 = wx.ToggleButton(self.notebook_1_wxToggleButton, wx.ID_ANY, _("Toggle Button 1"))
        self.button_4 = wx.ToggleButton(self.notebook_1_wxToggleButton, wx.ID_ANY, _("Toggle Button 2"), style=wx.BU_BOTTOM | wx.BU_EXACTFIT)
        self.notebook_1_wxTreeCtrl = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.tree_ctrl_1 = wx.TreeCtrl(self.notebook_1_wxTreeCtrl, wx.ID_ANY)
        self.static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        self.button_5 = wx.Button(self, wx.ID_CLOSE, "")
        self.button_1 = wx.Button(self, wx.ID_OK, "", style=wx.BU_TOP)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnNotebookPageChanged, self.notebook_1)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnNotebookPageChanging, self.notebook_1)
        self.Bind(wx.EVT_BUTTON, self.onStartConverting, self.button_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: All_Widgets_Frame.__set_properties
        self.SetTitle(_("All Widgets"))
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.ArtProvider.GetBitmap(wx.ART_TIP, wx.ART_OTHER, (32, 32)))
        self.SetIcon(_icon)
        self.SetSize((800, 417))
        self.All_Widgets_statusbar.SetStatusWidths([-1])

        # statusbar fields
        All_Widgets_statusbar_fields = [_("All Widgets statusbar")]
        for i in range(len(All_Widgets_statusbar_fields)):
            self.All_Widgets_statusbar.SetStatusText(All_Widgets_statusbar_fields[i], i)
        self.All_Widgets_toolbar.Realize()
        self.bitmap_button_icon1.SetSize(self.bitmap_button_icon1.GetBestSize())
        self.bitmap_button_icon1.SetDefault()
        self.bitmap_button_empty1.SetSize(self.bitmap_button_empty1.GetBestSize())
        self.bitmap_button_empty1.SetDefault()
        self.bitmap_button_icon2.SetBitmapDisabled(wx.EmptyBitmap(20, 20))
        self.bitmap_button_icon2.SetSize(self.bitmap_button_icon2.GetBestSize())
        self.bitmap_button_icon2.SetDefault()
        self.bitmap_button_art.SetSize(self.bitmap_button_art.GetBestSize())
        self.bitmap_button_art.SetDefault()
        self.checkbox_2.SetValue(1)
        self.checkbox_4.Set3StateValue(wx.CHK_UNCHECKED)
        self.checkbox_5.Set3StateValue(wx.CHK_CHECKED)
        self.checkbox_6.Set3StateValue(wx.CHK_UNDETERMINED)
        self.check_list_box_1.SetSelection(2)
        self.choice_filled.SetSelection(1)
        self.combo_box_filled.SetSelection(0)
        self.grid_1.CreateGrid(10, 3)
        self.list_box_filled.SetSelection(1)
        self.radio_box_filled1.SetSelection(1)
        self.radio_box_filled2.SetSelection(1)
        self.splitter_1.SetMinimumPaneSize(20)
        self.notebook_1_wxSplitterWindow_horizontal.SetScrollRate(10, 10)
        self.splitter_2.SetMinimumPaneSize(20)
        self.notebook_1_wxSplitterWindow_vertical.SetScrollRate(10, 10)
        self.label_1.SetForegroundColour(wx.Colour(255, 0, 0))
        self.label_4.SetBackgroundColour(wx.Colour(255, 0, 0))
        self.label_4.SetToolTipString(_("Background colour won't show, check documentation for more details"))
        self.label_5.SetBackgroundColour(wx.Colour(255, 0, 255))
        self.label_5.SetForegroundColour(wx.Colour(0, 255, 0))
        self.label_5.SetToolTipString(_("Background colour won't show, check documentation for more details"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: All_Widgets_Frame.__do_layout
        sizer_1 = wx.FlexGridSizer(3, 1, 0, 0)
        sizer_2 = wx.FlexGridSizer(1, 2, 0, 0)
        sizer_24 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_23 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_18 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_4 = wx.FlexGridSizer(1, 3, 0, 0)
        grid_sizer_3 = wx.FlexGridSizer(1, 3, 0, 0)
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.VERTICAL)
        sizer_25 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_33 = wx.BoxSizer(wx.VERTICAL)
        sizer_32 = wx.BoxSizer(wx.VERTICAL)
        sizer_29 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_31 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_30 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_16 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_22 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.StaticBoxSizer(wx.StaticBox(self.notebook_1_wxRadioButton, wx.ID_ANY, _("My RadioButton Group")), wx.HORIZONTAL)
        grid_sizer_2 = wx.FlexGridSizer(3, 2, 0, 0)
        grid_sizer_1 = wx.GridSizer(2, 2, 0, 0)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_20 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_19 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_17 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_26 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_21 = wx.GridSizer(2, 3, 0, 0)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_28 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.FlexGridSizer(2, 2, 0, 0)
        sizer_13.Add(self.bitmap_button_icon1, 1, wx.ALL | wx.EXPAND, 5)
        sizer_13.Add(self.bitmap_button_empty1, 1, wx.ALL | wx.EXPAND, 5)
        sizer_13.Add(self.bitmap_button_icon2, 1, wx.ALL | wx.EXPAND, 5)
        sizer_13.Add(self.bitmap_button_art, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_wxBitmapButton.SetSizer(sizer_13)
        sizer_13.AddGrowableRow(0)
        sizer_13.AddGrowableRow(1)
        sizer_13.AddGrowableCol(0)
        sizer_13.AddGrowableCol(1)
        sizer_28.Add(self.button_3, 0, wx.ALL, 5)
        self.notebook_1_wxButton.SetSizer(sizer_28)
        sizer_12.Add(self.calendar_ctrl_1, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_wxCalendarCtrl.SetSizer(sizer_12)
        sizer_21.Add(self.checkbox_1, 0, wx.EXPAND, 0)
        sizer_21.Add(self.checkbox_2, 0, wx.EXPAND, 0)
        sizer_21.Add(self.checkbox_3, 0, wx.EXPAND, 0)
        sizer_21.Add(self.checkbox_4, 0, wx.EXPAND, 0)
        sizer_21.Add(self.checkbox_5, 0, wx.EXPAND, 0)
        sizer_21.Add(self.checkbox_6, 0, wx.EXPAND, 0)
        self.notebook_1_wxCheckBox.SetSizer(sizer_21)
        sizer_26.Add(self.check_list_box_1, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_wxCheckListBox.SetSizer(sizer_26)
        sizer_5.Add(self.choice_empty, 1, wx.ALL, 5)
        sizer_5.Add(self.choice_filled, 1, wx.ALL, 5)
        self.notebook_1_wxChoice.SetSizer(sizer_5)
        sizer_7.Add(self.combo_box_empty, 1, wx.ALL, 5)
        sizer_7.Add(self.combo_box_filled, 1, wx.ALL, 5)
        sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)
        self.notebook_1_wxComboBox.SetSizer(sizer_6)
        sizer_17.Add(self.datepicker_ctrl_1, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        self.notebook_1_wxDatePickerCtrl.SetSizer(sizer_17)
        sizer_15.Add(self.gauge_1, 1, wx.ALL, 5)
        self.notebook_1_wxGauge.SetSizer(sizer_15)
        sizer_19.Add(self.grid_1, 1, wx.EXPAND, 0)
        self.notebook_1_wxGrid.SetSizer(sizer_19)
        sizer_20.Add(self.hyperlink_1, 0, wx.ALL, 5)
        self.notebook_1_wxHyperlinkCtrl.SetSizer(sizer_20)
        sizer_4.Add(self.list_box_empty, 1, wx.ALL | wx.EXPAND, 5)
        sizer_4.Add(self.list_box_filled, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_wxListBox.SetSizer(sizer_4)
        sizer_3.Add(self.list_ctrl_1, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_wxListCtrl.SetSizer(sizer_3)
        grid_sizer_1.Add(self.radio_box_empty1, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_1.Add(self.radio_box_filled1, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_1.Add(self.radio_box_empty2, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_1.Add(self.radio_box_filled2, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_wxRadioBox.SetSizer(grid_sizer_1)
        grid_sizer_2.Add(self.radio_btn_1, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_2.Add(self.text_ctrl_1, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_2.Add(self.radio_btn_2, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_2.Add(self.text_ctrl_2, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_2.Add(self.radio_btn_3, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_2.Add(self.text_ctrl_3, 1, wx.ALL | wx.EXPAND, 5)
        sizer_8.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        self.notebook_1_wxRadioButton.SetSizer(sizer_8)
        sizer_22.Add(self.slider_1, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_wxSlider.SetSizer(sizer_22)
        sizer_16.Add(self.tc_spin_button, 1, wx.ALL, 5)
        sizer_16.Add(self.spin_button, 1, wx.ALL, 5)
        self.notebook_1_wxSpinButton.SetSizer(sizer_16)
        sizer_14.Add(self.spin_ctrl_1, 1, wx.ALL, 5)
        self.notebook_1_wxSpinCtrl.SetSizer(sizer_14)
        sizer_30.Add(self.label_top_pane, 1, wx.ALL | wx.EXPAND, 5)
        self.splitter_1_pane_1.SetSizer(sizer_30)
        sizer_31.Add(self.label_buttom_pane, 1, wx.ALL | wx.EXPAND, 5)
        self.splitter_1_pane_2.SetSizer(sizer_31)
        self.splitter_1.SplitHorizontally(self.splitter_1_pane_1, self.splitter_1_pane_2)
        sizer_29.Add(self.splitter_1, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_wxSplitterWindow_horizontal.SetSizer(sizer_29)
        sizer_32.Add(self.label_left_pane, 1, wx.ALL | wx.EXPAND, 5)
        self.splitter_2_pane_1.SetSizer(sizer_32)
        sizer_33.Add(self.label_right_pane, 1, wx.ALL | wx.EXPAND, 5)
        self.splitter_2_pane_2.SetSizer(sizer_33)
        self.splitter_2.SplitVertically(self.splitter_2_pane_1, self.splitter_2_pane_2)
        sizer_25.Add(self.splitter_2, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_wxSplitterWindow_vertical.SetSizer(sizer_25)
        sizer_11.Add(self.bitmap_empty, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)
        sizer_11.Add(self.bitmap_file, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)
        sizer_11.Add(self.bitmap_nofile, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)
        sizer_11.Add(self.bitmap_art, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)
        self.notebook_1_wxStaticBitmap.SetSizer(sizer_11)
        sizer_10.Add(self.static_line_2, 1, wx.ALL | wx.EXPAND, 5)
        sizer_10.Add(self.static_line_3, 1, wx.ALL | wx.EXPAND, 5)
        sizer_9.Add(sizer_10, 1, wx.EXPAND, 0)
        sizer_9.Add(self.static_line_4, 1, wx.ALL | wx.EXPAND, 5)
        sizer_9.Add(self.static_line_5, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_wxStaticLine.SetSizer(sizer_9)
        grid_sizer_3.Add(self.label_1, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_3.Add(self.label_4, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_3.Add(self.label_5, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_wxStaticText.SetSizer(grid_sizer_3)
        grid_sizer_4.Add(self.label_3, 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_4.Add((60, 20), 1, wx.ALL | wx.EXPAND, 5)
        grid_sizer_4.Add(self.label_2, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_Spacer.SetSizer(grid_sizer_4)
        sizer_18.Add(self.text_ctrl, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_wxTextCtrl.SetSizer(sizer_18)
        sizer_23.Add(self.button_2, 1, wx.ALL, 5)
        sizer_23.Add(self.button_4, 1, wx.ALL, 5)
        self.notebook_1_wxToggleButton.SetSizer(sizer_23)
        sizer_24.Add(self.tree_ctrl_1, 1, wx.ALL | wx.EXPAND, 5)
        self.notebook_1_wxTreeCtrl.SetSizer(sizer_24)
        self.notebook_1.AddPage(self.notebook_1_wxBitmapButton, _("wxBitmapButton"))
        self.notebook_1.AddPage(self.notebook_1_wxButton, _("wxButton"))
        self.notebook_1.AddPage(self.notebook_1_wxCalendarCtrl, _("wxCalendarCtrl"))
        self.notebook_1.AddPage(self.notebook_1_wxCheckBox, _("wxCheckBox"))
        self.notebook_1.AddPage(self.notebook_1_wxCheckListBox, _("wxCheckListBox"))
        self.notebook_1.AddPage(self.notebook_1_wxChoice, _("wxChoice"))
        self.notebook_1.AddPage(self.notebook_1_wxComboBox, _("wxComboBox"))
        self.notebook_1.AddPage(self.notebook_1_wxDatePickerCtrl, _("wxDatePickerCtrl"))
        self.notebook_1.AddPage(self.notebook_1_wxGauge, _("wxGauge"))
        self.notebook_1.AddPage(self.notebook_1_wxGrid, _("wxGrid"))
        self.notebook_1.AddPage(self.notebook_1_wxHyperlinkCtrl, _("wxHyperlinkCtrl"))
        self.notebook_1.AddPage(self.notebook_1_wxListBox, _("wxListBox"))
        self.notebook_1.AddPage(self.notebook_1_wxListCtrl, _("wxListCtrl"))
        self.notebook_1.AddPage(self.notebook_1_wxRadioBox, _("wxRadioBox"))
        self.notebook_1.AddPage(self.notebook_1_wxRadioButton, _("wxRadioButton"))
        self.notebook_1.AddPage(self.notebook_1_wxSlider, _("wxSlider"))
        self.notebook_1.AddPage(self.notebook_1_wxSpinButton, _("wxSpinButton (with wxTextCtrl)"))
        self.notebook_1.AddPage(self.notebook_1_wxSpinCtrl, _("wxSpinCtrl"))
        self.notebook_1.AddPage(self.notebook_1_wxSplitterWindow_horizontal, _("wxSplitterWindow (horizontally)"))
        self.notebook_1.AddPage(self.notebook_1_wxSplitterWindow_vertical, _("wxSplitterWindow (vertically)"))
        self.notebook_1.AddPage(self.notebook_1_wxStaticBitmap, _("wxStaticBitmap"))
        self.notebook_1.AddPage(self.notebook_1_wxStaticLine, _("wxStaticLine"))
        self.notebook_1.AddPage(self.notebook_1_wxStaticText, _("wxStaticText"))
        self.notebook_1.AddPage(self.notebook_1_Spacer, _("Spacer"))
        self.notebook_1.AddPage(self.notebook_1_wxTextCtrl, _("wxTextCtrl"))
        self.notebook_1.AddPage(self.notebook_1_wxToggleButton, _("wxToggleButton"))
        self.notebook_1.AddPage(self.notebook_1_wxTreeCtrl, _("wxTreeCtrl"))
        sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)
        sizer_1.Add(self.static_line_1, 0, wx.ALL | wx.EXPAND, 5)
        sizer_2.Add(self.button_5, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        sizer_2.Add(self.button_1, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT, 0)
        self.SetSizer(sizer_1)
        sizer_1.SetSizeHints(self)
        sizer_1.AddGrowableRow(0)
        sizer_1.AddGrowableCol(0)
        self.Layout()
        self.Centre()
        self.SetSize((800, 417))
        # end wxGlade

    def onSelectUnix(self, event):  # wxGlade: All_Widgets_Frame.<event_handler>
        print("Event handler 'onSelectUnix' not implemented!")
        event.Skip()

    def onSelectWindows(self, event):  # wxGlade: All_Widgets_Frame.<event_handler>
        print("Event handler 'onSelectWindows' not implemented!")
        event.Skip()

    def onRemoveTabs(self, event):  # wxGlade: All_Widgets_Frame.<event_handler>
        print("Event handler 'onRemoveTabs' not implemented!")
        event.Skip()

    def OnRemoveWhiteSpaces(self, event):  # wxGlade: All_Widgets_Frame.<event_handler>
        print("Event handler 'OnRemoveWhiteSpaces' not implemented!")
        event.Skip()

    def OnKeepWhiteSpaces(self, event):  # wxGlade: All_Widgets_Frame.<event_handler>
        print("Event handler 'OnKeepWhiteSpaces' not implemented!")
        event.Skip()

    def onShowManual(self, event):  # wxGlade: All_Widgets_Frame.<event_handler>
        print("Event handler 'onShowManual' not implemented!")
        event.Skip()

    def OnNotebookPageChanged(self, event):  # wxGlade: All_Widgets_Frame.<event_handler>
        print("Event handler 'OnNotebookPageChanged' not implemented!")
        event.Skip()

    def OnNotebookPageChanging(self, event):  # wxGlade: All_Widgets_Frame.<event_handler>
        print("Event handler 'OnNotebookPageChanging' not implemented!")
        event.Skip()

    def onStartConverting(self, event):  # wxGlade: All_Widgets_Frame.<event_handler>
        print("Event handler 'onStartConverting' not implemented!")
        event.Skip()

# end of class All_Widgets_Frame
if __name__ == "__main__":
    gettext.install("AllWidgets28App") # replace with the appropriate catalog name

    AllWidgets28App = wx.PySimpleApp()
    All_Widgets = All_Widgets_Frame(None, wx.ID_ANY, "")
    AllWidgets28App.SetTopWindow(All_Widgets)
    All_Widgets.Show()
    AllWidgets28App.MainLoop()
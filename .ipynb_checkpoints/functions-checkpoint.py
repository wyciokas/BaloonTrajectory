from bokeh.plotting import figure, output_file, show


def plot_scatter(x, y, xlabel='', ylabel='', w=720, h=480, r=150):
    TOOLS="save,hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,box_select,poly_select,lasso_select,"

    p = figure(tools=TOOLS, plot_width=w, plot_height=h)

    p.scatter(x, y, radius=r, fill_alpha=1,
              color='black',line_color=None)
    p.xaxis.axis_label = xlabel
    p.yaxis.axis_label = ylabel
    p.yaxis.axis_label_text_font_size = "14pt"
    p.yaxis.major_label_text_font_size = "12pt"
    p.xaxis.axis_label_text_font_size = "14pt"
    p.xaxis.major_label_text_font_size = "12pt"
    show(p)


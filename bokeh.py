from bokeh.plotting import figure, output_file, show
import bokeh

x = [1,2,3,4,5]
y = [6,7,2,5,6]


output_file("line.html")
p = figure(title = "simple line example", x_axis_label = 'x', y_axis_label = 'y')
p.line(x, y, legend = 'Temp', line_width =2)

show(p)
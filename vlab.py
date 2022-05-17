import pandas as pd
from bokeh.models import ColumnDataSource, CustomJS, Slider
from bokeh.plotting import figure, show, ColumnDataSource
from bokeh.layouts import column


df = pd.DataFrame({'x':[11,12,13,14,15],'y':[22,23,24,25,26],'threshold':[1,2,3,4,5]})
data = df.to_dict()

source = ColumnDataSource(data=df)

plot = figure(plot_width=400, plot_height=400)
plot.circle('x', 'y', source=source)

slider = Slider(start=1, end=5, value=1, step=1, title="threshold")

callback = CustomJS(

    args=dict(source=source, slider=slider, data=data),

    code="""
            var index = [];
            var x = [];
            var y = [];
            var thresh = [];
            for (var i = 0; i < Object.keys(data.threshold).length; i++) {
                if(slider.value <= data.threshold[i]) {
                    index.push(i);
                    x.push(data.x[i]);
                    y.push(data.y[i]);
                    thresh.push(data.threshold[i]);
                }
            }
            source.data.index = index;
            source.data.x = x;
            source.data.y = y;
            source.data.threshold = thresh;
            source.change.emit();
         """
)

slider.js_on_change('value', callback)

show(column(slider,plot))

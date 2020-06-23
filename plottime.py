
# reference:
# http://datadebrief.blogspot.com/2010/10/plotting-sunrise-sunset-times-in-python.html


import datetime
import random

# use matplotlib with the 'Agg' backend
# this allows the plots to be drawn without a graphics card
# this use() must be called before importing pyplot module
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plot
import matplotlib.dates as mdates


def plot_24_hour_chart(title, control_label, actual_label, control, actual, filename, response_max=10.0):
    
    major_format = mdates.DateFormatter('%H:00')
    
    now = datetime.datetime.now()
    yday = now - datetime.timedelta(days=1)
    start = yday.replace(hour=00, minute=00, second=00, microsecond=0)
    
    fig = plot.figure(figsize=(15, 7))
    ax = fig.add_subplot(111)
    
    ax.xaxis.set_major_locator(mdates.HourLocator())
    ax.xaxis.set_major_formatter(major_format)
    ax.xaxis.set_minor_locator(mdates.HourLocator())
    ax.set_xlim(start, start + datetime.timedelta(days=1))
    ax.set_ylim(0.0, response_max)
    ax.grid(True)
              
    plot.title(title)

    plot.ylabel('Response Time in Seconds')
    
    # draw plots (draw actual first since it will be first in the legend)
    ax.plot(actual[0], actual[1], label=actual_label, color='green')
    ax.plot(control[0], control[1], label=control_label, color='blue')
        
    # Shrink current axis's height by 30% on the bottom
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.3,
                    box.width, box.height * 0.7])

    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
              fancybox=True, shadow=True, ncol=2)

    fig.autofmt_xdate()

    if filename:
        fig.savefig(filename)
    else:
        plot.show()


def example_plot():
    now = datetime.datetime.now()
    yday = now - datetime.timedelta(days=1)
    start = yday.replace(hour=00, minute=00, second=00, microsecond=0)

    minutes_per_day = 24 * 60

    control = [[], []]
    actual = [[], []]

    c = 3.0
    a = 2.0

    for min in range(minutes_per_day):
        control[0].append(start + datetime.timedelta(minutes=min))
        c = c + random.random() * 0.5 - 0.25
        if c < 2.0:
            c = 2.0
        control[1].append(c)
        
        a = a + random.random() * 0.5 - 0.25
        if a < 1.0:
            a = 1.0
        actual[0].append(start + datetime.timedelta(minutes=min))
        actual[1].append(a)
                
    plot_24_hour_chart('Server Response Check - December 11, 2019',
                   "http://www.CNN.com",
                   "Test Server",
                   control,
                   actual,
                   "plot.png")


if __name__ == '__main__':
    example_plot()

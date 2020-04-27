"""Shortcuts for plotting with plotnine (GGPlot)."""

import plotnine as gg
import mizani as scales
import math
import numpy as np
from pandas import CategoricalDtype


def figsize(width, height):
    """Set ggplot figure size in inches."""
    return gg.theme(figure_size=(width, height))


def bottom_legend():
    """Position the legend underneath the plot."""
    return gg.theme(
        legend_position="bottom",
        legend_box_spacing=0.6,
        legend_box_margin=0
    )


def interval_breaks(interval=1):
    """Supply breaks for a continuous scale at set intervals.
    
    This is useful for overriding the ggplot automatic break selection.
        
    Returns a function that can be passed to the `breaks` arg
    of a continuous scale, generating regularly-spaced breaks
    at the specified `interval` size.
    """
    def generate_breaks(limits):
        """ Compute breaks at set intervals between the given limits. """
        start = math.ceil(min(limits) / interval) * interval
        end = math.floor(max(limits) / interval) * interval
        return np.arange(start, end + interval / 2, step=interval)
    
    return generate_breaks


def log10_breaks(limits):
    """Supply breaks for a log10 scale.

    Returns a list of breaks at all integer powers of 10
    covered by the range.
    """
    if min(limits) > 0:
        start = math.ceil(math.log10(min(limits)))
    else:
        start = 0
    end = math.floor(math.log10(max(limits)))
    return 10 ** np.arange(start, end + 0.5)


def log10_minor_breaks(limits):
    """Supply minor breaks for a log10.

    Returns a list of breaks at the "halfway" point between
    the breaks computed by `log10_breaks()`. Eg. the minor
    break between 1 and 10 will be 5.
    """
    main_breaks = log10_breaks(limits)
    return [x / 2 for x in main_breaks[1:]]


def large_num_labels(decimals=None, siunits=False):
    if siunits:
        unit_labs = ("K", "M", "G", "T", "P", "E")
    else:
        unit_labs = ("K", "M", "B", "T")
    if decimals:
        fmt_template = "{{:,.{}f}}".format(decimals)
    else:
        fmt_template = "{:,}"

    def format_num(x):
        if (x - math.trunc(x)) == 0:
            x = int(x)
        return fmt_template.format(x)

    def label_for_val(x):
        if x == 0:
            return "0"
        precision = math.trunc(math.log10(abs(x)))
        unit_group = min(precision // 3, len(unit_labs))
        if unit_group > 0:
            x_fmt = x / (10 ** (3 * unit_group))
            return "{} {}".format(
                format_num(x_fmt),
                unit_labs[unit_group - 1]
            )
        else:
            return format_num(x)

    def labeller(arr):
        return [label_for_val(x) for x in arr]

    return labeller


def to_categorical(series, levels=None, remove_unused=True):
    """Convert a Series to Categorical dtype.
    
    series: the Series to convert
    levels: a list of values to be used as the ordered levels. If `None`,
            uses the ordered unique series values.
    remove_unused: if levels are specified, should unused levels be dropped?
        
    Returns a Categorical series.
    """
    categ = CategoricalDtype(categories=levels, ordered=True)
    s_categ = series.astype(categ)
    if levels and remove_unused:
        s_categ = s_categ.cat.remove_unused_categories()
    return s_categ


def x_date_fmt(date_breaks="1 week"):
    """Concise X-axis scale for dates."""
    return gg.scale_x_date(date_breaks=date_breaks,
                           date_labels="%b %d")


def axis_comma_fmt(axis, **kwargs):
    """Concise axis scale for large numbers."""
    args = {"labels": scales.formatters.comma_format()}
    args.update(kwargs)
    axis_func = getattr(gg, "scale_{}_continuous".format(axis))
    return axis_func(**args)


def y_comma_fmt(**kwargs):
    args = {"labels": scales.formatters.comma_format()}
    args.update(kwargs)
    return gg.scale_y_continuous(**args)


def x_comma_fmt(**kwargs):
    args = {"labels": scales.formatters.comma_format()}
    args.update(kwargs)
    return gg.scale_x_continuous(**args)


def y_pct_fmt(**kwargs):
    args = {"labels": scales.formatters.percent_format()}
    args.update(kwargs)
    return gg.scale_y_continuous(**args)


def y_pct_fmt_full(**kwargs):
    args = {
        "breaks": interval_breaks(0.2),
        "limits": (0, 1)
    }
    args.update(kwargs)
    return y_pct_fmt(**args)


def x_pct_fmt(**kwargs):
    args = {"labels": scales.formatters.percent_format()}
    args.update(kwargs)
    return gg.scale_x_continuous(**args)


def x_pct_fmt_full(**kwargs):
    args = {
        "breaks": interval_breaks(0.2),
        "limits": (0, 1)
    }
    args.update(kwargs)
    return x_pct_fmt(**args)


def y_log10_fmt(**kwargs):
    args = {
        "breaks": log10_breaks,
        "minor_breaks": log10_minor_breaks,
        "labels": scales.formatters.comma_format()
    }
    args.update(kwargs)
    return gg.scale_y_log10(**args)


def x_log10_fmt(**kwargs):
    args = {
        "breaks": log10_breaks,
        "minor_breaks": log10_minor_breaks,
        "labels": scales.formatters.comma_format()
    }
    args.update(kwargs)
    return gg.scale_x_log10(**args)
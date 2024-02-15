import numpy as np
from typing import Optional, Any

from uniplot.axis_labels.datetime_label_set import DatetimeLabelSet


def datetime_labels(
    x_min: Any,
    x_max: Any,
    available_space: int,
    vertical_direction: bool = False,
    unit: str = "",
    log: bool = False,
    verbose: bool = False,
) -> Optional[DatetimeLabelSet]:
    """
    A simple way to get started with datetime labelling.
    """
    # Try in decending order of number of labels.
    for nr_labels in range(8, 0, -1):
        d = (x_max - x_min) / nr_labels
        labels = np.array(
            [x_min + (i + 0.5) * d for i in range(nr_labels)], dtype="datetime64[ns]"
        )
        dls = DatetimeLabelSet(
            labels=labels,
            x_min=x_min,
            x_max=x_max,
            available_space=available_space,
            vertical_direction=vertical_direction,
            unit=unit,
        )
        if not dls.compute_if_render_does_overlap():
            return dls
    return None

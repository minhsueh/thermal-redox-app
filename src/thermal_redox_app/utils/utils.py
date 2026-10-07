from typing import Any, Literal
from uuid import uuid4

from dash import dcc, html
import dash_mp_components as mpc

def get_tooltip(
    tooltip_label: Any,
    tooltip_text: str,
    underline: bool = True,
    tooltip_id: str = "",
    wrapper_class: str = None,
    **kwargs,
):
    """Uses the tooltip component from dash-mp-components to add a tooltip, typically for help text.
    This component uses react-tooltip under the hood.
    :param tooltip_label: text or component to display and apply hover behavior to
    :param tooltip_text: text to show on hover
    :param tooltip_id: unique id of the tooltip (will generate one if not supplied)
    :param wrapper_class: class to add to the span that wraps all the returned tooltip components (label + content)
    :param kwargs: additional props added to Tooltip component. See the components js file in dash-mp-components for a full list of props.
    :return: html.Span.
    """
    if not tooltip_id:
        tooltip_id = uuid4().hex

    tooltip_class = "tooltip-label" if underline else None
    return html.Span(
        [
            html.Span(
                tooltip_label,
                className=tooltip_class,
                **{"data-tip": True, "data-for": tooltip_id},
            ),
            mpc.Tooltip(tooltip_text, id=tooltip_id, **kwargs),
        ],
        className=wrapper_class,
    )
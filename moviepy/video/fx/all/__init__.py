"""
moviepy.video.fx.all is deprecated.

Use the fx method directly from the clip instance (e.g. ``clip.resize(...)``)
or import the function from moviepy.video.fx instead.
"""
import warnings

from .. import *  # noqa 401,F403

warnings.warn(f"\nMoviePy: {__doc__}", UserWarning)

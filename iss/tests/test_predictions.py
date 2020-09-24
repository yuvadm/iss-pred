from pathlib import Path
from skyfield.api import Topos

from ..predictions import Predictions

DATA_DIR = Path(__file__).parent / "data"
STATIONS = DATA_DIR / "stations.txt"


def test_get_timescales():
    days = 5
    p = Predictions(lat=32.0853, lng=34.7817, days=days)
    t0, t1 = p.get_next_days()
    delta = t1.ut1 - t0.ut1
    assert delta == days


def test_custom_start():
    start = 2459117.245895914
    p = Predictions(lat=32.0853, lng=34.7817, start=start)
    t0, _t1 = p.get_next_days()
    assert t0.ut1 == start


def test_get_location():
    p = Predictions(lat=32.0853, lng=34.7817)
    tlv = Topos("32.0853 N", "34.7817 E")
    topos = p.get_location()
    assert topos.latitude.degrees == tlv.latitude.degrees
    assert topos.longitude.degrees == tlv.longitude.degrees


def test_get_predictions():
    start = 2459117.245895914

    p = Predictions(
        lat=32.0853, lng=34.7817, tz="Asia/Jerusalem", start=start, tle_file=STATIONS
    )
    preds = p.get_prediction_events()
    assert len(preds) == 16
    assert preds[0] == [
        "2020-09-24T21:31:31Z",
        "2020-09-24T21:32:57Z",
        "2020-09-24T21:34:24Z",
    ]

    p = Predictions(
        lat=32.0853,
        lng=34.7817,
        tz="Asia/Jerusalem",
        altitude=0,
        start=start,
        days=5,
        tle_file=STATIONS,
    )
    preds = p.get_prediction_events()
    assert len(preds) == 39

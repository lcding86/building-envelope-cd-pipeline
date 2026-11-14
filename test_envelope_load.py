import unittest
from envelope_load import (
    conductive_gain_w,
    solar_glazing_gain_w,
    total_envelope_load_kw,
)


class TestBuildingEnvelopeLoad(unittest.TestCase):
    def test_opaque_wall_conduction(self):
        self.assertEqual(conductive_gain_w(0.45, 40.0, 14.0), 252.0)

    def test_solar_glazing_gain(self):
        self.assertEqual(solar_glazing_gain_w(15.0, 0.35, 650.0), 3412.5)

    def test_total_envelope_load_kw(self):
        self.assertEqual(total_envelope_load_kw(252.0, 550.0, 336.0, 3412.5), 4.551)

    def test_invalid_shgc_raises_error(self):
        with self.assertRaises(ValueError):
            solar_glazing_gain_w(15.0, 1.25, 650.0)

    def test_non_positive_area_raises_error(self):
        with self.assertRaises(ValueError):
            conductive_gain_w(0.45, 0.0, 14.0)


if __name__ == "__main__":
    unittest.main()
from pymatgen.util.testing import PymatgenTest
import unittest
import os
import warnings
from pymatgen.analysis.topological.spillage import SOC_Spillage


class SolarTest(PymatgenTest):
    _multiprocess_shared_ = True

    def setUp(self):
        warnings.simplefilter("ignore")

    def tearDown(self):
        warnings.simplefilter("default")

    def test_spillage_from_vasprun(self):
        wf_noso = os.path.join(os.path.dirname(__file__), "WAVECAR-NonSOC")
        wf_so = os.path.join(os.path.dirname(__file__), "WAVECAR-SOC")
        # JVASP-1044
        gamma_max = SOC_Spillage(wf_noso=wf_noso, wf_so=wf_so).overlap_so_spinpol()

        self.assertAlmostEqual(gamma_max, 1.3634111271008775, places=5)


if __name__ == "__main__":
    unittest.main()

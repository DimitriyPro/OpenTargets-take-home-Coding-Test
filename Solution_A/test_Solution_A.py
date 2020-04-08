import unittest
import subprocess


class TestHello(unittest.TestCase):

    def test_disease_efo_0000616(self):
        sir_disease01 = b'OpenTargets take-home Coding Test (Part A) by Dmitrii Prosovetskii\r\nDiseas analysis ' \
                       b'for EFO_0000616\r\nStandard deviation for disease EFO_0000616 = 0.0\r\nMean for disease ' \
                       b'EFO_0000616 = 1.0\r\nMax for disease EFO_0000616 = 1.0\r\nMin for disease EFO_0000616 = ' \
                       b'1.0\r\n'
        self.assertEqual(
            subprocess.check_output(["python", "Solution_A.py", "-d", "EFO_0000616"]),
            sir_disease01
        )

    def test_disease_efo_0002422(self):
        sir_disease02 = b'OpenTargets take-home Coding Test (Part A) by Dmitrii Prosovetskii\r\nDisease analysis ' \
                       b'for EFO_0002422\r\nSorry... Nothing found. Please try again\r\nThere are more than one ' \
                       b'disease starting with "E". You could try this one:\r\n0: EFO_0000616\r\n1: EFO_0010285\r\n2: ' \
                       b'EFO_0000616\r\n3: EFO_0000508\r\n'
        self.assertEqual(
            subprocess.check_output(["python", "Solution_A.py", "-d", "EFO_0002422"]),
            sir_disease02
        )

    def test_target_ensg00000157764(self):
        str_target = b'OpenTargets take-home Coding Test (Part A) by Dmitrii Prosovetskii\r\nTarget analysis for ' \
                     b'ENSG00000157764\r\nStandard deviation for target ENSG00000157764 = 0.0\r\nMean for target ' \
                     b'ENSG00000157764 = 1.0\r\nMax for target ENSG00000157764 = 1.0\r\nMin for target ' \
                     b'ENSG00000157764 = 1.0\r\n'
        self.assertEqual(
            subprocess.check_output(["python", "Solution_A.py", "-t", "ENSG00000157764"]),
            str_target
        )


if __name__ == '__main__':
    unittest.main()

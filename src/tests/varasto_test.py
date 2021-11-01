import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.negvarasto = Varasto(-10, -10)
        self.taysvarasto = Varasto(1, 10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_virheellinen_tilavuus_nollaantuu(self):
        self.assertAlmostEqual(self.negvarasto.tilavuus, 0)
    
    def test_negatiivinen_alkusaldo_nollaantuu(self):
        self.assertAlmostEqual(self.negvarasto.saldo, 0)

    def test_varaston_saldo_ei_mene_yli(self):
        self.assertAlmostEqual(self.taysvarasto.saldo, 1)
    
    def test_ei_listata_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varaston_saldo_ei_ylita_tilavuutta(self):
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ei_oteta_varastosta_negatiivista_maaraa(self):
        self.varasto.ota_varastosta(-10)
        
    def test_varastosta_ei_oteta_saldoa_enempaa(self):
        self.varasto.ota_varastosta(100)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_varasto_tulostuu_oikein(self):
        print(self.varasto)
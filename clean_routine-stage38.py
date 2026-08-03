# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: CleanRoutine
import unittest


class TestEdgeCases(unittest.TestCase):
    """Тесты для ошибок, пограничных случаев и граничных условий."""

    def test_empty_zone_name(self):
        zone = Zone(name="", tasks=[("Включить свет", "ежедневно")])
        self.assertEqual(zone.name, "")

    def test_invalid_frequency(self):
        with self.assertRaises(ValueError):
            Zone(name="Кухня", tasks=[("Помыть стол", "раз в день")] )
            zone = Zone(name="Кухня", tasks=[("Помыть стол", "раз в день")])
            zone.frequency = "каждую неделю"  # некорректное значение
            self.assertFalse(zone.is_due())

    def test_zero_days_in_cycle(self):
        cycle = Cycle(frequency="ежедневно", days=0)
        self.assertTrue(cycle.is_complete())


if __name__ == "__main__":
    unittest.main()

# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: CleanRoutine
import unittest


class TestCleanRoutine(unittest.TestCase):
    def test_create_zone(self):
        zone = Zone("Kitchen", "Daily")
        self.assertEqual(zone.name, "Kitchen")
        self.assertEqual(zone.frequency, "Daily")

    def test_add_task_to_zone(self):
        zone = Zone("Kitchen", "Daily")
        task = Task("Wash dishes", 10)
        zone.add_task(task)
        self.assertEqual(len(zone.tasks), 1)
        self.assertEqual(zone.tasks[0].description, "Wash dishes")

    def test_add_multiple_tasks(self):
        zone = Zone("Kitchen", "Daily")
        for desc in ["Wash dishes", "Clean counter"]:
            zone.add_task(Task(desc, 15))
        self.assertEqual(len(zone.tasks), 2)

    def test_update_zone_frequency(self):
        zone = Zone("Kitchen", "Daily")
        zone.update_frequency("Weekly")
        self.assertEqual(zone.frequency, "Weekly")

    def test_get_stats_empty(self):
        stats = Stats()
        self.assertEqual(stats.total_tasks, 0)
        self.assertEqual(stats.completed_tasks, 0)
        self.assertEqual(stats.pending_tasks, 0)

    def test_record_task_completion(self):
        stats = Stats()
        task = Task("Wash dishes", 10)
        stats.record(task, True)
        self.assertEqual(stats.total_tasks, 1)
        self.assertEqual(stats.completed_tasks, 1)
        self.assertEqual(stats.pending_tasks, 0)

    def test_record_pending_task(self):
        stats = Stats()
        task = Task("Wash dishes", 10)
        stats.record(task, False)
        self.assertEqual(stats.total_tasks, 1)
        self.assertEqual(stats.completed_tasks, 0)
        self.assertEqual(stats.pending_tasks, 1)

    def test_display_stats(self):
        stats = Stats()
        stats.record(Task("Wash dishes", 10), True)
        stats.record(Task("Clean counter", 15), False)
        output = stats.display()
        self.assertIn("Total tasks: 2", output)
        self.assertIn("Completed tasks: 1", output)
        self.assertIn("Pending tasks: 1", output)

    def test_display_stats_empty(self):
        stats = Stats()
        output = stats.display()
        self.assertIn("Total tasks: 0", output)
        self.assertIn("Completed tasks: 0", output)
        self.assertIn("Pending tasks: 0", output)


if __name__ == "__main__":
    unittest.main()

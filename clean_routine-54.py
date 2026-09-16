# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: CleanRoutine
import random
from datetime import datetime

class FavoritesManager:
    def __init__(self, routine):
        self.routine = routine
        self._favorites = {}
        self._max_favorites = 5

    def add_favorites(self, zone_ids):
        if len(self._favorites) >= self._max_favorites:
            print(f"⚠️  Избранные: максимум {self._max_favorites} записей")
            return
        for zid in zone_ids:
            zone = self.routine.get_zone(zid)
            if zone:
                self._favorites[zid] = zone

    def get_favorites(self):
        return [self._favorites[zid] for zid in self._favorites]

    def get_random_favorite(self):
        favs = self.get_favorites()
        if not favs:
            return None
        return random.choice(favs)

    def show_favorites_menu(self):
        print("\n📌 Избранные записи:")
        for z in self.get_favorites():
            print(f"  - {z.name} ({z.periodicity})")
        if not self.get_favorites():
            print("  (нет избранных)")
        print()

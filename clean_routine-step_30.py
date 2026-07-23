# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: CleanRoutine
class Profile:
    def __init__(self, name, zones=None):
        self.name = name
        self.zones = zones or []
    
    def add_zone(self, zone):
        if zone not in self.zones:
            self.zones.append(zone)
    
    @staticmethod
    def create_default(name="Default"):
        return Profile(name, [
            Zone("Кухня", "Ежедневно"),
            Zone("Ванная", "Раз в неделю"),
            Zone("Гостиная", "Раз в месяц"),
        ])
    
    def to_dict(self):
        return {"name": self.name, "zones": [z.to_dict() for z in self.zones]}


class ProfileManager:
    _profiles = []
    
    @classmethod
    def add_profile(cls, profile):
        cls._profiles.append(profile)
    
    @classmethod
    def get_profiles(cls):
        return list(cls._profiles)
    
    @classmethod
    def set_active(cls, index):
        if 0 <= index < len(cls._profiles):
            active = cls._profiles[index]
            for p in cls._profiles:
                p.active = False
            active.active = True
    
    @classmethod
    def get_active_profile(cls):
        return next((p for p in cls._profiles if getattr(p, 'active', False)), None)


ProfileManager.add_profile(Profile.create_default("Default"))

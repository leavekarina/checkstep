# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: CleanRoutine
def bulk_update_records(db, zone_id, updates, record_ids):
    """Bulk-update multiple records for a zone.

    Args:
        db: SQLite connection.
        zone_id: ID of the zone to filter records.
        updates: dict of column_name -> new_value to apply.
        record_ids: list of record IDs to update.

    Returns:
        Number of rows affected.
    """
    if not updates or not record_ids:
        return 0
    placeholders = ", ".join(["?"] * len(record_ids))
    columns = ", ".join(updates.keys())
    sql = f"UPDATE records SET {columns} = {placeholders} WHERE zone_id = ? AND id IN ({placeholders})"
    args = [zone_id] + list(updates.values()) + record_ids
    cursor = db.cursor()
    cursor.execute(sql, args)
    db.commit()
    return cursor.rowcount

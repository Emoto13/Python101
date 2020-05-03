query_get_all_free_hours = '''SELECT id, date, start_hour
                              FROM RepairHour
                              WHERE vehicle is NULL;'''

query_get_free_hours_by_date = '''SELECT id, start_hour
                                  FROM RepairHour
                                  WHERE vehicle is NULL and date = ?;'''

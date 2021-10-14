class StoresSearchResult:
  def __init__(self, conn, text, limit=0, offset=0):
    self.text = text
    self.limit = limit
    self.offest = offset
    self.result = []
    
    limit_and_offset_query = ""
    if limit > 0:
      limit_and_offset_query += f" LIMIT {limit}"
      if offset > 0:
        limit_and_offset_query += f" OFFSET {offset}"
    
    # here there is room to improve the query, asking {limit} + 1 rows, 
    # we can know if there are others rows to get, and we can return this info to the API
    query = f''' 
      SELECT * FROM stores 
      WHERE name LIKE '%{text}%' OR postcode LIKE '%{text}%' 
      ORDER BY CASE WHEN postcode LIKE '%{text}%' THEN 0 ELSE 1 END
      {limit_and_offset_query};
    '''
    c = conn.cursor()
    c.execute(query)
    rows = c.fetchall()
    for row in rows:
      self.result.append(row)
    c.close()
    conn.close()

  def get_results(self):
    return self.result
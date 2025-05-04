class SQLQueryBuilder:
    def __init__(self):
        self._query_type = None
        self._table = None
        self._columns = []
        self._values = []
        self._conditions = []

    def select(self, *columns):
        self._query_type = "SELECT"
        self._columns = columns if columns else ["*"]
        return self

    def insert_into(self, table, **values):
        self._query_type = "INSERT"
        self._table = table
        self._columns = list(values.keys())
        self._values = list(values.values())
        return self

    def update(self, table):
        self._query_type = "UPDATE"
        self._table = table
        return self

    def set(self, **values):
        if self._query_type != "UPDATE":
            raise ValueError("SET can only be used with UPDATE queries")
        self._columns = list(values.keys())
        self._values = list(values.values())
        return self

    def delete_from(self, table):
        self._query_type = "DELETE"
        self._table = table
        return self

    def where(self, condition):
        self._conditions.append(condition)
        return self

    def build(self):
        if self._query_type == "SELECT":
            query = f"SELECT {', '.join(self._columns)} FROM {self._table}"
        elif self._query_type == "INSERT":
            columns = ", ".join(self._columns)
            placeholders = ", ".join(["%s"] * len(self._values))
            query = f"INSERT INTO {self._table} ({columns}) VALUES ({placeholders})"
        elif self._query_type == "UPDATE":
            set_clause = ", ".join(f"{col} = %s" for col in self._columns)
            query = f"UPDATE {self._table} SET {set_clause}"
        elif self._query_type == "DELETE":
            query = f"DELETE FROM {self._table}"
        else:
            raise ValueError("Invalid query type")

        if self._conditions:
            query += " WHERE " + " AND ".join(self._conditions)

        return query, self._values

# Example usage:
if __name__ == "__main__":
    builder = SQLQueryBuilder()

    # SELECT query
    select_query, _ = builder.select("id", "name").where("age > 30").build()
    print(select_query)

    # INSERT query
    insert_query, values = builder.insert_into("users", id=1, name="John").build()
    print(insert_query, values)

    # UPDATE query
    update_query, values = builder.update("users").set(name="Jane").where("id = 1").build()
    print(update_query, values)

    # DELETE query
    delete_query, _ = builder.delete_from("users").where("id = 1").build()
    print(delete_query)
import pymysql


class RDBAdaptor():

    # DFF TODO -- Probably should create an abstract base class for common API

    def __init__(self, connect_info):
        self._connect_info = connect_info
        self._db_connection = None

    def _get_connection(self):

        if self._db_connection is None:
            self._db_connection = pymysql.connect(**self._connect_info)
        return self._db_connection

    def run_query(self, q_string, q_params=None, fetch=False, commit=True, cnx=None, cursor=None):

        cursor_created = False
        connection_created = False
        the_cnx = None
        the_cursor = None
        res = None

        try:
            if cursor is None:
                if cnx is None:
                    the_cnx = self._get_connection()
                    #connection_created = True
                else:
                    the_cnx = cnx

                the_cursor = the_cnx.cursor()
            else:
                the_cursor = cursor

            print("Query string = ", the_cursor.mogrify(q_string, q_params))

            res = the_cursor.execute(q_string, q_params)

            if fetch:
                res = the_cursor.fetchall()
            if commit:
                the_cnx.commit()
        except Exception as e:
            print("run_query: Exception = ", e)

            if the_cnx is not None:
                the_cnx.rollback()

        if cursor_created:
            the_cursor.close()
        if connection_created:
            the_cnx.close()

        return res

    def insert(self, db_name, table_name, insert_dict, commit=True, cursor=None, cnx=None):

        cols = list(insert_dict.keys())
        vals = list(insert_dict.values())

        i_cols = "( " + ", ".join(cols) + " )"
        i_vals = ["%s" for v in vals]
        i_vals = ", ".join(i_vals)

        i_string = "insert into " + db_name + "." + table_name + " " + i_cols + \
            "values (" + i_vals + ")"

        res = self.run_query(i_string, vals, fetch=False, commit=commit, cursor=cursor, cnx=cnx)
        return res

    def get_by_primary_key (self, db_name, table_name, key_dict, commit=True, cursor=None, cnx=None):

        res = self.get_by_template(db_name, table_name, key_dict, commit=True, cursor=None, cnx=None)
        return res

    def get_by_template (self, db_name, table_name, key_dict, commit=True, cursor=None, cnx=None):

        # TODO DFF -- Move where clause into helper method
        # TODO DFF -- Add field selection.

        cols = list(key_dict.keys())
        vals = list(key_dict.values())
        wc_terms = [c + "=%s" for c in cols]
        wc = " and ".join(wc_terms)

        q = "select * from " + db_name + "." + table_name + " where " + wc
        res = self.run_query(q, vals, commit=commit, cursor=cursor, fetch=True, cnx=cnx)
        return res










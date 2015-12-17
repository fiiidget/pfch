from bs4 import BeautifulSoup
import requests

# def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
#     enc = file.encoding
#     if enc == 'UTF-8':
#         print(*objects, sep=sep, end=end, file=file)
#     else:
#         f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
#         print(*map(f, objects), sep=sep, end=end, file=file)

class BRScraper:

    def __init__(self, server_url="http://www.baseball-reference.com/"):
        self.server_url = server_url

    def parse_tables(self, resource, table_ids=None, verbose=False):
        """
        Given a resource on the baseball-reference server (should consist of
        the url after the hostname and slash), returns a dictionary keyed on
        table id containing arrays of data dictionaries keyed on the header
        columns. table_ids is a string or array of strings that can optionally
        be used to filter out which stats tables to return.
        """

        def is_parseable_table(tag):
            if not tag.has_attr("class"): return False
            return tag.name == "table" and "stats_table" in tag["class"] and "sortable" in tag["class"]

        def is_parseable_row(tag):
            if not tag.name == "tr": return False
            if not tag.has_attr("class"): return True  # permissive
            return "league_average_table" not in tag["class"] #and "stat_total" not in tag["class"] deal with this. what why????

        if isinstance(table_ids, str): table_ids = [table_ids]

        page = requests.get(self.server_url + resource)


        page_html = page.text


        soup = BeautifulSoup(page_html, "html.parser")


        # soup = BeautifulSoup(requests.get(self.server_url + resource), "html.parser")
        tables = soup.find_all(is_parseable_table)
        data = {}

        # Read through each table, read headers as dictionary keys
        for table in tables:

            if table_ids != None and table["id"] not in table_ids: continue
            if verbose: print("Processing table " + table["id"])
            data[table["id"]] = []

            headers = table.find("tfoot").find_all("tr", attrs = {"class" : "thead"})
            header_names = []
            for header in headers:
                if header.string == None:
                    base_header_name = "u"""
                else: base_header_name = header.string.strip()
                if base_header_name in header_names:
                    i = 1
                    header_name = base_header_name + "_" + str(i)
                    while header_name in header_names:
                        i += 1
                        header_name = base_header_name + "_" + str(i)
                    if verbose:
                        if base_header_name == "":
                            print("Empty header relabeled as %s" % header_name)
                        else:
                            print("Header %s relabeled as %s" % (base_header_name, header_name))
                else:
                    header_name = base_header_name
                header_names.append(header_name)

            # rows = table.find("tbody").find_all(is_parseable_row)
            # for row in rows:
            #     entries = row.find_all("td")
            #     entry_data = []
            #     for entry in entries:
            #         if entry.string == None:
            #             entry_data.append("u""")
            #         else:
            #             entry_data.append(entry.string.strip())
            #     if len(entry_data) > 0:
            #         data[table["id"]].append(dict(zip(header_names, entry_data)))

            foots = table.find("tfoot").find_all(is_parseable_row)
            for foot in foots:
                # ft = foot.find_all("tr", attrs = {"class" : "stat_total"})
                # for foottotal in ft:
                entries = foot.find_all("td")
                entry_data = []
                for entry in entries:
                    if entry.string == None:
                        entry_data.append("u""")
                    else:
                        entry_data.append(entry.string.strip())
                if len(entry_data) > 0:
                    data[table["id"]].append(dict(zip(header_names, entry_data)))

        return data

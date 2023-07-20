import csv

def save_to_file(search_term, jobs):
    """Write list jobs into csv
    :param search_term: str
    :param jobos: list[dict[str,str]]
    :return: None
    """
    file = open(f"{search_term}-Jobs.csv", mode="w",
    encoding="utf-8",newline="")
    writer = csv.writer(file)
    writer.writerow(["title","company","applyLink","location","description"])
    for job in jobs:
        writer.writerow(list(job.values()))